"""
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.

"""
from functools import wraps



def arg_rules(type_: type, max_length: int, contains: list):
    def arg_rules_func(func):
        @wraps(func)
        def checking(arg):
            if len(arg) >= max_length:
                print(False, 'Please make sure that the lenght is not more than:', max_length)
            if type(arg) != type_:
                print(False, 'Please make sure that the type is:', type_)
            for i in contains:
                if i not in arg:
                    print(False, 'Please make sure that your function contains:', contains)
            return func(arg)
        return checking
    return arg_rules_func


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# create_slogan('johndoe05@gmail.com')

print(create_slogan('S@SH05'))


