string = 'hello'
memory = 'world'
values = [0, 2, 4, 6, 8, 10]
counter = 0

while counter != 10:
    if counter > 7:
        print(string + ' ' + memory)
        print(string)

    memory = string
    if counter < 10:
        counter += 1
        print(memory)