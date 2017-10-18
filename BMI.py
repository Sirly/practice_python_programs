#   File: BMI.py
#   Finds BMI and BMR of user given input

def calcBMI(kg,cm):
    return (kg / ((cm / 100) * (cm / 100)))
#===========================================================================
def calcBMR(sex,kg,cm,age):
    if sex.upper() == 'M':  #male BMR
        return 88.362 + (13.397 * kg) + (4.799 * cm) - (5.677 * age)
    else:                   #female BMR
        return 447.593 + (9.247 * kg) + (3.098 * cm) - (4.33 * age)
#===========================================================================
def in2cm(inches):
    return inches * 2.54
#===========================================================================
def lb2kg(lb):
    return lb * 0.453592
#===========================================================================
def kg2lb(kg):
    return kg * 2.20462
#===========================================================================
def cm2in(cm):
    return cm * 0.393701
#===========================================================================
def getInfo():
    units = input("Which units will you be using? Metric or Imperial (M/I)")
    sex = input("Sex? (F/M)")
    age = eval(input("Age?"))
    if units.upper() == 'M': #if Metric units
        height = eval(input("height in centimeters?"))
        weight = eval(input("Weight in kilograms?"))
    else:                   #if Imperial units
        height = eval(input("height in inches?"))
        weight = eval(input("Weight in pounds?"))
        height = in2cm(height)
        weight = lb2kg(weight)
    return units, sex, age, height, weight
#===========================================================================
def BMIcategory(bmi):
    if bmi < 16:
        print("You are categorized as having severe thinness")
        print("Your target weight is in the normal range")
        return 0
    elif 16 <= bmi or bmi < 17:
        print("You are categorized as having moderate thinness")
        print("Your target weight is in the normal range")
        return 1
    elif 17 <= bmi or bmi < 17:
        print("You are categorized as having mild thinness")
        print("Your target weight is in the normal range")
        return 2
    elif 18.5 <= bmi or bmi < 25:
        print("You are categorized as within normal range")
        print("Congratulations")
        return 3
    elif 25 <= bmi or bmi < 30:
        print("You are categorized as overweight")
        print("Your target weight is in the normal range")
        return 4
    elif 30 <= bmi or bmi < 35:
        print("You are categorized as Obese class I (moderate)")
        print("Your target weight is in the normal range")
        return 5
    elif 35 <= bmi or bmi < 40:
        print("You are categorized as Obese class II (severe)")
        print("Your target weight is in the normal range")
        return 6
    elif 40 <= bmi:
        print("You are categorized as Obese class III (very severe)")
        print("Your target weight is in the normal range")
        return 7
    
#===========================================================================
def targetWeight(bCat, kg, cm):
    weeks = 0
    weightChange = 0
    while bCat != 3:
        if bCat < 3:
            kg += 0.45
            weightChange += 0.45
        elif 3 < bCat:
            kg -= 0.45
            weightChange -= 0.45
        weeks += 1
    return weeks, weightChange
#===========================================================================
def main():
    units, sex, age, height, weight = getInfo()
    BMR = calcBMR(sex, weight, height, age)
    BMI = calcBMI(weight, height)
    
    print("Your BMR is: ", BMR)
    print("your BMI is: ", BMI)
    bmiCat = BMIcategory(BMI)
    
    if bmiCat == 3:
        print("You do not need to adjust your caloric intake")
    else:
        weeks, wC = targetWeight(bmiCat, weight, height)
    if units.upper() == 'I':
        weight = kg2lb(weight)
        height = cm2in(height)
    if wC >0:
        print("In order to get within normal range, it will take you ", weeks, " weeks")
        print("to gain ", wC, " kilograms")
    else:
        print("In order to get within normal range, it will take you ", weeks, " weeks")
        print("to lose ", wC, " kilograms")

main()
