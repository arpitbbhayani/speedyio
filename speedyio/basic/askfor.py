def askfor(message, empty_allowed=True, default=None):
    while True:
        x = input(message + ": ")
        if empty_allowed is True:
            return x

        if default and not x: x = default
        if x: return x
