import __main__
from pathlib import Path


class Executable:
    _ = Path(__main__.__file__)
    s = dict()

    def __init__(self, file: str):
        self.command = file
        self.module = __import__(file)
        self.name = self.module.__name__

    def __getattr__(self, key):
        if hasattr(self.module, key):
            return getattr(self.module, key)
        elif hasattr(super(Executable, self), key):
            return super(Executable, self).__getattribute__(self, key)
        else:
            return lambda *args: None

    def __call__(self, *args, **kwargs):
        return getattr(self.module, self.name)(*args, **kwargs)

    @staticmethod
    def ismain():
        return Executable._.stem == 'main'


for executor in map(lambda x: x.stem,
                    filter(lambda x: x.name != Executable._.name,
                           Path('.').glob('*.py'))):
    Executable.s[executor] = Executable(executor)
