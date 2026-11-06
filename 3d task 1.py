def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter
user_input_len=int(input("Enter length: "))
user_input_breadth=int(input("Enter breadth: "))
area,perimeter = rectangle_area_perimeter(user_input_len,user_input_breadth)
print("Area :",area)
print("Perimeter:",perimeter) 
