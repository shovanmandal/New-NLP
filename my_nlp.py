import nltk
import pandas
import re
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn

class my_nlp:

     def excel_DATA_manipulation(self):                     ########################

          file = 'tags.xlsx'
          xl = pandas.ExcelFile(file)
          xl_data = xl.parse('Sheet1')
          tags = self.my_FOR(xl_data['Tag'])
          newTags = self.my_FOR(xl_data['NewTag'])
          pos_Dict= dict( zip( tags, newTags))

          return pos_Dict

     def test(self,a):
          
          alist=[]
          for i in range(1,a+1):
               string ='word'+str(i)
               alist.append(string);

          return alist

     def my_FOR(self, a):

          alist = []
          for i in a:
               if i == 0:
                    alist.append('0')
               else:
                    alist.append(i)

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
          #scorelist = []
          for word,pos in word_pos:                              #creating dictionary and List...
               newdict.update({word : pos})                      #with tokenized word and...
               newwordlist.append(word)                            #tagged POS
               newposlist.append(pos)
          for t in newposlist:
               for i,j in self.excel_DATA_manipulation().items():
                    if t == i:
                         newtaglist.append(j)
          NewSentimetDict = dict(zip(newwordlist,newtaglist))
          
          return NewSentimetDict
     

     def Sentiment_Scores(self):

          scorelist= []

          for i,j in self.My_NLP().items():
               if(j!= '0'):
                    synsets = list(swn.senti_synsets(i,j))
                    #print(synsets)
                    score = 0
                    if(len(synsets)>0):
                         for syn in synsets:
                              score+=syn.pos_score() - syn.neg_score()
                         scorelist.append(score/len(synsets))

          return scorelist

     def Visualization(self):

          wordlist= []
          taglist = []
          scorelist = self.Sentiment_Scores()

          for i,j in self.My_NLP().items():
               if(j!= '0'):
                    wordlist.append(i)
                    taglist.append(j)
          data = {'Scores':scorelist, 'Tags':taglist, 'Words':wordlist}
          table = pandas.DataFrame(data,index= self.test(len(wordlist)))
          print(table)
               
          

a = my_nlp()
a.Visualization()
#.Sentiment_Scores()
#a.My_NLP()
#(a.excel_DATA_manipulation())
