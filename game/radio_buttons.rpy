init python:
    class RadioButtonGroup:
        """A class to manage a group of radio buttons."""
        
        def __init__(self, options):
            """Initializes the RadioButtonGroup with given options."""
            self.selected = []
            self.options = [(idx, opt) for idx, opt in enumerate(options)]

        def set_option(self, option_id, max_choice=1):
            """Selects or deselects an option based on its ID."""
            if option_id in self.selected:
                self.selected.remove(option_id)
            else:
                if len(self.selected) >= max_choice:
                    num_to_remove = len(self.selected) - max_choice + 1
                    del self.selected[:num_to_remove]
                self.selected.append(option_id)

        def is_selected(self, option_id):
            """Checks if a given option ID is selected."""
            return option_id in self.selected
        
        def get_selected_index(self):
            """Returns the indices of selected options."""
            return sorted(self.selected)
        
        def get_selected_values(self):
            """Returns the values of selected options."""
            selection = self.get_selected_index()
            return [self.options[idx][1] for idx in selection]

screen radio_text_buttons(rb_group, max_choice=1):
    vbox:
        for option_id, option_text in rb_group.options:
            $ is_option_selected = rb_group.is_selected(option_id)
            textbutton "[option_text]" action Function(rb_group.set_option, option_id, max_choice):
                if is_option_selected:
                    text_color "#FFF000"
                else:
                    text_color "#FFFFFF"
        textbutton "Submit" action Return()

screen radio_image_buttons(rb_group, max_choice=1):
    hbox:
        for option_id, option_image in rb_group.options:
            vbox align (0.5, 0.0):
                $ is_option_selected = rb_group.is_selected(option_id)
                $ tint_factor = 1.0 if is_option_selected else 0.5
                $ tinted_image = im.MatrixColor(option_image, im.matrix.tint(tint_factor, tint_factor, tint_factor))
                imagebutton:
                    idle tinted_image
                    hover option_image
                    selected option_image
                    action Function(rb_group.set_option, option_id, max_choice)
        textbutton "Submit" action Return()
