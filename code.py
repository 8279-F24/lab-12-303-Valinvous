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

def main():
    print("Welcome to the Morse Code Converter!")
    print('Type "lolipop" to exit the program.')

    while True:
        # Get user input
        sentence = input("\nEnter a sentence to convert to Morse code: ").lower()
        
        # Check for exit condition
        if sentence == "lolipop":
            print("Goodbye!")
            break
        
        # Clean input (keep only valid characters)
        valid_chars = set(MORSE_CODE.keys())
        cleaned_sentence = ''.join(char for char in sentence if char in valid_chars)
        
        # Convert to Morse code
        morse_words = []
        for word in cleaned_sentence.split(' '):  # Split into words
            morse_word = '   '.join(MORSE_CODE[char] for char in word)  # 3 units between letters
            morse_words.append(morse_word)
        morse_code = '       '.join(morse_words)  # 7 units between words
        
        # Print the result
        print("\nMorse Code Equivalent:")
        print(morse_code)

# Run the program
if __name__ == "__main__":
    main()

