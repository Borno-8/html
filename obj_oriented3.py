class employee:

    def __init__(self):
        print('employee created')

    def __del(self):
        print("Destructor called")

def Create_obj():
    print('Making Object...')
    obj  = employee()
    print('function end...')
    return obj

print('Calling create_obj() function...')
obj = Create_obj()
print('Program End...')