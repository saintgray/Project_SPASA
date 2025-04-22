
def post_request(func):
    def wrapper(*args):
        print(args)
        return
    return wrapper
    
        