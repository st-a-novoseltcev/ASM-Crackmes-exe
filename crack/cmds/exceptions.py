class InvalidPathError(Exception):
    def __str__(self):
        return f'Invalid path: {self.args[0]}'


class InvalidSha1Error(Exception):
    def __str__(self):
        return f'INot found crack to file with sha1: {self.args[0]}'


class ArgvError(Exception):
    pass
