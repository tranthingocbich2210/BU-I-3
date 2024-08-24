# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:53:45 2024

@author: ADMIN
"""

a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
# Tính thương 
if b != 0:
        thuong = a / b
    # Làm tròn 2 chữ số
        thuong_lam_tron_2 = round(thuong, 2)
    # Làm tròn 3 chữ số
        thuong_lam_tron_3 = round(thuong, 3)
        chia_lay_du = a % b
        chia_lay_nguyen = a // b
else:
    print("Không xác định")
# In ra kết quả
print("Thương a và b (Làm tròn 2 chữ số)", thuong_lam_tron_2)
print("Thương a và b (làm tròn 3 chữ số)", thuong_lam_tron_3)
print("Chia lấy dư a và b:", chia_lay_du)
print("Chia lấy nguyên a và b:", chia_lay_nguyen)    
    
             
        
    




