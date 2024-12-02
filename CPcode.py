import time
from adafruit_circuitplayground import cp

# Morse code dictionary
MORSE_CODE = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.', 
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---', 
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---', 
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-', 
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--', 
    'z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '0': '-----', ' ': ' '  # Space for word separation
}

# Function to display a single Morse code element
def display_morse(unit_length, morse_element):
    if morse_element == ".":
        cp.pixels.fill((255, 255, 0))  # Yellow light for dot
        time.sleep(unit_length)
    elif morse_element == "-":
        cp.pixels.fill((255, 0, 255))  # Purple light for dash
        time.sleep(3 * unit_length)
    cp.pixels.fill((0, 0, 0))  # Turn off LEDs
    time.sleep(unit_length)  # Pause after each part of the letter

def main():
    print("Welcome to the Morse Code Display on Circuit Playground!")
    
    # Prompt user for unit length
    while True:
        try:
            unit_length = float(input("Enter the length of a unit (between 0 and 1 seconds): "))
            if 0 < unit_length <= 1:
                break
            else:
                print("Please enter a value between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 1.")

    # Prompt user for a sentence
    sentence = input("Enter a sentence to convert to Morse code: ").lower()

    # Clean input (keep only valid characters)
    valid_chars = set(MORSE_CODE.keys())
    cleaned_sentence = ''.join(char for char in sentence if char in valid_chars)

    # Convert to Morse code
    morse_list = []
    for word in cleaned_sentence.split(' '):
        morse_word = [MORSE_CODE[char] for char in word]
        morse_list.append(' '.join(morse_word))

    # Display Morse code on Circuit Playground
    print("\nDisplaying Morse Code...")
    for word in morse_list:
        for letter in word.split(' '):  # Process each letter
            for element in letter:  # Process each dot or dash
                display_morse(unit_length, element)
            time.sleep(3 * unit_length)  # Space between characters
        time.sleep(7 * unit_length)  # Space between words

    print("Morse Code display complete!")

# Run the program
if __name__ == "__main__":
    main()

