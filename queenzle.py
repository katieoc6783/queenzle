import random

class Square:
    def __init__(self, colour, queen):
        self.colour = colour
        self.queen = queen

rows, cols = (6,6)
squares = [[Square("", 0) for j in range(cols)] for i in range(rows)]
nums = [0]*(cols)
colours = ["Pink", "Red", "Light Blue", "Light Green", "Orange", "Yellow", "Violet", "Dark Green", "Dark Blue", "Dark Purple"]
#then just assign it by column eg when column 5 queen is placed, set it as colours[5]

for i in range(0, cols):
    done = False
    while done == False:
        num = random.randint(0, rows - 1)
        if i == cols - 3:
            for k in range(0, rows - 2):
                if nums[k] == nums[k + 1] and nums[k] == 0:
                    if squares[cols - 3][k].queen == 0:
                        num = k
                    else:
                        num = k + 1
        elif i == cols - 4:
            for k in range(0, rows - 3):
                if nums[k] == 0 and nums[k] == nums[k + 1] == nums[k + 2]:
                    num = k + 1

        if squares[num][i].queen == 0:
            squares[num][i].queen = 2
            nums[num] = 1
            done = True
            for j in range(rows):
                #make everything else in that column X
                if squares[j][i].queen == 0:
                    squares[j][i].queen = 1
                #make everything else in that row X
                if squares[num][j].queen == 0:
                    squares[num][j].queen = 1
            #make the adj values X
            if num - 1 >= 0:
                if i + 1 < 6:
                    squares[num - 1][i + 1].queen = 1
                if i - 1 >= 0:
                    squares[num - 1][i - 1].queen = 1
            if num + 1 < 6:
                if i + 1 < 6:
                    squares[num + 1][i + 1].queen = 1
                if i - 1 >= 0:
                    squares[num + 1][i - 1].queen = 1


for j in range(cols):
    for i in range(rows):
        print(squares[i][j].queen)
    print("\n")
print(nums)

          

