import random

dist = int(input("マスの数 = "))
while True:
    if dist < 20 or dist > 39:
        print ("20以上40未満を入力してください!")
        dist = int(input("マスの数 = "))
    else:
        break
        
human = int(input("人数 = "))
while True:
    if human < 2 or human > 5:
        print ("2以上6未満を入力してください!")
        dist = int(input("人数 = "))
    else:
        break

        
point=[0]*human
player=[0]*human
pointload=[0]

for i in range(1,dist):
    pointload.append(random.randint(1,10))
   
while player != [dist]*human:
    for i in range(0,human):
        if player[i] != dist:
            sai=random.randint(1,8)
            print("player"+str(i+1)+"の出た目は"+str(sai)+"です。")
            if sai % 2 == 1:
                sai=-sai
            player[i]+=sai
            if player[i] < 0:
                player[i]=0
            if player[i] < dist:
                print("player"+str(i+1)+"の進んだ目は"+str(player[i])+"です。")
                point[i]+=pointload[player[i]]
                print(str(pointload[player[i]])+"ポイント獲得！player"+str(i+1)+"の合計ポイントは"+str(point[i])+"です。")
            if player[i] == dist:
                print("player"+str(i+1)+"はゴール！")
                point[i]+= human/(player.count(dist))
                print(str(player.count(dist))+"番にゴールしたので、最終ポイントは"+str(point[i])+"です！")
            if player[i] > dist:
                print("player"+str(i+1)+"の進んだ目は"+str(player[i])+"です。振り出しに戻ります。")
                player[i]=0
                point[i]+=pointload[player[i]]
                print(str(pointload[player[i]])+"ポイント獲得！player"+str(i+1)+"の合計ポイントは"+str(point[i])+"です。")

print("全員ゴール！") 

        
    
    
    


