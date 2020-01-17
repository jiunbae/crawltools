import __main__
from typing import Union
from pathlib import Path


EXECUTABLES = 'crawler/*/spiders/*.py'


class Executable:
    _ = Path(__main__.__file__)
    s = dict()

    def __init__(self, file: str):
        self.command = file
        self.module = __import__(file, fromlist=(None, ))
        self.settings = __import__(f"{'.'.join(file.split('.')[:2])}.settings", fromlist=(None, ))
        self.name = next(reversed(file.split('.')))

    def __getattr__(self, key):
        if hasattr(self.module, key):
            return getattr(self.module, key)
        elif hasattr(super(Executable, self), key):
            return super(Executable, self).__getattribute__(self, key)
        else:
            return lambda *args: None

    def __call__(self, *args, **kwargs):
        return getattr(self.module, self.name)(*args, **kwargs)

    @property
    def setting(self):
        def _is_attribute_(key):
            return not key.startswith('_')
        return {
            key: getattr(self.settings, key)
            for key in filter(_is_attribute_, self.settings.__dict__)
        }

    @classmethod
    def add(cls, executor: Union[Path, str]):
        executor, *_ = str(executor).split('.')
        executor = executor.replace('/', '.')

        cls.s[next(reversed(executor.split('.')))] = cls(executor)

    @staticmethod
    def ismain():
        return Executable._.stem == 'spider'


any(map(Executable.add, filter(lambda x: x.name != Executable._.name and not x.name.startswith('__'),
                               Path('.').glob(EXECUTABLES))))
