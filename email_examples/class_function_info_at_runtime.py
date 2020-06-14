def main():
    print("Access the class name at runtime.")
    class MyClass: pass
    obj = MyClass()
    print(obj.__class__.__name__)
    print("Access the function name at runtime.")
    def myfunc(): pass
    print(myfunc.__name__)


if __name__ == '__main__':
    main()