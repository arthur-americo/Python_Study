'''Make a program that has a function called area(), which receives the dimensions of a rectangular terrain 
(width and length) and shows the area of the terrain.'''
def area(width, length):
    return width * length

width = float(input('Width (m): '))
length = float(input('Length (m): '))

print(f'The area of the terrain is {area(width, length)} m²')