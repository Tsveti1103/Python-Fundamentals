def operation(type, data):
    result = None
    if type == "int":
        result = 2 * int(data)
    elif type == "real":
        result = 1.5 * float(data)
        result = f"{result:.2f}"
    elif type == "string":
        result = f"${data}$"
    return result


data_type = input()
data = input()
print(operation(data_type, data))
