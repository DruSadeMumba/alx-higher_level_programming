#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    sqOrder = ['id', 'size', 'x', 'y']

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __str__(self):
        """str rep of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} " \
            f"- {self.width}"

    def update(self, *args, **kwargs):
        """update vals of square"""
        if args:
            for attr, val in zip(self.sqOrder, args):
                setattr(self, attr, val)

        if kwargs:
            for attr, val in kwargs.items():
                setattr(self, attr, val)

    def to_dictionary(self):
        """dict rep of square"""
        return {attr: getattr(self, attr) for attr in self.sqOrder}
