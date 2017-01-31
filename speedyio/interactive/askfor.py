import inquirer
from speedyio import terminal
from speedyio.errors import SpeedyIOInputError


def askfor(message, empty_allowed=True, default=None):
    message = terminal.bold(message)
    if default:
         message += "({})".format(default)

    questions = [
        inquirer.Text('value', message=message)
    ]

    while True:
        answers = inquirer.prompt(questions)
        if answers is None:
            raise SpeedyIOInputError("No input given!")

        x = answers['value']
        if empty_allowed is True:
            return answers.get('value')

        if default and not x: x = default

        if x: return x
