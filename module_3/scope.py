# Variable scope

var_1 = 1
var_2 = 2
var_3 = 3

def create_local_scope(var_1, var_2):
    var_4 = "a local variable"
    print(var_1, var_2, var_3, var_4)

create_local_scope(5, 4)

print(var_1)
print(var_2)
# print(var_4)  # will throw NameError in the global namespace
