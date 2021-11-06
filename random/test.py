#region zipTest
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

#%%
coordinate = ['x', 'y', 'z']
value = [3,4,5]

result = zip(coordinate, value)
result_list = list(result)

print(result_list)
c, v = zip(*result_list)
print(' c = ', list(c))
print(' v = ', v)

#endregion
#%%
#h e l o w o r l d
HW = ' h e l l o   w o r l d '
#create a list of the abc
listA = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in list(HW):
    if i in listA:
        print(i, end="")
        

#%%
print("its even") if int(input("enter a number")) % 2 == 0 else print("its odd")

#%%
from testFolder import testFile as test

test.test()

#%%
import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
while True:
    player_choice = str(input("rock, paper, or scissosrs?: "))
    if player_choice in choices:
        break

print(f"computer: {computer}")
print(f"player: {player_choice}")

#%%
import antigravity

# %%
import pywhatkit as kit
mess = "que onda trolo a vos seguro que te encanta la pija no? cuantas te comiste? 1,2,3,4,5?"
kit.sendwhatmsg("+5491131992464", mess,14,11)

#%%
import pyautogui as pyauto
import time
time.sleep(1)
for i in range(50):
    pyauto.typewrite("que onda puto vos seguro te comiste como " + str(i) + " pijas no? manco")
    pyauto.press("enter")