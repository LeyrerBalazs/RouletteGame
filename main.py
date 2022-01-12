import front, back

def main():
    money = 100000
    rulett_map = back.read_rulettmap()
    while True:
        print("Egyenleg: " + str(money) + " Ft")
        bet = back.betkit(money)
        while bet > money:
            print("Túl nagy tétet adtál meg! Ennyi pénzed nincs!")
            print("Egyenleg: " + str(money) + " Ft")
            bet = back.betkit(money)
        selected = back.select()
        while not back.isvalid(selected):
            selected = back.select()
        money += back.win_or_lose(selected, bet, rulett_map)
    pass

if __name__ == "__main__":
    main()
