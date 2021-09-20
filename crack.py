import os
import hashlib
import shutil
from sys import argv, exit

from crack_commands import *


argv_flags = list(flags.keys()) + [
    '-o',
    'exec',
]


def get_argv_commands():
    result = []
    flag = None
    for index in range(1, len(argv)):
        argument = argv[index]
        if argument.startswith('-'):
            if flag is not None:
                result.append((flag, ''))
            if index == len(argv):
                result.append(('exec', argument))
            else:
                flag = argument

        else:
            if flag is not None:
                result.append((flag, argument))
                flag = None
            else:
                result.append(('exec', argument))

    return result


def check_argv():
    if len(argv) == 1:
        raise ArgvError()

    commands = get_argv_commands()
    commands = [x for x in commands if x[0] in argv_flags]
    print(commands)
    solve_flag, input_path, output_path = None, None, None
    for command in commands:
        flag, value = command

        if flag == '-o':
            directory, file = os.path.split(value)
            if os.path.isdir(directory) or len(directory) == 0:
                if os.path.exists(value):
                    raise InvalidPathError(f"Output file already exists and can be rewrite")
            else:
                raise InvalidPathError(f"Invalid directory {directory}")
            output_path = value

        if flag == 'exec' or flag in flags:
            input_path = value
            if not os.path.exists(input_path):
                raise InvalidPathError(value)

        if flag in flags:
            solve_flag = flag

    if output_path is None:
        output_path = input_path
    else:
        shutil.copyfile(input_path, output_path)
    print(output_path)
    return solve_flag, output_path


def get_sha1sum(path):
    result = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            result.update(data)
    return result.hexdigest()


def get_solve_module(flag, path):
    if solve_flag is None:
        sha1 = get_sha1sum(path)
        result = sha1sum.get(sha1)
        if result is None:
            raise InvalidSha1Error(sha1)
        else:
            return result
    return flags[flag]


try:
    solve_flag, file_path = check_argv()
    solve_module = get_solve_module(solve_flag, file_path)
    solve_module.crack(file_path)
    print(f'{file_path} has been successfully cracked!!!')
    exit(0)
except ArgvError as e:
    print(e)
    print(f'Use script like: {argv[0]} \'path to file\'')
    exit(1)

except InvalidPathError as e:
    print(e)
    print(f'Use script like: {argv[0]} \'path to file\'')
    exit(1)

except InvalidSha1Error as e:
    print(f'Use explicit file flag: {argv[0]} -cp/tp/game \'path to file\'')
    exit(1)
