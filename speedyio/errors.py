class SpeedyIOError(Exception):
    def __init__(self, error_code, description):
        Exception.__init__(self)
        self.error_code = error_code
        self.description = description

    def jsonify(self):
        return {
            'error_code': self.error_code,
            'description': self.description
        }

    def __str__(self):
        return "({}) {}".format(self.error_code, self.description)


class SpeedyIOTypeError(SpeedyIOError):
    def __init__(self, message):
        SpeedyIOError.__init__(self, 'SPEEDYIO_TYPE_ERROR', message)
