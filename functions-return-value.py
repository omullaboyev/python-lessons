# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 00:43:23 2021

@author: omon
"""

# =============================================================================
# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
#     
# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")
# =============================================================================

# =============================================================================
# def toliq_ism_yasa(ism, familiya, otasining_ismi = ""):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"    
#     return toliq_ism.title()
# 
# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov", "abrorovich")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# =============================================================================


#=============================================================================
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {
            "kompaniya": kompaniya,
            "model": model,
            "rang": rangi,
            "korobka": korobka,
            "yil": yili,
            "narh": narhi
            }
    return avto
# 
# avto1 = avto_info("GM", "Malibu", "qora", "Avtomat", 2018)
# avto2 = avto_info("GM", "Gentra", "oq", "Mexanika", 2016, 15000)
# 
# print(f"avto1: {avto1}")
# print(f"avto2: {avto2}")
# 
# avtolar = [avto1, avto2]
# print(f"avtolar: {avtolar}\n")
# print("Onlayn bozordagi mavjud avtolar")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
# =============================================================================
    

# =============================================================================
# def oraliq(min, max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# 
# print(oraliq(0,10))
# print(oraliq(10,21))
# =============================================================================
        
# =============================================================================
# def oraliq(min, max, qadam = None):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         if qadam:
#             min += qadam
#         else:
#             min += 1
#     return sonlar
# 
# print(oraliq(0,5,))
# print(oraliq(0,10,2))
# print(oraliq(10,21,3))
# =============================================================================
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz")
avtolar = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting", end="")
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == "no":
        break
print("\nSalonimizdagi avtolar:")
for avto in avtolar:
     if avto["narh"]:
         narh = avto["narh"]
     else:
         narh = "Noma'lum"
     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
    