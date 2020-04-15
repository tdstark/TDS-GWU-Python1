startnumber = 0
lastnumber = 0
continueCount = ""
looper = "y"
while looper != "n":
    integercheck = True
    while(integercheck):
        try:
            prompt = int(input("How many numbers do you want to chain? "))
            integercheck = False
        except:
            print("Invalid Selection")

    lastnumber = startnumber + prompt
    for num in range(startnumber, lastnumber):
        print(num)

    #while continueCount != "y" or continueCount != "n":
    continueCount = input("Continue the chain? (y/n) ")
    
    startnumber = lastnumber
    looper = continueCount
