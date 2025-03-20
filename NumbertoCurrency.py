def format_indian_currency(number):
    parts = str(number).split('.')
    integer_part = parts[0]
    decimal_part = '.' + parts[1] if len(parts) > 1 else ''

    # Reverse the integer part
    reversed_digits = integer_part[::-1]
    result = ''
    for i in range(len(reversed_digits)):
        if i == 3 or (i > 3 and (i - 1) % 2 == 0):
            result += ','
        result += reversed_digits[i]

    return result[::-1] + decimal_part

# Taking user input
num = input("Enter a number to format (e.g., 1234567.89): ")
formatted = format_indian_currency(num)
print(f"Indian Currency Format: {formatted}")
