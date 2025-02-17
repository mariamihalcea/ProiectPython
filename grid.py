import pygame
from colors import Colors
import random
class Grid:
    def __init__(self):
        self.num_rows=20
        self.num_cols=10
        self.cell_size=30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors() #list to hold all the colors

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column],end = " ")  #to be able to see if the grid is ok
            print() 

    def is_inside(self,row,column):
        if row >= 0 and row <self.num_rows and column >= 0  and column < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    # check for full rows - in order to delete them
    def is_row_full(self, row):
        # check to see if there are any empty cells
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] == 0
    
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row): 
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    
    #draw metod
    def draw(self,screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column *self.cell_size + 11, row*self.cell_size+11, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) # surface, color, rect

    def remove_bottom_half(self):
        half = self.num_rows // 2
        for row in range(half, self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0  # Elimină partea de jos
        
        for row in range(half - 1, -1, -1):  # Mută partea superioară în jos
            for col in range(self.num_cols):
                self.grid[row + half][col] = self.grid[row][col]
                self.grid[row][col] = 0