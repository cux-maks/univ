from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
  def decorate(func):
    sig = signature(func)
    bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
    # @wraps(func)
    def wrapper(*args, **kwargs):
      bound_values = sig.bind(*args, **kwargs)
      for name, value in bound_values.arguments.items():
        if name in bound_types:
          if not isinstance(value, bound_types[name]):
            raise TypeError('Argument {} must be {}'. format(name, bound_types[name]))
      return func(*args, **kwargs)
    return wrapper
  return decorate

@typeassert(int, z=int)
def spam(x, y, z=42):
  print(x, y, z)

spam(1, 2, 3)
spam(1, 'hello', 3)
# spam(1, 'hello', 'world') # error_code

'''
from inspect import signature


def spam(x, y, z=42):
  print(x, y, z)

def sig_test(*ty_args, **ty_kwargs):
  sig = signature(spam)
  bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
  print(bound_types)

sig_test(int, int)
sig_test(int, z=int)
sig_test(y=int, z=int)
'''