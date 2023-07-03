#!/usr/bin/env python
# coding: utf-8

# In[1]:


weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = weight / (height ** 2)

if bmi < 16:
    status = "Gầy cấp độ III"
elif 16 <= bmi < 17:
    status = "Gầy cấp độ II"
elif 17 <= bmi < 18.5:
    status = "Gầy cấp độ I"
elif 18.5 <= bmi < 25:
    status = "Bình thường"
elif 25 <= bmi < 30:
    status = "Thừa cân"
elif 30 <= bmi < 35:
    status = "Béo phì cấp độ I"
elif 35 <= bmi < 40:
    status = "Béo phì cấp độ II"
else:
    status = "Béo phì cấp độ III"

print("Chỉ số BMI của bạn:", bmi)
print("Tình trạng cơ thể của bạn:", status)

