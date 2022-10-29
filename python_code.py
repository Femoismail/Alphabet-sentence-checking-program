#This is an alphabet sentence checking program.

sentence = input("Please enter a sentence :")

print("PLEASE NOTE: Your alphabet is case sensitive.")
alphabet = input("Please enter Alphabet :") 

sentence_list = sentence.split(" ")

counter = 0

word_counter = 0

while counter < len(sentence_list):  
    if sentence_list[counter][0] == alphabet:
        print("This word " + sentence_list[counter] + " begins with " + alphabet) 
        counter += 1 
        word_counter += 1
    else: 
        counter += 1

print(word_counter, f"words begin with {alphabet}")