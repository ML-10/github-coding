rows = int(input('How many rows do you want to have?\n'))
def pascal(n):
    def newrow(row):
        prev = 0
        for x in row:
            yield prev + x
            prev = x
        yield 1

    prevrow = [1]
    yield prevrow
    for x in range(n):
        prevrow = list(newrow(prevrow))
        yield prevrow

def printPascal(pascalNums):
    for line in pascalNums:
        print((rows - len(line)) * ' ' + str(line))
printPascal(list(pascal(rows - 1)))
