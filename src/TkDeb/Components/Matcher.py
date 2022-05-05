class Matcher:
    def __init__(self: object) -> object:
        self.properties: dict = {
            'Tk': {'Class': '', 'Name': '', 'Manager': '', 'Geometry': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': ''},
            'Toplevel': {'Class': '', 'Name': '', 'Manager': '', 'Geometry': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': ''},
            'TLabel': {'Class': '', 'Name': '', 'Manager': '', 'Manager Config': '', 'Parent': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': '', 'Text': '', 'WrapLength': '', 'Justify': '', 'Image': '', 'Compound': '', 'Style': ''},
            'TButton': {'Class': '', 'Name': '', 'Manager': '', 'Manager Config': '', 'Parent': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': '', 'Text': '', 'Image': '', 'Compound': '', 'Style': ''},
            'TFrame': {'Class': '', 'Name': '', 'Manager': '', 'Manager Config': '', 'Parent': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': '', 'Style': ''},
            'TRadiobutton': {'Class': '', 'Name': '', 'Manager': '', 'Manager Config': '', 'Parent': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': '', 'Text': '', 'Image': '', 'Compound': '', 'Style': ''},
            'TScale': {'Class': '', 'Name': '', 'Manager': '', 'Manager Config': '', 'Parent': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': '', 'Value': '', 'Style': ''},
            'TEntry': {'Class': '', 'Name': '', 'Manager': '', 'Manager Config': '', 'Parent': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': '', 'Value': '', 'Style': ''},
            'TProgressbar': {'Class': '', 'Name': '', 'Manager': '', 'Manager Config': '', 'Parent': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': '', 'Progress': ''},
            'TCheckbutton': {'Class': '', 'Name': '', 'Manager': '', 'Manager Config': '', 'Parent': '', 'Position': '', 'Dimentions': '', 'Binds': '', 'State': '', 'Visible': '', 'Text': '', 'WrapLength': '', 'Image': '', 'Compound': '', 'Style': ''}

        }

    def get_properties(self: object, widget: object) -> dict:
        properties: dict = {
            'Class': widget.winfo_class(),
            'Name': f'{widget}',
            'Manager': widget.winfo_manager(),
            'Geometry': widget.winfo_geometry(),
            'Parent': widget.winfo_parent(),
            'Text': widget['text'] if widget.winfo_class() in ('TLabel', 'Label', 'TButton', 'Button', 'TRadiobutton') else '',
            'WrapLength': widget['wraplength'] if widget.winfo_class() in ('TLabel', 'Label') else '',
            'Position': f'X: {widget.winfo_x()} Y: {widget.winfo_y()}',
            'Dimentions': f'Width: {widget.winfo_width()} Height: {widget.winfo_height()}',
            'Binds': widget.bind(),
            'Manager Config': self.__get_manager_config(widget),
            'Value': widget.get() if widget.winfo_class() in ('TScale', 'TEntry') else '',
            'State': widget.state() if widget.winfo_class()[0] == 'T' else '',
            'Progress': widget['value'] if widget.winfo_class() in ('TProgressbar') else '',
            'Image': widget['image'] if widget.winfo_class() in ('TButton', 'TLabel', 'TRadiobutton') else '',
            'Visible': bool(widget.winfo_ismapped()),
            'Compound': widget['compound'] if widget.winfo_class() in ('TLabel', 'TButton', 'TRadiobutton') else '',
            'Justify': widget['justify'] if widget.winfo_class() in ('TLabel') else '',
            'Style': widget['style'] if widget.winfo_class() not in ('Tk', 'Toplevel') else '',
        }
        return properties

    def match(self: object, widget: object) -> dict:
        properties: dict = self.get_properties(widget)
        widget_class: str = widget.winfo_class()
        available_properties: dict = {}
        if widget_class in self.properties:
            for key in self.properties[widget_class]:
                available_properties[key] = properties[key]
            return available_properties
        else:
            available_properties['WARNING'] = f' THIS IS A LEGACY OR UNKNOWN WIDGET'
            available_properties[''] = ' PROPS BELOW =>'

            for key in widget.keys():
                available_properties[key.capitalize()] = f' {widget[key]}'
            return available_properties

    def __get_manager_config(self: object, widget: object) -> str:
        manager: str = widget.winfo_manager()
        widget_config: dict = {}
        if manager == 'pack':
            widget_config = widget.pack_info()
        elif manager == 'grid':
            widget_config = widget.grid_info()
        elif manager == 'place':
            widget_config = widget.place_info()
        config: str = ''
        for key in widget_config:
            if key == 'in' or not widget_config[key] or widget_config[key] in ('None', 'none', 0):
                continue
            config += f'{key}: {widget_config[key]} '
        if config:
            return config
        return 'Unknown'
