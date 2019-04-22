# coding = "utf-8"
import xlrd
import xlwt
import jieba
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import sys


def main():
    argApi = {
        '-f': "",
        '-v': "",
        '-l': "",
        '-k': ""
    }
    arg_list = sys.argv
    for i in range(len(arg_list)):
        if arg_list[i][0] == '-':
            argApi[arg_list[i]] = arg_list[i + 1]
    jvlei(int(argApi['-k']), argApi['-f'], int(argApi['-l']), int(argApi['-v']))


def read_xls(fileName, line):
    readXls = xlrd.open_workbook(fileName)
    table = readXls.sheets()[0]
    textList = list()
    for i in range(table.nrows):
        textList.append(table.row_values(i)[line - 1].strip())
    return textList


def cut_word(text):
    readFile = open('./stop_words.txt', 'r', encoding='utf-8')
    stopWords = ['\n', ]
    oneWords = readFile.readline()
    while oneWords:
        stopWords.append(oneWords.strip())
        oneWords = readFile.readline()
    wordList = list()
    for i in jieba.cut(text):
        if i not in stopWords:
            wordList.append(i)
    return " ".join(wordList)


def jvlei(K, fileName, inLine, needWordNumber):
    textList = list()
    for i in read_xls(fileName, inLine):
        textList.append(cut_word(i))
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(textList))
    clf = KMeans(int(K))
    y_pred = clf.fit_predict(tfidf)
    flag = set(y_pred)
    result = dict()
    for i in flag:
        result[str(i)] = list()
    for i in range(len(y_pred)):
        result[str(y_pred[i])].append(textList[i])
    for i in result:
        tfidf_print(result[i], needWordNumber)


def tfidf_print(textList, needWordNumber):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(textList))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    wordDict = dict()
    weight = weight.T
    for i in range(len(weight)):
        wordDict[word[i]] = weight[i].sum()
    wordDict = sorted(wordDict.items(), key=lambda d: d[1], reverse=True)
    for i in range(needWordNumber):
        wordDict[i] = wordDict[i][0]
    print(wordDict[:needWordNumber])


if __name__ == "__main__":
    main()