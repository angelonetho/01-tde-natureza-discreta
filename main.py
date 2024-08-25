# Angelo Andrioli Netho

file = open("input2.txt", "r")
content = file.readlines()
file.close()

number_of_operations = int(content[0])

for i in range(len(content)):
    content[i] = content[i].replace('\n', '')


def parse_string_to_list(string: str):
    return string.replace(' ', '').split(',')


def union(list_A: str, list_B: str):
    return list_A + ', ' + list_B


def intersection(list_A, list_B):

    list_A = parse_string_to_list(list_A)
    list_B = parse_string_to_list(list_B)

    result = []
    for item_A in list_A:
        for item_B in list_B:
            if item_A == item_B:
                result.append(item_A)
    return result


def difference(list_A, list_B):

    list_A = parse_string_to_list(list_A)
    list_B = parse_string_to_list(list_B)

    for item_B in list_B:
        if (list_A.count(item_B) > 0):
            list_A.remove(item_B)

    return list_A


def cartesian_product(list_A, list_B):

    list_A = parse_string_to_list(list_A)
    list_B = parse_string_to_list(list_B)

    result = []

    for item_A in list_A:
        for item_B in list_B:
            value = f"({item_A},{item_B})"
            result.append(value)

    return result


for i in range(0, number_of_operations * 3, 3):
    operation = content[i + 1]

    if content[i + 1] == 'U':
        list_A = content[i + 2]
        list_B = content[i + 3]

        value = union(list_A, list_B)
        print(
            f'União: conjunto 1 {{{list_A}}}, conjunto 2 {{{list_B}}}. Resultado: {{{value}}}\n'
        )

    elif content[i + 1] == 'I':
        list_A = (content[i + 2])
        list_B = (content[i + 3])

        value = ", ".join(intersection(list_A, list_B))
        print(
            f'Intersecção: conjunto 1 {{{list_A}}}, conjunto 2 {{{list_B}}}. Resultado: {{{value}}}\n'
        )

    elif content[i + 1] == 'D':
        list_A = content[i + 2]
        list_B = content[i + 3]

        value = ", ".join(difference(list_A, list_B))
        print(
            f'Diferença: conjunto 1 {{{list_A}}}, conjunto 2 {{{list_B}}}. Resultado: {{{value}}}\n'
        )
    elif content[i + 1] == 'C':
        list_A = content[i + 2]
        list_B = content[i + 3]

        value = ", ".join(cartesian_product(list_A, list_B))
        print(
            f'Produto cartesiano: conjunto 1 {{{list_A}}}, conjunto 2 {{{list_B}}}. Resultado: {{{value}}}\n'
        )
