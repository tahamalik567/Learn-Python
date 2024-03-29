import prettytable

table = prettytable.PrettyTable(["Name", "Age", "City"])
table.add_row(["Alice", 25, "New York"])
table.add_row(["Bob", 30, "London"])
table.add_row(["Charlie", 35, "Paris"])
print(table)