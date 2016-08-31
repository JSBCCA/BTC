MENU_PATH = 'menu.txt'
TRANSACTIONS_PATH = 'transactions.txt'


def ask(message):
    print(message)
    return input()


def load_menu():
    """ () -> Menu

    Loads the menu data stored at 'MENU_PATH' and returns
    the constructed menu.

    The Menu is a list of MenuItem.
    Each MenuItem should be a dictionary with a name and price.

    Example Menu:
    [ {'name': 'coke', 'price': .93},
      {'name': 'chips', 'price': 1.50} ]
    """
    listof = []
    with open('menu.txt', 'r') as file:
        for line in file:
            contlist = line.strip().split(',')
            dictionary = {'name': contlist[0], 'price': float(contlist[1])}
            listof.append(dictionary)
        return listof


lm = load_menu()


def print_menu(lm):
    """ Menu -> NoneType

    Print a description of the menu for the user.

    Example Output:
    Menu:
    coke    @ $0.93
    chips   @ $1.50
    """
    print('Menu:')
    for i in lm:
        y = str(i['name'] + ' ')
        z = str(i['price'])
        print(y + '@ $' + z)


def get_order(lm):
    """ Menu -> Order

    Returns the order from the user.
    An Order is a list of 2-element tuples.
    The first element is a MenuItem.
    The second element is how many of that item were purchased.

    Example Order:
    [ ({'name': 'coke', 'price': .93}, 3),
      ({'name': 'chips', 'price': 1.50}, 1)]
    """
    newlist = []
    for i in lm:
        count = ask("How many of the " + i['name'] + " do you want?")
        if int(count) > 0:
            newlist.append((i, int(count)))
    return newlist


def order_str(order):
    """ Order -> str

    Returns a string representation of an order according to the following
    format: Name1, Price1, Count1; Name2, Price2, Count2; Name3, Price3,
    Count3; ...

    >>> order = [({'name': 'coke', 'price': .93}, 3), ({'name': 'chips',
    'price': 1.50}, 1)]

    >>> order_str(order)
    'coke, .93, 3; chips, 1.50, 1''
    """
    result = ''
    for i in order:
        n = str(i[0]['name'])
        p = str(i[0]['price'])
        q = str(i[1])
        result += str(n + ',' + ' ' + p + ',' + q + ';' + ' ')
    return result[:-2]


def log_order(order):
    """ Order -> NoneType

    Writes the order information to the transaction log at 'TRANSACTIONS_PATH'
    Each line in the transaction log should be an order.
    The format for each line is:
    Name1, Price1, Count1; Name2, Price2, Count2; Name3, Price3, Count3; ...

    Example Output:
    coke, .93, 3; chips, 1.50, 1
    """
    with open(TRANSACTIONS_PATH, 'a') as file:
        file.write(order_str(order) + '\n')


def main():
    menu = load_menu()
    order = get_order(menu)
    log_order(order)


if __name__ == '__main__':
    main()
