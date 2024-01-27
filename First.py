'''
#Store the given values into the file :

data = ['India','Germany','France','Australia']
file = open('countries.txt','w')
print('file created successfully')
for i in data:
    file.write(i)
    file.write(' ')
print('data loaded successfully')
file.close()

with open('countries.txt','r') as out:
    data = out.read()
    val = data.split()
    print(val)
'''
        
