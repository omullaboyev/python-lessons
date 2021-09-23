# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 01:58:07 2021

@author: omon
"""

# =============================================================================
#CYCLE FOR
# mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# print(mehmonlar)
# for mehmon in mehmonlar:
#     print("Salom ", mehmon)
#     print("Hayr, ", mehmon)
# print("Yana keling ", mehmon)
# =============================================================================

# =============================================================================
#CYCLE FOR + fstring
# mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon} sizni oshga chaqiramiz")
#     print("Hurmat bilan Corvax\n")
# =============================================================================

# =============================================================================
#CYCLE FOR + list, range
# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} sonining kvadrati {son**2} ga teng")
# =============================================================================


# =============================================================================
#CYCLE FOR + list + range + list.append
# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)
# =============================================================================

dostlar = []
print("5 ta eng yaqin do'stingi kim")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting >>> "))
print(dostlar)
for dost in dostlar:
    print(dost)