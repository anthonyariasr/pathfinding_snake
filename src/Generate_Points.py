import random
from Calculate_Route import calculate_route


"""
Generate Coordinates

This function creates a certain amount of points (3-5)
then it proceeds to sort the points using first the origin as a references, and 
then using the last point added. In this way, we ensure that the snake takes the
more optimal path between one point and another.
"""
def generate_coordinates(obstacles):
    def generate_random_coordinates(num_coordinates, matrix_size):
        coordinates = set()
        while len(coordinates) < num_coordinates:
            x = random.randint(0, matrix_size - 1)
            y = random.randint(0, matrix_size - 1)
            new_coordinate = (x, y)
            if new_coordinate not in coordinates and new_coordinate not in obstacles:  # Check if the coordinate is not already in the set
                coordinates.add(new_coordinate)
        return list(coordinates)


    num_coordinates = random.randint(5, 7)  # Generate a random number of coordinates between 3 and 5
    matrix_size = 20
    points = generate_random_coordinates(num_coordinates, matrix_size)

    
    """
    Sort Points

    Here is where the distance between points is calculated. And also where the points
    are sorted in a list that later on will be send to execute the final
    step before showing the snake route on screen.
    """
    def sort_points():
        sorted_coordinates = []
        aux = (0, 0)
        points_copy = points[:]  # Hacer una copia de la lista points
        while points_copy:
            len_aux = 100
            for point in points_copy:
                length = len(calculate_route(aux, point, obstacles))
                if length < len_aux:
                    len_aux = length
                    point_aux = point
            
            aux = point_aux
            sorted_coordinates.append(point_aux)
            points_copy.remove(point_aux)  # Eliminar el punto de la copia de la lista

        return sorted_coordinates
            

    sorted_coordinates = sort_points()
    
    return(sorted_coordinates)
