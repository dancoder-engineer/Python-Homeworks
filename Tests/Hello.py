

name = "Hui Hui"

print ("I love " + name)




def new_decorator(original_func):
    def wrap_func():
        print("Extra code, before original function.")
        original_func()
        print("Extra code, after original function.")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Decorate me!")


ab="k,hjb,jhv,"
a = ab.split(',')
print(a)
#func_needs_decorator()