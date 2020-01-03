
from tkinter import *

import analyzer_game_control as ana_game


# Remain list (from DB next time)
remain_list = ['Tim','Alisa','Rose']

# Initial
window = Tk()
game_agent = ana_game.analyzer_weight_agent()
game_agent.initial_by_list(remain_list)

# Title
window.title("La prochaing Fois:")
window.geometry('600x200')


# Current list
current_msg = "The bank contains: %s" % remain_list
lbl_remain = Label(window, text=current_msg)
lbl_remain.grid(column=0, row=0)


# Create label widget
lbl_request = Label(window, text="Random Choose!", font=("Arial Bold", 14))
lbl_request.grid(column=0, row=1)


# Clicked Function
def clicked():
    btn.configure(text="Clicked")

    # Select
    chair_obj ,_ = game_agent.pick_by_random_pop()
    record_obj,_ = game_agent.pick_by_random_pop()

    print(chair_obj,record_obj)
    # Msg
    chair_msg = "Chair:  %s"%chair_obj
    recor_msg = "Record: %s"%record_obj
    remain_msg = "%s"%game_agent.afficher_remain_weight_list()

    # Display
    lbl_chair_result = Label(window, text=chair_msg)
    lbl_chair_result.grid(column=0,row=3)

    lbl_recor_result = Label(window,text=recor_msg)
    lbl_recor_result.grid(column=0,row=4)


    lbl_remain      = Label(window,text=remain_msg)
    lbl_remain.grid(column=0,row=5)



# Button
btn = Button(window, text="Click Me",command=clicked)
btn.grid(column=1,row=1)




# Run
window.mainloop()
