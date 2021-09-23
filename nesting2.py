# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:49:45 2021

@author: omon
"""

#LUG'AT ICHIDA RO'YXAT - LIST IN DICT
# =============================================================================
# dasturchilar = {
#                "ali":["python", "c++"],
#                "vali":["html", "css", "js"],
#                "hasan":["php", "sql"],
#                "husan":["python", "php"],
#                "maryam":["c++", "c#"]
#                }
# for ism, tillar in dasturchilar.items():
#     print(f"{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())
#         
#         
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()} ", end="*")
# =============================================================================

hamkasblar = {
             "ali": {"familiya":"valiev",
                     "tyil":1995,
                     "malumot":"oliy",
                     "tillar":["python", "c++"]
                    },
             "vali": {"familiya":"aliev",
                     "tyil":2001,
                     "malumot":"o'rta-maxsus",
                     "tillar":["html", "css", "js"]
                    },
             "hasan": {"familiya":"husanov",
                     "tyil":1999,
                     "malumot":"maxsus",
                     "tillar":["python", "php"]
                    }
             }
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()} "
          f"{info['tyil']} - yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. "
          f"Quyidagi dasturlash tillarini biladi:")
    for til in info["tillar"]:
        print(f"{til.upper()} ", end="")