data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(ns):
    right = []
    for i in ns:
        if isinstance(i, int):
            right.append(i)

        elif isinstance(i, str):
            right.append(len(i))
        elif isinstance(i, dict):
            if len(i) > 0:
                right.append(calculate_structure_sum(list(i.keys())))
                right.append(calculate_structure_sum(list(i.values())))
        else:
            if len(i) > 0:
                right.append(calculate_structure_sum(i))
    else:
        return sum(right)
result = calculate_structure_sum(data_structure)
print(result)