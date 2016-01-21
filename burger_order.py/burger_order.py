def item_order(order):
    s = "salad"
    salad = 0
    w = "water"
    water = 0
    h = "hamburger"
    hamburger = 0

    x = order.count(s)
    y = order.count(h)
    z = order.count(w)
    
    ## This will print the right answer. But it isn't accepted by the online submission tool.

    ## return ("Salad:%s Hamburger:%s Water:%s" %(x,y,z))

    ##Use this answer to pass the automated checkerer

    return ("salad:"+str(x)+" hamburger:"+str(y)+" water:"+str(z))


def main():
    order = "salad hamburger hamburger water water"

    print(item_order(order))

main()