
# importing libraries
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re
# import nltk
# from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Input text - to summarize
# t = open('passage1.txt', 'r')
# text =
# text = t.read()


def __main__(text):
    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = nltk.word_tokenize(str(text))

    # words = word.lower() for word in words if re.match('^[a-zA-Z]+', word)
    # for word in words:
    #     if re.match('^[a-zA-Z]+', word):
    #         words = word.lower()
    # text = re.sub("[a-zA-Z]", "", str(text))
    # Creating a frequency table to keep the
    # score of each word

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score
    # of each sentence
    sentences = sent_tokenize(str(text))
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq



    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text

    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    return summary
# ''''# Tokenizing the text
# stopWords = set(stopwords.words("english"))
# words = word_tokenize(text)
#
# # Creating a frequency table to keep the
# # score of each word
#
# freqTable = dict()
# for word in words:
#     word = word.lower()
#     if word in stopWords:
#         continue
#     if word in freqTable:
#         freqTable[word] += 1
#     else:
#         freqTable[word] = 1
#
# # Creating a dictionary to keep the score
# # of each sentence
# sentences = sent_tokenize(text)
# sentenceValue = dict()
#
# for sentence in sentences:
#     for word, freq in freqTable.items():
#         if word in sentence.lower():
#             if sentence in sentenceValue:
#                 sentenceValue[sentence] += freq
#             else:
#                 sentenceValue[sentence] = freq
#
#
#
# sumValues = 0
# for sentence in sentenceValue:
#     sumValues += sentenceValue[sentence]
#
# # Average value of a sentence from the original text
#
# average = int(sumValues / len(sentenceValue))
#
# # Storing sentences into our summary.
# # summary = ''
# # for sentence in sentences:
# #     if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
# #         summary += " " + sentence
#
# ''''s = open('result1.txt', 'w')
# print(summary, file=s)
# # sys.summary = open('result1.txt', 'w')
# print("Please write this to file.\n")
# # sys.summary.close()
# s.close()
# t.close()
# ''''

t1 = open('Passage1.txt', 'r')

text1 = t1.read()

t2 = open('Passage2.txt', 'r')

text2 = t2.read()

t3 = open('Passage3.txt', 'r')

text3 = t3.read()

s1 = open("result1.txt", "w")
s2 = open("result2.txt", "w")
s3 = open("result3.txt", "w")
# print()
print(__main__(text1), file=s1)
print(__main__(text2), file=s2)
print(__main__(text3), file=s3)
s1.close()
s2.close()
s3.close()
t1.close()
t2.close()
t3.close()
# ''''
#     s = open(summary,file=w)
#     print(summary, file=s)
#     s.close()
# ''''
