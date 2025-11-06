#
# This is all function
#
def add(l, r):
    return l + r


def mul(l, r):
    return l * r


def div(l, r):
    return l / r

# self test code for this.module block or module packages
if __name__ == "__main__":
    print("This is", dir())
    print(add( 4, 2 ))
    print(mul( 4, 2 ))
    print(div( 4, 2 ))