from speedyio.errors import SpeedyIOInputError


def yesno(message, default=False):
    try:
        x = input(message + "(yes/no): ")
    except KeyboardInterrupt:
        raise SpeedyIOInputError("No input given!")

    if x.lower() in ['yes', 'y']:
        return True

    if x.lower() in ['no', 'n']:
        return False

    return default
