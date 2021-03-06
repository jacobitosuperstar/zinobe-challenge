from time import time

def TimeTaken(func):
    '''
    Muestra el tiempo de ejecución de los objetos que pasan a través
    de ella
    '''
    def wrap_func(*args, **kwargs):
        t_start = time()
        result = func(*args, **kwargs)
        t_end = time()
        time_total = t_end - t_start
        result.time = time_total
        return result
    return wrap_func
