def askfor(t, message, empty_allowed=True):
    while True:
        x = input(message + ": ")
        if empty_allowed is True or x:
            # if empty string is allowed return it.
            # if it is not allowd and some value of x is provided then return
            # else infinite ask again
            return t(x)
