"""
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""

def stop_words(words: list):
    def function(func: str):
        def wrapper(name):
            for i in words:
                for j in func(name).split():
                    if i == j:
                        func(name).replace(j, '*')
            return func(name)
        return wrapper
    return function




@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Steve"))
















# def stop_words(words: list):
#     def stop_words_func(func: str):
#         def wrapper(name):
#             result = func(name)
#             for i in range(len(words)):
#                 if words[i] in result:
#                     result.replace(words[i], '*')
#         return wrapper
#     return stop_words_func
#
#
