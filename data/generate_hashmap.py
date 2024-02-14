from collections import defaultdict

#Helper Functions:
files = [
    './files/hollywood_celebs.txt',
    './files/forbes_billionaires.txt',
    './files/general_celebs.txt',
    './files/politicians.txt'
]


def file_to_list(file_path):
    #Usage: converts the file into a list of words 
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines  


def generate_hashmap_of_famous_names(file_paths):
    #Usage: populates the hashmap we will be using to do a quick look up of celebrity names
    #We are building a hashmap instead of a set because we want to be able to detect names that closely resemble famous names
    global_list = []
    hashmap = defaultdict(list)

    for path in files:
        print(path)
        names = file_to_list(path)
        for name in names:
            first_letter = name[0].lower()

            #Store First Name
            hashmap[first_letter].append(name)

            #Store Last Name for people refered to by their last names 
            split_name = name.split(" ")
            if len(split_name) >= 2:
                hashmap[first_letter].append(split_name[-1])

    return hashmap



def get_total_hashmap_size(hashmap):
    #Usage: returns the total number of names stored on the hashmap
    total_size = sum(len(value) for value in hashmap.values())
    print("Total size of the hashmap including lengths of all lists:", total_size)




#Main Function:
def initialize_hashmap():
    hashmap = generate_hashmap_of_famous_names(files)
    get_total_hashmap_size(hashmap)
    return hashmap

initialize_hashmap()