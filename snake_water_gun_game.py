# import random module to generate random choices
import random

# import tkinter to create GUI window
import tkinter as tk


# variables to store scores
user_score = 0
computer_score = 0
draws = 0

# list to store game history
history = []

# list to store user previous choices (used for simple AI)
user_history = []


# function to decide computer move
def get_computer_choice():

    # simple AI logic
    # if user chooses snake many times
    # computer will choose gun to counter it
    if user_history.count("snake") > user_history.count("water"):
        return "gun"

    # otherwise computer chooses randomly
    return random.choice(["snake","water","gun"])


# main function that runs when user clicks a button
def play(user):

    # we need global variables to update scores
    global user_score, computer_score, draws

    # store user choice in history
    user_history.append(user)

    # computer makes its move
    computer = get_computer_choice()


    # check if both chose same option
    if user == computer:
        result = "Draw"
        draws += 1


    # user winning conditions
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):

        result = "You Win"
        user_score += 1


    # otherwise computer wins
    else:
        result = "Computer Wins"
        computer_score += 1


    # store round result in history
    history.append(f"You:{user}  Computer:{computer}  → {result}")


    # update result text on screen
    result_label.config(text=f"Computer chose: {computer}\n{result}")


    # update scoreboard
    score_label.config(
        text=f"You: {user_score}   Computer: {computer_score}   Draws: {draws}"
    )


    # show last 5 rounds history
    history_label.config(text="\n".join(history[-5:]))



# function to reset the whole game
def reset_game():

    # use global variables
    global user_score, computer_score, draws, history, user_history

    # reset scores
    user_score = 0
    computer_score = 0
    draws = 0

    # clear history lists
    history = []
    user_history = []

    # update GUI labels
    score_label.config(text="You: 0   Computer: 0   Draws: 0")
    result_label.config(text="Game Reset")
    history_label.config(text="")



# create main game window
root = tk.Tk()

# set window title
root.title("Snake Water Gun Pro")

# set window size
root.geometry("420x420")

# set background color
root.configure(bg="#1e1e1e")


# game title label
title = tk.Label(
    root,
    text="🐍 Snake Water Gun 🔫",
    font=("Arial",18),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=10)


# button for snake choice
snake_btn = tk.Button(
    root,
    text="🐍 Snake",
    width=15,
    command=lambda: play("snake")
)

snake_btn.pack(pady=5)


# button for water choice
water_btn = tk.Button(
    root,
    text="💧 Water",
    width=15,
    command=lambda: play("water")
)

water_btn.pack(pady=5)


# button for gun choice
gun_btn = tk.Button(
    root,
    text="🔫 Gun",
    width=15,
    command=lambda: play("gun")
)

gun_btn.pack(pady=5)


# label to display round result
result_label = tk.Label(
    root,
    text="",
    font=("Arial",12),
    bg="#1e1e1e",
    fg="yellow"
)

result_label.pack(pady=10)


# label to display score
score_label = tk.Label(
    root,
    text="You: 0   Computer: 0   Draws: 0",
    font=("Arial",12),
    bg="#1e1e1e",
    fg="white"
)

score_label.pack(pady=5)


# title for history section
history_title = tk.Label(
    root,
    text="Last Rounds",
    bg="#1e1e1e",
    fg="white"
)

history_title.pack()


# label to display round history
history_label = tk.Label(
    root,
    text="",
    bg="#1e1e1e",
    fg="lightgreen",
    justify="left"
)

history_label.pack()


# button to reset game
reset_btn = tk.Button(
    root,
    text="🎮 Play Again",
    command=reset_game
)

reset_btn.pack(pady=10)


# run the GUI loop
root.mainloop()