from random import sample
import sys

import pandas as pd
from curses.ascii import isascii
import numpy as np
from bisect import bisect_left
from scipy import spatial
import sys

# #load stopwords
stopwords=pd.read_csv("./reqd_csv/stopwords.csv")["Word"].tolist()
#load stop keys


#primarily removed stuff
remove = [".",",",":","\"","!","'","?","Tags","\t","\b"]


#remove the word if it has a digit in it
def has_number(word):
    for w in word:
        if ord(w)>=48 and ord(w)<=57:
            return True

    return False

def notEnglish(ch):
    if isascii(ch):
        return False
    else:
        return True

def bin_s(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def handle(q):

    #blank list to contain refined words
    pruned_s = []
    #strip spaces in the question
    q = q.strip()
    #remove all \t,\b
    q = ' '.join(q.split())

    #clean the query words just similar to mod statements

    #remove some punctuation marks 
    for r in remove:
        q = q.replace(r,"")

    #split the sentence into words
    words = q.split(" ")

    #go thru each word
    for word in words:
        #if word is a letter, leave it
        if(len(word)==1 or len(word)==0 ):
            continue

        word = word.lower()           
        flag = 1  #remains 1 if none of the stopwords present in word
        #word is a stopword
        if word in stopwords:
            flag=-1

        if has_number(word):
            flag=-1

        #go thru the word and find a stopkey
        # for l in word:
        #     if l in stop or notEnglish(l):
        #         flag=-1
        #         break

        if flag==-1:
            continue

        pruned_s.append(word)

    return pruned_s
    
def similarity(a1,a2):
    return 1 - spatial.distance.cosine(a1,a2)



'''MAIN'''
#MAIN part of the func
pruned_s = handle(sys.argv[1])
# pruned_s = handle("binary")

#load the idf csv
idf = pd.read_csv("./reqd_csv/idf.csv")
keywords = idf["Keyword"].tolist()
idfval = idf["IDF"].tolist()
cols = len(keywords)
#map to get freq of all words
m = {}
#to measure tot no. of keywords
f = 0

for k in pruned_s:
    if k in m:
        m[k]+=1
    else:
        m[k]=1

#map for tf
tf = np.zeros(cols)
#set of indices
s = set()
for k in pruned_s:
    #gives index in idf keyword column
    ind = bin_s(keywords,k)
    if ind!=-1:
        f+=1
        tf[ind] = m[k]
        s.add(ind)

#handling no keyword matched and blank search case
if len(s)==0:
    #no keyword found, so make a list of 10 random words from keywords and show
    pruned_s = sample(keywords,10)
    for k in pruned_s:
        if k in m:
            m[k]+=1
        else:
            m[k]=1

    for k in pruned_s:
        #gives index in idf keyword column
        ind = bin_s(keywords,k)
        if ind!=-1:
            f+=1
            tf[ind] = m[k]
            s.add(ind)


#calc the tf
for i in s:
    tf[i]/= f

# tfidf of the new sentence
tfidf2 = np.zeros(cols)

for i in range(cols):
    tfidf2[i] = tf[i] * idfval[i]


statements = pd.read_csv("./reqd_csv/merged_no_titles.csv")
tfidf = np.zeros((len(statements),cols))

table = pd.read_csv("./reqd_csv/tfidf.csv")
x_arr = table["X"]
y_arr = table["Y"]
f_arr = table["TF-IDF"]
tfidf[x_arr,y_arr] = f_arr

# return sorted_matrix


l = [similarity(tfidf[i,:],tfidf2) for i in range(len(statements))]
statements["Similarity"] = l
statements2 = statements.sort_values(by = "Similarity",ascending=False)
statements2 = statements2.drop_duplicates()
df = statements2.iloc[0:10,0:4].reset_index().iloc[:,1:]
new_data = df.to_json()
print(new_data)
sys.stdout.flush()