# main.py
from common import get_money
from coin import coin_game
from color import color_game
from loan import loan_system

user = input("이름 입력: ")

while True:
    money = get_money(user)

    print(f"\n보유 간식: {money}")
    if money < 0:
        print("🚨 대출하세요 🚨")

    print("\n=== MENU ===")
    print("1. 동전 던지기")
    print("2. 색깔 맞추기")
    print("3. 대출")
    print("0. 종료")

    sel = input("선택: ")

    if sel == "1":
        coin_game(user)
    elif sel == "2":
        color_game(user)
    elif sel == "3":
        loan_system(user)
    elif sel == "0":
        break