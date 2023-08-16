#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sort_dic = sorted(a_dictionary.items(), key=lambda x: x[1])
        new = dict(sort_dic)
        return list(new.keys())[-1]
