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
print(e)
'''
| Funksiya        | Vazifasi                          |
| --------------- | --------------------------------- |
| `reshape()`     | massiv shaklini o‘zgartirish      |
| `flatten()`     | massivni 1D ga aylantirish (copy) |
| `T`             | transpozitsiya (qator ↔ ustun)    |
| `expand_dims()` | yangi o‘lcham qo‘shish            |
| `squeeze()`     | 1-o‘lchamlarni olib tashlash      |
'''