#   This was an assignment. The program needed to draw a diagram that was
#   illustrated in the textbook. (The posted solution used 23 lines of code) 


a = str("+ - - - - ")
z = str("|         ")

def print_four(z):
    print(2*z + "|")
    print(2*z + "|")
    print(2*z + "|")
    print(2*z + "|")
    
def add_plus(a):
    print(2*a + "+")
    
add_plus(a)
print_four(z)
add_plus(a)
print_four(z)
add_plus(a)




    
