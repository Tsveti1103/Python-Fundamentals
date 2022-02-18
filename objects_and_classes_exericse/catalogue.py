class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [s for s in Catalogue.products if s.startswith(first_letter)]  # startswith - започва с(това)

    def __repr__(self):
        returned_string = f"Items in the {self.name} catalogue:\n"
        returned_string += '\n'.join(sorted(Catalogue.products))
        return returned_string


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
