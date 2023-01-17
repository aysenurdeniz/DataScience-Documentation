# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
df = pd.read_csv("L2-Python-Programlama/project/persona.csv")
df.head(5)

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].unique().__len__()
df["SOURCE"].value_counts()

# Soru 3: Kaç unique PRICE vardır?

df["PRICE"].unique().__len__()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
# Soru 7: SOURCE türlerine göre satış sayıları nedir?
# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?