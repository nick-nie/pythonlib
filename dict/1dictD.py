dict={}
for item in dir(dict):
    print(item + '\n')
dict1={'key1':'value1','key2':'value2'}
dict=dict1.copy()
print(dict)
print(dict1)
dict1.clear()
print(dict1)
print(dict.get('key1')) # return the value of key1
print(dict['key1']) # return the value for key1
print(list(dict.items())) # return a list of dict
for k, v in list(dict.items()):  # iterate dict
    print(k, v)


seq=['id','name','date','addr']
dict=dict.fromkeys(seq) # create new dict by keys in list
print(dict) 
seq1=('Id','Name','Date','Addr','Rate')
dict=dict.fromkeys(seq1)  # create new dict by keys in tuple
print(dict)
dict=dict.fromkeys(seq1,10) # create new dict by keys and set value 
print(dict)
dict['Type']=''
print(dict.get('Type'))   # print 
print('Id' in dict) # print true or false if has key
print(list(dict.keys()))   # print keys as a list
print(list(dict.values())) # print values as a list
dict3={'Field1':'value1','Field2':'value2'}
dict.update(dict3)
print(dict)
print(list(dict.items())) # convert dict to list
print(iter(dict.items()))
for i in dict.items(): # iterate dict key,value
    print(i)
print(iter(dict.keys()))
for i in dict.keys():  # iterate dict keys
    print(i)
print(iter(dict.values()))
for i in dict.values(): # iterate dict values
    print(i)
print(dict.items())     # view key, value
print(dict.values())    # view values
print(dict.keys())      # view keys
dict=sorted(dict.items())
print(dict)
print(dict.pop())
print(dict)
