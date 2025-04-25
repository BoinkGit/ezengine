file = open("test.eze", "r")
lines = file.readlines()
file.close()

for i in range(len(lines)):
    if lines[i][-1] == "\n":
        lines[i] = lines[i][:-1]

variables = {}
loops = {}
code = []

error = 0

# function list:
#   echo hello === print("hello")
#   read file: ... === print(...)
#   file: ... - ... === let ... =...
#   increment file ... by ... === ... += ...
#   decrement file ... by ... === ... -= ...
#   do ... ... times === for ... in range(...): ...

def echo(i):
    if code[i] == "echo":
        print(line[5:])

def read(i):
    if code[i] == "read":
        if code[i+1] != "file:":
            print(f"The code translator couldn't understand the code. Please replace \"{code[i+1]}\" with \"file:\".")
            error += 1
        else:
            if code[i+2] in variables:
                print(variables[code[i+2]])
            else:
                print(f"The code translator couldn't find this file. Please replace \"{code[i+2]}\" with a named file.")
                error += 1

def file(i):
    if code[i] == "file:":
        if code[i+2] != "-":
            print(f"The code translator couldn't understand the code. Please replace \"{code[i+2]}\" with \"-\".")
            error += 1
        if code[i+3][0] in ["\"","\'"]:
            variables[code[i+1]] = " ".join(code[i+3:])[1:-1]
        elif code[3] in variables:
            variables[code[i+1]] = variables[code[i+3]]
        else:
            variables[code[i+1]] = int(code[i+3])

def increment(i):
    if code[i] == "increment":
        if code[i+1] != "file":
            print(f"The code translator couldn't understand the code. Please replace \"{code[i+1]}\" with \"file\".")
            error += 1
        if code[i+2] not in variables:
            print(f"The code translator couldn't find this file. Please replace \"{code[i+2]}\" with a named file.")
            error += 1
        else:
            if code[i+3] != "by":
                print(f"The code translator couldn't understand the code. Please replace \"{code[i+3]}\" with \"by\".")
                error += 1
            if code[i+4] in variables:
                variables[code[i+2]] += variables[code[i+4]]
            else:
                variables[code[i+2]] += int(code[i+4])

def decrement(i):
    if code[i] == "decrement":
        if code[i+1] != "file":
            print(f"The code translator couldn't understand the code. Please replace \"{code[i+1]}\" with \"file\".")
            error += 1
        if code[i+2] not in variables:
            print(f"The code translator couldn't find this file. Please replace \"{code[i+2]}\" with a named file.")
            error += 1
        else:
            if code[i+3] != "by":
                print(f"The code translator couldn't understand the code. Please replace \"{code[i+3]}\" with \"by\".")
                error += 1
            if code[i+4] in variables:
                variables[code[i+2]] -= variables[code[i+4]]
            else:
                variables[code[i+2]] -= int(code[i+4])
#wip loop function
"""def do_times(i):
    if code[i] == "do:":
        end = 1
        for a in range(len(lines)):
            if line[a][:2] == "do":
                end += 1
            if line[a][-5:] == "times":
                end -= 1
            if end == 0:
                loops[index] = int(a[:-6])
                break
    if code[i][-5:] == "times":
        if code[i][:-6] in loops:
            loops[code[i][:-6]] -= 1
            index = 
"""
    
index = 0
while index < len(lines)-1:
    line = lines[index]
    code = line.split()
    echo(0)
    read(0)
    file(0)
    increment(0)
    decrement(0)
    if error > 0:
        break
    index += 1


if error == 1:
    print("\nQuit due to error.")
elif error > 1:
    print(f"\nHOW DID YOU GET {error} ERRORS?")
else: print("\nDone!")

print(f"Variables: {variables}")