# import streamlit as st
# import random

# # --- Your Original Functions (Adapted for Streamlit Widgets) ---

# def intro():
#     """Returns the welcome message for the title."""
#     return "Welcome to the Number Guessing Game"

# def set_difficulty(difficulty_choice):
#     """
#     Sets the number range based on the difficulty choice from a widget.
#     It returns the start and end values instead of using global variables.
#     """
#     if difficulty_choice == 'Easy':
#         start, end = 1, 3
#     elif difficulty_choice == 'Medium':
#         start, end = 1, 10
#     elif difficulty_choice == 'Hard':
#         start, end = 1, 50
#     else: # Default case
#         start, end = 1, 10
#     return start, end

# def game_logic(user_choice, system_choice, count):
#     """
#     This function now contains only the core logic from your original `game()` function's loop.
#     It compares the numbers and returns a message and the new game state.
#     """
#     if user_choice == system_choice:
#         # Win condition
#         return f"Guessed in {count} go(es). Well Done, Hurray!!!", True # Message, GameOver = True
    
#     count += 1
    
#     if count > 10:
#         # Lose condition (out of tries)
#         return f"Limit Exceeded - Failed. The number was {system_choice}", True # Message, GameOver = True
    
#     # Continue playing
#     if user_choice < system_choice:
#         return "Wrong guess, Try Again! Try something greater.", False # Message, GameOver = False
#     else:
#         return "Wrong guess, Try Again! Try something smaller.", False # Message, GameOver = False

# # --- Streamlit Application UI ---

# # Set the title using your intro() function
# st.title(intro())

# # Use the sidebar for game controls
# st.sidebar.header("Game Setup")

# # 1. SET DIFFICULTY
# # We use a radio button instead of input()
# difficulty = st.sidebar.radio("Choose the difficulty:", ('Easy', 'Medium', 'Hard'))

# # We use a button to start the game
# if st.sidebar.button("Start New Game"):
#     # When the button is clicked, we set up the game in Streamlit's memory
#     st.session_state.start, st.session_state.end = set_difficulty(difficulty)
#     st.session_state.secret_number = random.randint(st.session_state.start, st.session_state.end)
#     st.session_state.count = 1
#     st.session_state.game_over = False
#     st.session_state.message = f"I'm thinking of a number between {st.session_state.start} and {st.session_state.end}."

# # 2. RUN THE GAME
# # Check if a game has been started
# if 'secret_number' in st.session_state and not st.session_state.game_over:
    
#     # Display the current status
#     st.write(st.session_state.message)
#     st.write(f"This is guess #{st.session_state.count}")

#     # Use a form to get the user's guess. This prevents the page from reloading on every number change.
#     with st.form(key='guess_form', clear_on_submit=True):
#         user_guess = st.number_input("Guess the number:", 
#                                      min_value=st.session_state.start, 
#                                      max_value=st.session_state.end, 
#                                      step=1)
#         submit_button = st.form_submit_button(label='Submit')

#     if submit_button:
#         # When the user clicks "Submit", run the game logic
#         message, game_over = game_logic(user_guess, st.session_state.secret_number, st.session_state.count)
        
#         # Update the game state based on the logic's result
#         st.session_state.message = message
#         st.session_state.game_over = game_over
#         st.session_state.count += 1

#         # Rerun the script to show the updated message
#         st.rerun()

# # Display final messages after the game is over
# if 'game_over' in st.session_state and st.session_state.game_over:
#     # Check if the message contains "Well Done" to show a success message
#     if "Well Done" in st.session_state.message:
#         st.success(st.session_state.message)
#         st.balloons()
#     else:
#         st.error(st.session_state.message)

# st.info("To play, choose a difficulty and click 'Start New Game'.")

import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state variables
if "start" not in st.session_state:
    st.session_state.start = None
if "end" not in st.session_state:
    st.session_state.end = None
if "system_choice" not in st.session_state:
    st.session_state.system_choice = None
if "count" not in st.session_state:
    st.session_state.count = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.write("Welcome to the Number Guessing Game!")

# Difficulty selection
difficulty = st.selectbox("Choose Difficulty", ["Easy", "Medium", "Hard"])

if st.button("Set Difficulty"):
    if difficulty == "Easy":
        st.session_state.start, st.session_state.end = 1, 3
    elif difficulty == "Medium":
        st.session_state.start, st.session_state.end = 1, 10
    else:
        st.session_state.start, st.session_state.end = 1, 50

    # System picks number
    st.session_state.system_choice = random.randint(st.session_state.start, st.session_state.end)
    st.session_state.count = 0
    st.session_state.game_over = False
    st.success(f"Difficulty set to {difficulty}. Start guessing!")

# Game input only if difficulty set
if st.session_state.start is not None and not st.session_state.game_over:
    user_choice = st.number_input(f"Enter a number between {st.session_state.start} and {st.session_state.end}",
                                  min_value=st.session_state.start,
                                  max_value=st.session_state.end,
                                  step=1)

    if st.button("Guess"):
        st.session_state.count += 1
        if user_choice == st.session_state.system_choice:
            st.success(f"🎉 Well Done! You guessed it in {st.session_state.count} tries.")
            st.session_state.game_over = True
        elif st.session_state.count >= 10:
            st.error(f"❌ Limit Exceeded. The number was {st.session_state.system_choice}")
            st.session_state.game_over = True
        elif user_choice < st.session_state.system_choice:
            st.warning("Wrong guess. Try something greater!")
        else:
            st.warning("Wrong guess. Try something smaller!")

# Reset button
if st.button("Restart Game"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()
