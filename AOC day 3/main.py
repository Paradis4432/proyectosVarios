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
