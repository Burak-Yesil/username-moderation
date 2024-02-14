from data.generate_hashmap import celeb_hashmap
from data.similarity_test import check_similarity
# from ml_model.sentiment_analysis import sentiment_analysis



def is_valid_name(username):
    #Initialize populated hashmap
    target_names = celeb_hashmap[username[0].lower()]
    
    #Check if the name is in the populated hashmap 
    match = check_similarity(username, target_names)
    if match:
        return False
    
    #run inference on twitter model 
    return True







print(is_valid_name("Well Smith"))