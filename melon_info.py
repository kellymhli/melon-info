"""Print out all the melons in our inventory."""


from melons import melon_info_dict


def print_melon(name, seedless, price, flesh_color, rind_color, avg_weight):
    """Print each melon with corresponding attribute information."""

    print(f"""{name.upper()}"""
          f"""\n\tseedless: {seedless}"""
          f"""\n\tprice: {price}"""
          f"""\n\tflesh_color: {flesh_color}"""
          f"""\n\tweight: {avg_weight}"""
          f"""\n\trind_color: {rind_color}"""
         )


def add_info(melon_info_dict):

    melon = input("What melon would you like to add info to? ").title()
    info = input(f"What kind of info would you like to add to {melon}? ")
    value = input(f"What is the value for {info}? ")

    melon_info_dict[melon][info] = value
    return (melon_info_dict)


def main():

    for melon, info in melon_info_dict.items():
        price = info['price']
        seedless = info['seedless']
        flesh_color = info['flesh_color']
        rind_color = info['rind_color']
        avg_weight = info['avg_weight']
        print_melon(melon, seedless, price, flesh_color, rind_color, avg_weight)

    while input("Would you like to add new melon info? (Y/N) ") != 'N':
        add_info(melon_info_dict)




main()