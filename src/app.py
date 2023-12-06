# # this file basically runs the entire system, renders the relevant screen and calls the relevant functions
# # from utilis
# # import everything here
from frontend.loginscreen import Ui_Dialog
if __name__ == "__main__":
 screen_stack= []
 Login_screen=Ui_Dialog()
 screen_stack.append(Login_screen)
 Ui_Dialog.show_screen()



 
