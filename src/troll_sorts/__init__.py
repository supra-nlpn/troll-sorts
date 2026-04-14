from .sorts import communist_sort, capitalist_sort, island_sort, six_seven_sort
from .welcome import show_welcome

# Play the welcome animation (only once per user)
show_welcome()

__all__ = [
    'communist_sort', 
    'capitalist_sort', 
    'island_sort', 
    'six_seven_sort'
]
