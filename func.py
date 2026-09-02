def vowels(text):
    vowel = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowel:
            count += 1
    return count

print(vowels("Hello World"))  # Output: 3