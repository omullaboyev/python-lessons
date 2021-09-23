# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 23:05:16 2021

@author: omon
"""

# =============================================================================
# import auto_info_mod as aim
# auto1 = aim.avto_info("GM", "Captiva", "qora", "avtomat", 2020, 40000)
# aim.info_print(auto1)
# =============================================================================

# =============================================================================
# from auto_info_mod import avto_info, info_print
# auto1 = avto_info("GM", "Captiva", "qora", "avtomat", 2020, 40000)
# info_print(auto1)
# =============================================================================

# =============================================================================
# from auto_info_mod import avto_info as ainfo, info_print as iprint
# auto1 = ainfo("GM", "Captiva", "qora", "avtomat", 2020, 40000)
# iprint(auto1)
# =============================================================================

# =============================================================================
# from auto_info_mod import *
# auto1 = avto_info("GM", "Captiva", "qora", "avtomat", 2020, 40000)
# info_print(auto1)
# =============================================================================

# =============================================================================
# from auto_info_mod import avto_kirit, avto_info, info_print
# avtolar = avto_kirit()
# for avto in avtolar:
#     info_print(avto)
# =============================================================================

# =============================================================================
# import math
# print("Ildiz: ", math.sqrt(400))
# print("Power: ", math.pow(5, 3))
# print("PI: ", math.pi)
# print("Logarifm 2: ", math.log2(8))
# print("Logarifm 10: ", math.log10(100))
# =============================================================================


import random as r
# =============================================================================
# son = r.randint(0, 100)
# print(son)
# 
#choice
# ismlar = ["olim", "anvar", "hasan", "husan"]
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))
# =============================================================================

# =============================================================================
# x = list(range(0, 51, 5))
# print(x)
# print(r.choice(x))
# =============================================================================

#shuffle()
x = list(range(11))
print(x)
r.shuffle(x)
print(x)