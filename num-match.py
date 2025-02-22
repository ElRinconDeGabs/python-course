import random

arr_list = [random.randint(0, 9) for i in range(4)]
print(arr_list)

cnum = False
while cnum == False:
    pnum = input("Enter a possible number: ")
    pn_list = [i for i in map(int, pnum)]
    print(pnum)
    print(pn_list)
    
    arr_list.sort()
    pn_list.sort()
    quantity_list = [set(arr_list).intersection(set(pn_list))]
    quantity = [len(quantity_list)]
    print(quantity_list, quantity)

    if arr_list == pn_list:
        print("The number is correct: " + pnum)
        cnum = True
    else:
        print("The number is not  correct: " + pnum)
        print("correct quantity: ", quantity)
