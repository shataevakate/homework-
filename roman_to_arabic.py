def roman_to_arabic(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    arabic_value = 0
    prev_value = 0

    for char in reversed(roman):
        current_value = roman_numerals[char]
        if current_value < prev_value:
            arabic_value -= current_value
        else:
            arabic_value += current_value
        prev_value = current_value
    return arabic_value

roman_input = input("Введите римское число: ")
result = roman_to_arabic(roman_input)
print("Арабское значение:", result)
