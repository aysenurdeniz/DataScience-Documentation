# !pip install nltk
# !pip install textblob
# !pip install wordcloud

from warnings import filterwarnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, GridSearchCV, cross_validate
from sklearn.preprocessing import LabelEncoder
from textblob import Word, TextBlob
from wordcloud import WordCloud

# warningleri göz ardı et
filterwarnings('ignore')
# bütün sütunları göster
pd.set_option('display.max_columns', None)
# max genişlik 200 olsun
pd.set_option('display.width', 200)
# virgülden sonra iki basamak göster
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# ****************************
# Text Preprocessing
# ****************************

# ???? Dosya yolu güncellenecek !
df = pd.read_csv(
    "/datasets/amazon_reviews.csv",
    sep=",")
df.head()

# Desccription for dataset
# ---------------------------
# reviewerID: yorum yapan kişiler
# asin: ürün idleri
# reviewerName: yorum yapanların isimleri
# helpful: yorumlar faydalı mı [helpful_yes, total_vote]
# reviewText: yorumlar
# overall: verilen puanlar
# summary: reviewların özeti olarak düşünülebilir
# unixReviewTime, reviewTime, daydiff - zamanlar

# Normalizing Case Folding
# ------------------------

df['reviewText']

# büyük küçük harfleri tek forma dönüştürmek
# örn. hepsi küçük harf olsun
df['reviewText'] = df['reviewText'].str.lower()

# Noktalama işaretleri / Punctuations
# -----------------------------------

# noktalama işaretlerini kaldırmak ya da değiştirmek
# [^\u\s] -> a regular expression
df['reviewText'] = df['reviewText'].str.replace('[^\w\s]', '')

# Numbers Remove
# --------------

# sayilari yakalama
# \d -> a regular expression for numbers
df['reviewText'] = df['reviewText'].str.replace('\d', '')

# Stopwords (yaygın olarak kullanılan kelimeler)
# ----------------------------------------------

# import nltk
# nltk kütüphanesinden stopwords listesini indir
# nltk.download('stopwords')

# stopwrods listesi istenildiği gibi düzenlenip özel bir liste de ayarlanabilir
sw = stopwords.words('english')

# stopword listesinde bulunanları datasette bulup bu kelimeler silinmeli
# Öncelikle her satırda gezilmeli (apply) ve her satırda bütün kelimeleri de gezmeli (lambda)

df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in str(x).split() if x not in sw))

# Rarewords / Nadir Kelimeler
# ---------------------------

# kelimelerin frekanslarına bakarak belli bir sayı sınırından önceki kelimeler kaldırılabiilir
temp_df = pd.Series(' '.join(df['reviewText']).split()).value_counts()
# örn. birden az olan frekansa sahip olanlar alınsın
drops = temp_df[temp_df <= 1]

df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in x.split() if x not in drops))

# Tokenization
# -------------
import nltk
# nltk.download('punkt')

df['reviewText'].apply(lambda x: TextBlob(x).words).head()

# kalıcı işlem için atama yapılır:
# df['reviewText'] = df['reviewText'].apply(lambda x: TextBlob(x).words).head()

# Lemmatization / Kelimeleri köklerine ayırma işlemi örn. s takısı
# ----------------------------------------------------------------
import nltk
nltk.download('wordnet')

df['reviewText'] = df['reviewText'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

# ****************************
# Text Visualization
# ****************************

# Terim Frekanslarının Hesaplanması
#----------------------------------

tf = df['reviewText'].apply(lambda x: pd.value_counts(x.split())).sum(axis=0).reset_index()
# Sütun isimlerini güncelleme
# index, 0 -> words, tf
tf.columns = ["words", "tf"]
# Azalan olacak şekilde sıralama
tf.sort_values("tf", ascending=False)

# Barplot / Sütun grafik
#------------------------

# Sütun grafikte bütün değerler göstermek yerine sınır belirlemek daha mantıklı olacaktır

tf[tf["tf"] > 500].plot.bar(x="words", y="tf")
plt.show()

# Word Cloud / Kelime bulutu
#---------------------------

# Kelimelerin frekanslarına göre resim oluşturma işlemidir
# Bu işlem için veri setindeki bütün satırların tek bir string olarak ifade edilmesi gerekir
text = " ".join(i for i in df.reviewText)

wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("wordcloud_black.png")

# Örnek özelleştirme
wordcloud = WordCloud(
    max_font_size=50,
    max_words=100,
    background_color="white"
).generate(text)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("wordcloud_white.png")

# Şablonlara göre Word Cloud
#---------------------------

# bir resmin üzerine wordcloud yapılması amaçlanmaktadır
tr_mask = np.array(Image.open("L5-Dogal-Dil-Islemeye-Giris/tr.png"))

wc = WordCloud(
    background_color="white",
    max_words=1000,
    mask=tr_mask,
    contour_width=3,
    contour_color="firebrick"
)

wc.generate(text)
plt.figure(figsize=[10, 10])
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("wc_sablon.png")

# ****************************
# Sentiment Analysis
# ****************************

