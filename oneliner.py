val = int(input('>>enter a number: '))
if val > 100:
    vaal = val/2
else:
    val = val * 2
    print('>>the result is:',val)

    # true if condition else false 
val = int(input('>>enter a number:'))
val = val /2 if val>100 else val*2
print('>>the result is :',val)


name = input("enter ur name")
if name.isalpha():
    print("very good")
else:
    print("not good")


#one line code
print("very good") if name.isalpha() else print("not good")