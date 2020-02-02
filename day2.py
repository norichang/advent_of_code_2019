with open('day2.txt', 'r') as f:
    strInputs = f.read().split(',')

inputs = list(map(lambda str: int(str), strInputs))

def intcode(program, i = 0):
    opcode = program[i]
    if opcode == 99:
        return program[0]
    num1Index = program[i + 1]
    num2Index = program[i + 2]
    answerIndex = program[i + 3]
    if opcode == 1:
        program[answerIndex] = program[num1Index] + program[num2Index]
        i += 4
        return intcode(program, i)
    if opcode == 2:
        program[answerIndex] = program[num1Index] * program[num2Index]
        i += 4
        return intcode(program, i)

def setIntcode(program, pos1, pos2):
    programCopy = program.copy()
    programCopy[1] = pos1
    programCopy[2] = pos2
    return intcode(programCopy)

print(setIntcode(inputs, 12, 2))

for i in range(100):
    for j in range(100):
        test = setIntcode(inputs, i, j)
        if test == 19690720:
          print(100 * i + j)
