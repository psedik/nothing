def hello(name):
    if not name:
        return None
    return "Hello {}!".format(name)


if __name__ == "__main__":
    print(hello("world"))
