def rebuild_sentence(words , lengths):
    sentences ="" 
    for x , i in zip(words , lengths) : #to loop the two lists in parallel
        x = x[0 : i] #to slice the string [start : end]
        print(x , i)
        sentences += f"{x} "
        
        
    return sentences
        
        
print(rebuild_sentence( [ "the", "sky", "is", "blue" ] , [ 3, 2, 2, 1 ] ))
        