import random

dist = int(input("マスの数 = "))
player1=[0]
player2=[0]

while True:
    if sum(player1) < dist:
        sai1=random.randint(1,6)
        print ("player1の出た目は"+str(sai1)+"です")
        player1.append(sai1)
        masu1=sum(player1)
        print ("player1は現在"+str(masu1)+"マス進んでいます")
        if masu1 == dist:
            print ("player1 goal!")
            break
        
    elif sum(player1) >dist:
        sai1=random.randint(1,6)
        print ("player1の出た目は"+str(sai1)+"です")
        sai1=-sai1
        player1.append(sai1)
        masu1=sum(player1)
        print ("player1は現在"+str(masu1)+"マス進んでいます")
        if masu1 == dist:
            print ("plater1 goal!")
            break

        
    if sum(player2) < dist:
        sai2=random.randint(1,6)
        print ("player2の出た目は"+str(sai2)+"です")
        player2.append(sai2)
        masu2=sum(player2)
        print ("player2は現在"+str(masu2)+"マス進んでいます")
        if masu2 == dist:
            print ("player2 goal!")
            break
    elif sum(player2) >dist:
        sai2=random.randint(1,6)
        print ("player2の出た目は"+str(sai2)+"です")
        sai2=-sai2
        player2.append(sai2)
        masu=sum(player2)
        print ("player2は現在"+str(masu2)+"マス進んでいます")
        if masu2 == dist:
            print ("player2 goal!")
            break
    
    


