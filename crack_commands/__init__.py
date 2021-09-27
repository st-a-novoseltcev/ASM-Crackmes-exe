import hashlib

import crack_commands.cp
import crack_commands.tp
import crack_commands.game
from crack_commands.exceptions import *


sha1sum = {
    cp.sha1sum:     cp,
    tp.sha1sum:     tp,
    game.sha1sum: game,
}

flags = {
    '-cp':     cp,
    '-tp':     tp,
    '-game': game,
}


def get_sha1sum(path):
    result = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            result.update(data)
    return result.hexdigest()


def get_solver(flag, path):
    if flag is not None:
        return flags[flag]

    sha1 = get_sha1sum(path)
    result = sha1sum.get(sha1)
    if result is None:
        raise InvalidSha1Error(f'Unknown file sha1:{sha1}, use explicit file flag!')
    return result





