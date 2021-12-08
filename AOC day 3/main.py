#%%
import getData
values = getData.getValues()
# %%

c0 = [0,0,0,0,0,0,0,0,0,0,0,0]
c1 = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in values:
    pos = 0
    for x in i:
        if x == "0":
            c0[pos] += 1
        else:
            c1[pos] += 1
        pos += 1

print(c0,c1)

gr = ""
er = ""
for a,b in zip(c0,c1):
    if a > b:
        gr += "1"
        er += "0"
    else:
        gr += "0"
        er += "1"

decgr = int(gr, 2)
decer = int(er,2)

final = decgr * decer
final

#%%
len(values[0])
#%%
# oxygen rate
oxRate = 0
co2Rate = 0
fullList = values
for bit in range(len(values[0])):

    c0,c1 = 0,0
    for x in fullList:
        if x[bit] == "0":
            c0 += 1
        else:
            c1 += 1
    print("c0: ", c0)
    print("c1: ", c1)

    if c0 > c1:
        fullList = [x for x in fullList if x[bit] == "0"]
        print(fullList)
    elif c1 >= c0:
        fullList = [x for x in fullList if x[bit] == "1"]
        print(fullList)
    if len(fullList) == 1:
        break
print(fullList)
oxRate = int(fullList[0],2)
oxRate
#%%
#co2 rate
fullList = values
for bit in range(len(values[0])):

    c0,c1 = 0,0
    for x in fullList:
        if x[bit] == "0":
            c0 += 1
        else:
            c1 += 1
    print("c0: ", c0)
    print("c1: ", c1)

    if c0 <= c1:
        fullList = [x for x in fullList if x[bit] == "0"]
        print(fullList)
    elif c1 < c0:
        fullList = [x for x in fullList if x[bit] == "1"]
        print(fullList)
    if len(fullList) == 1:
        break
print(fullList)
co2Rate = int(fullList[0],2)
co2Rate

# %%
print(oxRate, co2Rate)
print(int(oxRate) * int(co2Rate))