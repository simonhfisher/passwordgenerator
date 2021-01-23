#pig latin maker 

def pig_latin_maker(word):
    first_letter = (word[0])
    rest_of_word = (word[1: ])
    pig_word = (rest_of_word) + (first_letter) + "ay" 

    return pig_word

#print(pig_latin_maker("chicken"))  


def pig_latin_sentence_fucker(words):
    output = " "
    list_made_from_input_string = (words.split()) 
    for word in list_made_from_input_string:
        output += pig_latin_maker(word) + " "

    return output.strip()    #strip is removing white space (leading or trailing spaces) - in this case the space after the last word


print(pig_latin_sentence_fucker("fuckin chicken mate"))

    





