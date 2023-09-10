[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# 🔘 RadioButtonGroup Plugin

![Please enter a title_-002](https://github.com/Wendy-Nam/RenPy-RadioButtonGroup/assets/142412339/2da54730-984e-4166-ab0f-fa567d2dbaee)

The RadioButtonGroup plugin provides a convenient way to create and manage groups of radio buttons with both text and image options in Ren'Py. This README file will guide you through the process of setting up and using the RadioButtonGroup plugin in your Ren'Py project.

## Introduction

The RadioButtonGroup plugin serves as a powerful solution for scenarios where you need to allow users to select multiple options within a single screen, overcoming limitations presented by the standard 'menu' syntax. This plugin empowers you to create option selectors using both text buttons and image buttons, enhancing user engagement and interaction within your Ren'Py visual novel.

![screenrecord](https://github.com/Wendy-Nam/RenPy-RadioButtonGroup/assets/142412339/640033d4-a66d-4ab9-9acd-31c59bdfbe71)

## Installation

1. <b>Clone the Repository:</b>
   Clone this repository and copy the `radio_buttons.rpy` file into your Ren'Py project directory.

2. <b>Image Resources (Optional):</b>
   If you plan to use image options, make sure to place your image files in a directory accessible to your Ren'Py project, and update the image paths in the examples accordingly.

## Usage

### Using Text Options

1.  <b>Create a RadioButtonGroup Object:</b>

    In your Ren'Py script, create a list of text options for your radio button group:

    ```renpy
    $ text_list = ["Option 1", "Option 2", "Option 3"]
    $ tbtn = RadioButtonGroup(text_list)
    ```

2.  <b>Call the Screen:</b>

    Call the appropriate screen for text options, passing the RadioButtonGroup object and the `max_choice` parameter:

    ```renpy
    "Select up to 2 options:"
    $ renpy.call_screen('radio_text_buttons', tbtn, max_choice=2)
    ```

3.  <b>Retrieve Selected Values:</b>

    After the screen is closed, retrieve the selected values from the RadioButtonGroup object:

    ```renpy
    $ res = tbtn.get_selected_values()
    "You selected [res] from the text options."
    ```

### Using Image Options

1.  <b>Create a RadioButtonGroup Object:</b>

    Similarly, create a list of image paths for your radio button group:

     ```renpy
     $ image_list = ["images/poker1.png", "images/poker2.png", "images/poker3.png", "images/poker4.png"]
     $ tbtn = RadioButtonGroup(image_list)
     ```

2.  <b>Call the Screen:</b>

    Call the screen for image options, providing the RadioButtonGroup object and the `max_choice` parameter:

    ```renpy
    "Select up to 1 option:"
    $ renpy.call_screen('radio_image_buttons', tbtn, max_choice=1)
    ```

3.  <b>Retrieve Selected Value:</b>

     Retrieve the selected values from the RadioButtonGroup object once the screen is closed:

     ```renpy
     $ res = tbtn.get_selected_values()
     "You selected [res] from the image options"

     ```

### Adding Actions to the buttons

1.  <b>Create a RadioButtonGroup Object with Actions:</b>

    Create a list of text options and corresponding actions for your radio button group:

    ```renpy
    $ text_list = ["Option 1", "Option 2", "Option 3"]
    $ text_actions = [ToggleScreen('option1_screen'), ToggleScreen('option2_screen'), ToggleScreen('option3_screen')]
    $ tbtn2 = RadioButtonGroup(text_list, text_actions)
    ```

2.  <b>Call the Screen:</b>

    Call the screen for text options with associated actions, passing the RadioButtonGroup object and the `max_choice` parameter:

    ```renpy
    "Select up to 2 options:"
    $ renpy.call_screen('radio_text_buttons', tbtn2, max_choice=2)
    ```

3.  <b>Retrieve Selected Values:</b>

    After the screen is closed, retrieve the selected values from the RadioButtonGroup object:

    ```renpy
    $ res = tbtn2.get_selected_values()
    "You selected [res] from the text options."
    ```

## Future Plans

This plugin is currently under development, with plans to incorporate additional features and improvements in the near future. As part of these enhancements, the plugin aims to offer increased customization options, streamlined integration with various Ren'Py projects, and improved user experience.

## License

This project is licensed under the ` MIT License`. You are free to use, modify, and distribute this code for both commercial and non-commercial purposes. Refer to the `LICENSE` file for more information.

Feel free to contribute to the project by submitting issues or pull requests on the `GitHub repository`. Your contributions are highly appreciated!

For questions, concerns, or further assistance, please contact 42.4.senam@gmail.com
