import nltk
class my_nlp:
     
     def My_NLP():

          file = open("Sample.txt", "r") 
          read_file = file.read()
          #print(read_file)

          word_token = nltk.word_tokenize(read_file)
          word_pos = nltk.pos_tag(word_token)
          #cnt = count(word_pos)

          #dist = map(dict, set(map(lambda x: tuple(x.item()), word_pos)))
          #print(dist)
          
          for x in word_pos:
               cnt = word_pos.count(x)
               
               print(x.unique(),':',cnt)
               #print(x, )
               #print (" :")
               #print(cnt)
          #cnt = {x:word_pos.count(x)print('/n') for x in word_pos}
          #print d
          #print(cnt ,"/n")
          
     
     

my_nlp.My_NLP()

     
