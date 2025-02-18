
#%%
mystr = "hello world!"
type(mystr)


mynum = 123
type(mynum)


mylist = ['apple','orange','grape','banana']
type(mylist)
for x in mylist:
    print(x)


#%%
myrange = range(1,11)
print(myrange)
type(myrange)
for i in myrange:
    print(i)

#%%
list(myrange)
type(list(myrange))
list(range(10))


#%% Dictionary

d = {"name":"Alan","age":20,"favColors":['red','yellow','blue'],"faveNums":[1,2,3]}
d.keys()
d.values()

d['name']

for key in d.keys():
    print(d[key])
    
    
d.items()

d['favFood']

d2 = d.copy()
d.pop("name")   
d.clear()   
del(d)


#%% Empty Dictionary from loop version 1 of 3

d = {}
names = ['alan','bob','charlie']
favNum = [2,7,13]
for i in range(3):
    d[names[i]] = favNum[i]
print(d)


#%% Empty Dictionary from loop version 2 of 3

d = {}
names = ['alan','bob','charlie']
favNum = [2,7,13]
for i,name in enumerate(names):
    d[name] = favNum[i]
print(d)


#%% Empty Dictionary from loop version 3 of 3

d = {}
names = ['alan','bob','charlie']
favNum = [2,7,13]
for name,num in zip(names,favNum):
    d[name] = num
print(d)

#%%

for name,num in zip(d.keys(),d.values()):
    print(name,num)


#%% Empty Dictionary from keys

names = ['alan','bob','charlie']
ages = 0
mydict3 = dict.fromkeys(names,ages)


#%%
mybool = bool()
print(mybool == False)
