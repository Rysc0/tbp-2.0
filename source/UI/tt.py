# import tkinter as tk

# class GridUI:
#     def __init__(self, root, rows, columns):
#         self.root = root
#         self.rows = rows
#         self.columns = columns

#         self.create_grid()

#     def create_grid(self):
#         for i in range(self.rows):
#             for j in range(self.columns):
#                 cell = tk.Label(self.root, text=f'Row {i+1}, Col {j+1}', borderwidth=1, relief='solid', width=15, height=5)
#                 cell.grid(row=i, column=j)

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Grid UI Example")

#     # Set the number of rows and columns in the grid
#     rows = 3
#     columns = 2

#     grid_ui = GridUI(root, rows, columns)

#     root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("Grid Example")

label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
button = tk.Button(root, text="Click me")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
button.grid(row=1, column=0, columnspan=2)

root.mainloop()

