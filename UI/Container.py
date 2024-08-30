from UI.UIComponent import UIComponent,ClassName
from UI.Style import Style,FlexBox
class Container(UIComponent):
    def __init__(self, children:list[UIComponent]=None,style:Style=None,className:ClassName=ClassName("div"),flexBox:FlexBox=None) -> None:
        if flexBox:
            className= ClassName(" "+flexBox.get_classNames())
        child = ""
        for ch in children:
            child += " "+ch.__str__()
        super().__init__(component = "div",voidElement=False,child=child,style=style,className=className)