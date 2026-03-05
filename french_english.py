""" def language (x,y):
    s = 0
    t = 0 
    for i in range(len(y)):
        if i == "s" or i == "S":
            s = s +1
        if i == "T" or i == "t":
            t = t +1


    if (s) > (t):
        print("French")
    elif  (s) == (t):
        print("probably french")
    else:
        print("english")


        language(100, "The red cat sat on the mat.")
 """

""" def lang(sent):
    s = 0
    t = 0
    for i in sent:
        if i == "S" or i == "s":
            s += 1
        elif i == "t" or i == "T":
            t += 1
    if (s) > (t):
        print("French")
    elif  (s) == (t):
        print("probably french")
    else:
        print("english")


lang("why are you so sad cat?")
lang("this is a ttttttest") """




 
""" def honi(x):
    h = 0
    o = 0
    n = 0
    e = 0
    honis = 0
    for i in x:
        if i == "h" or "H":
            h = h +1
        elif i == "o" or "O":
            o = o +1 
        elif i == "N" or "n":
            n = n +1
        else:
            i == "i" or "I"
            e = e + 1
        if (h + o + n + e) / 4 == 0:
            honis == (h + o + n + e) / 4

    honi("honihoni")
    print(honis) """




def honi():

    honi = ["H", "h","O", "o", "N", "n","I", "i"]
    b = 0
    c = 1
for i in honi:
    if i == "H" or "h":
        b += 2
        c += 2











        
def magnus(word):
    count = 0 
    state = 0 
    for char in word:
        if state == 0 and char.upper() == "H":
            state = 1
        elif state == 0 and char.upper() == "H":
            state = 2
        elif state == 0 and char.upper() == "H":
            state = 3
        elif state == 0 and char.upper() == "H":
            state = 0
            count += 1
    print (count)
magnus("HHHHONI")



