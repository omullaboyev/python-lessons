# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:34:26 2021

@author: omon
"""

# =============================================================================
# car_0 = {"model":"ferrari", "rang":"qizil"}
# print(car_0["model"])
# print(car_0["rang"])
# =============================================================================

# =============================================================================
# en_uz = {"apple":"olma", "apricot":"o'rik", "banana":"banan"}
# print(en_uz)
# print(en_uz["apple"])
# =============================================================================

# =============================================================================
# mevalar = {"olma":10000, "tarvuz":8000, "qovun":10000}
# print(f"Olma narhi {mevalar['olma']} so'm")
# print(f"Tarvuz narhi {mevalar['tarvuz']} so'm")
# print(f"Qovun narhi {mevalar['qovun']} so'm")
# =============================================================================


# =============================================================================
# talaba_0 = {"ism":"murod olimov", "yosh":20, "t_yil":2000}
# print(f"Talaba {talaba_0['ism'].title()},\
#       {talaba_0['t_yil']} - yilda tug'ilgan,\
#       {talaba_0['yosh']} - yoshda")
# talaba_0["kurs"] = 4
# talaba_0["fakultet"] = "informatika"
# talaba_0["ism"] = "abdulloh"
# =============================================================================

# =============================================================================
# talaba_1 = {}
# talaba_1["ism"] = "qobil rasulov"
# talaba_1["kurs"] = 3
# talaba_1["yosh"] = 20
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} - kurs")
# 
# talaba_1["kurs"] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} - kurs")
# =============================================================================
# =============================================================================
# talaba_0 = {"ism":"murod olimov", "yosh":20, "t_yil":2000}
# print(talaba_0)
# del talaba_0["yosh"]
# print(talaba_0)
# =============================================================================

# =============================================================================
# en_uz = {"apple":"olma", "apricot":"o'rik", "banana":"banan"}
# print(en_uz)
# del en_uz["banana"]
# print(en_uz)
# =============================================================================

telefonlar = {
    "ali":"iphone x",
    "vali":"galaxy s30",
    "olim":"mi 10 pro",
    "orif":"nokia 3310",
    "anvar":"pixel 3xl"
    }
print(telefonlar)

phone = telefonlar["ali"]
print(f"Alining telefoni {phone}")

phone = telefonlar.get("ali", "Bunday ism mavjud emas")
print(phone)

phone = telefonlar.get("hasan", "Bunday ism mavjud emas")
print(phone)

phone = telefonlar.get("hasan")
print(phone)


en_uz = {"apple":"olma", "apricot":"o'rik", "banana":"banan"}
meva = en_uz.get("apple", "Bunday meva mavjud emas")
print(meva)
en_uz = {"apple":"olma", "apricot":"o'rik", "banana":"banan"}
meva = en_uz.get("pineapple", "Bunday meva mavjud emas")
print(meva)
meva = en_uz.get("grapes")
print(meva)