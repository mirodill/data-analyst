import pandas as pd

# a = pd.read_csv("data.csv", header=None)
# b = pd.read_csv("data.csv", skiprows=2)
c = pd.read_csv("data.csv", decimal=".")

# print(c)

'''
| Parametr      | Vazifasi                           |
| ------------- | ---------------------------------- |
| `sep`         | ajratgich belgisi                  |
| `header`      | birinchi qator ustun nomi bo‘lishi |
| `names`       | ustun nomlarini berish             |
| `index_col`   | index o‘rnatish                    |
| `usecols`     | faqat tanlangan ustunlarni o‘qish  |
| `nrows`       | nechta qator o‘qish                |
| `skiprows`    | yuqoridan qator tashlash           |
| `encoding`    | kodlash turi                       |
| `parse_dates` | sanani datetimega aylantirish      |
| `na_values`   | Null bo‘ladigan qiymatlar ro‘yxati |
'''

df = pd.read_csv("data.csv")
# df["city"].fillna("Unknown", inplace=True)
df["score"].fillna(df["score"].mean(), inplace=True)
tashkent_students = df[df["city"] == "Tashkent"]
result = df.groupby("city")["score"].mean()

# print(result)

# df = pd.read_excel("employees.xlsx", sheet_name="Sheet1")
# print(df)


# df = pd.DataFrame({
#     "name": ["Ali", "Vali", "Hasan"],
#     "age": [20, 25, 30]
# })

# df.to_csv("students.csv", index=False)


df = pd.DataFrame({
    "Name": ["Ali", "Vali", "Hasan", "Gulshan", "Malika"],
    "Age": [20, 25, 19, 23, 22],
    "Score": [85, 90, 88, 92, 95]
})

# print(df.head())        # 1. dastlabki 5 qator
# print(df.tail())        # 2. oxirgi 5 qator
# print(df.info())        # 3. to'liq ma'lumot
# print(df.describe())    # 4. statistik ma'lumotlar
# print(df.shape)         # 5. o'lcham
# print(df.columns)       # 6. ustun nomlari
# print(df.index)         # 7. indekslar
# 1. Ustun tanlash
print(df["Name"])
print(df[["Name", "Score"]])

# 2. Yangi ustun qo‘shish
df["Status"] = df["Age"].apply(lambda x: "Yosh" if x < 23 else "Katta")

# 3. Ustunni o‘chirish
df.drop(columns=["Score"], inplace=True)

# 4. Indeksni o‘rnatish
df = df.set_index("Name")

# 5. loc bilan qator tanlash
print(df.loc["Ali"])

# 6. iloc bilan qator tanlash
print(df.iloc[0])

# 7. Shart bilan tanlash
print(df[df["Age"] > 20])
'''
| Funksiya           | Vazifasi                   |
| ------------------ | -------------------------- |
| `df["column"]`     | Ustun tanlash              |
| `df.drop()`        | Ustun yoki qator o‘chirish |
| `df.set_index()`   | Indeksni o‘zgartirish      |
| `df.loc[]`         | Nom bo‘yicha tanlash       |
| `df.iloc[]`        | Raqam bo‘yicha tanlash     |
| `df.reset_index()` | Indeksni qaytarish         |
'''

# 1. Age bo'yicha o'sish
print(df.sort_values("Age"))

# 2. Score bo'yicha kamayish
print(df.sort_values("Score", ascending=False))

# 3. Ikki ustun bo'yicha saralash
print(df.sort_values(["Age", "Score"], ascending=[True, False]))

# 4. Indeks bo'yicha saralash
print(df.sort_index())

# 5. Ustunlarni saralash
print(df.sort_index(axis=1))

'''
| Funksiya                   | Vazifasi                     |
| -------------------------- | ---------------------------- |
| `sort_values()`            | Ustun(lar) bo‘yicha saralash |
| `sort_index()`             | Indeks bo‘yicha saralash     |
| `ascending=True/False`     | O‘sish / kamayish            |
| `na_position="first/last"` | NaN bosh/oxirga              |
| `inplace=True`             | Joyida saralash              |
'''

# df = pd.DataFrame({
#     "Name": ["Ali", "Vali", "Hasan", "Gulshan"],
#     "Age": [20, None, 19, 23],
#     "Score": [88, 92, np.nan, 85],
#     "Country": [None, "Uzbekistan", None, "Kazakhstan"]
# })

# # 1. Qaysi joyda Null bor?
# print(df.isnull())

# # 2. Har bir ustundagi bo'sh qiymatlar soni
# print(df.isnull().sum())

# # 3. Faqat Age bo'sh bo'lgan qatorlar
# print(df[df["Age"].isnull()])

# # 4. Nulllarni o'chirish
# df_clean = df.dropna()

# # 5. Nulllarni 0 bilan to'ldirish
# df_fill_zero = df.fillna(0)

# # 6. Age ustunini o'rtacha qiymat bilan to'ldirish
# df["Age"] = df["Age"].fillna(df["Age"].mean())

# # 7. Matn ustunini Unknown bilan to'ldirish
# df["Country"] = df["Country"].fillna("Unknown")

# # 8. Forward fill va Backward fill
# df_ffill = df.fillna(method="ffill")
# df_bfill = df.fillna(method="bfill")
'''
| Funksiya    | Vazifasi                        |
| ----------- | ------------------------------- |
| `isnull()`  | Bo‘sh qiymatlarni aniqlaydi     |
| `notnull()` | Bo‘sh bo‘lmaganlarni aniqlaydi  |
| `dropna()`  | Bo‘sh qiymatlarni o‘chiradi     |
| `fillna()`  | Bo‘sh qiymatlarni to‘ldiradi    |
| `replace()` | NaN qiymatlarni almashtiradi    |
| `ffill`     | Oldingi qiymat bilan to‘ldirish |
| `bfill`     | Keyingi qiymat bilan to‘ldirish |
'''

import pandas as pd

df = pd.DataFrame({
    "City": ["Toshkent", "Toshkent", "Samarqand", "Samarqand", "Buxoro"],
    "Sales": [120, 150, 100, 130, 90],
    "Employees": [10, 8, 6, 7, 5]
})

print(df)
