
import pandas as pd
from sklearn.utils import shuffle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import io
import re
import string
tokenizer = RegexpTokenizer(r'\w+')

f = open('label','w',encoding="utf-8")
fname = 'label'
data = pd.read_csv('phish.csv',encoding = "ISO-8859-1")
data = shuffle(data)
X = data.iloc[:, 1]
from nltk.tokenize import word_tokenize
print(X[1])
y = data.iloc[:, 0]
f = open('label','w',encoding="utf-8")
try:
  for i in range(1000):
    X[i] = X[i].lower()
    X[i] = re.sub(r'\d+', '', X[i])
    X[i] = tokenizer.tokenize(X[i])
    X_str = ''.join(X[i])
    # stop_words = set(stopwords.words('english'))
    # tokens = word_tokenize(X_str)
    # X_clean = []
    # for w in tokens:
    #   if w not in stop_words:
    #     X_clean.append(w)
    # last_X = ''.join(X_clean)

    y[i] = y[i].lower()
    y[i] = re.sub(r'\d+', '', y[i])
    y[i] = tokenizer.tokenize(y[i])
    y_str = ' '.join(y[i])
    # stop_words = set(stopwords.words('english'))
    # tokensy = word_tokenize(y_str)
    # y_clean = []
    # for w in tokensy:
    #   if w not in stop_words:
    #     y_clean.append(w)
    # print(tokensy)
    # print(y_clean)
    # last_y = ' '.join(y_clean)
    f.write('__label__'+X_str+ ' '+y_str+'\n')
except:
  pass
f.close()
train = open('label.train','w')
with open("label") as myfile:
    head = [next(myfile) for x in range(500)]
    for i in head:
      train.write(i)

valid = open('label.valid','w')
def tail(file, n=1, bs=1024):
    f = open(file)
    f.seek(0,2)
    l = 1-f.read(1).count('\n')
    B = f.tell()
    while n >= l and B > 0:
            block = min(bs, B)
            B -= block
            f.seek(B, 0)
            l += f.read(block).count('\n')
    f.seek(B, 0)
    l = min(l,n)
    lines = f.readlines()[-l:]
    f.close()
    return lines

lines = tail("label", 200)
for line in lines:
  valid.write(line)

import fasttext

model = fasttext.train_supervised(input="label.train",epoch=25,lr=0.5,dim=50, loss='ova')
model.save_model("label.bin")
model.test("label.valid")
# text = input()
# print(model.predict(input))
while True:
  test = str(input('>'))
  print(model.predict(test))


