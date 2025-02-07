# Variable scope

var_1 = 1
var_2 = 2
var_3 = 3

def create_local_scope(var_1, var_2):
    print(var_1, var_2, var_3)

create_local_scope(5, 4)

print(var_1)
print(var_2)
