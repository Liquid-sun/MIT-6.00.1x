#!/usr/bin/env python

order = "hamburger salad hamburger"

def item_order(order):
    o = order.split()
    sal = o.count('salad')
    ham = o.count('hamburger')
    wat = o.count('water')
    s = "salad:{} hamburger:{} water:{}".format(sal, ham, wat)
    return s

print item_order(order)

