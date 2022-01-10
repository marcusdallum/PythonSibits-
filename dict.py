#New nested dictonary
print('New Nested Dictonary')
new_nesteddict = {'Key 1' : {'Key 1.1' :'Key 1.1 Data' ,
                         'Key 1.2': 'Key 1.2 Data' },
              'Key 2' : {'Key 2.1' :'Key 2.1 Data' ,
                         'Key 2.2':'Key 2.2 data' } 
                 }
print(new_nesteddict)
print('\n')

#add new key with empty nest
print('New Key 3 empy nest')
new_nesteddict['Key 3'] = {}
print(new_nesteddict['Key 3'])
print('\n')

#add new nested key to Key 3
print('New Key 3.1 data')
new_nesteddict['Key 3']['Key 3.1'] = 'Key 3.1 Data'
print(new_nesteddict['Key 3'])
print('\n')

#access data from Key 3.1
print('Data from Key 3.1')
x = new_nesteddict['Key 3']['Key 3.1']
print(x)
print('\n')

#get top keys from dict
print('Nested top keys')
for x in new_nesteddict:
	print(x)
print('\n')

# get the nested items in all top keys
print('Nested items in top level')
for keys , nested_dict in new_nesteddict.items():
	print(nested_dict)
print('\n')

# get the nested keys
print('Nested keys')
for keys , nested_dict in new_nesteddict.items():
	for nested_keys , nested_data in nested_dict.items():
		print(nested_keys)
print('\n')

# get the nested data
print('Nested data')
for keys , nested_dict in new_nesteddict.items():
	for nested_keys , nested_data in nested_dict.items():
		print(nested_data)
print('\n')
