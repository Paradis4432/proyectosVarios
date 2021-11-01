listA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
listB = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

#create a list with the values merged between listA and listB with the patern: A1, B2, C3
listC = [x+str(y) for x,y in zip(listA,listB)]
print(listC)

#%%
test = [1,2,3,4]
test2 = [5,6,7,8]

test3 = zip(test,test2)
test4 = [str(x)+str(y) for x,y in test3]

test4[1]

#%%
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(list(result_set)[1])



# %%
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v =  zip(*result_list)
print('c =', list(c)[1])
print('v =', v)