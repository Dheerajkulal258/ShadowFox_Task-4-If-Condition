# ShadowFox Internship - Task 4: If Conditions

## Overview

This is Task 4 of the ShadowFox Python Development Internship. The objective of this task is to understand decision-making in Python using `if`, `elif`, and `else` statements. The program uses user input to calculate BMI categories, identify the country of a city, and check whether two cities belong to the same country.

---

## Task Objectives

This task consists of three questions based on conditional statements.

### Question 1: BMI Category Calculator

Create a program that accepts the user's height in meters and weight in kilograms, calculates BMI using the formula:

**BMI = Weight / (Height × Height)**

Based on the BMI value, the program displays the following categories:

* BMI ≥ 30 → Obesity
* BMI between 25 and 29.9 → Overweight
* BMI between 18.5 and 24.9 → Normal
* BMI < 18.5 → Underweight

### Sample Output

```text
Enter height in meters: 1.75
Enter weight in kilograms: 70

Your BMI is: 22.86
Category: Normal
```

---

### Question 2: Find Country by City Name

Create a program to determine the country to which a city belongs.

The cities are stored in different lists:

**Australia:**

* Sydney
* Melbourne
* Brisbane
* Perth

**UAE:**

* Dubai
* Abu Dhabi
* Sharjah
* Ajman

**India:**

* Mumbai
* Bangalore
* Chennai
* Delhi

The program takes a city name as input and checks which country's list contains the city.

### Sample Output

```text
Enter a city name: Abu Dhabi

Abu Dhabi is in UAE
```

---

### Question 3: Check Whether Two Cities Belong to the Same Country

Create a program that accepts two city names from the user and checks whether both cities belong to the same country.

The program uses conditional statements and logical operators to compare the cities.

### Sample Output 1

```text
Enter the first city: Mumbai
Enter the second city: Chennai

Both cities are in India
```

### Sample Output 2

```text
Enter the first city: Sydney
Enter the second city: Dubai

They don't belong to the same country
```

---

## 💻 Technologies Used

* Python 3
* Conditional Statements (`if`, `elif`, `else`)
* Lists
* User Input Handling (`input()`)
* Logical Operators (`and`)
* Membership Operator (`in`)

---

## 🛠️ Python Concepts Used

* `if` statement – Executes a block of code when a condition is true.
* `elif` statement – Checks multiple conditions when previous conditions are false.
* `else` statement – Executes when none of the conditions are true.
* `input()` function – Accepts data from the user.
* Lists – Stores multiple values such as city names.
* `in` operator – Checks whether a value exists in a list.
* `and` operator – Combines multiple conditions.

---

## 📁 Project Structure

```
Task-4_If_Condition/
│
└── main.py
```

---

## 📚 Learning Outcomes

Through this task, I learned:

* How to use `if`, `elif`, and `else` statements for decision-making.
* How to take user input and process it in Python.
* How to perform mathematical calculations like BMI.
* How to work with lists and search for elements using the `in` operator.
* How to use logical operators to compare multiple conditions.
* How to solve real-world problems using conditional statements.

---

## 👨‍💻 Author

**Dheeraj **
