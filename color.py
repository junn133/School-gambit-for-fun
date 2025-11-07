# color.py
import random
from common import get_money, set_money

def color_game(user):
    bet = int(input("베팅 수량: "))
    choice = input("빨/파/초 선택: ")

    if random.choice(["빨","파","초"]) == choice:
        print("정답!")
        set_money(user, get_money(user) + bet)
    else:
        print("틀림!")
        set_money(user, get_money(user) - bet)