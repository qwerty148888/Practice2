balance, withdraw = map(int, input().split())
if balance > withdraw:
    print(balance - withdraw)
else:
    print("Insufficient Funds")