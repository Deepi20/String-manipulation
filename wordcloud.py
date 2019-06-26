import matplotlib.pyplot as plt
from wordcloud import WordCloud

word_freq = gen_freq(dataset.text.str)

wc = WordCloud(width= 400,height= 330, max_words = 100, background_color = 'white').generate_from_frequencies(word_freq)

plt.figure(figsize = (12,8))
plt.imshow(wc,interpolation = 'bilinear')
plt.axis('off')
plt.show()
