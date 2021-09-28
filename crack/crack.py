import os
from stat import S_IEXEC
import shutil
import argparse

from cmds import *


class ArgsChecker:
    solver_flag = None

    def __init__(self, args: argparse.Namespace):
        self._args = args
        self._path = args.path
        self.destination = args.destination

    def _check_path(self):
        if not os.path.exists(self._path):
            raise InvalidPathError(f'Source file: {self._path} not exist')

    def _check_solver_flag(self):
        solve_flag = [f_flag for f_flag, val in vars(args).items() if '-' + f_flag in flags and val]
        if len(solve_flag) > 1:
            raise ArgvError('Explicit file flag should be one or none')

        if len(solve_flag) == 1:
            self.solver_flag = '-' + solve_flag[0]

    @staticmethod
    def _mkdir(directory):
        try:
            os.mkdir(directory)
        except OSError:
            print(f'Failed create directory')
            raise InvalidPathError(f'No directory: \'{directory}\'')
        print(f'Success create directory')

    def _create_dir_question(self, directory):
        while True:
            answer = input('').lower().lstrip().rstrip()
            if answer[0] == 'y':
                self._mkdir(directory)
                break
            elif answer[0] == 'n':
                raise InvalidPathError(f'No directory: \'{directory}\'')
            else:
                print('Invalid operation: try again...')

    def _check_dir(self, directory):
        if not (os.path.isdir(directory) or len(directory) == 0):
            print(f'Output directory not exist: \'{directory}\'')
            print(f'Do you want to create it?  Y\\n')
            self._create_dir_question(directory)

    def _check_destination(self):
        if self.destination is None:
            self.destination = self._path
            return

        if os.path.exists(self.destination):
            raise InvalidPathError(f"Output file should not already exist")

        directory, _ = os.path.split(self.destination)
        self._check_dir(directory)

    def _run_copy(self):
        if self.destination != self._path:
            shutil.copyfile(self._path, self.destination)

    def run(self):
        self._check_path()
        self._check_destination()
        self._check_solver_flag()
        self._run_copy()


# region Init parser
parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, help='Path to the source file')
parser.add_argument('-d', '--destination', type=str, default=None, help='')  # TODO
files_group = parser.add_argument_group(title='files', description='Explicit file flag')
for flag in flags.keys():
    files_group.add_argument(flag, action='store_true')
# endregion

try:
    args = parser.parse_args()
    args_checker = ArgsChecker(args)
    args_checker.run()
    file_path, solver_flag = args_checker.destination, args_checker.solver_flag
    solver = get_solver(solver_flag, file_path)
    solver.crack(file_path)
    os.chmod(file_path, S_IEXEC)
    parser.exit(0, f'File {file_path} has been successfully cracked!!!\n')
except (ArgvError, InvalidPathError, InvalidSha1Error) as e:
    parser.error(f'{e.args[0]}')

parser.exit(-1)
