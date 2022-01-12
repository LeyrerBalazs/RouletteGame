import json, front, random

def betkit(money:int) -> int:
    bet = int(input("Add meg a téted: "))
    return bet

def select():
    front.write_rulett_map()
    return input("Add meg a mezőt: ").lower()

def isvalid(selected:str) -> bool:
    iftrue = False
    for i in range(36):
        if selected == "fekete" or selected == "piros" or selected == "1-18" or selected == "19-36" or selected == "paros" or selected == "páros" or selected == "páratlan" or selected == "paratlan" or selected == "1-12" or selected == "13-24" or selected == "35-36" or selected == "oszlop1" or selected == "oszlop2" or selected == "oszlop3" or selected == str(i):
            iftrue = True
            break  
    return iftrue

def read_rulettmap():
    with open("rulett.json", encoding="utf-8") as file:
        rulett_map = json.load(file)
    return rulett_map

def win_or_lose(selected:str, bet:int, rulett_map) -> int:
    randomelem = random.randint(0,36)
    winmoney = -bet
    front.spin(randomelem, rulett_map)
    for i in range(0,36):
        if selected == str(i) and selected == str(randomelem):
            winmoney += bet * 36
            print("\u001b[32mNyertél!\u001b[0m")
            break
        elif selected == "1-12":
            for j in range(1, 12):
                if j == randomelem:
                    winmoney += bet * 3
                    print("\u001b[32mNyertél!\u001b[0m")
                    break
        elif selected == "13-24":
            for j in range(13, 24):
                if j == randomelem:
                    winmoney += bet * 3
                    print("\u001b[32mNyertél!\u001b[0m")
                    break
        elif selected == "25-36":
            for j in range(25, 36):
                if j == randomelem:
                    winmoney += bet * 3
                    print("\u001b[32mNyertél!\u001b[0m")
                    break
        elif selected == "oszlop1":
            for j in range(3, 36, 3):
                if j == randomelem:
                    winmoney += bet * 3
                    print("\u001b[32mNyertél!\u001b[0m")
                    break
        elif selected == "oszlop2":
            for j in range(2, 35, 3):
                if j == randomelem:
                    winmoney += bet * 3
                    print("\u001b[32mNyertél!\u001b[0m")
                    break
        elif selected == "oszlop3":
            for j in range(1, 34, 3):
                if j == randomelem:
                    winmoney += bet * 3
                    print("\u001b[32mNyertél!\u001b[0m")
                    break
        elif selected == "1-18":
            for j in range(1, 18):
                if j == randomelem:
                    winmoney += bet * 2
                    print("\u001b[32mNyertél!\u001b[0m")
                    break
        elif selected == "19-36":
            for j in range(19, 36):
                if j == randomelem:
                    winmoney += bet * 2
                    print("\u001b[32mNyertél!\u001b[0m")
                    break
        elif selected == "paros" and randomelem % 2 == 0 or selected == "páros" and randomelem % 2 == 0:
            winmoney += bet * 2
            print("\u001b[32mNyertél!\u001b[0m")
            break
        elif selected == "paratlan" and randomelem % 2 != 0 or selected == "páratlan" and randomelem % 2 != 0:
            winmoney += bet * 2
            print("\u001b[32mNyertél!\u001b[0m")
            break
        elif selected == "fekete" and selected == rulett_map[randomelem]:
            winmoney += bet * 2
            print("\u001b[32mNyertél!\u001b[0m")
            break
        elif selected == "piros" and selected == rulett_map[randomelem]:
            winmoney += bet * 2
            print("\u001b[32mNyertél!\u001b[0m")
            break
    if winmoney < 0:
        print("\u001b[31mVesztettél!\u001b[0m")
    return winmoney
