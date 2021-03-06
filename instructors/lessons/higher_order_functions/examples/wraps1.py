"""
So why would we use a decorator?

This example is fairly contrived, but it puts some control flow
into a decorator to catch extra input that the sample() function
isn't written to accept.
"""
from functools import wraps


def mydecorator(func):
    """ A decorator that simply passes through a function.
    """
    print "Decorator is go!"
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        """
        We'll need to run the function in the wrapper in order
        to extend the functionality and/or modify the output.
        """
        # Lets intercept the return if there are too many values.
        # I have been explicit in this compound if statement, but 
        # remember an empty dict/list is false, so there's a better way.
        if len(args) > 0 or len(kwargs.keys()) > 0:
            return func()
        else:
            return func(*args, **kwargs)

    return function_wrapper


# Using the decorator.
@mydecorator
def sample():
    """ A sample function which we will decorate and extend.
    """
    print "instantiating sample function"
    return 'sample'

# This would break if it wasn't wrapped/decorated!
print sample('too', 'many', 'arguments')

print "We've wrapped our decorator's wrapper in @wraps(func)"
print 'This function is named:', sample.__name__
print "Sample function docs:"
print sample.__doc__
