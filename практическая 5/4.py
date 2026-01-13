print("Универсальный калькулятор площади")
import math

width = float(input("Введите ширину прямоугольника:"))
height = float(input("Введите высоту прямоугольника:"))
def calculate_rectangle_area (width, height):
    """
    вычисляет площадь прямоугольника.

    Args:
        width (float): ширина прямоугольника
        height (float): высота прямоугольника
        
    Returns:
        float: площадь прямоугольника
    """
    return width * height
print(f"Площадь прямоугольника: {calculate_rectangle_area (width, height):.2f}")

radius = float(input("Введите радиус круга:"))
def calculate_circle_area(radius):
    """
    вычисляет площадь круга.

    Args:
        radius(float): радиус круга

    Return:
        float: площадь круга
    """
    return radius * math.pi ** 2
print(f"Площадь круга: {calculate_circle_area(radius):.2f}")

