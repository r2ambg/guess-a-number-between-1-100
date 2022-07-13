import random
SecretNumb = random.randint(1, 100)
Gnumb = int(input("guess a number between 1 to 100: "))

while Gnumb in range(1, 101):
    for guessesTaken in range(1, 5):
        guessesTaken = guessesTaken+1
        Gnumb = int(input("guess a number: "))
        
        if Gnumb < SecretNumb :
            print("your guess is too low")
            
        elif Gnumb > SecretNumb :
            print("your guess is too high")
            
        else : 
            break
        
    if SecretNumb == Gnumb :
        print("correct")     
    else :
        print("no more attempt")
        break
