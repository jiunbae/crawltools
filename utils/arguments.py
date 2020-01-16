import argparse

from .executable import Executable


class Arguments:
    parse = argparse
    parser = argparse.ArgumentParser(
        description='Crawler')

    @classmethod
    def add_argument(cls, *args, **kwargs):
        cls.parser.add_argument(*args, **kwargs)

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

        return cls.parser.parse_args()
