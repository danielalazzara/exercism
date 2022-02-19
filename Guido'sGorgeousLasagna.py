EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """
    Return how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers): 
    """
    Return how many minutes you would spend making the lasagna layers
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
  
    """
    Return the total number of minutes you've been cooking
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
  
