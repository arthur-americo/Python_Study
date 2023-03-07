'''Create a program that has a tuple with several words (don't use accents). After that, you must show, for each
word, what are its vowels.'''
word = ('apple', 'banana', 'orange', 'grape', 'watermelon', 'strawberry', 'pineapple', 'pear', 'peach', 'cherry')
for w in word:
    print(f'\nIn the word {w.upper()} the vowels are: ', end='')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')

    

