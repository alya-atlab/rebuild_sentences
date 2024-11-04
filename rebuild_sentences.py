def rebuild_sentence(words, lengths):
    for x , i in zip(words , lengths) :
        x = x[0:i]
        print(x , i)
        
    return words
        
        
print(rebuild_sentence( [ "the", "sky", "is", "blue" ] , [ 3, 2, 2, 1 ] ))
        