dict={}
for item in dir(dict):
    print item + '\n'
dict1={'key1':'value1','key2':'value2'}
dict=dict1.copy()
print dict
print dict1
dict1.clear()
print dict1
print dict.get('key1') # return the value of key1
print dict['key1'] # return the value for key1
print dict.items() # return a list of dict
for k, v in dict.items():  # iterate dict
    print k, v


seq=['id','name','date','addr']
dict=dict.fromkeys(seq) # create new dict by keys in list
print dict 
seq1=('Id','Name','Date','Addr','Rate')
dict=dict.fromkeys(seq1)  # create new dict by keys in tuple
print dict
dict=dict.fromkeys(seq1,10) # create new dict by keys and set value 
print dict
dict['Type']=''
print dict.get('Type')   # print 
print dict.has_key('Id') # print true or false if has key
print dict.keys()   # print keys as a list
print dict.values() # print values as a list
dict3={'Field1':'value1','Field2':'value2'}
dict.update(dict3)
print dict
print dict.items() # convert dict to list
print dict.iteritems()
for i in dict.iteritems(): # iterate dict key,value
    print i
print dict.iterkeys()
for i in dict.iterkeys():  # iterate dict keys
    print i
print dict.itervalues()
for i in dict.itervalues(): # iterate dict values
    print i
print dict.viewitems()     # view key, value
print dict.viewvalues()    # view values
print dict.viewkeys()      # view keys
dict=sorted(dict.items())
print dict
print dict.pop()
print dict
