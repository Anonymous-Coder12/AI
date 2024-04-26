def tower(n, src, helper, dest):
    if (n == 0):
        return
    tower(n-1, src, dest, helper)
    print("move disk", n, "from rod", src, "to rod", dest)
    tower(n-1, helper, src, dest)


n = int(input("enter a number:"))
tower(n, "a", "b", "c")
