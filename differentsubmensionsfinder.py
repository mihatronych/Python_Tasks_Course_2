objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
id_objects = [id(i) for i in objects]
setted_objects = set(id_objects)
print(len(setted_objects))
