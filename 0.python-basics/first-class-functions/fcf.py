# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError('Divisor cannot be 0.')
#     return dividend / divisor


# def calculate(*values, operator):
#     return operator(*values)


# result = calculate(20, 4, operator=divide)
# print(result)

def search(sequence, expected, finder):
    for el in sequence:
        if finder(el) == expected:
            return el
    raise RuntimeError(f'Could not find element with {expected}.')


friends = [
    {'name': 'Rolf Smith', 'age': 24}
]


def get_friend_name(friend):
    return friend['name']


print(search(friends, 'Rolf Smith', get_friend_name))
