# Part 1 -
## 1.1. Create variables
name = "Angela"
age = 46
height = round((((5 * 12) + 4) / 12), 2)
favorite_color = "Purple"

## 1.2. Print each variable
## 1.2.1 each variable at a time separate print statements
print(name)
print(age)
print(height)
print(favorite_color)

## 1.2.2 print all variables using one print statement
print(name, age, height, favorite_color)

## 1.2.3 print with Python formats
print(f"Hello: I'm {name} and my favorite color is {favorite_color}!")
print(f"I'm {age} and am {height} feet tall.")

## 1.2.4 print with format specifiers within a multi-line string
print(f"""
      Name: {name}
      Age: {age}
      Height: {height}
      Favorite Color: {favorite_color}""")

## 1.3. new variable
import math
circle_area = round(math.pi*(5**2), 1)
print(circle_area)

# Part 2 -
## 2.1. used in part 1.3

## 2.2 sq root
age_sq = math.sqrt(age)
print(age_sq)

## 2.3 Sine & Cosine
h_sin = math.sin(height)
h_cos = math.cos(height)
print(h_sin, h_cos)

# Part 3
## 1. arithmetic ops
age_plus5 = age = 5
h_4 = height - 4
ah = age * height
h_2 = height / 2
age_3 = age // 3
age_topower2 = age ** 2

print(age_plus5)
print(h_4)
print(ah)
print(h_2)
print(age_3)
print(age_topower2)

## Part 4
# F to C
temp_f = float(input("Enter the temperature in Fahrenheit: "))
f = round(float((temp_f - 32) * 5/9), 2)
print(f"The temperature in Celsius is {f}°C")

