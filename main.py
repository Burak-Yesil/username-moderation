from data.generate_hashmap import celeb_hashmap
from data.similarity_test import check_similarity
from ml_model.sentiment_analysis import sentiment_analysis



def is_valid_name(username):
    #Usage: returns true if the username is valid and passes all of the tests 

    #Initialize populated hashmap
    target_names = celeb_hashmap[username[0].lower()]
    
    #Check if the name is in the populated hashmap 
    match = check_similarity(username, target_names)
    if match:
        return {"is_valid_name": False}
    
    #run inference on twitter model 
    is_positive = sentiment_analysis(username) 
    if not is_positive:
        return {"is_valid_name": False} 

    return {"is_valid_name": True}


def is_valid_comment(comment):
    #Usage: returns true if the comment does not contain hate
    
    #run inference on twitter model 
    is_positive = sentiment_analysis(comment) 
    if not is_positive:
        return {"is_valid_comment": False}

    return {"is_valid_comment": True}





print(is_valid_name("Well Smith")) #Detects Will Smith misspelled
