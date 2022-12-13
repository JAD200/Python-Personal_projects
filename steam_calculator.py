games = list(map(float, input("Enter the price of the games: ").split()))
games_with_taxes = []

for game in games:
    tax = game * 0.75
    tax_price = game + tax
    games_with_taxes.append(tax_price)
    print(f'Game {game:0.2f}\tTax price {tax_price:0.2f}')

games_total = sum(games)
final_price = sum(games_with_taxes)

print (f'Total {games_total:0.2f}\tTotal with taxes: {final_price:0.2f}')
