def calculate_charges(rate1, rate2, consumptions):
    bills = []
    for consumption in consumptions:
        if consumption <= 1000:
            bill = consumption * rate1
        else:
            bill = 1000 * rate1 + (consumption - 1000) * rate2
        bills.append((consumption, bill))
    return bills


if __name__ == '__main__':
    rate1, rate2 = map(int, input().split())
    n = int(input())
    consumptions = [int(input()) for _ in range(n)]
    bills = calculate_charges(rate1, rate2, consumptions)
    for consumption, bill in bills:
        print(f'{consumption} {bill}')
