import random

RandomNumber = random.randrange(1,20)
userInput =  int(input("Guess the Number:"))
if userInput > RandomNumber :
    print(" the user number to high")
elif RandomNumber > userInput :
    print(" the number is too low")
else:
    print(" Yes. The Number Is Correctly Matched.")


RandomNumber = random.randrange(1,20)
userInput =  int(input("Guess the Number:"))
if userInput > RandomNumber :
    print(RandomNumber)
    print(" the user number to high")
elif RandomNumber > userInput :
    print(RandomNumber)
    print(" the number is too low")
else:
    print(RandomNumber)
    print(" Yes. The Number Is Correctly Matched.")


RandomNumber = random.randrange(1,20)
print(RandomNumber)
userInput =  int(input("Guess the Number:"))
if userInput > RandomNumber :
    print(RandomNumber)
    print(" the user number to high")
elif RandomNumber > userInput :
    print(RandomNumber)
    print(" the number is too low")
else:
    print(RandomNumber)
    print(" Yes. The Number Is Correctly Matched.")