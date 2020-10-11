def create(namespace, parent):
    global requests
    if parent in requests.keys():
        requests[parent]["ns"].append(namespace)
        requests[namespace] = {"ns": [], "args": []}
    else:
        requests[parent] = {"ns": [namespace], "args": []}
        requests[namespace] = {"ns": [], "args": []}


def add(namespace, var):
    global requests
    requests[namespace]["args"].append(var)


def get(parent, var):
    if var in requests[parent]["args"]:
        print(parent)
    else:
        if parent == "global":
            print("None")
        else:
            for value in requests.items():
                if parent in value[1]["ns"]:
                    get(value[0], var)


n = int(input())
requests = {"global": {"ns": [], "args": []}}
for i in range(n):
    cmd, name_sp, arg = input().split()
    if cmd == "create":
        create(name_sp, arg)
    if cmd == "add":
        add(name_sp, arg)
    if cmd == "get":
        get(name_sp, arg)
