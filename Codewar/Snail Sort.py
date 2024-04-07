import test

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
finished = True
def snail(snail_map):
    global finished
    newList = []
    breakpoint()
    rowNum = len(snail_map)-1; colNum = len(snail_map[0])-1
    breakpoint()
    x = 0; y = 0
    while finished:
        if x < colNum:
            newList.append(snail_map[y][x])
            x += 1
        elif x == colNum and y <= 2:
            newList.append(snail_map[y][x])
            y += 1
            breakpoint()
        elif y == rowNum:
            newList.append(snail_map[y][x])
            x -= 1
        elif x == 0 and y > 1:
            newList.append(snail_map[y][x])
            y -= 1
            breakpoint()
        elif y == 1 and x < 1:
            newList.append(snail_map[y][x])
            x += 1
            finished = False
    return newList

# test.assert_equal(snail(array),expected)
print(snail(array))