#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = 0
    best_score_key = None
    for key, score in a_dictionary.items():
        if score > best_score:
            best_score = score
            best_score_key = key
    return (best_score_key)
