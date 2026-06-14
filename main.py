# =====================================
# Question 1: BMI Category Calculator
# =====================================

print("Question 1: BMI Calculator")

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi >= 30:
    print("Category: Obesity")

elif bmi >= 25 and bmi < 30:
    print("Category: Overweight")

elif bmi >= 18.5 and bmi < 25:
    print("Category: Normal")

else:
    print("Category: Underweight")


# =====================================
# Question 2: Find Country by City
# =====================================

print("\nQuestion 2: Find Country by City")

australia = ["sydney", "melbourne", "brisbane", "perth"]
uae = ["dubai", "abu dhabi", "sharjah", "ajman"]
india = ["mumbai", "bangalore", "chennai", "delhi"]

city = input("Enter a city name: ").strip().lower()

if city in australia:
    print(city, "is in Australia")

elif city in uae:
    print(city, "is in UAE")

elif city in india:
    print(city, "is in India")

else:
    print("City not found in the list")


# =====================================
# Question 3: Check Two Cities
# =====================================

print("\nQuestion 3: Check if two cities belong to the same country")

city1 = input("Enter the first city: ").strip().lower()
city2 = input("Enter the second city: ").strip().lower()

if city1 in australia and city2 in australia:
    print("Both cities are in Australia")

elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")

elif city1 in india and city2 in india:
    print("Both cities are in India")

else:
    print("They don't belong to the same country")