# def display_main_menu():
#     print("Enter some numbers separated by commas (e.g. 5, 67,32)")


def get_user_input():  
    userinput = input()
    string_list = userinput.split(",")
   # print (string_list )
    float_list = []
    for string in string_list:
        float_num = float(string)
        float_list.append(float_num)

    #print("float_list", float_list)
    return float_list




def calc_average_temperature(flist):
    s = sum(flist)
    avg = s/len(flist)
    print(round(avg,2))

def calc_min_max_temperature(flist):
    maxi = max(flist)
    minu = min(flist)
    l = [maxi,minu]
    print(l)

   
def main():
    l = get_user_input()
    calc_average_temperature(l)
    calc_min_max_temperature(l)

if __name__ == "__main__":
    main()
# display_main_menu()

# # print(res)



