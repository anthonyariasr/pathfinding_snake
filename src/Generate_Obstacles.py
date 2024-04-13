import random

def generate_obstacles():
    # Function to generate a set of random coordinates representing obstacles within a matrix.
    def generate_random_coordinates(num_coordinates, matrix_size):
        # Generate unique random coordinates within the matrix.
        coordinates = set()
        while len(coordinates) < num_coordinates:
            x = random.randint(0, matrix_size - 1)
            y = random.randint(0, matrix_size - 1)
            new_coordinate = (x, y)
            if new_coordinate not in coordinates:  # Check if the coordinate is not already in the set
                coordinates.add(new_coordinate)
        return list(coordinates)
    
    # Define parameters for generating obstacles.
    num_coordinates = random.randint(10, 25)  # Generate a random number of coordinates between 10 and 25
    matrix_size = 20  # Assuming the matrix size is fixed at 20x20
    obstacles = generate_random_coordinates(num_coordinates, matrix_size)

    # Return the generated obstacles.
    return obstacles


