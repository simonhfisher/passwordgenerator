import csv 
import random


def text_grabber(file_name): 
    
    word_list=[]

    with open(file_name, "r") as file_to_read:
        reader = csv.reader(file_to_read)

        for data in reader:
            
            word_list.append(data[0])

    return word_list



 




if __name__ == "__main__":
    
    words_to_use_for_password_gen = text_grabber("FiveLetterWordsGood.txt")
   
