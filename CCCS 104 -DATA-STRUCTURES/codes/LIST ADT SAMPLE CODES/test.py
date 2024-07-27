menu_options = {
    0:'Exit',
    1:'Insert At Start',
    2:'Insert At End',
    3:'Insert At Position',
    4:'Delete At Start',
    5:'Delete At End',
    6:'Delete At Position',
    7:'Delete Number',
    8:'Search Number',
    9:'Display Number At Position',
    10:'Display List',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )

def option0():
     print('Confirm Exit?')

def option1():
     print('Handle option \'Option 3\'')

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

def option4():
     print('Handle option \'Option 3\'')
     
def option5():
     print('Handle option \'Option 3\'')
 
def option6():
     print('Handle option \'Option 3\'')

def option7():
     print('Handle option \'Option 3\'')

def option8():
     print('Handle option \'Option 3\'')

def option9():
     print('Handle option \'Option 3\'')

def option10():
     print('Handle option \'Option 3\'')
     
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 0:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')