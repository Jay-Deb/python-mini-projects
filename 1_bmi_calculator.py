# Body Mass Index Calculator
# Ensure height is in meters & weight is in kilograms

height = float(input("Enter your height (in meter): "))
weight = float(input("Enter your weight (in kilogram): "))

bmi = weight / (height ** 2)
print("Your Body Mass Index is:", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight !!")
elif 18.5 <= bmi <= 24.9:
    print("You are normal weight !!")
elif 25.0 <= bmi <= 29.9:
    print("You are overweight !!")
else:
    print("You are obese !!")