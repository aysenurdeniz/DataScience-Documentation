# Sales Prediction with Linear Regression
# ------------------------------------------


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

# Simple Linear Regression with OLS Using Scikit-Learn
# ----------------------------------------------------

df = pd.read_csv("L2-Python-Programlama/datasets/advertising.csv")
df.shape

X = df[["TV"]]  # bağımsız değişken
y = df[["sales"]]  # bağımlı değişken

# Model
# -----

reg_model = LinearRegression().fit(X, y)

# y_hat = b + w*TV

# sabit (b - bias)
reg_model.intercept_[0]

# tv'nin katsayısı (w1)
reg_model.coef_[0][0]

# Tahmin Uygulamaları
# --------------------

# 150 birimlik TV harcaması olsa ne kadar satış olması beklenir?

reg_model.intercept_[0] + reg_model.coef_[0][0] * 150

# 500 birimlik tv harcaması olsa ne kadar satış olur?

reg_model.intercept_[0] + reg_model.coef_[0][0] * 500

# df ile ilgili istatistikler (count, mean, st, min, %25-50-75, max)
df.describe().T

# Modelin Görselleştirilmesi
# ---------------------------

# regresyon modelini görselleştirmek için regplot kullanılır

g = sns.regplot(x=X, y=y, scatter_kws={'color': 'b', 's': 9},
                ci=False, color="r")

# round{ ,2} -> virgülden sonra 2 basamağa yuvarla

g.set_title(f"Model Denklemi: Sales = {round(reg_model.intercept_[0], 2)} + TV*{round(reg_model.coef_[0][0], 2)}")
g.set_ylabel("Satış Sayısı")
g.set_xlabel("TV Harcamaları")
plt.xlim(-10, 310)  # x limit
plt.ylim(bottom=0)  # y limit
plt.show()

# Tahmin Başarısını Değerledirme
# -----------------------------------

# MSE
y_pred = reg_model.predict(X)
mean_squared_error(y, y_pred)  # 10.51
y.mean()  # 14.02
y.std()  # 5.22
# Ortalama ve standart sapmaya bakıldığında 10.51 biraz büyük bir hata gibi görünüyor.


# RMSE
np.sqrt(mean_squared_error(y, y_pred))
# 3.24

# MAE
mean_absolute_error(y, y_pred)
# 2.54

# R-KARE -> Bağımsız değişkenlerin bağımlı değişkenleri açıklama yüzdesidir.
# Dikkat !!
# Değişken sayısı arttıkça R-KARE artmaya meyillidir
# Burada düzeltilmiş R-KARE durumunun da göz önünde bulundurulması gerekir
# Ek olarak burada istatistiki çıktılar ile ilgilenilmiyor, makine öğrenmesi açısından bakılıyor
reg_model.score(X, y)
# 0.611


# Multiple Linear Regression
# ---------------------------

df = pd.read_csv("L2-Python-Programlama/datasets/advertising.csv")

X = df.drop('sales', axis=1)  # bağımsız değişkenler (sales'i sil)

y = df[["sales"]]  # bağımlı değişken (sales)

# Model
# ------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

X_test.shape
X_train.shape

y_test.shape
y_train.shape

# Train seti için
reg_model = LinearRegression().fit(X_train, y_train)

# sabit (b - bias)
reg_model.intercept_

# coefficients (w - weights)
reg_model.coef_

# Tahmin Değerlendirme
# ---------------------

# Aşağıdaki gözlem değerlerine göre satışın beklenen değeri nedir?

# TV: 30
# radio: 10
# newspaper: 40

# 2.90 (b)
# 0.0468431 , 0.17854434, 0.00258619 (w1, w2, w3)

# Sales = 2.90  + TV * 0.04 + radio * 0.17 + newspaper * 0.002 (Model denklemi)

2.90794702 + 30 * 0.0468431 + 10 * 0.17854434 + 40 * 0.00258619

yeni_veri = pd.DataFrame([[30], [10], [40]]).T

reg_model.predict(yeni_veri)  # Result ?

# Tahmin Başarısını Değerlendirme
# ---------------------------------

# Train RMSE
y_pred = reg_model.predict(X_train)
np.sqrt(mean_squared_error(y_train, y_pred))
# 1.73

# TRAIN RKARE
reg_model.score(X_train, y_train)
# 0.89

# Test RMSE
y_pred = reg_model.predict(X_test)  # X_test için bağımlı değişkenlerini tahmin ediyor
np.sqrt(mean_squared_error(y_test, y_pred))
# 1.41

# Test RKARE
reg_model.score(X_test, y_test)

# Test hatasının train hatasından yüksek çıkması istenilen bir senaryodur

# 10 Katlı CV RMSE
# neg_mean_squared_error -> negatif sonuç verdiğinden cross_val_score (-) ile çarpılır
np.mean(np.sqrt(-cross_val_score(reg_model,
                                 X,
                                 y,
                                 cv=10,
                                 scoring="neg_mean_squared_error")))
# 1.69


# 5 Katlı CV RMSE
np.mean(np.sqrt(-cross_val_score(reg_model,
                                 X,
                                 y,
                                 cv=5,
                                 scoring="neg_mean_squared_error")))


# 1.71


# -----------------------------------------------------------
# Simple Linear Regression with Gradient Descent from Scratch
# -----------------------------------------------------------

# Manuel olarak Cost fonksiyonunun yazılması ve çalıştırılması

# Cost function MSE
def cost_function(Y, b, w, X):
    m = len(Y)
    sse = 0

    for i in range(0, m):
        y_hat = b + w * X[i]
        y = Y[i]
        sse += (y_hat - y) ** 2

    mse = sse / m
    return mse


# update_weights
def update_weights(Y, b, w, X, learning_rate):
    m = len(Y)
    b_deriv_sum = 0
    w_deriv_sum = 0
    for i in range(0, m):
        y_hat = b + w * X[i]
        y = Y[i]
        b_deriv_sum += (y_hat - y)
        w_deriv_sum += (y_hat - y) * X[i]
    new_b = b - (learning_rate * 1 / m * b_deriv_sum)
    new_w = w - (learning_rate * 1 / m * w_deriv_sum)
    return new_b, new_w


# train fonksiyonu
def train(Y, initial_b, initial_w, X, learning_rate, num_iters):
    print("Starting gradient descent at b = {0}, w = {1}, mse = {2}".format(initial_b, initial_w,
                                                                            cost_function(Y, initial_b, initial_w, X)))

    b = initial_b
    w = initial_w
    cost_history = []

    for i in range(num_iters):
        b, w = update_weights(Y, b, w, X, learning_rate)
        mse = cost_function(Y, b, w, X)
        cost_history.append(mse)

        if i % 100 == 0:
            print("iter={:d}    b={:.2f}    w={:.4f}    mse={:.4}".format(i, b, w, mse))

    print("After {0} iterations b = {1}, w = {2}, mse = {3}".format(num_iters, b, w, cost_function(Y, b, w, X)))
    return cost_history, b, w


df = pd.read_csv("datasets/advertising.csv")

X = df["radio"]
Y = df["sales"]

# hyper parameters
learning_rate = 0.001
initial_b = 0.001
initial_w = 0.001
num_iters = 100000

cost_history, b, w = train(Y, initial_b, initial_w, X, learning_rate, num_iters)
