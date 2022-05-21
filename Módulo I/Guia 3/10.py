# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para
# cada tipo de pizza aparecen a continuación.
#
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su
# respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un
# ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar
# por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pizza_option = input("¿Quiere una pizza vegetariana?\n")
veggie_pizza = pizza_option == "si"
if veggie_pizza:
    veggie_ingredient = input("Elija un ingrediente extra: pimiento o tofu.\n")
    print(f"La pizza elegida es vegetariana, los ingredientes son: tomate, mozzarella y {veggie_ingredient}.")
else:
    no_veggie_ingredient = input("Elija un ingredientes extra: Peperoni, Jamón o Salmón.\n")
    print(f"La pizza elegida no es vegetariana, los ingrediente son: tomate, mozzarella y {no_veggie_ingredient}.")
