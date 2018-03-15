'''
Created on 06-Mar-2018

@author: Prateek
'''
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
        
    mapfrom = list(map_from)
    mapto = list(map_to)
    coded = list(code)
    decoded = []
    dict = {}
    for n in range(0,len(mapfrom)):
        dict[mapfrom[n]] = mapto[n] 
    for item in coded:
         decoded.append(dict[item])
           
    return (dict,''.join(decoded))
        
        
x = cipher("abcd", "dcba", "dab")
print(x)