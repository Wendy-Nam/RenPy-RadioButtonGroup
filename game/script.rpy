
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
    
    #### HOW TO USE WITH TEXTS ####
    
    $ text_list = ["Option 1", "Option 2", "Option 3"] # The list can contain text or image paths.
    $ tbtn = RadioButtonGroup(text_list) # Create a RadioButtonGroup object with the list of options.
    
    "Select up to 2 options:"
    
    $ renpy.call_screen('radio_text_buttons', tbtn, max_choice=2) # Call the screen 'radio_text_buttons'
    $ res = tbtn.get_selected_values() # Get the selected values from the RadioButtonGroup object, when the screen is closed.
    
    "You selected [res] from the text options."

    #### HOW TO USE WITH IMAGES ####
    
    $ image_list = ["images/poker1.png", "images/poker2.png", "images/poker3.png", "images/poker4.png"] # The list can contain text or image paths.
    $ tbtn = RadioButtonGroup(image_list) # Create a RadioButtonGroup object with the list of options.
    
    "Select up to 1 options:"
    
    $ renpy.call_screen('radio_image_buttons', tbtn, max_choice=1)
    $ res = tbtn.get_selected_values()
    
    "You selected [res] from the image options."