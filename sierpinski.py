def stampaj(stepenRekurzije : int) -> None:
    n = 2**(stepenRekurzije+1)
    for y in range(n-1, -1, -1):
        # stampamo razmak y puta
        for _ in range(0,y):
            print(" ",end="")
 
        # crtamo '*'
        for x in range(0, n-y):
            if (x & y):
                print(" ", end = " ")
            else:
                print("*", end = " ")
         
        print()
         
stepenRek = 5
stampaj(stepenRek)