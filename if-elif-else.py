# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 02:54:34 2021

@author: omon
"""

# =============================================================================
# son = 50
# if son < 0:
#     print("Manfiy")
# else:
#     print("Musbat")
# =============================================================================


# =============================================================================
# yosh = int(input("Yoshingiz necchida?\n>>>"))
# if yosh <= 4:
#     print("Sizga kirish bepul")
# elif yosh <= 12:
#     print("Sizga kirish 5 000 so'm")
# elif yosh <= 18:
#     print("Sizga kirish 8 000 so'm")
# else:
#     print("Sizga kirish 10 000 so'm")
# =============================================================================


# =============================================================================
# yosh = int(input("Yoshingiz necchida?\n>>>"))
# if yosh <= 4:
#     narh = 0
# elif yosh <= 12:
#     narh = 5000
# elif yosh <= 18:
#     narh = 8000
# else:
#     narh = 1000
# print(f"Sizga kirish {narh} so'm")
# =============================================================================

# =============================================================================
#IF + OR
# kun = input("Bugun qaysi kun?\n>>>")
# if kun.lower()=="shanba" or kun.lower() == "yakshanba":
#     print("Dam olish kuni")
# else:
#     print("Ish kuni")
# =============================================================================

# =============================================================================
# kun = input("Bugun qaysi kun?\n>>>")
# harorat = float(input("Havo harorati qanday?>>>"))
# if (kun.lower()=="yakshanba" or kun.lower()=="shanba") and harorat >= 30:
#     print("Cho'milgani ketdik :)")
# elif (kun.lower()=="yakshanba" or kun.lower()=="shanba") and harorat < 30:
#     print("Uyda dam olamiz :(")
# else:
#     print("Ishga boramiz :(")
# =============================================================================


# =============================================================================
# narh = 15000
# choy = True
# salat = False
# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
# else:
#     narh = narh
# print(f"Jami: {narh}")
# =============================================================================


# =============================================================================
# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
# print(f"Jami {narh} so'm")
# =============================================================================

#True = 1, False = 0
# =============================================================================
# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1
# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
# print(f"Jami {narh} so'm")
# =============================================================================

# =============================================================================
# #IN OPERATORI
# menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
# ovqat = input("Nima ovqat yeysiz: ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print(f"Bizda {ovqat} yoq")
# =============================================================================
    
# =============================================================================
# #NOT IN OPERATORI
# menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
# ovqat = input("Nima ovqat yeysiz: ")
# if ovqat.lower() not in menu:
#     print(f"Bizda {ovqat} yoq")
# else:
#     print("Buyurtma qabul qilindi")
# =============================================================================

menu = ["osh", "qozonkabob", "shashlik", "norin", "somsa"]
#buyurtmalar = []
buyurtmalar = ["osh", "somsa", "manti", "shashlik"]
if buyurtmalar:
    print(f"{len(buyurtmalar)}ta buyurtma berildi")
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else:
    print("Buyurtmalar ro'yhati bo'sh")