# %%
from typing import cast
import data

values = data.getData()

# %%
count = 0
for i in range(3, len(values)):
    if values[i] > values[i-3]:
        count += 1

print(count)
