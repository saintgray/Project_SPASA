import time
import traceback

def aop_excution_time(func):
    def wrapper(*args):
        try:
            start_time = time.time() * 1000
            result = func(*args)
        except Exception as ex:
            print("[] error occured".format(func.__name__))
            print("{}".format(traceback.format_exc()))
            raise ex
        finally:
            end_time= time.time() * 1000
            print("[{}] progress time : {} ms".format(func.__name__, (end_time - start_time)))
        return result
    return wrapper