coffee_is_grinding = False

def press_grind_beans():
    global coffee_is_grinding

    if coffee_is_grinding:
        print( "Stopping the grind")
        coffee_is_grinding = False
    else:
        print("Grinding is about to begin" )
        coffee_is_grinding = True

press_grind_beans() # t h e c o f f e e i s n o t grinding
press_grind_beans() # t h e c o f f e e i s grinding

