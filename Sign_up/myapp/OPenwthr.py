KINGDOM_VS_EMBLEM = {"SPACE": "GORILLA", "LAND": "PANDA", "WATER": "OCTOPUS", "ICE": "MAMMOTH", "AIR": "OWL",
                     "FIRE": "DRAGON"}
OUTPUT = ''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
file = open("data_Femy.txt", "r")
lines = file.readlines()
decrypt = ''

# iterate eachline from data.txt file
for input in lines:
    # ignoring empty lines
    if len(input.strip()) != 0:
        kingdom, emblem = str(input.strip()).split(' ')
        # decripting message from the file
        for i in emblem:
            key = len(KINGDOM_VS_EMBLEM[kingdom])
            pos = alphabet.find(i)
            newpos = pos - key
            if (newpos < 0):
                newpos += 26
            elif newpos > 25:
                newpos -= 26
            decrypt += alphabet[newpos]
        var = KINGDOM_VS_EMBLEM[kingdom]
        isWonKingdom = True
        # checking  if the decripted messege contain emblem of the kingdom
        for i in var:
            value = decrypt.find(i)
            if value != -1:
                decrypt = decrypt.replace(i, '', 1)
            else:
                isWonKingdom = False
                break
                # appending kingdoms which are one
        if isWonKingdom == True:
            if OUTPUT == '':
                OUTPUT = kingdom
            else:
                OUTPUT += ' ' + kingdom
print(OUTPUT)

file.close()





