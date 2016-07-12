MENU_PATH = 'menu.txt'
TRANSACTIONS_PATH = 'transactions.txt'

def load_menu():
    """ () -> Menu

    Loads the menu data stored at `MENU_PATH` and returns
    the constructed menu.

    The Menu is a list of MenuItem.
    Each MenuItem should be a dictionary with a name and price.

    Example Menu:
    [ {'name': 'coke', 'price': .93},
      {'name': 'chips', 'price': 1.50} ]
    """
    # YOUR CODE HERE

def get_order(menu):
    """ Menu -> Order

    Returns the order from the user.
    An Order is a list of 2-element tuples.
    The first element is a MenuItem.
    The second element is how many of that item were purchased.

    Example Order:
    [ ({'name': 'coke', 'price': .93}, 3),
      ({'name': 'chips', 'price': 1.50}, 1)]
    """
    # YOUR CODE HERE

def log_order(order):
    """ Order -> NoneType

    Writes the order information to the transaction log at `TRANSACTIONS_PATH`
    Each line in the transaction log should an order.
    The format for each line is:
    Name1, Price1, Count1; Name2, Price2, Count2; Name3, Price3, Count3; ...; NameN, PriceN, CountN

    Example Output:
    coke, .93, 3; chips, 1.50, 1
    """
    # YOUR CODE HERE