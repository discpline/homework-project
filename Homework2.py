import math
side_a = 0.3 #сторона 1
side_b = 0.4 #сторона 2 
side_c = 0.5 #сторона 3
Poly_perimetr = ("Полу-периметр = ", side_a+side_b+side_c)/2 #нахождение полу-периметра по формуле
Plosh4ad = math.sqrt("Площадь = ",Poly_perimetr*(Poly_perimetr-side_a)*(Poly_perimetr-side_b)*(Poly_perimetr-side_c)) #нахождение площади по формуле
print(Poly_perimetr)
print(Plosh4ad)



