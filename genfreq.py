import pandas as pd 

dataset = pd.read_csv("...../user/text.csv")
def gen_freq(text):
  word_list = []
  for words in text.split():
    word_list.extend(words)
  word_freq = pd.Series(word_list).value_counts()
  word_freq[:20]
  return word_freq

gen_freq(dataset.text.str)
 
    
  
