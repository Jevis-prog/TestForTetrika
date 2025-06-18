def strict(func):
    def wrapper(*args):
        annotations = func.__annotations__
        for name, value in zip(annotations, args):
            if name in annotations:
                expected_type = annotations[name]
                if type(value) is not expected_type:
                    raise TypeError(
                        f"Argument '{name}' must be of type {expected_type.__name__}, got {type(value).__name__}"
                    )
        return func(*args)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

print(sum_two(1, 2))     # OK: 3
print(sum_two(1, 2.4))   # Ошибка: TypeError