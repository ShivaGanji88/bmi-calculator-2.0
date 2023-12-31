#bmi calculator 2.0
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_convert = int(weight)

bmi = weight_convert / height ** 2
bmi = weight_convert / (height * height)
bmi_round = round(bmi)

if bmi_round < 18.5:
    print(f"Your BMI is {bmi_round}, you are underweight.")
elif bmi_round >= 18.5 and bmi_round < 25:
    print(f"Your BMI is {bmi_round}, you have a normal weight.")    
elif bmi_round >= 25 and bmi_round < 30:
    print(f"Your BMI is {bmi_round}, you are slightly overweight.")   
elif bmi_round >= 30 and bmi_round < 35:
    print(f"Your BMI is {bmi_round}, you are obese.") 
elif bmi_round >= 35:
    print(f"Your BMI is {bmi_round}, you are clinically obese.")       