

class _Media:
    def __init__(self, **entries):
        self.__dict__.update(entries)
    def __str__(self):
        return f'Attributes: {self.__dict__}'