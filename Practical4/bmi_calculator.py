#assign a varible to storage the weight (in kg)
weight = float(input("Enter your body weigh (in kg):"))
#assign a varible to storage the height (in m)
height = float(input("Enter your body height (in m):"))
#calculate the BMI
bmi = weight / height**2
#decide the BMI category
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi <= 30:
    print(f"Your bmi is {bmi}, you are normal weight")
else:
    print(f"Your bmi is {bmi}, you are obese")
