#alle formules van de verschillende zombies
formula_beginnings = [1, 2, 4, 8, 16, 32, 767, 82678, 92767]

#een functie om de prijs te bepalen van een zombie
def calculate_price(zombie_num, zombies_bought):
    formula_beginning = formula_beginnings[zombie_num - 1]
    cost = formula_beginning * 10 ** (0,14 * (zombies_bought + 1))
    return cost

#een functie de die goedkoopste optie geeft
def give_lowest_price(price1, price2):
    if price1 > price2:
        return price1
    else:qw
        return price2

#een functie die kijkt of je beter een zombie kunt kopen of 2x degene er onder
def calculate_cheaper_option(what_zombie, zombies_bought_info):
    if len(zombies_bought_info) != 12:
        return "Error"

    info_zombies_bought = zombies_bought_info

    if what_zombie == 1:
        return calculate_price(what_zombie, info_zombies_bought[what_zombie - 1])

    price1 = calculate_price(what_zombie, info_zombies_bought[what_zombie - 1])
    price2_begin = calculate_price(what_zombie-1, info_zombies_bought[what_zombie - 2])
    price2_end = calculate_price(what_zombie-1, info_zombies_bought[what_zombie - 2]-1)
    price2 = price2_begin + price2_end

    return give_lowest_price(price1, price2)


print(calculate_cheaper_option(1, [4, 5, 3, 2, 5, 4, 3, 5, 67, 43, 23, 4]))








