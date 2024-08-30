from UI.Button import Button
from UI.Container import Container  
from UI.UIComponent  import ClassName
from UI.Style import *
from flask import Flask
from Manager import Manager
app = Flask(__name__)


print(Manager.root)
@app.route("/")
def hello_world():
    Manager.root=Container(
        flexBox=FlexBox(JustifyContent.SPACE_AROUND),
        style=Style(backgroundColor=Color(Colors.RED)),
        children=[
            Container(
                children=[
                    Button(text="hello World")
                ]
            )
        ]
            )
    
    return Manager.get_document()


