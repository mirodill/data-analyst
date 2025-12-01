import pandas as pd
# Series - bu bitta ustundan iborat ma’lumotlar to‘plami. Har bir elementning yonida index (indeks) bo‘ladi.
a = pd.Series([10,20,30]) # List array
b = pd.Series({"a": 10, "b": 20, "c": 30}) # Dictionary array
c = a[:2]
# print(c)
# DataFrame — bu jadval ko‘rinishidagi ma’lumotlar tuzilmasi.
data = {
    "name": ["Ali", "Vali", "Hasan"],
    "age": [20, 25, 30]
}

df = pd.DataFrame(data)
print(df)

