#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return 0, None
    x = len(sentence)
    return x, sentence[0]
