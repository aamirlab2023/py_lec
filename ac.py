import random

def ac(amb_temp, set_temp):

    if amb_temp > set_temp: # summer season
        while set_temp <= amb_temp:
            print(f"{set_temp:.2f}    {amb_temp:.2f}")
            amb_temp -= random.random()

    elif amb_temp < set_temp: # winter season
        while amb_temp <= set_temp:
            print(f"{set_temp:.2f}    {amb_temp:.2f}")
            amb_temp += random.random()

    elif amb_temp == set_temp:
        print("No need to use AC")

    print(f"Ambient temperature is {amb_temp:.0f}")

ac(5, 26) # winter season
ac(50, 26) # summer season
ac(26, 26) # no need
        
