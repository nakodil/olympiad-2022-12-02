"""
3 2
1 3 2
2
1 2
2 3
"""
data = input().split()
position = int(data[1]) - 1  # индексы начинаются с 0, а пользователь вводит с 1-го!

all_positions = input().split()
all_positions = list(map(int, all_positions))

turns = int(input())

for i in range(turns):
    change = input().split()
    src = int(change[0]) - 1  # с какой позиции забрали балерину
    dest = int(change[1]) - 1  # в какую позицию переместили балерину
    all_positions[src], all_positions[dest] = all_positions[dest], all_positions[src]  # обмениваем местами

print(all_positions[position])
