import argparse
from functools import partial

from .executable import Executable


class Arguments:
    parse = argparse
    parser = argparse.ArgumentParser(
        description='Crawler')

    UPDATE_KEY = {
        'IMAGES_STORE': 'output'
    }

    @classmethod
    def add_argument(cls, *args, **kwargs):
        cls.parser.add_argument(*args, **kwargs)

    @staticmethod
    def update_argument(arguments, keyset):
        target, key = keyset
        setattr(arguments, target, getattr(arguments, key))

    def __new__(cls):
        # auto executable command
        executables = tuple(Executable.s)
        if len(executables) and Executable.ismain():
            cls.parser.add_argument("command", metavar="<command>",
                                    choices=executables,
                                    help=f'Choice from {", ".join(executables)}')

        for executor in executables:
            Executable.s[executor].arguments(cls.parser)

        cls.parser.add_argument('-o', '--output', required=False, default='output.json', type=str,
                                help="Path to output")
        cls.parser.add_argument('--config', required=False, default=None, type=str,
                                help="Path to config file")

        arguments = cls.parser.parse_args()

        # custom arguments
        for key, value in Executable.s[arguments.command].setting.items():
            setattr(arguments, key, value)

        any(map(partial(cls.update_argument, arguments), cls.UPDATE_KEY.items()))

        return arguments
