from acme import Product as prod
import random
#
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num=30):
    """
    Randomly generates a number of Product objects
    :param num: Number of products to generate
    :return: List of randomly generated products
    """
    prods = []

    for i in range(0, num):
        name = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0, 2.5)
        x = prod(name, price, weight, flammability)
        prods.append(x)

    return prods


def inventory_report(products_list):
    """
    Prints out a report for a list of Products
    :param products_list: list of products to report on
    :return: null
    """
    names = []
    mean_price = 0
    mean_weight = 0
    mean_flam = 0

    for x in products_list:
        print('Product #' + str(products_list.index(x) + 1) + ", codename: " + x.name + ".")
        print('Price: ', x.price)
        print('Weight: ', x.weight)
        print('Flammability: ', x.flammability)
        print('')
        if x.name in names:
            pass
        else:
            names.append(x.name)
        mean_price += x.price
        mean_weight += x.weight
        mean_flam += x.flammability

    mean_price = mean_price/len(products_list)
    mean_weight = mean_weight/len(products_list)
    mean_flam = mean_flam/len(products_list)

    print('ACME CORP OFFICIAL INVENTORY REPORT')
    print("Number of unique product names: ", len(names))
    print("Mean price of list of products: ", mean_price)
    print("Mean weight of list of products: ", mean_weight)
    print("Mean flammability of list of products: ", mean_flam)

    return 0


if __name__ == '__main__':
    inventory_report(generate_products())



