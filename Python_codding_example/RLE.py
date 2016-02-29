def rle(seq):
    result = []
    old = seq[0]
    count = 1
    for num in seq[1:]:
        if num == old:
            count += 1
        else:
            result.append((old, count))   
            count = 1      
            old = num
    result.append((old, count))    
    return result
    
print rle("Codding word")
