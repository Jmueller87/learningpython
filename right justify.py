#   This was an assignment. The program needed to print any string input
#   with enough leading spaces so that the last letter of the string
#   was in column 70 of the display

def right_justify(s):
    x = len(s)
    y = 70 - x
    print((y*" " + s))

while True:
    s = input(str(""))
    right_justify(s)
    continue

          
#   This program has no prompt - simply run it, type your string, and hit enter
          
