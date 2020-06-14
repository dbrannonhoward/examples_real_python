from timeit import timeit

print(timeit('"-".join(str(n) for n in range(100))', number=10000))
print(timeit('"-".join([str(n) for n in range(100)])', number=10000))
print(timeit('"-".join(map(str, range(100)))', number=10000))


