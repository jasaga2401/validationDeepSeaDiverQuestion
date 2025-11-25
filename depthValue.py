# Deep Sea Diver Algorithm

# rejects negative values
def rejectNegativeValues(depthValue):
    depthValue = int(depthValue)
    if (depthValue < 0):
        print('You cannot have a negative value\n')
        depthValue = False
        return depthValue
    return True

# input a depth value  
def inputValue():
    depthValue = input('Enter a depth value between 0-40m:')
    return depthValue

# main programming hub
def main():
    valid = False
    while (not valid):
        valid = True        
        depthValue = inputValue()
        valid = rejectNegativeValues(depthValue)
        

# starts the program
if (__name__ == "__main__"):
    main()





    
