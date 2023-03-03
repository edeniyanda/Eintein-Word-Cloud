# Import required modules
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import PIL.Image

# Open file for reading

with open("physics.txt", "r") as fhand:
    text = fhand.read()

py_background = np.array(PIL.Image.open("img/Eintein.jpeg"))

w_cloud = WordCloud(
    stopwords = set(STOPWORDS),
    mask = py_background,
    min_font_size=3,
    max_words=5000,
    background_color= "white",
    contour_color= "black",
    contour_width=3,
)

word_cloud = w_cloud.generate(text)
plt.imshow(word_cloud)
plt.axis("off")
plt.show()