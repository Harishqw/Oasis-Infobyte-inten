import os
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def calculate_bmi(weight, height):
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    while True:
        try:
            weight = float(input("Enter weight (in kg): "))
            height = float(input("Enter height (in cm): "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    clear_screen()
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()