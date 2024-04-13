
from Generate_Points import generate_coordinates
from Calculate_Route import calculate_route
from Generate_Obstacles import generate_obstacles
import tkinter as tk
from PIL import Image, ImageTk

"""
Generate Board

In this function we manage everything related to the GUI. There's the movement function
which is used to modify the matrix in order to update and show the changes on screen.
"""
def generate_board():
    # Create an empty matrix of size 20x20 to use as board
    matrix = [["" for _ in range(20)] for _ in range(20)]
    obstacles = generate_obstacles()
    points = generate_coordinates(obstacles)
    
    for i in points:
        matrix[i[0]][i[1]] = "X"

    for o in obstacles:
        matrix[o[0]][o[1]] = "*"

    matrix[0][0] = "O"



    class MatrixBoardApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Automate Snake - Anthony Arias")

            # Create a 2D list to hold references to the labels in the grid
            self.labels = [[None] * 20 for _ in range(20)]

            # Load the images
            self.photo_mouse = ImageTk.PhotoImage(Image.open("Pathfinding Snake/assets/img/grass_mouse.png").resize((40, 40), Image.BILINEAR))
            self.photo_snake = ImageTk.PhotoImage(Image.open("Pathfinding Snake/assets/img/grass_snake.png").resize((40, 40), Image.BILINEAR))
            self.photo_obstacle = ImageTk.PhotoImage(Image.open("Pathfinding Snake/assets/img/obstacle.png").resize((40, 40), Image.BILINEAR))
            self.photo_grass = ImageTk.PhotoImage(Image.open("Pathfinding Snake/assets/img/grass.png").resize((40, 40), Image.BILINEAR))

            # Create and fill the grid with labels containing images
            for i in range(20):
                for j in range(20):
                    self.labels[i][j] = tk.Label(root, width=40, height=40, borderwidth=1)
                    self.labels[i][j].grid(row=i, column=j, padx=1, pady=1)

            self.update_board(matrix)

        def update_board(self, matrix):
            for i in range(20):
                for j in range(20):
                    if matrix[i][j] == "X":
                        self.labels[i][j].config(image=self.photo_mouse, width=32, height=32)
                    elif matrix[i][j] == "O":
                        self.labels[i][j].config(image=self.photo_snake, width=40, height=40)
                    elif matrix[i][j] == "*":
                        self.labels[i][j].config(image=self.photo_obstacle, width=40, height=40)   
                    else:
                        self.labels[i][j].config(image=self.photo_grass, width=40, height=40)

    #Creating the board
    root = tk.Tk()
    app = MatrixBoardApp(root)

    """
    Movement takes the previusly sorted list of points and re calculate the route
    in order to move box by box updating the matrix content and updating the displayed board.
    """
    def movement (points, initial=(0, 0)):
        
        if not points:
            return

        print("Points:", points)

        for x in points:
            #Calculate the route
            route = calculate_route(initial, x, obstacles)

            for point in route:
                matrix[initial[0]][initial[1]] = ""
                matrix[point[0]][point[1]] = "O"
                app.update_board(matrix)
                initial = point
                root.update()  # Update the GUI to reflect the changes
                root.after(100)  # Pause for 100 milliseconds

        return

    movement(points)

    root.mainloop()

    

    return

