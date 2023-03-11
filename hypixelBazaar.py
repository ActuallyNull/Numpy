import requests
import time
import json
print("#########################################################")
print("######   welcome to my my   #############################")
print("######   piece of shit code #############################")
print("######   its shit but it    #############################")
print("######   works lol oh and   #############################")
print("######   RobbieW made it    #############################")
print("######   this only grabs    #############################")
print("######   shit and  you need something else to parse it lol")
print("#########################################################")
apiKey = "7da911e8-0ce9-4fc9-849d-d79d76bd18d0"
x = 1
for i in range(0, 115): 
    prijs = (requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey).json()["products"]["RECOMBOBULATOR_3000"]["quick_status"]["buyPrice"])
    f = open("data.txt","a+")
    f.write(f'{x} {prijs} \n')
    f.close
    print(prijs)
    i = i ++ 1
    x = x ++ 1
    time.sleep(60)
print("115 requests we done lol")