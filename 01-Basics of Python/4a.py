
import string
#program to remove punctuations from a phrase 
def remove_punc(phrase):
    p_wo_punc = ' '
    for letter in phrase:
        if letter not in  string.punctuation:
            p_wo_punc += letter
    return p_wo_punc
    
my_story = "India is my country! All Indians are my brothers; and Sisters I Love my country!!"
result = remove_punc(my_story)
print("Phrase without punctuations: " + result)
words = result.split()
print(words)

