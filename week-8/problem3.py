#!/usr/bin/env python


def dict_invert(d):
    '''
    d: dict
    '''
    x = {}
    for k,v in d.items():
        if v not in x.keys():
            x[v] = [k]
        else:
            x[v].append(k)

    res = {k:sorted(v) for k,v in x.items()}
    return res


if __name__=="__main__":
    d1 = {1:10, 2:20, 3:30}
    d2 = {1:10, 2:20, 3:30, 4:30}
    d3 = {4:True, 2:True, 0:True}

    for d in (d1, d2, d3):
        print dict_invert(d)


