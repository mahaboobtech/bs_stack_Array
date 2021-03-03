
class stack:
    # initialize the data array
    def __init__(self):
        self.data = []
        print("started")
    # appends the data in the array
    def push(self, n):
        self.data.append(n)
    # show the top data in the array and delete from the array
    def pop(self):
        self.data.pop()
    # chech the stack array is empty or not
    def is_emptyA(self):
        if len(self.data) == 0:
            return True
        else :
            return False
    # it just shows the whether there is element are not on top of stack array
    def top(self):
        return self.data[-1]
    # it print all element in stack from top
    def display(self):
        if self.is_emptyA():
            print("this is empty ")
        else:
            top = len(self.data)-1
            print("elements in the stack are:")
            for i in range(top, -1, -1):
                print(self.data[i])


aSd = stack()
a = aSd.is_emptyA() # check initally empty or not value goes to a and show true
print(a)
aSd.display()       # as stack is empty show there is empty
aSd.push(30)        # pushing following element
aSd.push(4221)
aSd.push(200)
aSd.push(46563)
aSd.pop()           # removing following element and showing
aSd.display()       # finally display all elements in stack
print("the top element is : ", aSd.top())       # seing top element on stack
