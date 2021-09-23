# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 01:40:07 2021

@author: omon
"""

#KLASS VA OBJECT
matn = "Assalomy alaykum"
class Kompyuter:
    def __init__ (self, model, ram, hdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu
        
    def info(self):
        inf = f"{self.model}, RAM: {self.ram}, SSD: {self.hdd}, CPU: {self.cpu}"
        return inf
        
macbook = Kompyuter("Apple Macbook", "8GB", "512GB", "M1", "M1")