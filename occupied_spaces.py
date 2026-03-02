def occupied(n,y,t):
    found = 0
    for i in range(n):
        if y[i] == "c" and t[i] == "c":
            found +=1
    print(found)        

occupied(5,"cc..c","..ccc.")
