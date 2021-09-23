# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 00:36:20 2021

@author: omon
"""

# =============================================================================
# ism = input("Ismingiz nima? >>>")
# savol = f"Salom, {ism.title()}, yoshingiz nechchida? >>>"
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz nechchi metr? >>>")
# height = float(height)
# =============================================================================

# =============================================================================
# son = 1
# while son <=5:
#     print(son, end=" ")
#     son += 1
# print("Dastur tugadi")
# =============================================================================

# =============================================================================
# print("Istalgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing) >>> "
# qiymat = ""
# while qiymat != "exit":
#     qiymat = input(savol)
#     if qiymat!="exit":
#         print(float(qiymat)**2)
# print("Dastur tugadi")
# =============================================================================

# =============================================================================
#ISHORA - FLAG
# print("Istalgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing) >>> "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat=="exit":
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur to'xtadi")
# =============================================================================

# =============================================================================
# #WHILE + BREAK
# print("Istalgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing) >>> "
# while True: #abadiy tsikl
#     qiymat = input(savol)
#     if qiymat=="exit":
#         break #tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi!")
# =============================================================================


# =============================================================================
#FOR + BREAK
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f"{son} ning kvadrati {son**2} ga teng")
# =============================================================================

# =============================================================================
#FOR + CONTINUE
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue    
#     print(f"{son} ning kvadrati {son**2} ga teng")
# =============================================================================


# =============================================================================
#WHILE + CONTINUE
# son = 0
# while son < 10:
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
# =============================================================================

#infinite loop
# =============================================================================
# son = 0
# while son < 10:
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)  
# =============================================================================
# =============================================================================
# INFINITE LOOP
# son = 1
# while son > 0:
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)  
# =============================================================================
