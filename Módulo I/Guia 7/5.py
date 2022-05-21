def circle_area(radius: float) -> float:
    pi = 3.1415
    return pi * radius ** 2


def cylinder_volume(radius: float, high: float) -> float:
    return circle_area(radius) * high


print(cylinder_volume(3, 5))