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

    return "".join(password_list)

    

    

if __name__ == "__main__":
    
    words_to_use_for_password_gen = text_grabber("FiveLetterWordsGood.txt")
   
    print(password_length_generator(4,words_to_use_for_password_gen))


    
 
 

