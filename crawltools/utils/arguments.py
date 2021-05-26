import argparse
from functools import partial

from .executable import Executable


class Arguments:
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
        parser = argparse.ArgumentParser(description='Crawler')
        executables = tuple(Executable.s)

        if not len(executables):
            raise NotImplementedError('No implemented executables are detected!')

        if Executable.ismain():
            parser.add_argument("command", metavar="<command>",
                                choices=executables,
                                help=f'Choice from {", ".join(executables)}')

        parser.add_argument('-o', '--output', required=False, default='output', type=str,
                            help="Path to output directory")
        parser.add_argument('--config', required=False, default=None, type=str,
                            help="Path to config file")
        
        cmd_args, remain_args = parser.parse_known_args()

        executor = Executable.s.get(cmd_args.command)
        
        exec_parser = argparse.ArgumentParser()
        executor.arguments(exec_parser)
        args = exec_parser.parse_args(remain_args)
        
        # previous arguments
        for arg_key, arg_val in vars(cmd_args).items():
            setattr(args, arg_key, arg_val)

        # custom arguments
        for key, value in executor.setting.items():
            setattr(args, key, value)

        any(map(partial(cls.update_argument, args), cls.UPDATE_KEY.items()))

        return args
