import random
SecretNumb = random.randint(1, 100)
print("the number that I have in my mind is between 1 to 100")
for Gnumb in range(1, 101):
    Gnumb = int(input("guess a number: "))
    if Gnumb < SecretNumb :
        print("your guess is too low")
    elif Gnumb > SecretNumb :
        print("your guess is too high")
    elif Gnumb not in range(1, 101) :
        print("not valid(out of range)")
    else : 
        print("you've won yohooo the number was %d" %(SecretNumb))
        break
