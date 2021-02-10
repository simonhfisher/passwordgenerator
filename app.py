import csv       #csv means comma speratated values
import random


def text_grabber(file_name): 
    
    word_dict= {}

    with open(file_name, "r") as file_to_read:
        reader = csv.reader(file_to_read)

        for data in reader:
            sorter(data[0],word_dict)
            
    return word_dict


def sorter(word,word_dict):

    first_letter_of_word = word[0]    
    if first_letter_of_word in word_dict.keys():       # the .keys is for readability and is not necessary
        word_dict[first_letter_of_word].append(word)
    else :
        word_dict[first_letter_of_word] = [word] 


def random_word_generator(word_list):
    length_of_word_list = len(word_list)
    random_number = random.randrange(length_of_word_list)
    random_word = word_list[random_number]
    
    return random_word


def password_generator(password_length, dict_of_words, prevent_duplicates = True, use_acronym = None):

    if type(use_acronym) == str :
        password = password_generator_with_acronym(dict_of_words, use_acronym, prevent_duplicates)

    else :
        password = password_generator_without_acronym(dict_of_words, password_length, prevent_duplicates)

    if type(password) == str :
        print_fail_message(password)
        return None 

    string_password = " ".join(password) 
    print(string_password)    #temporary print
    return string_password   


def password_generator_with_acronym(word_dict, acronym, prevent_duplicates):
    acronym_word_list = []
    for letter in acronym:
        try:
            individual_acronym_word = random_word_generator(word_dict[letter.upper()])
        except:
            return letter.upper()   
        acronym_word_list.append(individual_acronym_word)
        if prevent_duplicates == True :
            word_dict[letter.upper()].remove(individual_acronym_word)

    return acronym_word_list   


def password_generator_without_acronym(word_dict, password_length, prevent_duplicates):
    total_word_list = []
    for word_list in word_dict.values():
        total_word_list += word_list

    password_list = []
    for i in range(password_length) :
    
        random_word = (random_word_generator(total_word_list))
        password_list.append(random_word)
        if prevent_duplicates == True :
            total_word_list.remove(random_word)

    
    response = input("Are you happy with " + ("".join(password_list)) + " as your password? Type 'yes' if so, or anything else to generate a new one:\n>>> ")

    if response.lower() == "yes":
        return password_list
    else:
        return password_generator_without_acronym(word_dict, password_length, prevent_duplicates)

def print_fail_message(letter_not_present):

    print(f"you have run out of {letter_not_present} words")


if __name__ == "__main__":
    
    words_to_use_for_password_gen = text_grabber("FiveLetterWordsGood.txt")
    #words_to_use_for_password_gen = ["GRIPE","BINGO","ROWDY","JOINT"]
    password_generator(4,words_to_use_for_password_gen, True, ("A"*30))
   
 
#password_generator(password_length, dict_of_words, prevent_duplicates = True, use_acronym = None)
#prevent word duplication - done 
#user can provide first letters of words eg C,A,K,E
#provide the case 
#searches for letters similar to numbers and replaces with those numbers
#prints 10 passwords for user selection 
# function that shows the amount of words beginning with a letter 

# temp_word_list = copy.deepcopy(word_list)  how to possibly make a deep copy of a list