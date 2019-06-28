import re
from wordcloud import STOPWORDS

def text_clean(text):
    text = re.sub(r'&amp;','&',text)
    text = re.sub(r'[!?.,;:#@-]','',text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r'RT','',text)
    text = text.lower()
    return text

text = dataset.text.apply(lambda x: text_clean(x))
word_freq = gen_freq(text.str)
word_freq = word_freq.drop(labels = STOPWORDS, errors = 'ignore')

