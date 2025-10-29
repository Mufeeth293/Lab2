def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = round(weight/(height*height),2)
    print("Bmi = " + str(bmi))
    if bmi < 18.5:
        print("Underweight")
    elif (bmi>= 18.5 and bmi <= 25):
        print("Normal weight")
    else:
        print("Overweight")

    






calculate_bmi(weight=65, height=1.73)