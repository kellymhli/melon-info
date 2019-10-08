"""Print out all the melons in our inventory."""


from melons import melon_info_dict


def print_melon(name, seedless, price, flesh_color, rind_color, avg_weight):
    """Print each melon with corresponding attribute information."""

    print(f"""{name.upper()}"""
          f"""\n\tseedless: {seedless}"""
          f"""\n\tprice: {price:.2f}"""
          f"""\n\tflesh_color: {flesh_color}"""
          f"""\n\tweight: {avg_weight}"""
          f"""\n\trind_color: {rind_color}"""
         )


def add_info(melon_info_dict):
    """Add melon information to melon_info_dictionary."""

    # Prompt user for info to add to melon dictionary.
    melon = input("What melon would you like to add info to? ").title()
    info = input(f"What kind of info would you like to add to {melon}? ").lower()
    value = input(f"What is the value for {info}? ")

    # Add melon info to dictionary.
    melon_info_dict[melon][info] = value


def main():

    # Promp user if they want to add new info to the melon dictionary.
    while input("Would you like to add new melon info? (Y/N) ").upper() != 'N':
        add_info(melon_info_dict)

    # Print out each melon and its formation.
    for melon, info in melon_info_dict.items():
        print(melon.upper())
        for key, value in info.items():
            print(f'\t{key}: {value}')


main()