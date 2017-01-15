import inquirer
from speedyio import terminal


def askfor(message, empty_allowed=True, default=None):
    message = terminal.bold(message)
    if default:
         message += "({})".format(default)

    questions = [
        inquirer.Text('value', message=message)
    ]

    while True:
        answers = inquirer.prompt(questions)
        x = answers['value']
        if empty_allowed is True:
            return answers.get('value')

        if default and not x: x = default

        if x: return x
