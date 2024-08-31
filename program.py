from UI.Button import Button
from UI.Container import Container  
from UI.Document import Document  
from UI.UIComponent  import ClassName, UIComponent
from UI.Style import *

from flask import Flask

app = Flask(__name__)
class App:
    def __str__(self) -> str:
        x = "Hello world"
        return Document(
        title="MyApp",
        body=Container(
        flexBox=FlexBox(JustifyContent.SPACE_BETWEEN),
        style=Style(backgroundColor=Color(Colors.RED)),
        children=[
            Container(
                flexBox=FlexBox(justifyContent=JustifyContent.SPACE_BETWEEN),
                children=[
                    Button(text=x+'1'),
                    Button(text=x+'2'),
                    Button(text=x+'3')
                ]
            )
        ]
            )
    ).__str__()
@app.route("/")
def hello_world():
    return App().__str__()



