# 🧍‍♂️ BMI (IMC) Calculator in Python

This project is a **BMI (Body Mass Index / IMC - Índice de Massa Corporal) calculator** developed in Python, as part of my learning journey in programming logic and Python fundamentals.  
The program asks the user for their **name, height, and weight**, calculates their BMI, and displays the corresponding **health classification**.

---

## 🚀 What I Learned from This Project
While developing this BMI calculator, I practiced and learned important programming concepts such as:

- **Input and output handling** with the `input()` function.  
- **Type conversion** using `float()` and `int()`.  
- **Mathematical operations** with custom formulas (`weight / (height * height)`).  
- **Looping with `while True`** to allow multiple calculations until the user chooses to exit.  
- **Conditional structures (`if/elif/else`)** to check BMI ranges and return the correct classification.  
- **Good programming practices**, such as validating input, looping until exit, and providing clear feedback to the user.  

---

## ⚙️ Features
- Asks for the user's name, height, and weight.  
- Calculates BMI using the formula:  
  \[
  \text{BMI} = \frac{\text{weight}}{\text{height}^2}
  \]  
- Displays health classification according to BMI value:
  - 🟦 Underweight (≤ 18.5)  
  - 🟩 Normal weight (18.6 – 24.9)  
  - 🟨 Pre-obesity (25 – 29.9)  
  - 🟧 Obesity I (30 – 34.9)  
  - 🟥 Obesity II (35 – 39.9)  
  - ⛔ Obesity III (≥ 40)  
- Continuous loop until the user chooses to exit.  

---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/bmi-calculator.git
