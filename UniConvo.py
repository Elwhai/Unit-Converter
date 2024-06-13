
def get_valid_input(prompt,choice):
    while True:
        user_input = input(prompt)
        if user_input in choice:
            return user_input
        else:
            print("Huh? That wasn't provided... ＞︿＜ Please select from the provided options! ")

# asking the user for input and categorize into which section they'll trigger
def ask():
    category = get_valid_input("\nCategories available: \n1.Length \n2.Weight/Mass \n3.Temperature \n4.Time \n5.Speed/Velocity \nWhich category would you like to use? ",["1","2","3","4","5","6"])
    if category == "1":
        length()
    elif category == "2":
        weight()
    elif category == "3":
        temparature()
    elif category == "4":
        time()
    elif category == "5":
        speed()
    elif category == "6":
        print("You haven't even started using me... Hope to see you soon QwQ")

def reuse():
    print("\nWanna use other categories? \n1.Yes! \n2.Nope... \n")
    again = get_valid_input("What's your choice? ",["1","2"]) 


    if again == "1":
        print("-------------------------------------------------\n")
        return ask()
    elif again == "2":
        print("Oh okay! See you again! /(ㄒoㄒ)/~~")
        
def length():
    conversion_factors = { #all conversion factors are based on meter
        "1" : 0.01, #cm
        "2" : 0.0254, #inch
        "3" : 1, #meter
        "4" : 0.3048, #foot
        "5" : 1000, #km
        "6" : 0.9144, #yard
        "7" : 0.0254, #miles
        }

    print("\nYou are at the length converter! ヾ(•ω•`)o")
    print ("Here are a few options! \n1.Centimeters \n2.Inches \n3.Meters \n4.Foot \n5.Kilometer \n6.Yard \n7.Miles \n8.Exit")
    from_convert = get_valid_input("Which one would you like to convert from? ",["1","2","3","4","5","6","7","8"])

    if from_convert == "8":
        return reuse()
    
    to_convert = input("Which to convert to? ")

    if to_convert == "8":
        return reuse()
    
    while from_convert == to_convert:
        print("Huh? That's the same unit... Wanna try again? ")
        to_convert = input("Which to convert to? ")
    
    if from_convert != to_convert:
        value = input("What's the value to convert? ")
        while value == "0":
            print("There's no point of converting 0... o(￣┰￣*)ゞ")
            value = input("What's the value to convert? ")

        value = float(value)
        amount_in_baseunit = value * conversion_factors[from_convert]
        converted_amount = amount_in_baseunit / conversion_factors[to_convert]
        print("The converted value is",round(converted_amount,3))
        return reuse()


def weight():
    conversion_factors = { #all conversion factors are based on kg
        "1" : 0.001, #grams
        "2" : 1, #kg
        "3" : 0.1020, #newton
        "4" : 1000, #tonnes
        "5" : 0.4536, #pounds
        "6" : 0.02835, #ounces   
        }

    print("\nYou are at the weight/mass converter! ヾ(•ω•`)o")
    print ("\nHere are a few options! \n1.Grams \n2.Kilogram \n3.Newton \n4.Tonnes \n5.Pounds \n6.Ounces \n7.Exit")
    from_convert = get_valid_input("Which one would you like to convert from? ",["1","2","3","4","5","6","7"])

    if from_convert == "7":
        return reuse()
    
    to_convert = input("Which to convert to? ")

    if to_convert == "7":
        return reuse()


    while from_convert == to_convert:
        print("Huh? That's the same unit... Wanna try again? ")
        to_convert = input("Which to convert to? ")

    if from_convert != to_convert:
        value = input("What's the value to convert? ")
        while value == "0":
            print("There's no point of converting 0... o(￣┰￣*)ゞ")
            value = input("What's the value to convert? ")

        value = float(value)
        amount_in_baseunit = value * conversion_factors[from_convert]
        converted_amount = amount_in_baseunit / conversion_factors[to_convert]
        print("The converted value is",round(converted_amount,3))
        return reuse()


def temparature():
    print("\nYou are at the temperature converter! ヾ(•ω•`)o")
    print ("\nHere are a few options! \n1.Celsius \n2.Fahrenheit \n3.Kelvin \n4.Exit")
    from_convert = get_valid_input("Which one would you like to convert from? ",["1","2","3","4"])

    if from_convert == "4":
        return reuse()
    
    to_convert = input("Which to convert to? ")

    if to_convert == "4":
        return reuse()
    
    while from_convert == to_convert:
        print("Huh? That's the same unit... Wanna try again? ")
        to_convert = input("Which to convert to? ")

    
    value = input("What's the value to convert? ")

    while value == "0":
            print("There's no point of converting 0... o(￣┰￣*)ゞ")
            value = input("What's the value to convert? ")
    
    value = float(value)

    if from_convert == "1" and to_convert == "2":
        converted_amount = (value * (9/5)) + 32  # Celsius to Fahrenheit
    elif from_convert == "1" and to_convert == "3":
        converted_amount = value + 273.15  # Celsius to Kelvin
    elif from_convert == "2" and to_convert == "1":
        converted_amount = (value - 32) * (5/9)  # Fahrenheit to Celsius
    elif from_convert == "2" and to_convert == "3":
        converted_amount = (value - 32) * (5/9) + 273.15  # Fahrenheit to Kelvin
    elif from_convert == "3" and to_convert == "1":
        converted_amount = value - 273.15  # Kelvin to Celsius
    elif from_convert == "3" and to_convert == "2":
        converted_amount = (value - 273.15) * (9/5) + 32  # Kelvin to Fahrenheit
    
    print("The converted value is", round(converted_amount, 3))
    return reuse()

def time():
    conversion_factors = { #all conversion factors are based on minute
        "1" : 1/60, #second
        "2" : 1, #minute
        "3" : 60, #hours
        "4" : 1440, #days
        "5" : 1/60000, #milisecond  
        }

    print("\nYou are at the time converter! ヾ(•ω•`)o")
    print ("\nHere are a few options! \n1.Second \n2.Minute \n3.Hours \n4.Days \n5.Milisecond \n5.Exit")
    from_convert = get_valid_input("Which one would you like to convert from? ",["1","2","3","4","5"])

    if from_convert == "5":
        return reuse()
    
    to_convert = input("Which to convert to? ")

    if to_convert == "5":
        return reuse()
    

    while from_convert == to_convert:
        print("Huh? That's the same unit... Wanna try again? ")
        to_convert = input("Which to convert to? ")

    if from_convert != to_convert:
        value = input("What's the value to convert? ")

        while value == "0":
            print("There's no point of converting 0... o(￣┰￣*)ゞ")
            value = input("What's the value to convert? ")

        value = float(value)
        amount_in_baseunit = value * conversion_factors[from_convert]
        converted_amount = amount_in_baseunit / conversion_factors[to_convert]
        print("The converted value is",round(converted_amount,3))
        return reuse()

def speed():
    conversion_factors = { #all conversion factors are based on m/s
        "1" : 1, #m/s
        "2" : 1000, #km/s
        "3" : 0.4470, #miles/h
        "4" : 0.2778, #km/h
        "5" : 0.01, #cm/s 
        }

    print("\nYou are at the speed/velocity converter! ヾ(•ω•`)o")
    print ("\nHere are a few options! \n1.Meter/second \n2.Kilometer/second \n3.Miles/hour \n4.Kilometer/hour \n5.Centimeters/second \n6.Exit")
    from_convert = input("Which one would you like to convert from? ",["1","2","3","4","5","6"])

    if from_convert == "6":
        return reuse()
    
    to_convert = input("Which to convert to? ")

    if to_convert == "6":
        return reuse()
    

    while from_convert == to_convert:
        print("Huh? That's the same unit... Wanna try again? ")
        to_convert = input("Which to convert to? ")
    if from_convert != to_convert:
        value = input("What's the value to convert? ")

        while value == "0":
            print("There's no point of converting 0... o(￣┰￣*)ゞ")
            value = input("What's the value to convert? ")

        value = float(value)
        amount_in_baseunit = value * conversion_factors[from_convert]
        converted_amount = amount_in_baseunit / conversion_factors[to_convert]
        print("The converted value is",round(converted_amount,3))
        return reuse()

print("----Welcome to Unit Converter (●' ◡ '●)!----- \nTip: You should only be using numbers throughout this program!")
ask()