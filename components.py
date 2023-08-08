from customtkinter import CTkLabel, CTkButton
from settings import *


# --------- Outputs --------- #
class Output(CTkLabel):
    def __init__(self, parent, text, font):
        super().__init__(master=parent, textvariable=text, font=font)
        self.grid(rowspan=1, columnspan=4, padx=5, pady=0)


class EquationOutput(Output):
    def __init__(self, parent, row, col, text, span):
        super().__init__(parent, text, font=parent.lgfont)
        self.grid(row=row, column=col, columnspan=span, sticky="w")


class SolutionOutput(Output):
    def __init__(self, parent, row, col, text, span):
        super().__init__(parent, text, font=parent.lgfont)
        self.grid(row=row, column=col, columnspan=span, sticky="W")


# --------- Inputs --------- #
class Input(CTkButton):
    def __init__(self, parent, row, col, text, function, font, color, span):
        super().__init__(
            master=parent,
            text=text,
            command=function,
            font=font,
            corner_radius=3,
            fg_color=APP_COLORS[color]["fg"],
            hover_color=APP_COLORS[color]["hover"],
            text_color=APP_COLORS[color]["text"],
        )
        self.grid(row=row, column=col, columnspan=span, sticky="news", padx=1, pady=1)


class UtilityInput(Input):
    def __init__(self, parent, row, col, span, text, function):
        super().__init__(
            parent=parent,
            row=row,
            col=col,
            span=span,
            text=text,
            function=function,
            font=parent.smfont,
            color="dark_gray",
        )


class NumberInput(Input):
    def __init__(self, parent, row, col, span, text, function):
        super().__init__(
            parent=parent,
            row=row,
            col=col,
            span=span,
            text=text,
            function=function,
            font=parent.mdfont,
            color="light_gray",
        )


class OperatorInput(Input):
    def __init__(self, parent, row, col, span, text, function):
        super().__init__(
            parent=parent,
            row=row,
            col=col,
            span=span,
            text=text,
            function=function,
            font=parent.mdfont,
            color="orange",
        )
