# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 01:52:44 2021

@author: omon
"""

# =============================================================================
#*ARGS
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     #return sum(sonlar)
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# 
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))
# print(summa(1))
# print(summa())
# =============================================================================


# =============================================================================
# def summa(x, y, *sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x + y + sum(sonlar)    
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))
# print(summa(1))
# =============================================================================


# =============================================================================
#**KWARGS
# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar["kompaniya"] = kompaniya
#     malumotlar["model"] = model
#     return malumotlar
# 
# avto1 = avto_info("GM", "malibu", rang = "qora", yil = 2018)
# avto2 = avto_info("KIA", "K5", rang = "qizil", narh = 35000, yil = 2020, korobka = "avtomat")
# 
# avtolar = [avto1, avto2]
# print(avtolar)
# =============================================================================
