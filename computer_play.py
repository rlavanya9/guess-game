a = int(input("can you tell the start range: "))
b = int(input("can you tell the end range: "))
comp_guess = (a+b)//2
print(comp_guess)
check = input("is it too high or low: ").upper()
while(check != "WON"):
    if (check == "HIGH"):
        b = comp_guess
        comp_guess = (a + b)//2 
        print(comp_guess)
        check = input("is it too high or low: ").upper()
    elif (check == "LOW"):
        a = comp_guess
        comp_guess = (a +b)//2
        print(comp_guess)
        check = input("is it too high or low: ").upper()    
print("you won!")


  
