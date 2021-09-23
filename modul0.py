# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:55:34 2021

@author: omon
"""

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


def avto_kirit():
    """Foydaslanuvchiga avto_info funksiyais yordamida bir nechta avtolar haqida ma'lumotlarni bittadan kiritish imkonini beradi"""
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

        
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar kiritinlgan lug'atni konsolga chiqaruvchi funksiya"""
    print("\nSalonimizdagi avtolar:")
    for avto in avtolar:
        if avto["narh"]:
            narh = avto["narh"]
        else:
            narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")