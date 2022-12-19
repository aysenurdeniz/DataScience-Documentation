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
    "C:\\Users\\anurd\\Documents\\GitHub\\DataScience-Documentation\\L5-Dogal-Dil-Islemeye-Giris\\datasets\\amazon_reviews.csv",
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

df['reviewText'] = df['reviewText'].apply(lambda x: " ".join([Word(word).lemmatize for word in x.split()]))


