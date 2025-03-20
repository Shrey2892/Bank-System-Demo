def caesar_encode(message, shift):
    result = ''
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decode(message, shift):
    return caesar_encode(message, -shift)

# Taking user input
message = input("Enter the message: ")
shift = int(input("Enter shift amount (integer): "))
choice = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()

if choice == 'encode':
    encoded = caesar_encode(message, shift)
    print(f"Encoded message: {encoded}")
elif choice == 'decode':
    decoded = caesar_decode(message, shift)
    print(f"Decoded message: {decoded}")
else:
    print("Invalid choice!")
