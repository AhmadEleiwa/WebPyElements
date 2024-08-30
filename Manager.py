from UI.UIComponent import UIComponent
class Manager(object):
    root:UIComponent  =  None
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Manager, cls).__new__(cls)
        return cls.instance
    def get_document():
        with open('src/style.d.css', 'r') as file:
            return f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <style>
                {file.read()}
                </style>
            </head>
            <body>
                {Manager.root.__str__()}
            </body>
            </html>
        """