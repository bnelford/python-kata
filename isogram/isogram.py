def is_isogram(word):
    ind=0
    w=word.lower()
    for letter in w:
        if letter.isalpha() != True:
            break
        else:
            if(w.find(letter,ind+1)>-1):
                return False
            else:
                ind+=1
    return True
