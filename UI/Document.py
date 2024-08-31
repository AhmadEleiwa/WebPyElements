from UI import UIComponent  
class Document:
    def __init__(self, title:str ="WebPyElement", body:UIComponent = None) -> None:
        with open('src/style.d.css', 'r') as file:        
            self.head = f'''
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{title}</title>
                       <style>
                        {file.read()}
                        </style>
                </head>
            '''
        self.body = f"""
            <body>
            {body}
            </body>
        """
    def __str__(self):
        return f"""
            <!DOCTYPE html>
            <html lang="en">
                {self.head}
                {self.body}
            </html>
            """
    def __repr__(self) -> str:
        return f"""
            <!DOCTYPE html>
            <html lang="en">
                {self.head}
                {self.body}
            </html>
            """