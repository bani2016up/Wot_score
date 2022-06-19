import matplotlib.pyplot as plt
import numpy as np
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017") #or ("localhost", 27017)

# connect or create  DB
db = client["WotDB"]

# collection (if not exist -> create)
collection = db["WotDB"]

user1 = input('Имя игрока 1: ')
user2 = input('Имя игрока 2: ')
user3 = input('Имя игрока 3: ')

kofUser1 = int(input('Доп. коэффициент для ' + user1 + ": "))
kofUser2 = int(input('Доп. коэффициент для ' + user2 + ": "))
kofUser3 = int(input('Доп. коэффициент для ' + user3 + ": "))

frascore = int(input('Сколька оч. за фраг: '))


Fraguser1 = int(input('сколько фрагов сделал ' + user1 + ": "))
scoreUser1 = int(input('Сколько урона сделал ' + user1 + ": "))
scoresvetUser1 = int(input('Сколько засвета сделал  ' + user1 + ": "))

Fraguser2 = int(input('сколько фрагов сделал ' + user2 + ": "))
scoreUser2 = int(input('Сколько урона сделал ' + user2 + ": "))
scoresvetUser2 = int(input('Сколько засвета сделал ' + user2 + ": "))

Fraguser3 = int(input('сколько фрагов сделал ' + user3 + ": "))
scoreUser3 = int(input('Сколько урона сделал ' + user3 + ": "))
scoresvetUser3 = int(input('Сколько засвета сделал ' + user3 + ": "))

data = {
    'fragscore': frascore,
    
    'name1': user1,
    'Kof1': kofUser1,
    'Fraguser1': Fraguser1,
    'scoreUser1': scoreUser1,
    'scoresvetUser1': scoresvetUser1,
    
    'name2': user2,
    'Kof2': kofUser2,
    'Fraguser2': Fraguser2,
    'scoreUser2': scoreUser2,
    'scoresvetUser2': scoresvetUser2,
    
    'name2': user2,
    'Kof2': kofUser2,
    'Fraguser2': Fraguser2,
    'scoreUser2': scoreUser2,
    'scoresvetUser2': scoresvetUser2,
    
}
collection.insert_one(data)

Fuser1 = Fraguser1 * frascore + scoreUser1 + scoresvetUser1 * kofUser1
Fuser2 = Fraguser2 * frascore + scoreUser2 + scoresvetUser2 * kofUser2
Fuser3 = Fraguser3 * frascore + scoreUser3 + scoresvetUser3 * kofUser3

print(user1 + ' набрал(a) ' + str(Fuser1) + ' оч.' )
print(user2 + ' набрал(a) ' + str(Fuser2) + ' оч.' )
print(user3 + ' набрал(a) ' + str(Fuser3) + ' оч.' )

allScore = Fuser1 + Fuser2 + Fuser3
onePersent = allScore/100


persU1 = round(Fuser1/onePersent, 0)
persU2 = round(Fuser2/onePersent, 0)
persU3 = round(Fuser3/onePersent, 0)

# print(persU1)
# print(persU2)
# print(persU3)

x = np.array([persU1,persU2,persU3])

labels = [user1, user2, user3]
colors = ["red", "green", "orange"]

plt.pie(x, labels=labels, colors=colors)
plt.show()

for i in collection.find():
    print(i)