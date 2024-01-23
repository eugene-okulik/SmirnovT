text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = text.split()
modified_words = []
for word in words:
    if word[-1] in ',.':
        modified_word = word[:-1] + 'ing' + word[-1]
    else:
        modified_word = word + 'ing'
    modified_words.append(modified_word)
modified_text = ' '.join(modified_words)
print(modified_text)
