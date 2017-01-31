from speedyio.errors import SpeedyIOInputError


def askfor(message, empty_allowed=True, default=None):
    if default:
         message += "({})".format(default)

    while True:
        try:
            x = input(message + ": ")
        except KeyboardInterrupt:
            raise SpeedyIOInputError("No input given!")

        if empty_allowed is True: return x
        if default and not x: x = default
        if x: return x
