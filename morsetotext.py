import re
import argparse

# Morse Code Dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
}

def binary_to_morse(binary_signal):
    # Convert binary to morse code using 1s and 0s patterns
    binary_signal = binary_signal.strip('0')  # Remove leading/trailing zeros
    binary_signal = re.sub(r'0000000+', ' / ', binary_signal)  # Word gap
    binary_signal = re.sub(r'000+', ' ', binary_signal)  # Letter gap
    binary_signal = re.sub(r'111+', '-', binary_signal)  # Long signals to '-'
    binary_signal = re.sub(r'1+', '.', binary_signal)  # Short signals to '.'
    binary_signal = re.sub(r'0+', '', binary_signal)  # Remove extra zeros
    return binary_signal

def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(MORSE_CODE_DICT.get(letter, '?') for letter in letters)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

def binary_to_ascii(binary_signal):
    morse_code = binary_to_morse(binary_signal)
    return morse_to_text(morse_code)

def main():
    parser = argparse.ArgumentParser(description="Decode Morse code from binary or direct Morse input.")
    parser.add_argument("-b", "--binary", type=str, help="Binary encoded Morse code")
    parser.add_argument("-f", "--file", type=str, help="File containing Morse code")
    args = parser.parse_args()
    
    if args.binary:
        output = binary_to_ascii(args.binary)
        print("Decoded Text:", output)
    elif args.file:
        with open(args.file, 'r') as file:
            morse_code = file.read().strip()
        output = morse_to_text(morse_code)
        print("Decoded Text:", output)
    else:
        print("Please provide a binary string (-b) or a file containing Morse code (-f).")

if __name__ == "__main__":
    main()
