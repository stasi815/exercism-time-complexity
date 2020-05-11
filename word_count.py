import re

def count_words(sentence):
    # clean the sentence of unwanted characters and punctuation
    new_string = re.sub(r"\t|\n|:|!|@|#|\$|%|\^|&|,|\.| '|' |'$| \"|\" |_|''", ' ', sentence.lower())
    # split the sentence into words and make a list of those words
    words = new_string.split()
    word_count={}
    count = 1

    # iterate through the list of words and add words and their counts as the
    # key-value pairs in the dictionary 
    for word in words:
        if word not in word_count:
            word_count[word] = count
        else:
            word_count[word] += 1
    return word_count

# The time complexity for this function is O(n) because the time depends on the length of the sentence being input.
# The space complexity is O(N).


print(count_words("cat cat Cat Dog cat Dog"))
print(count_words("one,\ntwo,\nthree"))
print(count_words("Joe can't tell between 'large' and large."))
print(count_words("rah rah ah ah ah	roma roma ma	ga ga oh la la	want your bad romance"))
print(count_words("hey,my_spacebar_is_broken"))