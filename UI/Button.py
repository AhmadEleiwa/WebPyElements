from UI.UIComponent import UIComponent,ClassName
from UI.Style import Style
class Button(UIComponent):
    def __init__(self, text="",style:Style=None,className:ClassName=ClassName("btn")) -> None:
        super().__init__(component = "button",voidElement=False,child=text,style=style,className=className)