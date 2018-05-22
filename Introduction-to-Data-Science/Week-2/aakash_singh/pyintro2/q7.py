# sort using values in dictionary

def sortDictionary(D,rev=False):
    sortedKeys = sorted(D,key=(lambda x:D[x]),reverse=rev)
    newD={}
    for key in sortedKeys:
        newD[key]=D[key]
    return newD


a={1:9,2:7,3:5,4:8}  # code to test the function
print(sortDictionary(a))