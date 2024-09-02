# palindrome or not

def is_palindrome(word):
    reverse=word[::-1]
    return word==reverse
print(is_palindrome("malayalam"))
    
# create a function with parameterr return reversed string

def reverse(word):
    reversed_str=word[::-1]
    return reversed_str
print(reverse("gouri"))