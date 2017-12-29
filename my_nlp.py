import nltk
import pandas
import re
from nltk.corpus import wordnet

class my_nlp:

     def test(self,a):
          
          alist=[]
          for i in range(1,a+1):
               string ='word'+str(i)
               alist.append(string);
          return alist
     
     def My_NLP(self):
          
          file = open("Sample.txt", "r") 
          read_file = file.read()
          cleanString = re.sub('\W+',' ', read_file )            #cleanse the unwanted expressions
          
          word_token = nltk.word_tokenize(cleanString.lower())           #Word tokenization
          word_series = pandas.Series(word_token)
          a=len(word_series)
          word_pos = nltk.pos_tag(word_token)                    #POS Tagging
          
          newdict= {}
          newwordlist = []
          newposlist = []
          newtaglist = []
          for word,pos in word_pos:                              #creating dictionary and List...
               newdict.update({word : pos})                      #with tokenized word and...
               newwordlist.append(word)                            #tagged POS
               newposlist.append(pos)
          for t in newposlist:
               print(t)

               
               '''newtag = ''
               if t == 'NN':
                    newtag = 'n'
               elif t == 'JJ':
                    newtag = 'a'
               elif t == 'V':
                    newtag = 'v'
               elif t == 'R':
                    newtag = 'r'
               else:
                    newtag = ''
               newtaglist.append(newtag)
          #print(newtaglist)
               
          word_freq = nltk.FreqDist(newposlist)
          word_features = list(word_freq.keys())''' 
          
          data={'Words':newwordlist,'POS':newposlist,'NewTag':newtaglist}
          table = pandas.DataFrame(data, index = self.test(a))
          #print(table)

          #classifier = NaiveBayesClassifier.train(cleanString)    #classifier()
          

a = my_nlp()
a.My_NLP()
