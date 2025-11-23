while True:
    if can_harvest():
        harvest()
        move(North)
    else:
        do_a_flip()