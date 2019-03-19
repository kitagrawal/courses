def anti_vowel(text):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    new_string = []
    for i in text:
        if i not in vowel:
            new_string.append(i)
    
    """for j in new_string:
        for v in vowel:
            if i.lower() == j:
                new_string.pop(i)"""
    
    return "".join(new_string)

print anti_vowel("Hey there!")
