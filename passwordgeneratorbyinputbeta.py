print("""
    
    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@                                                                                                                                             @@@@@
@@@@  @@@@@@@@@@@@@        @@@@@@@@@@@      @@@@       @@@@    @@@@@@@@@@@@               @@@@@@@@@@@      @@@@@@@@@@@@@@@    @@@@       @@@@    @@@@@
@@@@  @@@@       @@@@    @@@@               @@@@       @@@@    @@@@       @@@           @@@@               @@@@               @@@@@@@@@  @@@@    @@@@@
@@@@  @@@@       @@@@      @@@@@@@@@@@      @@@@   @@  @@@@    @@@@       @@@@  @@@@@@  @@@@     @@@@@@    @@@@@@@@@@@@@      @@@@   @@@@@@@@    @@@@@
@@@@  @@@@@@@@@@@@@                 @@@@    @@@@@@@@@@@@@@@    @@@@       @@@@  @@@@@@  @@@@       @@@@    @@@@               @@@@     @@@@@@    @@@@@
@@@@  @@@@               @@@@       @@@@    @@@@@@   @@@@@@    @@@@     @@@@            @@@@       @@@@    @@@@               @@@@       @@@@    @@@@@
@@@@  @@@@                 @@@@@@@@@@@      @@@@       @@@@    @@@@@@@@@@@                @@@@@@@@@@  @    @@@@@@@@@@@@@@@    @@@@       @@@@    @@@@@
@@@@                                                                                                                                             @@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

by arthurvmbl & HenriqueMenezesN   

    """)
from itertools import permutations
from math import floor
def list_generator(list_of_possible_words,namelist):
    try:
        with open(namelist + ".txt",mode="wb") as f:
            list_of_possible_words = list(filter(None,list_of_possible_words))
            try:
                length = int(input(f"How many words do you want to combine? "))
                if length>len(list_of_possible_words):length = len(list_of_possible_words)
            except:length = len(list_of_possible_words)             
            for i in range(length,1,-1):
                try:
                    print('Permutation lenght: ',i)
                    permutation_examples = list(permutations(list_of_possible_words, length))
                    break
                except MemoryError as e:
                    print("Memory Error: ",e,'\nTrying to reduce the permutation lenght.')
                    permutation_examples = list()
            permutation_examples = list(permutations(list_of_possible_words, length))
            output = [(''.join(_)+'\n').encode() for _ in permutation_examples]
            f.writelines(output)
        return True
    except:return False
if __name__=='__main__':
    namelist = input("Give your list a name: ")
    lista = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'.split(' ')
    
    if list_generator(lista,namelist):
        print("Your list is ready!")
    else:
        print('Error on list creation.')