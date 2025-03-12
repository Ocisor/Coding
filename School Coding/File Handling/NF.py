def stripInstruction(string):
    words = string.split()
    instructions = words[0]
    operand = words[1]
    return instructions, operand
i, o = stripInstruction("LOAD 001")

print(f"i: {i}   o: {o}")