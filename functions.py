# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:56:51 2021

@author: omon
"""

# =============================================================================
# def salom_ber():
#     """Salom beruvchi funktsiya"""
#     print("Assalomu alaykum!")
#     
# salom_ber()
# =============================================================================

# =============================================================================
# def salom_ber(ism):
#      """Foydalanuvchi ismini qabil qilib,
#      unga salom beruvchi funktsiya"""
#      print(f"Assalomu alaykum, hurmatli {ism.title()}!")
#      
# salom_ber("hasan")
# salom_ber("olim")
# =============================================================================

def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funktsiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
    
# =============================================================================
# toliq_ism("olim", "hakimov")
# toliq_ism("hakimov", "olim")
# =============================================================================


# =============================================================================
# def  yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2021 - tugilgan_yil} yoshda")
#     
# yosh_hisobla("ali", 2011)
# yosh_hisobla(tugilgan_yil = 2011, ism = "ali")
# 
# toliq_ism(familiya = "hakimov", ism = "olim")
# =============================================================================

def yosh_hisobla(tugilgan_yil, joriy_yil = 2021):
    """Foydalauvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")
    
yosh_hisobla(1980, 2021)
yosh_hisobla(2011)