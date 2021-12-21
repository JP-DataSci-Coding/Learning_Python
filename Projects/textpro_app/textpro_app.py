def sentence_maker(phrase):
    capitalised = phrase.capitalize()  # Capitalises the first letter of string

    # To evaluate whether or not a phrase is a question, we are just going to simply check if it starts
    # with a interrogative word
    interrogative_words = ('Which', 'When', 'Where',
                           'Who', 'Whom', 'Whose', 'Why', 'Whether', 'How')

    # startswith() can be used with a single string or tuple of strings
    if capitalised.startswith(interrogative_words):
        # Inserts specified text into square bracket placeholder
        return '{}?'.format(capitalised)
    else:
        return '{}.'.format(capitalised)


phrases = []

while True:
    user_input = input('Say something please: ')  # Asks the user for input

    if not user_input:
        break  # Terminates current loop and executes next statement
    else:
        # Call sentence_maker() and append result
        phrases.append(sentence_maker(user_input))


# join() method takes all items in an iterable and joins them into one string with a separator.
print(' '.join(phrases))
