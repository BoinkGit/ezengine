print("Ez Engine v0.1.0\n")
file = open("test.eze", "r")
lines = file.readlines()
variables = {}
file.close()

error = 0

# function list:
#   echo hello: print(hello)
#   file: ... - ...: let ... =...
#   increment file ... by ...: ... += ...
#   decrement file ... by ...: ... -= ...

for line in lines:
    code = line.split()
    if code[0] == "echo":
        print(line[5:])
    elif code[0] == "file:":
        if code[2] != "-":
            print(f"The code translator couldn't understand the code. Please replace \"{code[2]}\" with \"-\".")
            error += 1
            break
        if code[3][0] in ["\"","\'"]:
            variables[code[1]] = " ".join(code[3:])[1:-1]
        elif code[3] in variables:
            variables[code[1]] = variables[code[3]]
        else:
            variables[code[1]] = int(code[3])
    elif code[0] == "increment":
        if code[1] != "file":
            print(f"The code translator couldn't understand the code. Please replace \"{code[1]}\" with \"file\".")
            error += 1
            break
        if code[2] not in variables:
            print(f"The code translator couldn't find this file. Please replace \"{code[2]}\" with a named file.")
            error += 1
            break
        else:
            if code[3] != "by":
                print(f"The code translator couldn't understand the code. Please replace \"{code[3]}\" with \"by\".")
                error += 1
                break
            if code[4] in variables:
                variables[code[2]] += variables[code[4]]
            else:
                variables[code[2]] += int(code[4])
    elif code[0] == "decrement":
        if code[1] != "file":
            print(f"The code translator couldn't understand the code. Please replace \"{code[1]}\" with \"file\".")
            error += 1
            break
        if code[2] not in variables:
            print(f"The code translator couldn't find this file. Please replace \"{code[2]}\" with a named file.")
            error += 1
            break
        else:
            if code[3] != "by":
                print(f"The code translator couldn't understand the code. Please replace \"{code[3]}\" with \"by\".")
                error += 1
                break
            if code[4] in variables:
                variables[code[2]] -= variables[code[4]]
            else:
                variables[code[2]] -= int(code[4])

if error == 1:
    print("\nQuit due to error.")
elif error > 1:
    print(f"\nHOW DID YOU GET {error} ERRORS?")
else: print("\nDone!")

print(f"Variables: {variables}")