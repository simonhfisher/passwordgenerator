import csv       #csv means comma speratated values
import random


def text_grabber(file_name): 
    
    word_list=[]

    with open(file_name, "r") as file_to_read:
        reader = csv.reader(file_to_read)

        for data in reader:
            
            word_list.append(data[0])

    return word_list

def random_word_generator(word_list):
    length_of_word_list = len(word_list)
    random_number = random.randrange(length_of_word_list)
    random_word = word_list[random_number]


    return random_word 


def password_generator(password_length, list_of_words, prevent_duplicates = True):

    password_list = []
    for i in range(password_length) :
        
        random_word = (random_word_generator(list_of_words))
        password_list.append(random_word)
        if prevent_duplicates == True :
            list_of_words.remove(random_word)















    ###### OPTION ONE ######
    ###### A loop to make something like: "HOUSECLIMBAFTERDRAMA" --> "HouseClimbAfterDrama"

    #for word in password_list:
    #    word_starting_with_uppercase = word.title()
    #    password_list.append(word_starting_with_uppercase)

    #return "".join(password_list)

    ########################

    ###### OPTION TWO ######
    ###### A loop to generate new passwords when the user isn't happy with the suggestion

    response = input("Are you happy with " + ("".join(password_list)) + " as your password? Type 'yes' if so, or anything else to generate a new one:\n>>> ")

    if response.lower() == "yes":
        return "".join(password_list)
    else:
        return password_generator(password_length, list_of_words)
        
    ########################

    

    

if __name__ == "__main__":
    
    words_to_use_for_password_gen = text_grabber("FiveLetterWordsGood.txt")
    words_to_use_for_password_gen = ["GRIPE","BINGO","ROWDY","JOINT"]
    print(password_generator(4,words_to_use_for_password_gen))


    
 
 
#prevent word duplication 
#user can provide first letters of words eg C,A,K,E
#provide the case 
#searches for letters similar to numbers and replaces with those numbers
#prints 10 passwords for user selection 
