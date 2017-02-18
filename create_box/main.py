"""This is the entry point of the program."""

def create_box(height, width, character):
    for i in range(height):
        box = width*character + '\n'
        box *= height
    return box

if __name__ == '__main__':
    my_box = create_box(3, 4, '*')
    print(my_box)
