import csv 
import random


def text_grabber(file_name): 
    
    word_list=[]

    with open(file_name, "r") as file_to_read:
        reader = csv.reader(file_to_read)

        for data in reader:
            
            word_list.append(data[0])

    return word_list

def password_generator(word_list):
    length_of_word_list = len(word_list)
    random_number = random.randrange(length_of_word_list)
    random_word = word_list[random_number]


    return random_word 



def password_length_generator(password_length, list_of_words):

    password_list = []
    for i in range(password_length) :

        password_list.append(password_generator(words_to_use_for_password_gen))

    ###### OPTION ONE ######
    ###### A loop to make something like: "HOUSECLIMBAFTERDRAMA" --> "HouseClimbAfterDrama"

    for word in password_list:
        word_starting_with_uppercase = word.title()
        password_list.append(word_starting_with_uppercase)

    ########################

    ###### OPTION TWO ######
    ###### A loop to generate new passwords when the user isn't happy with the suggestion

    response = input("Are you happy with " + ("".join(password_list)) + " as your password? Type'yes' if so, or anything else to generate a new one:\n>>> ")

    if response.lower() == "yes":
        return "".join(password_list)
    else:
        return password_length_generator(password_length, list_of_words)
        
    ########################

    

    

if __name__ == "__main__":
    
    words_to_use_for_password_gen = text_grabber("FiveLetterWordsGood.txt")
   
    print(password_length_generator(4,words_to_use_for_password_gen))


    
 
 

