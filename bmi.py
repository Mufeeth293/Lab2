def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = round(weight/(height*height),2)
    print("Bmi = " + str(bmi))
    if bmi < 18.5:
        print(-1)
    elif (bmi>= 18.5 and bmi <= 25):
        print(0)
    else:
        print(1)

    






calculate_bmi(weight=65, height=1.73)