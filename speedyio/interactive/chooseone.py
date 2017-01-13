import inquirer

from speedyio.errors import SpeedyIOTypeError
from speedyio.entities import Item


def chooseone(options, message="Select one"):
    if type(options) != list:
        raise SpeedyIOTypeError("Options to choose from should be a list")

    if len(options) == 0:
        raise SpeedyIOTypeError("Options cannot be empty")

    if len(options) > 0 and type(options[0]) != Item:
        raise SpeedyIOTypeError("Every item of options should be a SelectableItem")

    questions = [
        inquirer.List('value',
              message=message,
              choices=[(c.label, c.item) for c in options],
        )
    ]

    answers = inquirer.prompt(questions)
    return answers['value']
