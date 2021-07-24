# Lists

mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik'] # mevalar ro'yxati
print(mevalar)
print(len(mevalar))
narxlar = [12000, 18000, 10900, 22000]
print(narxlar)
print(len(narxlar))
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
print(sonlar)
ismlar = [] # bo'sh ro'yxat
print(ismlar)
print('Birinchi meva:', mevalar[0]) # pythonda index raqami 0 dan boshlanadi 1 dan emas
print("Ikkinchi meva:", mevalar[1])
print("Uchinchi meva:", mevalar[2])
print("To'rtinchi meva:", mevalar[3])
print("Listdagi oxirgi narx:",  narxlar[-1]) # minus index orqali murojat qilish

print('Birinchi meva:', mevalar[0].title())
print("Ikkinchi meva:", mevalar[1].title())
print("Uchinchi meva:", mevalar[2].title())
print("To'rtinchi meva:", mevalar[3].title())


print('Birinchi meva:', mevalar[0].upper())
print("Ikkinchi meva:", mevalar[1].upper())
print("Uchinchi meva:", mevalar[2].upper())
print("To'rtinchi meva:", mevalar[3].upper())

print(narxlar[0] + narxlar[1])
print(narxlar[2] + narxlar[3])
print(narxlar[2] + 40000)

mevalar[0] = 'anor'
print(mevalar[0])
print(mevalar)
mevalar[-1] = 'uzum'
print(mevalar)

# ro'yxatni oxiridan obyekt qo'shish
# .append
mevalar.append('nok')
mevalar.append('behi')
print(mevalar)
print(mevalar[-1])

# ma'lum bir joyga obyekt qo'shish
# .insert
mevalar.insert(0, 'banan')
print(mevalar)
mevalar.insert(3, 'tarvuz')
print(mevalar)
mevalar.insert(1, 'mandarin')
print(mevalar)
print()

cars = []
cars.append('Lacetti')
cars.append('Nexia')
cars.append('Matiz')
cars.append('Spark')
print(cars)
for i in range(0, 4):
    car = input("Add a car to the list: ")
    cars.append(car.title())
print(cars)

# listdan elemenlarni o'chirish
del cars[-1]
print(cars)
del cars[0]
print(cars)
cars.append('Malibu')
cars.insert(2, 'Tracker')
print(cars)
cars.remove('Matiz')
print(cars)

hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
print(hayvonlar)
hayvonlar.remove('mushuk')
print(hayvonlar)

bozorlik = ['yog\'', 'un', 'piyoz', 'banan', 'go\'sht']
print(bozorlik)
mahsulotlar = bozorlik.pop(1)
print(mahsulotlar)
print(bozorlik)
print("Olinmagan mahsulotlar:", bozorlik)



# Homeworks

ismlarr = ['john', 'bob', 'oppo_doda']

print("Salom", ismlarr[0].title(), 'bugun choyxona bormi?')
print('Salom', ismlarr[1].title(), 'bugun choyxona bormi?')
print('Salom', ismlarr[2].title(), 'bugun choyxona bormi?')
print()
print(ismlarr[0].title(), "choyxonaga boramizmi?")
print(ismlarr[1].title(), 'choyxonaga boramizmi?')
print(ismlarr[2].title(), 'choyxonaga boramizmi?')

numbers = [-1, 10, 10.5, 100, 95]
print(numbers)
numbers[0] = 1
print(numbers)
print(numbers[1] + 50)
numbers[-2] = numbers[-2] + 5
print(numbers)
numbers.insert(1, 50)
print(numbers)
numbers[3] = str(numbers[3])
print(numbers)
t_shaxslar = ['imom buxoriy', 'alisher navoiy', 'ahmad yassaviy']
z_shaxslar = ['bill gates', 'ilon mask', 'jim rohn']
print('Men tarixiy shaxslardan', t_shaxslar.pop(0).title(), 'bilan, zamonaviy shaxslardan esa', z_shaxslar.pop().title(), 'bilan suhbat qilishni istar edim.')
print(t_shaxslar)
print(z_shaxslar)
friends = []
friends.append("alisher")
friends.append("doter")
friends.append("molan")
friends.append("sardor")
friends.append("salim")
print(friends)
friends.remove("alisher")
friends.remove('doter')
friends.remove('molan')
friends.remove('sardor')
friends.remove('salim')
print(friends)

