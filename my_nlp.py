import nltk
import pandas
import re

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
          cleanString = re.sub('\W+',' ', read_file )
          
          word_token = nltk.word_tokenize(cleanString)
          word_series = pandas.Series(word_token)
          a=len(word_series)
          word_pos = nltk.pos_tag(word_token)
          newdict= {}
          newwordlist=[]
          newposlist=[]
          for word,pos in word_pos:
               #dictelement= word + ':' + pos
               #print(dictelement)
               newdict.update({word : pos})
               newwordlist.append(word)
               newposlist.append(pos)
                    
          data={'Words':newwordlist,'POS':newposlist}
          table = pandas.DataFrame(data, index = self.test(a))
          print(table)
          
          

a = my_nlp()
a.My_NLP()
#a.sample()
