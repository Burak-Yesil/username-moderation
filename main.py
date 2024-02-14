from data.generate_hashmap import celeb_hashmap
from data.similarity_test import check_similarity
from ml_model.sentiment_analysis import sentiment_analysis

print(celeb_hashmap['a'])

def is_valid_name(username):
    target_names = celeb_hashmap(username[0])
    print(target_names)



