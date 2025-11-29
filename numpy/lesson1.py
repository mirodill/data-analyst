# NumPy – raqamli massivlar (ndarray) bilan ishlovchi eng tezkor Python kutubxonasi.
import numpy as np # Numpyni import qilish

# ------ Array yaratish ------
arr  = np.array([1,2,3,4,5,6]) # bir o'lchamli massiv
arr2 = np.array([[1,2,3], # ikki o'lchovli massiv
                 [4,5,6]])
arr3 = np.array([[[1,2,3], # uch o'lchovli massiv
                  [4,5,6],
                  [7,8,9]]])
zeros = np.zeros((2, 3)) # Nolga to'ldirilgan massiv yaratadi
ones = np.ones((2, 3)) # Birga to'ldirilgan massiv
full = np.full((2, 3), 7) # Berilgan qiymatga to'ldiradi
arange_arr = np.arange(0, 10, 2) # Oraliq bo'yicha array
lin = np.linspace(0, 10, 5) # Chiziqli taqsimlangan sonlar
rand = np.random.rand(2, 3) # Tasodifiy sonlar
rand_int = np.random.randint(0, 10, (2, 3))
# print(rand_int)

# ------ Massiv atributlari ------
arr = np.array([[1,2,3],[4,5,6]])
shape = arr.shape # Massiv o'lchami (qator, ustun)
ndim = arr.ndim # O'lchamlar soni (dimension)
size = arr.size # Massiv ichida nechta umumiy element borligini qaytaradi.
dtype = arr.dtype # Ma'lumot turi
astype = arr.astype(float) # Ma'lumot turini o'zgartirish
# print(astype)

# ------ Indexlash va kesish ------
arr = np.array([10,20,30,40])
a = arr[1] # Oddiy indekslash 
b = arr[1:3] # Start - end 
c= arr[::-1] # Teskari tartiblash
arr2 = np.array([[1,2,3],
                 [4,5,6]])
d = arr2[1, 2] # 2D massivlarda indekslash
e = arr2[:, 1] # Butun ustunni olish
# print(e)
'''
| Ko‘rinish | Ma’nosi                      |
| --------- | ---------------------------- |
| `a[i]`    | i-element                    |
| `a[i:j]`  | i dan j gacha (j kirmaydi)   |
| `a[::-1]` | teskari massiv               |
| `b[i, j]` | i-qator, j-ustun elementi    |
| `b[:, j]` | barcha qatorlarning j-ustuni |
| `b[i, :]` | i-qatorning barcha ustunlari |
'''

# ------ Array shaklini o'zgartirish -------
arr = np.array([[1,2,3],[4,5,6]])
a = arr.reshape(2, 3) # O'lchamni o'zgartirish
b = arr.flatten() # Ko'p o'lchamli massivni 1D ga aylantirish
c = arr.T # Transpozitsiya
d = np.array([[[1,2,3]]])
e = np.squeeze(d) # Keraksiz 1-o'lchamlarni olib tashlash
# print(e)
'''
| Funksiya        | Vazifasi                          |
| --------------- | --------------------------------- |
| `reshape()`     | massiv shaklini o‘zgartirish      |
| `flatten()`     | massivni 1D ga aylantirish (copy) |
| `T`             | transpozitsiya (qator ↔ ustun)    |
| `expand_dims()` | yangi o‘lcham qo‘shish            |
| `squeeze()`     | 1-o‘lchamlarni olib tashlash      |
'''

# ------ Matematik funksiyalar ------

# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# print("a + b:", a + b)
# print("a - b:", a - b)
# print("a * b:", a * b)
# print("a / b:", a / b)
# print("a ** 2:", a ** 2)


# ------ Statistika ------
nums = np.array([1,2,3,4,5])
mean = np.mean(nums) # O'rtacha qiymat Massivdagi barcha sonlarning o‘rtacha qiymatini qaytaradi.
median = np.median(nums) # Raqamlar tartiblangan holda o‘rtadagi qiymat. Agar juft element bo‘lsa → 2 ta o‘rta qiymatning o‘rtachasi olinadi.
std = np.std(nums) # Standart og'ish Ma’lumot qanchalik tarqalganini ko‘rsatadi. Qiymatlar o‘rtachadan qanchaga uzoq — shuni o‘lchaydi.
minn = np.min(nums) # Eng kichik son
maxx = np.max(nums) # Eng katta son
per = np.percentile(nums, 50) # 50 percentil
# print(per)
'''
| Funksiya     | Nimani beradi                   |
| ------------ | ------------------------------- |
| `mean`       | o‘rtacha qiymat                 |
| `median`     | o‘rtadagi qiymat                |
| `std`        | qiymatlar tarqalishi            |
| `min`        | eng kichik qiymat               |
| `max`        | eng katta qiymat                |
| `percentile` | foiz bo‘yicha chegaraviy qiymat |
'''
# ------ Agregat funksiyalar ------ 

nums = np.array([1,2,3,4,5])
summ = np.sum(nums) # Barcha elementlar yig'indisi
prod = np.prod(nums) # Barcha sonlar ko'paytmasi
cums = np.cumsum(nums) # Yig'indilar ketma-ketligi
cump = np.cumprod(nums) # Ko'paytmalar ketma-ketligi
# print(cump)
'''
| Funksiya           | Vazifasi                      | Misol natija |
| ------------------ | ----------------------------- | ------------ |
| `np.sum(nums)`     | Barcha elementlar yig‘indisi  | 10           |
| `np.prod(nums)`    | Barcha elementlar ko‘paytmasi | 24           |
| `np.cumsum(nums)`  | Har bosqichdagi jamlanma      | `[1 3 6 10]` |
| `np.cumprod(nums)` | Har bosqichdagi ko‘paytma     | `[1 2 6 24]` |
'''
# ------ Massivlarni birlashtirish ------
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])
conc = np.concatenate([a, b, c]) # Massivlarni qo‘shib bitta massiv qilish
vstack = np.vstack([a, b]) # Massivlarni pastga qarab, ya’ni vertikal tarzda qo‘shadi. Natija 2D massiv bo‘ladi.
hstack = np.hstack([a, b]) # Massivlarni yonma-yon, ya’ni horizontal tarzda qo‘shadi.
# print(hstack)
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6]])

#print(np.vstack([A, B]))     # pastga qo'shish
#print(np.hstack([A, B.T]))   # yonma-yon qo'shish
'''
| Funk­siya       | Ma’nosi                         | Natija turi                |
| --------------- | ------------------------------- | -------------------------- |
| **concatenate** | Oddiy qo‘shish                  | 1D yoki mavjud shaklga mos |
| **vstack**      | Vertikal qo‘shish (ustma-ust)   | 2D massiv                  |
| **hstack**      | Gorizontal qo‘shish (yonma-yon) | 1D yoki 2D                 |
'''

# ------ Random ------ 
#np.random.seed(42) # Tasodifiy sonlarni takrorlanadigan qilish
# print(np.random.rand(3, 3))

nums = np.random.randint(1, 10, 5)
# print(nums)

# ------ Mantiqiy operatorlar ------
arr = np.array([10, 20, 30])

# print(arr > 15)
# print(arr < 25)
# print(arr == 20)
# print(arr != 30)

arr = np.array([10, 20, 30, 40, 50])

# 30 dan katta elementlar
print(arr[arr > 30])

# 10–40 oralig‘idagi elementlar
print(arr[(arr >= 10) & (arr <= 40)])

# 40 dan katta mavjudmi?
print(np.any(arr > 40))

# Barcha elementlar 5 dan katta ekanligini tekshirish
print(np.all(arr > 5))

# Indekslarni olish
print(np.where(arr > 25))
'''
| Amallar           | Ma’nosi                      |
| ----------------- | ---------------------------- |
| `arr > 10`        | Boolean array                |
| `np.where(shart)` | Shartga mos indekslar        |
| `np.any(shart)`   | Kamida 1 ta True bo‘lsa True |
| `np.all(shart)`   | Barchasi True bo‘lsa True    |
| `&`               | AND                          |
| `\|`              | OR                           |
| `~`               | NOT                          |
| `arr[shart]`      | Filtrlash                    |
'''