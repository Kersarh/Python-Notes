def fun():
    try:
        return 1
    finally:
        return 2


print(fun())  # 2
