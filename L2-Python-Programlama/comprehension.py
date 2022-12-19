# Comprehensions

# List Comprehension

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

comp_list = [new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

# Maaşı  2 katına çıkar

[salary * 2 for salary in salaries]

# Maaşı 3000 den küçük olanları iki katına çıkar

[salary * 2 for salary in salaries if salary < 3000]

# Maaşı 3000 den yukarısı için else ekleyelim

[salary * 2 if salary < 3000 else new_salary(salary * 0) for salary in salaries]

#################################

# students no da olmayanarı büyük yapacak, var olmayanları küçük yapacak
students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

stud_list = [student.lower() if student in students_no else student.upper() for student in students]
stud_list_2 = [student.upper() if student not in students_no else student.lower() for student in students]

############################### Dict Comprehension

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

dictionary.keys()
dictionary.values()
dictionary.items()

# valueların değerinin karesi alınsın
{k: v ** 2 for (k, v) in dictionary.items()}

# keyler büyük harf ile yazılsın
{k.upper(): v for (k, v) in dictionary.items()}

############ MÜLAKAT SORUSU ############

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# keyler orijinal değerler value'lar ise değiştirilmiş değerler olacak

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

results_list = {n: n ** 2 for n in numbers if n % 2 == 0}

#################### List & Dict Comprehension Uygulamalar ####################

# Bir veri setindeki değişken isimlerini değiştirmek

# before
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'abbrev']

# after
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'ABBREV']

import seaborn as sns

df = sns.load_dataset("car_crashes")

a = []
[a.append(col.upper()) for col in df.columns]

df.columns = [col.upper() for col in df.columns]

# İsminde  "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG ekleyiniz

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

# Amaç key'i string, value'su aşağıdaki gibi bir liste olacak sözlük oluşturmak
# Bu işlemi sadece sayısal değişkenler için yapmak istiyoruz

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col.lower()] = agg_list

# kısa yol
new_dic = {col: agg_list for col in num_cols}

df[num_cols].head()

# her columnda aggreagation uygulama
df[num_cols].agg(new_dic)
