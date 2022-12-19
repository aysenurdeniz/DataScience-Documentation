# PANDAS - Veri analizi ve veri manipülasyonları - Ekonomik ve Zaman serileri için ortaya çıkmıştır
####################################################

# Pandas Series - En yaygın kullanılan Pandas veri yapılarıdır

import pandas as pd

# veri indeksleyerek tutar
# 0    10
# 1    77
# 2    12
# 3     4
# 4     5
# dtype: int64

s = pd.Series([10, 77, 12, 4, 5])
type(s)

s.index
s.dtype
s.size
s.ndim
s.values
s.head(3)   # Baştan 3 indexi ve değerlerini getir
s.tail(3)   # Sondan 3 indexi ve değerlerini getir

# Veri Okuma (Reading Data) - Dış kaynaklardan (csv vs.)

df = pd.read_csv("datasets/advertising.csv")
df.head()

# Veriye Hızlı Bakış (Quick Look at Data)

import seaborn as sns

df1 = sns.load_dataset("titanic")
df1.head()
df1.tail()
df1.shape
df1.info()  #object ve category tipleri kategorik değişkenlerdir.
df1.columns
df1.index

df1.describe()
df1.describe().T    # Transpozunu alarak okunabilirliğini artırıyoruz

df1.isnull().values.any()   # Eksik bilgi var mı kontrol et
df1.isnull().sum()          # Eksik bilgilerin olduğu yerde kategorik olarak kaç tane olduğunu hesaplar

# Cinsiyette (sex) kaç tane kadın kaç tane erkek var
df1["sex"].value_counts()

# Pandas'ta Seçim İşlemleri (Selection in Pandas)
df1.drop(0, axis=0)    # Satırdan 0. indexi sil
df1.drop(0, axis=0).head()

# Birden fazla indexteki veriyi silme yapılacaksa
delete_indexes = [1, 3, 5, 7]
df1.drop(delete_indexes, axis=0)
# Atama yapmadan inplace metodu ile de kalıcı silme yapılabilir
# df1.drop(delete_indexes, axis=0, inplace=True)
df1.drop(delete_indexes, axis=0).head()

# Değişkeni indexe çevirme
df1["age"].head()
df1.age.head()

df1.index = df1["age"]  # Yaş bilgisi index olarak eklendi
df1.drop("age", axis=1, inplace=True) # axis=1 ile silme işleminin sütunlardan olacağını belirttik

# Indexi değişkene çevirme
df1["age"] = df1.index  # first way
df1 = df1.reset_index()       # second way

# Gösterileccek maksimum sayı olmasın (...), columnların hepsinin göster
pd.set_option("display.max_columns", None)

"age" in df1    # age değişkeni df1 veri setinin içerisinde var mı?

df1["age"].head()
type(df1["age"].head())

df1[["age"]].head()
type(df1[["age"]].head())   # [[""]] iki parantez dataframe olarak kalmasını sağlar

df1[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df1[col_names]

# yeni bir değişken ekleme, yok ise ekleme işlemi yapar var ise atama işlemi yapar
df1["age2"] = df1["age"] ** 2
df1.head()

df1["age3"] = df1["age"] / df1["age2"]

# Değişken silme
df1.drop(["age3", "age2"], axis=1).head()

# Bütüns sütunlarda age stringi içeren sütunları getir
df1.loc[:, df1.columns.str.contains("age")].head()
df1.loc[:, ~df1.columns.str.contains("age")].head() # ~ işareti ile tersini, değildiri seçiyor

# iloc(integer bilgisi yani index bilgisi vererek seçim yapmayı ifade eder yani integer-based level)
# loc (labellara göre seçim yapar-label based selectiondır)
# -> Dataframelerde seçim işlemi yapmak için kullanılır

# 3 Dahil değil - e kadar devam eder
df1.iloc[0:3]
# 3 dahildir, label mutlak olarak alınır.
df1.loc[0:3]

df1.iloc[0:3, "age"] #ValueError hatası verir çünkü integer tabanlı olduğu için str beklemiyor
df1.iloc[0:3, 0:3]

df1.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df1.loc[0:3, col_names] #fancy index kullanıldı

# Koşullu Seçim (Conditional Selection)

# yaşı 50 den büyük olanları getirsin
df1[df1["age"] > 50].head()
# Yaşı 50 den büyük olanların sayısını getirsin

df1[df1["age"] > 50].count() # Hangi sütun olacağını belitmediğimiz için bütün sütunlarda count yapar
# OutpuT:
# survived       64
# pclass         64
# sex            64
# age            64
# sibsp          64
# parch          64
# fare           64
# embarked       63
# class          64
# who            64
# adult_male     64
# deck           33
# embark_town    63
# alive          64
# alone          64
# dtype: int64

df1[df1["age"] > 50]["age"].count()
# Out: 64

df1.loc[df1["age"] > 50, ["age", "class"]].head()

df1.loc[(df1["age"] > 50)
        & (df1["sex"] == "male"),
        ["age", "class"]].head()

# df1.loc[(şart 1) & (şart 2) | ((şart3) | şart4),
#        [istenilensütun1, istenilensütun2, istenilensütun3]]
# Şartlar paranteze alınmalı!!!!!

#####################################################
# Toplulaştırma ve Gruplama  (Aggregation & Grouping)
#####################################################

# Groupby fonksiyonu ile kullanılabilecek fonksiyonlar:
# _____________________________________________________
# count()
# first()
# last()
# mean()
# median()
# min()
# max()
# std()
# var()
# sum()

df1.groupby("sex")["age"].mean()

df1.groupby("sex").agg({"age": "mean"})

# pivot table -> Groupby işlemlerine benzer şekilde kırılımlar yapar

# cut -> sınıfları tanımlayabiliyorsak kullanılır
# qcut -> sınıfları tanımlayamıyorsak, yüzdeliklere bellir bir oranalra göre kategorik yapar
# -> nümerik(sayısal) değişkenleri kategorik değişkene çevirir


######################################################
pd.set_option('display.max_columns', None)
# Bütün değerleri yanyaa yazdırma için kullanılır
pd.set_option('display.width', 500)
######################################################

# Apply -> satır ve sütunlarda otomatik olarak fonksyon çalıştırmaya yarar
# Lambda -> fonksiyon tanımlama şekli ama kullan at formundadır

# Birleştirme (Join) İşlemleri

import numpy as np

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 100
# concat

pd.concat([df1, df2], ignore_index=True, axis=1) #ignore_index: önceki indexler boş ver ve yeni index ata
# axis 1 ise sütun bazlı birleştirir, axis 0 ise satır bazlı birleştirir

# merge -> ortak argümana göre birleştirme yapar (on ile hangi argüman olduğu da belirtilebilir)
