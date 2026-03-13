# ---- 1 ----
def draw_grid_2x2():
    row_top = "+ - - - - + - - - - +"
    row_mid = "|         |         |"

    print(row_top)
    for i in range(4):
        print(row_mid)
    print(row_top)
    for i in range(4):
        print(row_mid)
    print(row_top)

draw_grid_2x2()

# ---- 2 ----
def draw_grid_4x4():
    row_top = "+ - - - + - - - + - - - + - - - +"
    row_mid = "|       |       |       |       |"

    for i in range(4):
        print(row_top)
        for j in range(4):
            print(row_mid)
    print(row_top)

draw_grid_4x4()
