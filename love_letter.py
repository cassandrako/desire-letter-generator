#referencing https://github.com/Sangale1811/Mad-Libs-Generator/blob/master/play_mad_libs.py
import random
import sys

greetings = ["Hello from", "Greetings from", "Wishing you were here in", "Sending thoughts from", "A warm hello from"]
locations = ["the down under", "Banff", "Mount Everest", "Thailand", "Japan"]
desires = ["I wish to stay here forever", "I long for a longer PTO", "I dream of spending my life here", "I yearn for another cocktail", "I seek more good food"]
secrets = ["tiring", "exhausting", "not wanted", "making me sleepy", "burning me out"]
farewells = ["Yours truly", "Forever yours", "With love", "Missing you", "Not eager to return"]

def shift_letters(text, shift):
    shifted_text = []
    for char in text:
        if char.isalpha():
            shift_char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            shifted_text.append(shift_char.lower() if char.islower() else shift_char)
        else:
            shifted_text.append(char)
    return ''.join(shifted_text)

def prompt_or_random(prompt_text, options):
    user_input = input(f"{prompt_text} (Type 'RANDOM' for a random choice): ").strip()
    if user_input.upper() == "RANDOM":
        return random.choice(options)
    return user_input

def generate_letter():
    greeting = prompt_or_random("Please enter a greeting", greetings)
    location = prompt_or_random("Please enter a location", locations)
    desire = prompt_or_random("Please enter a desire", desires)
    secret = prompt_or_random("Please enter a secret", secrets)
    farewell = prompt_or_random("Please enter a farewell", farewells)

    # Extended letter with more sentences
    letter = (
        f"{greeting} {location}!\n\n"
        f"My life here is so eventful, freeing, every day feels like a dream. {desire}.\n"
        f"Between exploring new places and trying out local cuisine in both the street markets and restaurants, I've found so much joy here.\n"
        f"But the thought of returning to daily routines is {secret}. \n"
        f"I've made so many memories, and I can't wait to share them with you. When will I see you again... if I choose to never return ever again.\n"
        f"{farewell},\nCassandra"
    )
    return letter


def main():
    letter = generate_letter()
    print("\nGenerated Letter:\n")
    print(letter)


    try:
        shift_amount = int(input("\nEnter a number to shift each letter (e.g., 3 for Caesar cipher): ").strip())
    except ValueError:
        print("Invalid input. Using default shift of 0.")
        shift_amount = 0


    shifted_letter = shift_letters(letter, shift_amount)
    print("\nShifted Letter:\n")
    print(shifted_letter)

if __name__ == "__main__":
    main()
