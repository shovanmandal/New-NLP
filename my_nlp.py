import nltk
import pandas
class my_nlp:

     def test(a):
          alist=[]
          for i in range(1,a+1):
               string ='word'+str(i)
               alist.append(string);
          return alist
          
               
               

     
     def My_NLP():

          file = open("Sample.txt", "r") 
          read_file = file.read()

          word_token = nltk.word_tokenize(read_file)
          word_series = pandas.Series(word_token)
          a=len(word_series)
          table = pandas.DataFrame(word_series, index = [x for x in range(a+1)])
          print(table)
          word_pos = nltk.pos_tag(word_token)
          
          #cnt = count(word_pos)

          #dist = map(dict, set(map(lambda x: tuple(x.item()), word_pos)))
          #print(dist)
          
          #for x in word_pos:
               #cnt = word_pos.count(x)
               
               #print(x.unique(),':',cnt)
               #print (" :")
               #print(cnt)
          #cnt = {x:word_pos.count(x)print('/n') for x in word_pos}
          #print d
         #print(cnt ,"/n")


my_nlp.My_NLP()
