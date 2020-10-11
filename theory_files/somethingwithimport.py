from somethingwitherrors import BadName, greet as gr  #Эт пример использования своего кода в качестве модуля

#from somethingwitherrors import * # импортировать все имена

import fib # - долго считается
import sys
#print(some_e.greet("Student"))
print(fib.fib(5))

print(type(sys.modules))
print(sys.modules)

for path in sys.path:
    print(path)

gr()
