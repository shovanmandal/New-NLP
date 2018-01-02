import nltk
import pandas
import re
import PyPDF2
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn

class my_nlp:

     insert_file = input('Pease insert the file name:')

     def file_open(self):

          file_content = ''
          file_name = my_nlp.insert_file

          if file_name.endswith('.pdf'):
               pdf_file = open(file_name,'rb')                        #Reading PDF file
               read_pdf = PyPDF2.PdfFileReader(pdf_file)
               number_of_pages = read_pdf.getNumPages()
               page = read_pdf.getPage(0)
               file_content = page.extractText()

          elif file_name.endswith('.txt'):
               file = open(file_name, "r")                        # Reading Text file
               file_content = file.read()

          cleanString = re.sub('\W+',' ', file_content )            #cleanse the unwanted expressions
          cleanString = cleanString.lower()
          #print(cleanString)
          return cleanString

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
                    
          word_token = nltk.word_tokenize(self.file_open())           #Word tokenization
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
               for i,j in self.excel_DATA_manipulation().items():
                    if t == i:
                         newtaglist.append(j)
          NewSentimetDict = dict(zip(newwordlist,newtaglist))
          return NewSentimetDict
     

     def Sentiment_Scores(self):

          scorelist= []
          wordlist = []
          taglist = []

          for i,j in self.My_NLP().items():
               if(j!= '0'):
                    synsets = list(swn.senti_synsets(i,j))
                    score = 0
                    if(len(synsets)>0):
                         for syn in synsets:
                              score+=syn.pos_score() - syn.neg_score()
                         scorelist.append(score/len(synsets))
                         wordlist.append(i)
                         taglist.append(j)
                         
          data = {'Scores':scorelist, 'Tags':taglist, 'Words':wordlist}
          return data

     def Visualization(self):
          lenth = []
          for key,val in self.Sentiment_Scores().items():
               lenth.append(len(val))
               
          table = pandas.DataFrame(self.Sentiment_Scores(),index=self.test(lenth[0]))
          print(table)
               
          
a = my_nlp()

a.Visualization()

#a.file_open()
#a.My_NLP()
#a.Sentiment_Scores()
#(a.excel_DATA_manipulation())
