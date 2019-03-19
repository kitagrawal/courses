def censor(text, word):
    
    words = text.split()
    for i in range(len(words)):
        if word in words[i]:
            words[i] = '*' * len(words[i])
            text = ' '.join(words)
    return text

print censor('this hack is wack hack','hack')
