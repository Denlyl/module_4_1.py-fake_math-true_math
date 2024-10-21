from math import inf

from py2app.recipes.virtualenv import retry_import


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first/second