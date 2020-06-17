# BMI (Body Mass Index) calculator
# Formula: weight(kg) / (height(cm) ** 2) 

def main():
    username = input("Hello! Enter your name: ")
    print(f"Hello, {username}! This program shows your BMI (Body Mass Index)")
    weight = float(input("First, enter your weight(kg): "))
    height = float(input("Great! Now enter your height(cm): "))
    print(f"Your BMI is: {bmi(weight, height)}. {info(bmi(weight, height))}")


def bmi(weight, height):
    bmi = weight / ((height/100)**2)
    return round(bmi, 1)


def info(bmi):
    info = ""
    if bmi < 18.50:
        info = "You're underweight!"
    elif bmi >= 18.50 and bmi <= 24.99:
        info = "Your weight is OK!"
    elif bmi >= 25.00 and bmi <= 29.99:
        info = "You're overweight!"
    elif bmi >= 30.00:
        info = "You're obese!"
    else:
        return "Try again, please..."

    return info

main()
