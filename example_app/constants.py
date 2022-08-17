from enum import Enum


class ExampleStatus(Enum):
    OPENING = 'O'
    CLOSED = 'C'

    @classmethod
    def choices(cls):
        return [
            (cls.OPENING.value, 'Opening'),
            (cls.CLOSED.value, 'Confirmed')
        ]
