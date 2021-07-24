son = -6
if son < 0:
    print("Manfiy son")
else:
    print('Musbat son')


# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     narh = 0
# elif yosh <= 12:
#     narh = 5000
# elif yosh <= 18:
#     narh = 8000
# else:
#     narh = 10000
# print(f'Sizga kirish {narh} so\'m.')

# or

# kun = input("Bugun nima kun? ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')


# and

# kun = input("Bugun nima kun? ")
# harorat = float(input('Havo harorati qanday? '))
#
# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30:
#     print('Cho\'milgani ketdik!')
# elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat < 30:
#     print('Uyda dam olamiz!')


# narx = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
#
# if choy:
#     print('Mijoz choy oldi.')
#     narx = narx + 3000
#
# if salat:
#     print('Mijoz salat oldi.')
#     narx = narx + 5000
#
# if non:
#     print('Mijoz non oldi.')
#     narx = narx + 2000
#
# if kompot:
#     print('Mijoz kompot sotib oldi.')
#     narx = narx + 5000
#
# if assorti:
#     print('Mijoz assorti oldi.')
#     narx = narx + 15000
#
# print(f'Jami {narx} so\'m.')


# in

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz? ')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q.')


# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
#
# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda True qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f'Menuda {taom} bor.')
#         else:
#             print(f'Kechirasiz, menuda {taom} yo\'q.')
# else: # agar ro'yxat bo'sh bo'lsa
#     print('Savatchangiz bo\'sh.')


# Home works

# raqam = int(input('Juft son kiriting: '))
# if raqam % 2 == 0:
#     print('Rahmat.')
# else:
#     print('Juft son emas.')
#
# age = int(input('Necha yoshdasiz? '))
# if age <= 4 or age >= 60:
#     cost = 0
# elif age <= 18:
#     cost = 10000
# else:
#     cost = 20000
#
# print(f'Siz uchun kirish {cost} so\'m.')
#
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
#
# if num1 > num2:
#     print('First number is bigger than second.')
# elif num1 < num2:
#     print('Second number is bigger than first.')
# else:
#     print('Both numbers are equal.')


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n + 1}-mahsulotni qo'shing: "))
#
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#     print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


foydalanuvchilar = ['oxunjon', 'sherzod', 'anvar', 'avaz', 'olim']
login = input('Yangi login tanlang: ')
if login in foydalanuvchilar:
    print('Login band yangi login tanlang!')
else:
    print('Xush kelibsiz!')


son = int(input('Istalgan butun son kiriting: '))
for n in range(2, 11):
    if not (son % n):
        print(f'{son} soni {n} ga qoldiqsiz bo\'linadi.')
