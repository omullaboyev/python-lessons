# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 01:36:38 2021

@author: omon
"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar;

talabalar = ["ali", "vali", "hasan", "husan"]
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)