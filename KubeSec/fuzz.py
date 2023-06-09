from scanner import *
from graphtaint import *

def fuzzValues():
    # Will isValidUserName allow a username of just empty space?
    res = isValidUserName(" ")
    print(res)   
    print('='*100)

    # Will isValidPasswordName allow a password of just empty space?
    res = isValidPasswordName(" ")
    print(res)   
    print('='*100)

    # Will getYAMLFiles handle errant input?
    res = getYAMLFiles("errant input")
    print(res)   
    print('='*100)

    # Will getSHFiles handle errant input?
    res = getSHFiles("errant input")
    print(res)   
    print('='*100)

    # Will readBashAsStr handle errant input?
    res = readBashAsStr("errant input")
    print(res)   
    print('='*100)

def simpleFuzzer(): 
    fuzzValues()


if __name__=='__main__':
    simpleFuzzer()