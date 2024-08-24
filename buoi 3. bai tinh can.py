# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:11:23 2024

@author: ADMIN
"""
import math
a = float(input("Nhập số thực a"))
b = float(input("Nhập só thực b"))
#Tính giá trị biểu thức
A = ( ( math.sqrt(a)-math.sqrt(b) )/( pow(a,1/4)-pow(b,1/4) ) )-( (math.sqrt(a)+pow(a*b,1/4) )/( pow(a,1/4)+pow(b,1/4) ) )
print("Kết quả:", round(A, 3))

