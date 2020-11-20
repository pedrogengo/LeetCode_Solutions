# 1418. Display Table of Food Orders in a Restaurant

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = [order[2] for order in orders]
        foods = sorted(list(set(foods)))
        len_food = len(foods)
        tables = sorted(list(set([order[1] for order in orders])), key=lambda x: int(x))
        display_tables = [[tables[i]] + (["0"] * len_food) for i in range(len(tables))]
        for i in range(len(orders)):
            order = orders[i]
            table = tables.index(order[1])
            food = foods.index(order[2])
            display_tables[table][food+1] = str(int(display_tables[table][food+1]) + 1)
        
        output = [['Table'] + foods] + display_tables
        return output
