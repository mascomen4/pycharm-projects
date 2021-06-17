# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins = 0
    coins += money // 10
    money -= coins*10
    coins += money // 5
    money -= (money // 5)*5
    coins += money
    return coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
