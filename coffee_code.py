#top secret combination
secretCombination = 246

#comments are words of wisdom to the clueless
print("Hello World, Let's make some coffee")

#getting user input, to make the delightful coffee, we all deserve
coffee = int(input("How many teaspoons of coffee? "))
sugar = int(input("How many teaspoons of sugar? "))

#stored values
water = 180
milk = 60

#user combination
userCombination = 0

#function to add ingredients
def Add(ingredients):
    global userCombination
    userCombination = userCombination + ingredients

#call function to add suagr and coffee
Add(sugar*coffee)

#boolean variable
boiled = False

#function to boil water
def Boil(water):
    boiled = True
    #print a new line
    print("\n")

#condition statement to ensure water boils 
if boiled == False:
    Boil(water)
    
Add(water)
Add(milk)

def Stir():
    if userCombination == secretCombination:
        print("Great!!! You love coffee as much as I do")
    else:
        print("Coffee making, is indeed an art!")

    print("Enjoy your coffee...")

Stir()
print("\n")
input("...Press enter to close...")