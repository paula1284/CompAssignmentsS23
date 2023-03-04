def rm_smallest(d):
    values = list(d.values())
    if not(values):
        return d
    n = values[0]
    for i in range(len(values)):
        if values[i] < n:
            n = values[i]
    d.pop(list(d.keys())[values.index(n)])
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
