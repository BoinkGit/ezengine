file = open("test.eze", "r")
lines = file.readlines()
variables = {}
file.close()

error = 0

# function list:
#   echo: print
#   file: let
#   increment ... by: +=
#   decrement ... by: -=

for line in lines:
    code = line.split()
    if code[0] == "echo":
        print(line[5:])
    elif code[0] == "file:":
        if code[2] != "-":
            print(f"The code translator couldn't understand the code. Please replace \"{code[2]}\" with \"-\".")
            error += 1
            break
        if code[3] in variables:
            variables[code[1]] = variables[code[3]]
        if code[3][0] in ["\"","\'"]:
            variables[code[1]] = " ".join(code[3:])[1:-1]
        else:
            variables[code[1]] = int(code[3])


if error >= 1:
    print("\nQuit due to error.")
else: print("\nDone!")

print(f"Variables: {variables}")