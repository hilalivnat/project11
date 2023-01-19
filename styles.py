######################################################################
# FILE: styles.py
# WRITERS: Michal_Caduri, michal.caduri, 213088735
# Hila_Livnat, hilalivnat, 324862028
# EXERCISE: intro2cs1 ex11 2023
# DESCRIPTION: A program defines styles constants for the game.
######################################################################

# images:
START_SCREEN = "./assets/start_screen.png"
GAME_OVER_SCREEN = "./assets/game_over_screen.png"
BOGGLE_LOGO = "./assets/re_boggle_logo.png"
CLEAR_BUTTON = "./assets/re_clear_button.png"
YES_BUTTON = "./assets/re_yes_button.png"
NO_BUTTON = "./assets/re_no_button.png"

# colors:
TEXT_COLOR = "#052266"
DISABLED_COLOR = "#45a9ba"
BTN_BG = "#B4DDEC"
INVALID_COLOR = "#E55959"
BACKGROUND_COLOR = "#EEFBFF"
WHITE = "white"


MAIN_FRAME = {
    # "width":50, 
    # "height":50
}

DISPLAY_WORD ={
    "font":("Asimon", 15),
    "fg":TEXT_COLOR
}

BUTTON_STYLE ={
    "font":("Asimon", 15),
    "bg":BTN_BG, 
    "fg": TEXT_COLOR, 
    "width":2, 
    "height":2
}

FOUND_WORDS = {
    "font":("Asimon", 15),
    "fg":TEXT_COLOR, 
    "height":3
}

START_GAME_BTN = {
    "width":10, 
    "height":5, 
    "border": 0
}


