def rebuild_sentence(words , lengths):
    sentences ="" #create a string to add the sentence
    for x , i in zip(words , lengths) : #to loop the two lists in parallel
        x = x[0 : i] #to slice the string [start : end]
        sentences += f"{x} " # add the new string after slicing 
            
    return sentences
        
        
print(rebuild_sentence( [ "the", "sky", "is", "blue" ] , [ 3, 2, 2, 1 ] )) #for testing
        