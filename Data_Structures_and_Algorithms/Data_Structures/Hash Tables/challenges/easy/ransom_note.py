# ----- Ransom Note: Dictionary Exercise -----

# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his
# handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create
# an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole
# words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note
# exactly using whole words from the magazine; otherwise, print No.

# ----- Optimal Solution -----

def checkMagazine(magazine, note):
    # Write your code here
    magazine_words = {}

    # magazine is a
    # note is b

    # Time = O(a)
    # Space = O(a)
    for word in magazine:
        if word in magazine_words:
            magazine_words[word] += 1
        else:
            magazine_words[word] = 1

    note_words_in_magazine = 0

    # Time = O(b)
    # Space = O(1)
    for word in note:
        if word in magazine_words:
            note_words_in_magazine += 1
            magazine_words[word] -= 1

            if magazine_words[word] == 0:
                del magazine_words[word]

    if note_words_in_magazine == len(note):
        print('Yes')
    else:
        print('No')

# Time = O(a) + O(b) or just O(n)
# Space = O(a)

# ----- Test Run -----


magazine = ['give', 'me', 'one', 'grand', 'today', 'night']

note = ['give', 'one', 'grand', 'today']

# Returns 'Yes'
print(checkMagazine(magazine, note))
