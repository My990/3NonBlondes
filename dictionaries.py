# d = {'fox':['Fuchs','shual']
# ,'dog':'Hund'
# }
# d['cat'] = 'Katze'  #adds a key value pair


# print(d)

# print(d.values())   #shows the values witheout the keys

# print(d.keys() )   #shows the keys without the values

# print('fox' in d)       #checks if the key 'fox' exists (bool)
# print('Fuchs' in d)     #false. cannot check for a value inside a key when looking on the dict.

# d.setdefault('fish',0)
# print (d)                   #sets default value to fish when we did not assign one?

# print(d.get('dog'))         #returns the value for the key 'dog'
# print(d.get('fox'))
# print(len(d))               #returns the length of d - incl the fish. (how many pairs)

# #print(d['Katze'])           #error. []cannot return the key for the value, only search over the keys

dogs = ['poodle','husky','shiba inu','shiba inu','husky','husky' ]
counts = {}
for dog in dogs:
    if dog not in counts:
        counts[dog] = 0
    counts[dog] +=1

print(counts)