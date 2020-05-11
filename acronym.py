import re

def abbreviate(words):
    # handle punctuation and special characters
    new_words = re.sub(r"\t|\n|:|!|@|#|\$|%|\^|&|,|\.| '|' |'$| \"|\" |_|''|-", ' ', words)
    # split string of words into a list
    words = new_words.split()

    # add the first letter of each word in uppercase form to the new list then
    # convert the list of uppercase first letters back into a string
    acronym_list = []
    for word in words:
        letter = word[0].upper()
        acronym_list.append(letter)
        acronym = ''.join(acronym_list)
    return acronym

# Time complexity is O(n) because it depends on the length of the original string.
# Space complexity is O(N).


print(abbreviate("Big long Journey"))
print(abbreviate("First In, First Out"))
print(abbreviate("Complementary metal-oxide semiconductor"))
print(abbreviate("Rolling On The Floor Laughing And Shaking"))
print(abbreviate("The Road _Less_ Travelled"))


