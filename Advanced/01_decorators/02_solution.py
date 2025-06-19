

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Args: {args}")  # Args: ('sarthak', 22, 'male')
        print(f"Kwargs: {kwargs}")  # Kwargs: {'weight': None, 'height': None}
        args_value = ', '.join([str(arg) for arg in args])
        kwargs_value = ', '.join([f"{k}: {v}" for k, v in kwargs.items()])
        print(f"NAME: {func.__name__}, ARGUMENT VALUES: {args_value}, KEYWORD ARGUMENTS: {kwargs_value}")  # NAME: guess_my_name, ARGUMENT VALUES: sarthak, 22, male, KEYWORD ARGUMENTS: weight: None, height: None
        return 
    return wrapper


@debug
def guess_my_name(name, age, gender, weight=72, height=177):
    return

@debug
def my_name_is(name, code_name="Slim Shady"):
    return

guess_my_name("sarthak", 22, "male", weight=None, height=None)

my_name_is("Eminem", code_name="SLIM SHADY")