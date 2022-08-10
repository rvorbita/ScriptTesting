#board 
# size = int(input("Enter size: "))

def create_board(size):

    x = " ---"
    y = "|   "

    for i in range(size):

        print(f"{x*size}")
        print(f"{y*(size + 1)}")

    print(f"{x*size}")

#create_board(3)

#winner
winner_is_2 = [[1, 2, 2],
	           [2, 2, 0],
	           [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	                [2, 1, 0],
	                [2, 1, 1]]

no_winner = [[1, 2, 0],
	         [2, 1, 0],
	         [2, 1, 2]]

also_no_winner = [[1, 2, 0],
	              [2, 1, 0],
	              [2, 1, 0]]

def check_the_winner(grid):

    #row checking
    for row in grid:
        if row[0] == row[1] == row[2] != 0:
            print(f"player {row[0]} wins")
            return
    #column checking
    for i in range(0, len(grid)):

        if grid[0][i] == grid[1][i] == grid[2][i] != 0:
            print(f"player {grid[0][i]} wins")
            return

    # #diagonal checking \
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        print(f"player {grid[0][0]} wins")
        return

    #diagonal checking /
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        print(f"player {grid[0][2]} wins")
        return
    
    return print("no winner")

check_the_winner(winner_is_2)
check_the_winner(winner_is_1)
check_the_winner(winner_is_also_1)
check_the_winner(no_winner)
check_the_winner(also_no_winner)

