from speedyio.errors import SpeedyIOTypeError
from speedyio.entities import Item


def chooseone(options, message="Select one"):
    if type(options) != list:
        raise SpeedyIOTypeError("Options to choose from should be a list")

    if len(options) == 0:
        raise SpeedyIOTypeError("Options cannot be empty")

    if len(options) > 0 and type(options[0]) != Item:
        raise SpeedyIOTypeError("Every item of options should be a SelectableItem")

    print("")
    for i in range(len(options)):
        print(" {}. {}".format(i+1, options[i].label))
    print("")

    while True:
        index = input(message + ": ")

        try:
            index = int(index)
        except:
            print("Invalid selection. Please choose a correct option.")
            continue

        if index <= 0 or index > len(options):
            print("Invalid selection. Please choose a correct option.")
            continue

        return options[index-1].item
