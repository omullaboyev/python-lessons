# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:48:10 2021

@author: omon
"""

# =============================================================================
# talaba_0 = {
#             "ism": "alijon",
#             "familiya":"shamshiyev",
#             "yosh":22,
#             "fakultet": "matematika",
#             "kurs":4
#            }
# print(talaba_0.items())
# print(talaba_0["ism"])
# print(talaba_0["yosh"])
# print(talaba_0["familiya"])
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"qiymat: {qiymat}\n")
# =============================================================================

# =============================================================================
# telefonlar = {"ali":"iphone x", "vali":"galaxy s9", "olim":"mi 10 pro", "orif":"nokia 3310"}
# for k, v in telefonlar.items():
#     print(f"{k.title()}ning telefoni {v.title()}")
# =============================================================================


#.keys
# =============================================================================
# mahsulotlar = {"olma":10000, "anor":20000, "uzum":40000, "anjir":25000, "shaftoli":30000}
# 
# print(mahsulotlar.keys())
# print(mahsulotlar.values())
# 
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
# =============================================================================
    

# =============================================================================
# mahsulotlar = {"olma":10000, "anor":20000, "uzum":40000, "anjir":25000, "shaftoli":30000}
# bozorlik = ["anor", "uzum", "non", "baliq"]
# print("Do'konda bor mahsulotlar")
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#         
# 
# print("\nDo'konda yo'q mahsulotlar")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do'koningizga {buyum} ham olib keling")
#         
#         
# print("\nDo'konimizdagi mahsulotlar")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# =============================================================================


# =============================================================================
# telefonlar = {"ali":"iphone x", "vali":"galaxy s9", "olim":"mi 10 pro", "orif":"nokia 3310"}
# print(telefonlar.values())
# 
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for tel in telefonlar.values():
#     print(tel)
# =============================================================================


telefonlar = {
              "ali":"iphone x",
              "vali":"galaxy s9",
              "olim":"mi 10 pro",
              "orif":"nokia 3310",
              "hamida":"galaxy s9",
              "maryam":"huawei p30",
              "tohir":"iphone x",
              "umar":"iphone x"
              }
# =============================================================================
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for tel in telefonlar.values():
#     print(tel)
# =============================================================================
    
# =============================================================================
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for tel in set(telefonlar.values()):
#     print(tel)
# =============================================================================


#SET
toys = {"ball", "car", "lamp", "ball", "bear", "car"}
print(type(toys))
print(toys)