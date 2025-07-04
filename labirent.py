import random
import copy

labirent = [
    ["X", "X", "X", "X", "X", "X"],
    ["X", "O", ".", ".", "X", "X"],
    ["X", "X", ".", "X", ".", "X"],
    ["X", "X", ".", "X", ".", "X"],
    ["X", "X", ".", ".", "Ç", "X"],
    ["X", "X", "X", "X", "X", "X"],
]

easyLabirents = [

    # 1. Çok basit düz yol
    [
        ["X", "X", "X", "X", "X"],
        ["X", "O", ".", ".", "Ç"],
        ["X", "X", "X", "X", "X"]
    ],

    # 2. Sağdan kolay çıkış yolu
    [
        ["X", "X", "X", "X", "X"],
        ["X", "O", ".", ".", "Ç"],
        ["X", "X", "X", "X", "X"]
    ],

    # 3. Kısa L şekli
    [
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
        ["X", ".", ".", "Ç"],
        ["X", "X", "X", "X"]
    ],

    # 4. Düz ve küçük bir engel
    [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", ".", "X", "X"],
        ["X", "X", "X", ".", "Ç", "X"],
        ["X", "X", "X", "X", "X", "X"]
    ],

    # 5. Çift küçük köşe
    [
        ["X", "X", "X", "X", "X"],
        ["X", "O", ".", "X", "X"],
        ["X", ".", ".", ".", "Ç"],
        ["X", "X", "X", "X", "X"]
    ]

]

mediumLabirents = [

    # 1. Daha fazla engel ve birkaç dönüş
    [
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", "X", ".", ".", "X"],
        ["X", ".", ".", "X", ".", "X", "X"],
        ["X", "X", ".", ".", ".", ".", "X"],
        ["X", "X", "X", "X", "X", "Ç", "X"],
        ["X", "X", "X", "X", "X", "X", "X"]
    ],

    # 2. Uzun ve dar koridorlar, birkaç engel
    [
        ["X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", ".", "X", ".", ".", "X"],
        ["X", "X", "X", ".", "X", ".", "X", "X"],
        ["X", ".", ".", ".", ".", ".", ".", "X"],
        ["X", ".", "X", "X", "X", "X", ".", "X"],
        ["X", ".", ".", ".", ".", "Ç", ".", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X"]
    ],

    # 3. Dönüşlerin fazla olduğu bir labirent
    [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", "X", ".", "X"],
        ["X", ".", ".", "X", ".", "X"],
        ["X", ".", "X", ".", ".", "X"],
        ["X", ".", ".", ".", "Ç", "X"],
        ["X", "X", "X", "X", "X", "X"]
    ],

    # 4. Engel dolu orta koridor
    [
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", ".", ".", ".", "X"],
        ["X", "X", "X", ".", "X", "X", "X"],
        ["X", ".", ".", ".", ".", ".", "X"],
        ["X", ".", "X", "X", "X", ".", "X"],
        ["X", ".", ".", ".", "Ç", ".", "X"],
        ["X", "X", "X", "X", "X", "X", "X"]
    ],

    # 5. Dairesel bir rota içeren labirent
    [
        ["X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", ".", "X", ".", "Ç", "X"],
        ["X", ".", "X", ".", "X", ".", "X", "X"],
        ["X", ".", "X", ".", ".", ".", "X", "X"],
        ["X", ".", ".", "X", "X", ".", "X", "X"],
        ["X", "X", ".", ".", ".", ".", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X"]
    ]

]

hardLabirents = [

    # 1. Karmaşık koridorlar ve çok sayıda engel
    [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", "X", ".", ".", ".", "X", "X"],
        ["X", ".", ".", "X", ".", "X", ".", ".", "X"],
        ["X", "X", ".", ".", ".", "X", ".", "X", "X"],
        ["X", ".", "X", "X", ".", ".", ".", "X", "X"],
        ["X", ".", ".", ".", ".", "X", ".", ".", "X"],
        ["X", "X", "X", "X", ".", "X", "X", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", "Ç", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
    ],

    # 2. Çoklu çıkmaz sokak ve uzun koridorlar
    [
        ["X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", "X", ".", ".", ".", "X"],
        ["X", ".", ".", "X", ".", "X", ".", "X"],
        ["X", "X", ".", ".", ".", "X", ".", "X"],
        ["X", ".", "X", "X", ".", ".", ".", "X"],
        ["X", ".", ".", ".", "X", "X", ".", "X"],
        ["X", ".", "X", ".", ".", ".", "Ç", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X"]
    ],

    # 3. Dar koridorlar ve labirentin merkezinde çıkış
    [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", ".", "X", ".", ".", ".", ".", "X"],
        ["X", "X", "X", ".", "X", ".", "X", "X", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", "X", ".", "X"],
        ["X", ".", "X", "X", "X", "X", ".", "X", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", "X", ".", "X"],
        ["X", "X", ".", "X", "X", ".", "X", "X", ".", "X"],
        ["X", ".", ".", "X", ".", ".", ".", ".", ".", "X"],
        ["X", ".", ".", "X", ".", "X", "X", "X", "Ç", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
    ],

    # 4. Çıkmazlar ve geniş alanlar
    [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", ".", ".", "X", ".", ".", "X"],
        ["X", "X", "X", ".", "X", "X", ".", "X", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", ".", "X", "X", "X", "X", "X", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", "X", "X", ".", "X", "X", "X", ".", "X"],
        ["X", ".", ".", ".", ".", ".", "Ç", ".", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
    ],

    # 5. Kompleks ve uzun labirent
    [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "O", ".", ".", "X", ".", ".", ".", ".", ".", "X"],
        ["X", "X", "X", ".", "X", ".", "X", "X", "X", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", "X", ".", "X"],
        ["X", ".", "X", "X", "X", "X", "X", ".", "X", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", "X", ".", "X"],
        ["X", "X", "X", "X", "X", "X", ".", "X", "X", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", "X", ".", ".", "X"],
        ["X", ".", "X", "X", "X", ".", "X", "X", ".", "Ç", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
    ]

]

defaultLabirent = copy.deepcopy(labirent)
defaultLabirents = [
    copy.deepcopy(easyLabirents),
    copy.deepcopy(mediumLabirents),
    copy.deepcopy(hardLabirents)
]


lastPlace=["zooort"]

# labirenti gösterir
def showLabirent():
    for i in labirent:
        print(i)


# oyuncunun o anki konumunu döndürür (a,b)
def findPlayer():
    for x in range(len(labirent)):
        for y in range(len(labirent[0])):
            if labirent[x][y]=="O":
                return x,y
            
    raise Exception("Listede oyuncu bulunamadı!")


# o anki konumda gidebilecegi noktaların yerini gösteren liste döndürür
def whereToGo():
    playerX,playerY=findPlayer()
    validPlaces=[]

    try:

        #solundaysa
        if labirent[playerX][playerY-1] in [".","Ç","*"]:
            validPlaces.append("left")
    
    except Exception:
        pass

    try:

        #yukarısındaysa
        if labirent[playerX-1][playerY] in [".","Ç","*"]:
            validPlaces.append("up")
    
    except Exception:
        pass

    try:

        #sağındaysa
        if labirent[playerX][playerY+1] in [".","Ç","*"]:
            validPlaces.append("right")
    
    except Exception:
        pass

    try:

        #altındaysa
        if labirent[playerX+1][playerY] in [".","Ç","*"]:
            validPlaces.append("down")
    
    except Exception:
        pass

    return validPlaces


# labirenti hareketten sonraki konumu gösterir
def makeMove():

    global lastPlace

    validPlaces= whereToGo()
    # current location cordinates
    x,y=findPlayer()

    while True:

        move=input()

        if (move.lower()=="w" or move.lower()=="a" or move.lower()=="s" or move.lower()=="d"):
            break

    if move.lower()=="w":
        if "up" in validPlaces:
            lastPlace[0]=labirent[x-1][y]

            labirent[x][y]="*"
            labirent[x-1][y]="O"

    elif move.lower()=="a":
        if "left" in validPlaces:
            lastPlace[0]=labirent[x][y-1]

            labirent[x][y]="*"
            labirent[x][y-1]="O"

    elif move.lower()=="s":
        if "down" in validPlaces:
            lastPlace[0]=labirent[x+1][y]

            labirent[x][y]="*"
            labirent[x+1][y]="O"
            
    elif move.lower()=="d":
        if "right" in validPlaces:
            lastPlace[0]=labirent[x][y+1]

            labirent[x][y]="*"
            labirent[x][y+1]="O"

# oyunu başlatır
def playGame():

    stepCount=0

    while not (lastPlace[0]=="Ç"):

        showLabirent()

        makeMove()
        stepCount+=1

    print(f"Tebrikler {stepCount} harekette Kazandınız!")
    resetLabirent()

# labirent zorlugu seçer
def level():
    global labirent
    while True:
        y=input()

        try:
            zorluk=int(y)
            if 0<zorluk<4:
                break
        except Exception:
            pass

    if zorluk==1:
        labirent=easyLabirents[random.randint(0,len(easyLabirents)-1)]
    elif zorluk==2:
        labirent=mediumLabirents[random.randint(0,len(mediumLabirents)-1)]
    else:
        labirent=hardLabirents[random.randint(0,len(hardLabirents)-1)]

# labirentleri resetler
def resetLabirent():
    global labirent
    global easyLabirents, mediumLabirents, hardLabirents

    labirent = copy.deepcopy(defaultLabirent)
    lastPlace[0] = "zoooort"
    easyLabirents = copy.deepcopy(defaultLabirents[0])
    mediumLabirents = copy.deepcopy(defaultLabirents[1])
    hardLabirents = copy.deepcopy(defaultLabirents[2])

# oyun menüsü
def menu():

    while True:

        print("1| Zorluk seç\n2| Oyunu oyna\n3| Çıkış")

        while True:

            x=input()

            try:
                secim=int(x)
                if 0<secim<4:
                    break
            except Exception:
                pass

        if secim==1:
            print("1| Kolay\n2| Orta\n3| Zor")
            level()
        
        elif secim==2:
            playGame()

        elif secim==3:
            print("Görüşmek Üzere!")
            break

        
menu()