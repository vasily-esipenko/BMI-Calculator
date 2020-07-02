# BMI (Body Mass Index) calculator
# Formula (metric): weight(kg) / (height(cm) ** 2)
# Formula (imperial): 703 * weight(lbs) / (height(in))

def main():
    username = input("Hello! Enter your name: ")
    print(f"Hello, {username}! This program shows your BMI (Body Mass Index)")
    choice = input("Which measuring system do you prefer? (write \"m\" for metric or \"i\" for imperial) ")

    if choice == "m":
        weight = float(input("First, enter your weight(kg): "))
        height = float(input("Great! Now enter your height(cm): "))
        print(f"Your BMI is: {bmi_m(weight, height)}. {info(bmi_m(weight, height))}")
    elif choice == "i":
        weight = int(input("First, enter your weight(lbs): "))
        print("Great! Now enter your height")
        feet = int(input("Feet: "))
        inches = int(input("Inches: "))
        height = (feet * 12) + inches
        print(f"Your BMI is: {bmi_i(weight, height)}. {info(bmi_i(weight, height))}")
    else:
        print("Something went wrong... Try to repeat your input")


def bmi_m(weight, height):
    bmi = weight / ((height/100)**2)
    return round(bmi, 2)


def bmi_i(weight, height):
    bmi = 703 * weight / (height ** 2)
    return round(bmi, 2)


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
