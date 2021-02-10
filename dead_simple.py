import random


my_list = ["chicken","berlin","shoe", "gin", "mallet", "clamp", "scientology", "lamp"]


def thing_weighter(list_, number_of_outputs):
    weight_list = []
    for i in list_ :
        weight_list.append(len(i))

    return (random.choices(list_, weights = weight_list, k = number_of_outputs))
    
sample_data = thing_weighter(my_list, 10000)   


def thing_weighter_counter(sample_data):
    unique_word_dictionary = {}
    
    for word in sample_data :
        if word in unique_word_dictionary.keys():
            unique_word_dictionary[word] += 1
        else :
            unique_word_dictionary[word] = 1 

    print(unique_word_dictionary)

thing_weighter_counter(sample_data)


