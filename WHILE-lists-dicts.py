# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 01:36:39 2021

@author: omon
"""

# =============================================================================
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n} - do'stingizning ismini kiriting >>> "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi (ha/yo'q)? >>> ")
#     n += 1
#     if takrorlash != "ha":
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
# =============================================================================

# =============================================================================
# print("Do'stlaringiz yoshini saqlaymiz")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting >>> ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting >>> ")
#     dostlar[ism] = int(yosh)
#     javob = input("Yana ma'lumot qo'shasizmi (ha/yo'q')? >>> ")
#     if javob!= "ha":
#         ishora = False
#         
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
# =============================================================================

# =============================================================================
# cars = ["lacetti", "nexia", "toyota", "nexia", "audi", "malibu", "nexia"]
# car = "lacetti"
# while car in cars:
#     cars.remove(car)
# print(cars)
# =============================================================================
talabalar = ["hasan", "husan", "olim", "botir"]
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting >>> ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)
for ism, baho in baholangan_talabalar.items():
    print(f"{ism.title()}ning bahosi {baho}")