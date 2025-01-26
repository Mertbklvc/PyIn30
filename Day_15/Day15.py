# from turtle import Turtle, Screen

# memo= Turtle()
# memo.shape("turtle")
# memo.color("pink")
# memo.forward(250)
# memo.left(30)
# memo.forward(150)
# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type", "Base Stats", "Abilities"]

table.add_row(["Pikachu", "Electric", 320, "Static, Lightning Rod"])
table.add_row(["Charizard", "Fire/Flying", 534, "Blaze, Solar Power"])
table.add_row(["Bulbasaur", "Grass/Poison", 318, "Overgrow, Chlorophyll"])
table.add_row(["Squirtle", "Water", 314, "Torrent, Rain Dish"])
table.add_row(["Gengar", "Ghost/Poison", 500, "Cursed Body"])
table.add_row(["Snorlax", "Normal", 540, "Immunity, Thick Fat"])
table.add_row(["Dragonite", "Dragon/Flying", 600, "Inner Focus, Multiscale"])


print(table)
print(table[1])

