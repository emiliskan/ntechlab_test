from sqlalchemy.sql import func


def calc_distance(x1, x2, y1, y2):
    return func.sqrt(func.pow(x1 - x2, 2) + func.pow(y1 - y2, 2))