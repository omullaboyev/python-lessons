# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:45:26 2021

@author: omon
"""

# =============================================================================
#LISTS
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
#narhlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2]
# sonlar = ["bir", "ikki", 3, 4, 5]
# ismlar = []
# =============================================================================

# =============================================================================
#LISTS INDEX
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])
# 
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())
# print("Uchinchi meva: ", mevalar[2].capitalize())
# 
# print(narhlar[2]+narhlar[3])
# =============================================================================

# =============================================================================
#LISTS APPEND\INSERT
# car_models = ["Toyota", "GM", "Volvo", "BMW", "Hyundai", "Kia", "Volkswagen"]
# mevalar.append("tarvuz")
# mevalar.insert(0, "banan")
# mevalar.insert(3, "banan")
# =============================================================================

# =============================================================================
# cars = []
# cars.insert(0, "Malibu")
# cars.insert(1, "Lacetti")
# cars.insert(2, "Tracker")
# cars.insert(3, "Nexia 3")
# print(cars)
# =============================================================================
# =============================================================================
#LISTS DEL\REMOVE
# del cars[1]
# cars.remove("GM")
# =============================================================================

#hayvonlar = ["it", "mushuk", "sigir", "qo'y", "quyon", "mushuk"]

# =============================================================================
#LISTS POP
# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# print(bozorlik)
# mahsulot = bozorlik.pop(3);
# print("Men "+mahsulot+" sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)
# 
# mahsulot2 = bozorlik.pop()
# print("Oldim: ", mahsulot2)
# =============================================================================
# =============================================================================
# cars = ["bmw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]
# print(cars)
# 
# cars.sort()
# print("sorted", cars)
# 
# cars.sort(reverse=True)
# print("reverse sorted", cars)
# 
# print(sorted(cars))
# print(sorted(cars, reverse = True))
# =============================================================================


# =============================================================================
#LIST SORT\REVERSE SORT\SORTED\REVERSE SORTED
#sonlar = [12, 45, 23, 56, 998, 1, -5, -7.2]
# sonlar.sort()
# sonlar.sort(reverse = True)
# print("sonlar", sonlar)
# print("sonlar sorted", sorted(sonlar))
# print("sonlar reverse sorted", sorted(sonlar, reverse = True))
# =============================================================================
# =============================================================================
# cars = ["bmw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]
# print(cars)
# cars.reverse()
# print(cars)
# print("List Length: ", len(cars))
# =============================================================================
# =============================================================================
# sonlar = list(range(0, 10))
# sonlar2 = list(range(21, 31))
# toq_sonlar = list(range(1, 20, 2))
# juft_sonlar = list(range(0, 20, 2))
# sanash = list(range(0, 101, 10))
# max_toq = max(toq_sonlar)
# min_toq = min(toq_sonlar)
# max_juft = max(juft_sonlar)
# min_juft = min(juft_sonlar)
# =============================================================================
# =============================================================================
#MAX\MIN\SUM
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# print(narhlar)
# print("MAX narh: ", max(narhlar))
# print("MIN narh: ", min(narhlar))
# print("SUM narh: ", sum(narhlar))
# =============================================================================

# =============================================================================
#LISTS CUT
#cars = ["bmw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]
#print(cars[0:3])
#print(cars[2:5])
#print(cars[:3])
#print(cars[1:])
# =============================================================================

# =============================================================================
# #LISTS COPY
# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar[:]
# sonlar2.append(6)
# sonlar2.append(7)
# print("sonlar: ", sonlar)
# print("sonlar2: ", sonlar2)
# =============================================================================

# =============================================================================
# #LISTS CLONE (give second name to LIST)
# cars = ["bmw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]
# my_cars = cars
# print("cars: ", cars)
# print("my cars: ", my_cars)
# my_cars.remove("volvo")
# print("my cars: ", my_cars)
# my_cars[0] = "lacetti"
# print("cars: ", cars)
# print("my cars: ", my_cars)
# cars.append("bmw")
# print("cars: ", cars)
# print("my cars: ", my_cars)
# =============================================================================

# =============================================================================
# LIST COPY
# cars = ["bmw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]
# my_cars = cars[:]
# print("cars: ", cars)
# print("my cars: ", my_cars)
# my_cars.remove("volvo")
# print("my cars: ", my_cars)
# my_cars[0] = "lacetti"
# print("cars: ", cars)
# print("my cars: ", my_cars)
# cars.append("bmw")
# print("cars: ", cars)
# print("my cars: ", my_cars)
# =============================================================================

# =============================================================================
# #TUPLES
# toys = ("bus", "car", "bear", "dino", "snake", "lizard")
# print(toys)
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
# print(toys[3:])
# #toys[0] = "teddy" - ERROR
# #toys.append("teddy") - ERROR
# #toys.remove("bear") - ERROR
# =============================================================================

# =============================================================================
#TUPLE <=> LIST
# toys = ("bus", "car", "bear", "dino", "snake", "lizard")
# print("tupe: ", toys)
# toys = list(toys)
# print("type: ", type(toys))
# print("list: ", toys)
# toys.append("dragon")
# print("list: ", toys)
# toys.remove("bus")
# print("list: ", toys)
# toys[1] = "mcqueen"
# print("list: ", toys)
# toys = tuple(toys)
# print("type: ", type(toys))
# =============================================================================
