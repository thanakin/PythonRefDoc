print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
    def _len__(self):
        return 0

myobj = myclass()
print(bool(myobj))


x = 200
print(isinstance(x, int))
