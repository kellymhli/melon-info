"""Print out all the melons in our inventory."""


from melons import melon_info


def print_melon(name, seedless, price, flesh_color, rind_color, avg_weight):
    """Print each melon with corresponding attribute information."""

    # have_or_have_not = 'have'
    # if seedless:
    #     have_or_have_not = 'do not have'

    # print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')

    print(f"""{name.upper()}"""
          f"""\n\tseedless: {seedless}"""
          f"""\n\tprice: {price}"""
          f"""\n\tflesh_color: {flesh_color}"""
          f"""\n\tweight: {avg_weight}"""
          f"""\n\trind_color: {rind_color}"""
         )


def main():

    for melon, info in melon_info.items():
        price = info['price']
        seedless = info['seedless']
        flesh_color = info['flesh_color']
        rind_color = info['rind_color']
        avg_weight = info['avg_weight']
        print_melon(melon, seedless, price, flesh_color, rind_color, avg_weight) 


main()