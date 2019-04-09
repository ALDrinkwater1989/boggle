def make_grid(width, height):
    """
   Creates a grid
    """
    
    
    return{(row, col):  ' ' for row in range (height)
        for col in range (width)
    }