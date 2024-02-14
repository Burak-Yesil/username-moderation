from fuzzywuzzy import fuzz

def check_similarity(input_name, target_names, threshold=80):
    #Usage: compares input_name to target_names and returns if they are similar
    similar_names = []
    for target_name in target_names:
        similarity_score = fuzz.ratio(input_name.lower(), target_name.lower())
        if similarity_score >= threshold:
            similar_names.append(target_name)
    return len(similar_names) > 0

