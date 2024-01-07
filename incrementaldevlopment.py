import math
def dist(x1,x2,y1,y2):
    d_x= abs(x1-x2)
    d_y=abs(y1-y2)

    distance = math.sqrt(d_x*d_x)+(d_y * d_y)
    return distance

# Example usage:
x1, y1 = 1, 2
x2, y2 = 4, 6

euclidean_distance = dist(x1, x2, y1, y2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is: {euclidean_distance}")
