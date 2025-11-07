# coin.py
import random
from common import get_money, set_money

def coin_game(user):
    bet = int(input("베팅 수량: "))
    choice = input("앞/뒤 선택: ")

    if random.choice(["앞","뒤"]) == choice:
        print("승리!")
        set_money(user, get_money(user) + bet)
    else:
        print("패배!")
        set_money(user, get_money(user) - bet)