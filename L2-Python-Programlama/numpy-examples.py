# PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WITH PYTHON)
#####################################################

# NumPy - Matematiksel işlemler için ortaya çıkmıştır. Python programlama dünyasından veri analitiği dünyasına geçişte akıllara gelen ilk kütüphanedir.
# Pandas (NumPy kütüpanesi üzerine kurulmuştur) - Veri analizi, Veri manipülasyonu
# Veri Görseleştirme: Matplotlib (Low Level Library) & Seaborn (High Level Library)
# Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis)

####################################################

# NumPy (Numerical Python) - Listelerden farkı:
# - Verimli veri saklama
# - Yüksek seviyeli işlemler (Vektörel işlemelerdir)

# Neden NumPy? (Why NumPy?)
import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

# Klasik yol ile iki listeyi çarpma işlemi

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# NumPy ile iki listeyi çarpma
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
ab = a * b  # yüksek seviyeden vektörel işlemler yapabiliyor

# NumPy Array'i Oluşturmak (Creating of NumPy Arrays)

np.array([1, 2, 3, 4, 5])
# type(np.array([1, 2, 3, 4, 5]))

# elemanı sıfırlardan oluşan array yapar
np.zeros(10, dtype=int)

# rastgele array oluşturma = 0 ile 10 arasinda 10(size) tane int sayı türet
np.random.randint(0, 10, size=10)

# Kitlenin ortalaması, standart sapma, matris boyutu
np.random.normal(3, 4, (4, 4))

# NumPy Array Özellikleri (Attributes of NumPy Arrays)

a = np.random.randint(10, size=5)

# ndim: boyut sayısı
a.ndim
# shape: boyut bilgisi
a.shape
# size: toplam eleman sayısı
a.size
# dtype: array veri tipi
a.dtype

# Yeniden Şekillendirme (Reshaping) - NumPy Array'ın boyutunu değiştirmek için kullanırız

# a = np.random.randint(1, 10, size=9).reshape(3,3)
a = np.random.randint(1, 10, size=9)
a.reshape(3, 3)

# Index Seçimi (Index Selection)

a = np.random.randint(10, size=10)

a[0]
a[0:5]

b = np.random.randint(10, size=(3, 5))
# [satır, sütun]
b[1, 2]

# Slicing

b[:, 0]     #[bütün satırlar, 0. sütun]
b[0, :]     #[0. satır, bütün sütunlar]
b[0:2, 1:2]

# Fancy Index

# 0'dan 30'a kadar 3 er artan bir array oluştur (arange)
v = np.arange(0, 30, 3)

# birden fazla index'in değerine ulaşma
catch = [1, 3, 5]   #indexlerin tutulduğu liste
v[catch]

# NumPy'da Koşullu İşlemler (Conditions on NumPy)

z = np.array([1, 2, 3, 4, 5])

# 3 ten önceki değerlere ulaşma - Klasik yöntem ile
ab = []
for i in z:
    if i < 3:
        ab.append(i)

# 3 ten önceki değerlere ulaşma - NumPy yöntem ile (arka planda fancy indexx çalışıyor)

z < 3 # z listesinin hepsini gezer 3 ten küçükleri True büyüklere False ile gösterir
z[z < 3]
z[z > 3]
z[z <= 3]
z[z != 3]

# Matematiksel İşlemler (Mathematical Operations)

t = np.array([1, 2, 3, 4, 5])

# bütün elemanlara bu işlemleri uygulamış olur
t / 5
t * 5 / 10
t ** 2

np.subtract(t, 1)   # her indexteki veriden 1 çıkar
np.add(t, 1)        # her indexteki veriye 1 ekle
np.mean(t)
np.sum(t)
np.min(t)
np.max(t)
np.var(t)

# NumPy ile iki bilinmeyenli denklem çözümü

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])  # bilinmeyen katsayıların listeleri
b = np.array([12, 10])          # sonuç listeleri

np.linalg.solve(a, b)
