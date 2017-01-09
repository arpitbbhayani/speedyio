from speedyio.errors import SpeedyIOTypeError
from speedyio.entities import SelectableItem


def choose_one_basic(l):
    if type(l) != list:
        raise SpeedyIOTypeError("Should be of type list")

    if len(l) > 0 and type(l[0]) != SelectableItem:
        raise SpeedyIOTypeError("Should be of type SelectableItem")

    if len(l) == 0:
        raise SpeedyIOTypeError("Should not be of length 0")

    while True:
        for i in range(len(l)):
            print("{}. {}".format(i, l[i].label))

        index = int(input("Select one - "))

        if index < 0 or index >= len(l):
            print("Invalid selection. Please choose a correct option.")
        else:
            return l[index].item
