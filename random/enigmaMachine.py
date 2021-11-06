# %%
alphabet = "abcdefghijklmnopqrstuvwxyz"
puntuaction = ".,?'! "

# %%
messege = "hey vishal! This is a super cool cipher, thanks for showing me! What else you got?"
mensaje_cifrado = ""
# %%
for letter in messege:
    if not letter in puntuaction:
        letter_value = alphabet.find(letter)
        mensaje_cifrado += alphabet[(letter_value - 10) % 26]
    else:
        mensaje_cifrado += letter
print(mensaje_cifrado)

# %%
messege = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
mensaje_traducido = ""

# %%
for letter in messege:
    if not letter in puntuaction:
        letter_value = alphabet.find(letter)
        mensaje_traducido += alphabet[(letter_value + 10) % 26]
    else:
        mensaje_traducido += letter
print(mensaje_traducido)

