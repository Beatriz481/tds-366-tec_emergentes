import csv

class Drink:
    def __init__(self, country, beer_servings, spirit_servings, wine_servings, total_litres_of_pure):
        self.country = country
        self.beer_servings = beer_servings
        self.spirit_servings = spirit_servings
        self.wine_servings = wine_servings
        self.total_litres_of_pure = total_litres_of_pure 


    def ler_dados(arquivo_csv):
        with open(arquivo_csv, 'r') as f:
            reader = csv.reader(f)
            data = [row for row in reader]
        return data    


    data = ler_dados('drinks.csv')
    print(data)

