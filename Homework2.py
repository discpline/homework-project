import math
side_a = 0.3  # сторона 1
side_b = 0.4  # сторона 2
side_c = 0.5  # сторона 3
poly_perimeter = (side_a + side_b + side_c) / 2  # нахождение полу-периметра по формуле
ploshchad = math.sqrt(poly_perimeter * (poly_perimeter - side_a) * (poly_perimeter - side_b) * (poly_perimeter - side_c))  # нахождение площади по формуле
print("Полу-периметр =", poly_perimeter)
print("Площадь =", ploshchad)




