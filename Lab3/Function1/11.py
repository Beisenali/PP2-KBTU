def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))
