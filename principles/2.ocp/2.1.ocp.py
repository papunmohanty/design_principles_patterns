"""
OCP: Open-Closed Principle
"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products: list(Product), color: Color):
        for p in products:
            if p.color == color: yield p

    # following new function addition violates OCP
    def filter_by_size(self, products: list(Product), size: Size):
        for p in producrs:
            if p.size == size: yield p

    # following new function addition violates OCP
    def filter_by_color_and_size(self, products: list(Product), color: Color, size: Size):
        for p in products:
            if p.color == color and p.size == size: yield p
