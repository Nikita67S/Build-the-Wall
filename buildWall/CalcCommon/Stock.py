"""Comments about module"""


from math import ceil


def stock_func(bricks_in: float, kg_in: float, constant1: float, constant2: float) -> tuple[int, int]:
    """

    Args:
        bricks_in:
        kg_in:
        constant1:
        constant2:

    Returns:

    """
    bricks = ceil(bricks_in * constant1)
    k = ceil(kg_in * constant2)

    return bricks, k
