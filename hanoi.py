
def print_move(fr, to):
    print('move from {} to {}'.format(fr, to))


def towers(n, fr, to, spare):
    if n==1:
        print_move(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)


if __name__=="__main__":
    print towers(1, 'f', 't', 's')
    print
    print towers(5, 'f', 't', 's')

