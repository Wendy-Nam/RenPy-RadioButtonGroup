
label start:
    # Example of using the RadioButtonGroup class to create a group of radio buttons.
    # Text and images can be used as options.
    # The max_choice parameter can be used to limit the number of options that can be selected.
    # The default value is 1, which means only one option can be selected.
    
    # How to use:
    # 1. Create a RadioButtonGroup object with a list of options. (The list can contain text or image paths)
    # 2. Call the screen 'radio_text_buttons' or 'radio_image_buttons' with the RadioButtonGroup object as the first parameter.
    # 3. Get the selected values from the RadioButtonGroup object.
    # 4. Use the selected values to do whatever you want. (In this example, the selected values are printed to the screen.)
    
    ### HOW TO USE WITH TEXTS ####
    
    $ text_list = ["Option 1", "Option 2", "Option 3"] # The list can contain text or image paths.
    $ tbtn = RadioButtonGroup(text_list) # Create a RadioButtonGroup object with the list of options.
    
    "Select up to 2 options:"
    
    $ renpy.call_screen('radio_text_buttons', tbtn, max_choice=2) # Call the screen 'radio_text_buttons'
    $ res = tbtn.get_selected_values() # Get the selected values from the RadioButtonGroup object, when the screen is closed.
    
    "You selected [res] from the text options."

    #### HOW TO USE WITH IMAGES ####
    
    $ image_list = ["images/poker1.png", "images/poker2.png", "images/poker3.png", "images/poker4.png"] # The list can contain text or image paths.
    $ imgbtn = RadioButtonGroup(image_list) # Create a RadioButtonGroup object with the list of options.
    
    "Select up to 1 options:"
    
    $ renpy.call_screen('radio_image_buttons', imgbtn, max_choice=2)
    $ res = imgbtn.get_selected_values()
    
    "You selected [res] from the image options."
    
    ### HOW TO USE WITH ACTIIONS ###
    
    $ text_list = ["Option 1", "Option 2", "Option 3"] # The list can contain text or image paths.
    # The list can contain actions that will be executed when the option is selected.
    $ text_actions = [ToggleScreen('poker_card1'), ToggleScreen('poker_card2'), \
        ToggleScreen('poker_card3'), ToggleScreen('poker_card4')] # The list must be the same size as the list of options. (if shorter it will be padded with NullAction)
    $ tbtn2 = RadioButtonGroup(text_list, text_actions) # Create a RadioButtonGroup object with the list of options.
    "Select up to 1 options:"
    # The screen 'radio_text_buttons' can be used with actions. also does the screen 'radio_image_buttons'.
    $ renpy.call_screen('radio_text_buttons', tbtn2, max_choice=2)
    $ res = tbtn2.get_selected_values()
    "You selected [res] from the text options."

screen poker_card1:
    image 'images/poker1.png' align (.5,.1)
    
screen poker_card2:
    image 'images/poker2.png' align (.5,.2)

screen poker_card3:
    image 'images/poker3.png' align (.5,.3)
