userA = {
    "name": "user A",
    "card no": "1111",
    "pwd":"1111",
    "cash": 2000,
}
userB = {
    "name": "user B",
    "card no": "1112",
    "pwd":"1112",
    "cash": 500,
}
accounts ={
    userA['card no']: userA,
    userB['card no']: userB,
}

# print(accounts)
def addCash(card,pwd,cash):
    if(card in accounts):
        if(accounts[card]['pwd'] == pwd):
            accounts[card]['cash'] += cash
            print(f"user: {accounts['1111']['name']}\ncurrent cash: {accounts['1111']['cash']}")
        else:
            print("wrong password")
    else:
        print("wrong card no")

addCash("1111","1111",200)

