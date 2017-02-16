def mini_project():
    list1 = []
    while True:
        input_num = int(input("Enter a number: "))
        if input_num > 0:
            list1.append(input_num)
            print ("Your current list is {}".format(list1))
        elif input_num < 0:
            if abs(input_num) in list1:
                list1.remove(abs(input_num))
                print ("Your current list is {}".format(list1))
        else:
            break
    print ("Your final list is {}".format(list1))
    
mini_project()