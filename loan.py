# loan.py
from common import get_money, set_money

def loan_system(user):
    lender = ["김산", "이승준"]
    print(f"빌려주는 사람: {lender}")

    loan = int(input("빌릴 간식 수: "))
    print("3일 안에 갚으세요.")

    set_money(user, get_money(user) + loan)