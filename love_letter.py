#referencing https://github.com/Sangale1811/Mad-Libs-Generator/blob/master/play_mad_libs.py
import random
import sys

# word choices
greetings = ["Hello from", "Greetings from", "Wishing you were here in", "Sending thoughts from", "A warm hello from"]
locations = ["the down under", "Banff", "Mount Everest", "Thailand", "Japan"]
desires = ["I wish to stay here forever", "I long for a longer PTO", "I dream of spending my life here", "I yearn for another cocktail", "I seek more good food"]
secrets = ["tiring", "exhausting", "not wanted", "making me sleepy", "burning me out"]
farewells = ["Yours truly", "Forever yours", "With love", "Missing you", "Not eager to return"]

def generate_letter():
    greeting = random.choice(greetings)
    location = random.choice(locations)
    desire = random.choice(desires)
    secret = random.choice(secrets)
    farewell = random.choice(farewells)
    
    letter = f"{greeting} {location}!\n\n{desire}. Going to work and school is {secret}. \n\n{farewell},\nCassandra"
    return letter

def generate_combinations():
    combinations = []
    for greeting in greetings:
        for location in locations:
            for desire in desires:
                for secret in secrets:
                    for farewell in farewells:
                        letter = f"{greeting} {location}!\n\n{desire}. Hidden within is {secret}. \n\n{farewell},\nCassandra"
                        combinations.append(letter)
    return combinations

def main():
    if len(sys.argv) < 2:
        print("Please provide a flag such as -one, -two, -scramble.")
        return
    
    flag = sys.argv[1]
    
    if flag == "-one":
        letter = generate_letter()
        print(letter)
        
    elif flag == "-two":
        for _ in range(2):
            letter = generate_letter()
            print(letter)
            print("\n" + "-"*50 + "\n")
            
    elif flag == "-three":
        for _ in range(3):
            letter = generate_letter()
            print(letter)
            print("\n" + "-"*50 + "\n")
    
    elif flag == "-scramble":
        scrambled = generate_combinations()
        random.shuffle(scrambled)
        for letter in scrambled:
            print(letter)
            print("\n" + "-"*50 + "\n")
    
    else:
        print("Invalid syntax. Please use -one, -two, -three, or -scramble.")

if __name__ == "__main__":
    main()
