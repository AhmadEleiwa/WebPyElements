
class Colors:
    RED = '#ff2c2c' 
    BLUE = '#305cde'
    PINK =  "#ff8da1"
    HOT_PINK = "#ff46a2"
    YALLOW = '#ffde21'
    GOLD = '#efbf04'
    ORANGE = "#ffa500"
    NEON_ORANGE = '#ff5c00'
    BRONZE = "#ce8946"
    VOLITE = '#7f00ff'
    PURPLE = "#9d00ff"
    GREEN= "#008000"
    LIGHT_GRAY = '#d3d3d3'
    SLATE_GRAY = "#6d8196"
    JET_BLACK  ="#252525"
    BLACK = "#000000"
class Color:
    def __init__(self, hex:str="") -> None:
        self.color = hex
    def __str__(self):
        return self.color
class BorderType:
    SOLID = "solid"
    DOTTED = "dotted"
class Border:
    def __init__(self, 
                 borderSize:int = 1, 
                 borderColor:Color = Color("#000000"),
                 borderType:str=BorderType.SOLID,
              ) -> None:
        self.borderSize = borderSize
        self.borderColor = borderColor
        self.borderType = borderType
    def __str__(self):
        return f"border: {self.borderSize}px {self.borderType} {self.borderColor};"

class JustifyContent:
    SPACE_BETWEEN = {'rule': 'space-between', 'className': 'jc-between'}
    SPACE_AROUND = {'rule': 'space-around', 'className': 'jc-around'}
    START = {'rule': 'start', 'className': 'jc-start'}
    END = {'rule': 'end', 'className': 'jc-end'}
    EVENLY = {'rule': 'space-evenly', 'className': 'jc-evenly'}

class AlignItems:
    START = {'rule': 'start', 'className': 'ai-start'}
    END = {'rule': 'end', 'className': 'ai-end'}
    CENTER = {'rule': 'center', 'className': 'ai-center'}
    BASELINE = {'rule': 'baseline', 'className': 'ai-baseline'}
    STRETCH = {'rule': 'stretch', 'className': 'ai-stretch'}


class FlexBox:
    def __init__(self,justifyContent:dict = JustifyContent.SPACE_AROUND ,alignItems:dict=AlignItems.CENTER) -> None:
        self.justifyContent =justifyContent
        self.alignItems= alignItems
    def get_classNames(self):
        return f"flex {self.justifyContent['className']} {self.alignItems['className']}"
    def __str__(self):
        return f"display:flex;justify-content:{self.justifyContent['rule']}; align-items:{self.alignItems['rule']};"
        
class Style:
    def __init__(self,color:Color=None,border:Border=None,backgroundColor:Color= None) -> None:
        self.color = color
        self.border = border
        self.backgroundColor= backgroundColor

    def __str__(self):
        style= 'style="'
        if self.color:
            style+= f"color:{self.color};"
        if self.border:
            style += self.border.__str__()
        if self.backgroundColor:
            style+= f"background-color:{self.backgroundColor};"
        return style+'"'