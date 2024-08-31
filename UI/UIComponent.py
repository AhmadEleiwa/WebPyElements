from typing import Any
from UI.Style import Style
from typing import TypedDict
from UI.Style import *

class ClassName:
    def __init__(self, clasName) -> None:
        self.className = clasName
    def __str__(self) -> str:
        return f"class='{self.className}'"
class Property(TypedDict):
    className:ClassName
    style:Style
    width:str
    flexBox:FlexBox
class UIComponent:
    def __init__(self,component:str,voidElement:bool, child,**args) -> None:
        self.component:str  = component
        self.child  = child
        self.voidElement = voidElement
        self.props:Property = args
    def __str__(self) -> str:
        attrub  = ""
        for i in self.props.keys():
            if self.props[i]:
                attrub += self.props[i].__str__()+' '
        if not self.voidElement:
            return f'<{self.component} {attrub}>{self.child}</{self.component }>'
        return f'<{self.component} {attrub}>{self.child}/>'