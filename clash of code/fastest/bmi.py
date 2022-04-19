# solved in 3m
weight = int(input())
feet, inches = [int(i) for i in input().split()]

bmi = 703 * (weight / (feet * 12 + inches) ** 2 )
print(f"{bmi:.1f}")

print("Underweight" if bmi < 18.5 else "Normal" if bmi < 24.9 else "Overweight" if bmi < 29.9 else "Obese")
