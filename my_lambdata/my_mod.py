# print('hello')
def data_string(str):
    ##     """feature enginering toi get length of a string varible 
##     to still be used in a dataframe """

    counter = 0
    for i in str :
        counter += 1
    return counter    

str = ('')
# print(data_string(str)) 


# print(data_string('magic the gathering'))
if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    y = (input("Please type a string to get its count"))
    print(y, data_string(y))


  
def enlarge(n):
    return int(n) * 100



if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))