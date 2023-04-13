import random

rnum = random.randint(1111, 9999)
print(rnum)
cnum = False
while cnum == False:
    pnum = input("Enter a possible number: ")
    print(pnum)
    if int(pnum) == rnum:
        print("The number is correct: " + pnum)
        cnum = True
    else:
        print("The number is not  correct: " + pnum)
