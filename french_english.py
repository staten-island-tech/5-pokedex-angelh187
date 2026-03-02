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

def lang(sent):
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
lang("this is a ttttttest")
    
