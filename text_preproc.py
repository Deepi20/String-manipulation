import re

def text_clean(text):
    text = re.sub(r'&amp;','&',text)
    text = re.sub(r'[!?.,;:#@-]','',text)
    text = re.sub(r'RT','',text)
    text = text.lower()
    return text
    