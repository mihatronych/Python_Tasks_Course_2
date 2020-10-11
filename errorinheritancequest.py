def find_Parents(error):
    newSetErrors = error.copy()
    for err in list(error):
        if err in dict_Of_classErrors:
            for name in dict_Of_classErrors[err]:
                newSetErrors.add(name)
    return newSetErrors


def finish(error):
    if error in final_Dict:
        for i in final_Dict[error]:
            if i in error_txt:
                # print(indOferror, error_txt.index(i))
                if indOferror > error_txt.index(i):
                    return print(error)


list_Of_classErrors = []
listOfErrors = []
n = int(input())  ###countOfClassErrors
for i in range(n):
    classEr = input().split()
    list_Of_classErrors.append(classEr)

# for i in list_Of_classErrors:
#     print(i)
dict_Of_classErrors = dict()
for er in list_Of_classErrors:
    key = er[0]
    # print(key)
    dict_Of_classErrors[key] = set()
    if len(er) > 1:
        for sign in er[2:]:
            if sign != ' ':
                dict_Of_classErrors[key].add(sign)
# for i in dictOfclassErrors:
#     print(i, dictOfclassErrors[i], sep=' : ')

list_Of_Errors = []
n = int(input()) ### count Of Errors
for i in range(n):
    error = input()
    list_Of_Errors.append(error)

final_Dict = dict()

for keyErr in dict_Of_classErrors:
    final_Dict[keyErr] = set()
    d = dict_Of_classErrors[keyErr]
    while  len(d) != len(final_Dict[keyErr]): ### dict_Of_classErrors[keyErr]
        d = final_Dict[keyErr]
        error_parents = dict_Of_classErrors[keyErr].union(final_Dict[keyErr])

        if len(error_parents) > 0:
            error = find_Parents(error_parents).copy()
            final_Dict[keyErr] = set()
            final_Dict[keyErr] = error
        # else:
        #     final_Dict[keyErr] = set()
# for i in final_Dict:
#     print(i, final_Dict[i], sep=' : ')

# print(list_Of_Errors)
k = 1
error_txt = list_Of_Errors
for i in error_txt[1:]:
    error = i
    indOferror = k
    if error in error_txt:
        if indOferror > error_txt.index(error):
            print(error)
        else:
            finish(error)
    k += 1
# print(len(list_Of_Errors))
# print(len(error_txt))







            # print(error)
# print(list_Of_Errors[:3])
