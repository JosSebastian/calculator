import customtkinter as ctk
import darkdetect as dd

import sympy as sp

from components import *
from settings import *


class Calculator(ctk.CTk):
    def __init__(self, mode):
        # CALL THE PARENT CLASS CONSTRUCTOR
        super().__init__(fg_color=(APP_COLORS["white"], APP_COLORS["black"]))

        # SET APPEARANCE MODE
        ctk.set_appearance_mode(mode)

        # SET WINDOW SIZE AND PREVENT RESIZING
        self.geometry(APP_SIZE)
        self.resizable(False, False)

        # CONFIGURE PADDING AND LAYOUT
        self.configure(padx=3, pady=3)
        self.rowconfigure(list(range(APP_LAYOUT_ROWS)), weight=1, uniform="a")
        self.columnconfigure(list(range(APP_LAYOUT_COLUMNS)), weight=1, uniform="a")

        # CREATE FONTS WITH DIFFERENT SIZES
        self.smfont = ctk.CTkFont(family=APP_FONT_STYLE, size=APP_FONT_SIZE["small"])
        self.mdfont = ctk.CTkFont(family=APP_FONT_STYLE, size=APP_FONT_SIZE["medium"])
        self.lgfont = ctk.CTkFont(family=APP_FONT_STYLE, size=APP_FONT_SIZE["large"])

        # SET THE WINDOW TITLE AND INITIALIZE ATTRIBUTES
        self.title("")
        self.expression = []
        self.inverse = False
        self.angle = "RAD"

        # CREATE STRINGVAR VARIABLES FOR EQUATION AND SOLUTION
        self.equation = ctk.StringVar(value="")
        self.solution = ctk.StringVar(value="")

        # CALL INITIALIZATION AND MAIN FUNCTIONS
        self.initalize()
        self.main()

    def initalize(self):
        self.outputs = {
            "equation": EquationOutput(
                self,
                row=APP_OUTPUTS["equation"]["row"],
                col=APP_OUTPUTS["equation"]["col"],
                span=APP_OUTPUTS["equation"]["span"],
                text=self.equation,
            ),
            "solution": SolutionOutput(
                self,
                row=APP_OUTPUTS["solution"]["row"],
                col=APP_OUTPUTS["solution"]["col"],
                span=APP_OUTPUTS["solution"]["span"],
                text=self.solution,
            ),
        }
        self.inputs = {
            "utilities": {
                "inverse": UtilityInput(
                    self,
                    row=APP_INPUTS["utilities"]["inverse"]["row"],
                    col=APP_INPUTS["utilities"]["inverse"]["col"],
                    span=APP_INPUTS["utilities"]["inverse"]["span"],
                    text=APP_INPUTS["utilities"]["inverse"]["character"],
                    function=lambda: self.utility_inverse(),
                ),
                "angle": UtilityInput(
                    self,
                    row=APP_INPUTS["utilities"]["angle"]["row"],
                    col=APP_INPUTS["utilities"]["angle"]["col"],
                    span=APP_INPUTS["utilities"]["angle"]["span"],
                    text=APP_INPUTS["utilities"]["angle"]["character"],
                    function=lambda: self.utility_angle(),
                ),
                "clear_entry": UtilityInput(
                    self,
                    row=APP_INPUTS["utilities"]["clear_entry"]["row"],
                    col=APP_INPUTS["utilities"]["clear_entry"]["col"],
                    span=APP_INPUTS["utilities"]["clear_entry"]["span"],
                    text=APP_INPUTS["utilities"]["clear_entry"]["character"],
                    function=lambda: self.utility_clear_entry(),
                ),
                "clear_entries": UtilityInput(
                    self,
                    row=APP_INPUTS["utilities"]["clear_entries"]["row"],
                    col=APP_INPUTS["utilities"]["clear_entries"]["col"],
                    span=APP_INPUTS["utilities"]["clear_entries"]["span"],
                    text=APP_INPUTS["utilities"]["clear_entries"]["character"],
                    function=lambda: self.utility_clear_entries(),
                ),
                "open_parenthesis": UtilityInput(
                    self,
                    row=APP_INPUTS["utilities"]["open_parenthesis"]["row"],
                    col=APP_INPUTS["utilities"]["open_parenthesis"]["col"],
                    span=APP_INPUTS["utilities"]["open_parenthesis"]["span"],
                    text=APP_INPUTS["utilities"]["open_parenthesis"]["character"],
                    function=lambda: self.utility_parenthesis("open"),
                ),
                "close_parenthesis": UtilityInput(
                    self,
                    row=APP_INPUTS["utilities"]["close_parenthesis"]["row"],
                    col=APP_INPUTS["utilities"]["close_parenthesis"]["col"],
                    span=APP_INPUTS["utilities"]["close_parenthesis"]["span"],
                    text=APP_INPUTS["utilities"]["close_parenthesis"]["character"],
                    function=lambda: self.utility_parenthesis("close"),
                ),
                "invert": UtilityInput(
                    self,
                    row=APP_INPUTS["utilities"]["invert"]["row"],
                    col=APP_INPUTS["utilities"]["invert"]["col"],
                    span=APP_INPUTS["utilities"]["invert"]["span"],
                    text=APP_INPUTS["utilities"]["invert"]["character"],
                    function=lambda: self.utility_invert(),
                ),
            },
            "numbers": {
                "0": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["0"]["row"],
                    col=APP_INPUTS["numbers"]["0"]["col"],
                    span=APP_INPUTS["numbers"]["0"]["span"],
                    text=APP_INPUTS["numbers"]["0"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["0"]["character"]
                    ),
                ),
                "1": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["1"]["row"],
                    col=APP_INPUTS["numbers"]["1"]["col"],
                    span=APP_INPUTS["numbers"]["1"]["span"],
                    text=APP_INPUTS["numbers"]["1"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["1"]["character"]
                    ),
                ),
                "2": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["2"]["row"],
                    col=APP_INPUTS["numbers"]["2"]["col"],
                    span=APP_INPUTS["numbers"]["2"]["span"],
                    text=APP_INPUTS["numbers"]["2"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["2"]["character"]
                    ),
                ),
                "3": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["3"]["row"],
                    col=APP_INPUTS["numbers"]["3"]["col"],
                    span=APP_INPUTS["numbers"]["3"]["span"],
                    text=APP_INPUTS["numbers"]["3"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["3"]["character"]
                    ),
                ),
                "4": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["4"]["row"],
                    col=APP_INPUTS["numbers"]["4"]["col"],
                    span=APP_INPUTS["numbers"]["4"]["span"],
                    text=APP_INPUTS["numbers"]["4"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["4"]["character"]
                    ),
                ),
                "5": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["5"]["row"],
                    col=APP_INPUTS["numbers"]["5"]["col"],
                    span=APP_INPUTS["numbers"]["5"]["span"],
                    text=APP_INPUTS["numbers"]["5"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["5"]["character"]
                    ),
                ),
                "6": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["6"]["row"],
                    col=APP_INPUTS["numbers"]["6"]["col"],
                    span=APP_INPUTS["numbers"]["6"]["span"],
                    text=APP_INPUTS["numbers"]["6"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["6"]["character"]
                    ),
                ),
                "7": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["7"]["row"],
                    col=APP_INPUTS["numbers"]["7"]["col"],
                    span=APP_INPUTS["numbers"]["7"]["span"],
                    text=APP_INPUTS["numbers"]["7"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["7"]["character"]
                    ),
                ),
                "8": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["8"]["row"],
                    col=APP_INPUTS["numbers"]["8"]["col"],
                    span=APP_INPUTS["numbers"]["8"]["span"],
                    text=APP_INPUTS["numbers"]["8"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["8"]["character"]
                    ),
                ),
                "9": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["9"]["row"],
                    col=APP_INPUTS["numbers"]["9"]["col"],
                    span=APP_INPUTS["numbers"]["9"]["span"],
                    text=APP_INPUTS["numbers"]["9"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["9"]["character"]
                    ),
                ),
                ".": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["."]["row"],
                    col=APP_INPUTS["numbers"]["."]["col"],
                    span=APP_INPUTS["numbers"]["."]["span"],
                    text=APP_INPUTS["numbers"]["."]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["."]["character"]
                    ),
                ),
                "pi": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["pi"]["row"],
                    col=APP_INPUTS["numbers"]["pi"]["col"],
                    span=APP_INPUTS["numbers"]["pi"]["span"],
                    text=APP_INPUTS["numbers"]["pi"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["pi"]["operator"]
                    ),
                ),
                "i": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["i"]["row"],
                    col=APP_INPUTS["numbers"]["i"]["col"],
                    span=APP_INPUTS["numbers"]["i"]["span"],
                    text=APP_INPUTS["numbers"]["i"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["i"]["operator"]
                    ),
                ),
                "e": NumberInput(
                    self,
                    row=APP_INPUTS["numbers"]["e"]["row"],
                    col=APP_INPUTS["numbers"]["e"]["col"],
                    span=APP_INPUTS["numbers"]["e"]["span"],
                    text=APP_INPUTS["numbers"]["e"]["character"],
                    function=lambda: self.number_input(
                        APP_INPUTS["numbers"]["e"]["operator"]
                    ),
                ),
            },
            "operators": {
                "log": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["log"]["row"],
                    col=APP_INPUTS["operators"]["log"]["col"],
                    span=APP_INPUTS["operators"]["log"]["span"],
                    text=APP_INPUTS["operators"]["log"]["character"],
                    function=lambda: self.operator_input("log"),
                ),
                "exp": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["exp"]["row"],
                    col=APP_INPUTS["operators"]["exp"]["col"],
                    span=APP_INPUTS["operators"]["exp"]["span"],
                    text=APP_INPUTS["operators"]["exp"]["character"],
                    function=lambda: self.operator_input("exp"),
                ),
                "div": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["div"]["row"],
                    col=APP_INPUTS["operators"]["div"]["col"],
                    span=APP_INPUTS["operators"]["div"]["span"],
                    text=APP_INPUTS["operators"]["div"]["character"],
                    function=lambda: self.operator_input("div"),
                ),
                "mul": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["mul"]["row"],
                    col=APP_INPUTS["operators"]["mul"]["col"],
                    span=APP_INPUTS["operators"]["mul"]["span"],
                    text=APP_INPUTS["operators"]["mul"]["character"],
                    function=lambda: self.operator_input("mul"),
                ),
                "sub": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["sub"]["row"],
                    col=APP_INPUTS["operators"]["sub"]["col"],
                    span=APP_INPUTS["operators"]["sub"]["span"],
                    text=APP_INPUTS["operators"]["sub"]["character"],
                    function=lambda: self.operator_input("sub"),
                ),
                "add": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["add"]["row"],
                    col=APP_INPUTS["operators"]["add"]["col"],
                    span=APP_INPUTS["operators"]["add"]["span"],
                    text=APP_INPUTS["operators"]["add"]["character"],
                    function=lambda: self.operator_input("add"),
                ),
                "equ": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["equ"]["row"],
                    col=APP_INPUTS["operators"]["equ"]["col"],
                    span=APP_INPUTS["operators"]["equ"]["span"],
                    text=APP_INPUTS["operators"]["equ"]["character"],
                    function=lambda: self.operator_input("equ"),
                ),
                "sin": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["sin"]["row"],
                    col=APP_INPUTS["operators"]["sin"]["col"],
                    span=APP_INPUTS["operators"]["sin"]["span"],
                    text=APP_INPUTS["operators"]["sin"]["character"],
                    function=lambda: self.operator_input("sin"),
                ),
                "cos": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["cos"]["row"],
                    col=APP_INPUTS["operators"]["cos"]["col"],
                    span=APP_INPUTS["operators"]["cos"]["span"],
                    text=APP_INPUTS["operators"]["cos"]["character"],
                    function=lambda: self.operator_input("cos"),
                ),
                "tan": OperatorInput(
                    self,
                    row=APP_INPUTS["operators"]["tan"]["row"],
                    col=APP_INPUTS["operators"]["tan"]["col"],
                    span=APP_INPUTS["operators"]["tan"]["span"],
                    text=APP_INPUTS["operators"]["tan"]["character"],
                    function=lambda: self.operator_input("tan"),
                ),
            },
        }

    def main(self):
        self.mainloop()

    # UTILITY FUNCTIONS

    def utility_inverse(self):
        if self.inverse:
            self.inputs["operators"]["sin"] = OperatorInput(
                self,
                row=APP_INPUTS["operators"]["sin"]["row"],
                col=APP_INPUTS["operators"]["sin"]["col"],
                span=APP_INPUTS["operators"]["sin"]["span"],
                text=APP_INPUTS["operators"]["sin"]["character"],
                function=lambda: self.operator_input("sin"),
            )
            self.inputs["operators"]["cos"] = OperatorInput(
                self,
                row=APP_INPUTS["operators"]["cos"]["row"],
                col=APP_INPUTS["operators"]["cos"]["col"],
                span=APP_INPUTS["operators"]["cos"]["span"],
                text=APP_INPUTS["operators"]["cos"]["character"],
                function=lambda: self.operator_input("cos"),
            )
            self.inputs["operators"]["tan"] = OperatorInput(
                self,
                row=APP_INPUTS["operators"]["tan"]["row"],
                col=APP_INPUTS["operators"]["tan"]["col"],
                span=APP_INPUTS["operators"]["tan"]["span"],
                text=APP_INPUTS["operators"]["tan"]["character"],
                function=lambda: self.operator_input("tan"),
            )
        else:
            self.inputs["operators"]["sin"] = OperatorInput(
                self,
                row=APP_INPUTS["operators"]["asin"]["row"],
                col=APP_INPUTS["operators"]["asin"]["col"],
                span=APP_INPUTS["operators"]["asin"]["span"],
                text=APP_INPUTS["operators"]["asin"]["character"],
                function=lambda: self.operator_input("asin"),
            )
            self.inputs["operators"]["cos"] = OperatorInput(
                self,
                row=APP_INPUTS["operators"]["acos"]["row"],
                col=APP_INPUTS["operators"]["acos"]["col"],
                span=APP_INPUTS["operators"]["acos"]["span"],
                text=APP_INPUTS["operators"]["acos"]["character"],
                function=lambda: self.operator_input("acos"),
            )
            self.inputs["operators"]["tan"] = OperatorInput(
                self,
                row=APP_INPUTS["operators"]["atan"]["row"],
                col=APP_INPUTS["operators"]["atan"]["col"],
                span=APP_INPUTS["operators"]["atan"]["span"],
                text=APP_INPUTS["operators"]["atan"]["character"],
                function=lambda: self.operator_input("atan"),
            )
        self.inverse = not self.inverse

    def utility_angle(self):
        if self.angle == "RAD":
            self.angle = "DEG"
            self.inputs["utilities"]["angle"].configure(text="DEG")
        elif self.angle == "DEG":
            self.angle = "RAD"
            self.inputs["utilities"]["angle"].configure(text="RAD")

    def utility_clear_entry(self):
        if not self.expression:
            return
        self.expression.pop()
        self.auxiliary_generate()
        self.auxiliary_evaluate()

    def utility_clear_entries(self):
        self.expression = []
        self.equation.set("")
        self.solution.set("")

    def utility_parenthesis(self, parenthesis):
        if parenthesis == "open":
            last_element = self.expression[-1] if self.expression else None
            if last_element and self.auxiliary_number(last_element):
                self.expression.append("*")
            self.expression.append("(")
        elif parenthesis == "close":
            self.expression.append(")")

        self.auxiliary_generate()
        self.auxiliary_evaluate()
        print(self.expression)

    def utility_invert(self):
        if not self.expression:
            return
        first_last_element = self.expression[-1]
        second_last_element = self.expression[-2] if len(self.expression) > 1 else None
        try:
            if self.auxiliary_number(first_last_element):
                self.expression[-1] = str(float(first_last_element) * -1)
        except Exception:
            if (
                self.auxiliary_constant(first_last_element)
                and second_last_element == "-"
            ):
                self.expression.pop()
                self.expression.pop()
                self.expression.append(first_last_element)
            elif self.auxiliary_constant(first_last_element):
                self.expression.pop()
                self.expression.append("-")
                self.expression.append(first_last_element)
        self.auxiliary_generate()
        self.auxiliary_evaluate()

    # NUMBER FUNCTIONS

    def number_input(self, number):
        # CHECK IF EXPRESSION IS EMPTY
        if not self.expression:
            self.expression.append(number)
        else:
            last_element = self.expression[-1]
            # CHECK IF LAST ELEMENT IS A NUMERIC VALUE AND NUMBER IS A SPECIAL CONSTANT
            if self.auxiliary_number(last_element) and self.auxiliary_constant(number):
                self.expression.append("*")
                self.expression.append(number)
            # CHECK IF LAST ELEMENT IS A SPECIAL CONSTANT AND NUMBER IS A NUMERIC VALUE
            elif self.auxiliary_constant(last_element) and self.auxiliary_number(
                number
            ):
                self.expression.append("*")
                self.expression.append(number)
            # CHECK IF LAST ELEMENT IS A NUMERIC VALUE
            elif self.auxiliary_number(last_element):
                self.expression[-1] += number
            else:
                self.expression.append(number)

        # UPDATE EQUATION DISPLAY WITH NUMBER CHARACTER
        self.auxiliary_generate()
        self.auxiliary_evaluate()
        print(self.expression)

    # OPERATOR FUNCTIONS

    def operator_input(self, operator):
        # CHECK IF THE OPERATOR IS EQUALS
        if operator == "equ":
            self.auxiliary_evaluate()
            self.equation.set(self.solution.get())
            self.expression = [self.equation.get()]
            self.solution.set("")
            return

        # CHECK IF THE OPERATOR IS UNARY
        if operator in APP_INPUTS["operators"]["unary"]:
            # APPEND UNARY OPERATOR TO EXPRESSION
            last_element = self.expression[-1] if self.expression else None
            if self.auxiliary_number(last_element):
                self.expression.append("*")
            self.expression.append(APP_INPUTS["operators"][operator]["operator"])
            self.expression.append("(")
        # CHECK IF THE OPERATOR IS BINARY
        elif operator in APP_INPUTS["operators"]["binary"]:
            # GET LAST ELEMENT FROM EXPRESSION
            last_element = self.expression[-1] if self.expression else None
            # CHECK IF LAST ELEMENT IS A NUMERIC VALUE DIGIT OR SPECIAL CONSTANTS
            if last_element and (self.auxiliary_number(last_element)):
                # APPEND BINARY OPERATOR TO EXPRESSION
                self.expression.append(APP_INPUTS["operators"][operator]["operator"])
            elif last_element and last_element in {"(", ")"}:
                # APPEND BINARY OPERATOR TO EXPRESSION
                self.expression.append(APP_INPUTS["operators"][operator]["operator"])

        self.auxiliary_generate()
        self.auxiliary_evaluate()
        print(self.expression)

    # AUXILIARY FUNCTIONS

    def auxiliary_number(self, number):
        if not number:
            return False

        try:
            float(number)
            return True
        except ValueError:
            if self.auxiliary_constant(number):
                return True
            else:
                return False

    def auxiliary_constant(self, constant):
        if constant in {"pi", "I", "E"}:
            return True
        else:
            return False

    def auxiliary_generate(self):
        self.equation.set("")
        for element in self.expression:
            if element == APP_INPUTS["operators"]["log"]["operator"]:
                element = APP_INPUTS["operators"]["log"]["character"]
            elif element == APP_INPUTS["operators"]["exp"]["operator"]:
                element = APP_INPUTS["operators"]["exp"]["character"]
            elif element == APP_INPUTS["operators"]["div"]["operator"]:
                element = APP_INPUTS["operators"]["div"]["character"]
            elif element == APP_INPUTS["operators"]["mul"]["operator"]:
                element = APP_INPUTS["operators"]["mul"]["character"]
            elif element == APP_INPUTS["operators"]["sub"]["operator"]:
                element = APP_INPUTS["operators"]["sub"]["character"]
            elif element == APP_INPUTS["operators"]["add"]["operator"]:
                element = APP_INPUTS["operators"]["add"]["character"]
            elif element == APP_INPUTS["operators"]["sin"]["operator"]:
                element = APP_INPUTS["operators"]["sin"]["character"]
            elif element == APP_INPUTS["operators"]["cos"]["operator"]:
                element = APP_INPUTS["operators"]["cos"]["character"]
            elif element == APP_INPUTS["operators"]["tan"]["operator"]:
                element = APP_INPUTS["operators"]["tan"]["character"]
            elif element == APP_INPUTS["operators"]["asin"]["operator"]:
                element = APP_INPUTS["operators"]["asin"]["character"]
            elif element == APP_INPUTS["operators"]["acos"]["operator"]:
                element = APP_INPUTS["operators"]["acos"]["character"]
            elif element == APP_INPUTS["operators"]["atan"]["operator"]:
                element = APP_INPUTS["operators"]["atan"]["character"]
            elif element == APP_INPUTS["numbers"]["pi"]["operator"]:
                element = APP_INPUTS["numbers"]["pi"]["character"]
            elif element == APP_INPUTS["numbers"]["i"]["operator"]:
                element = APP_INPUTS["numbers"]["i"]["character"]
            elif element == APP_INPUTS["numbers"]["e"]["operator"]:
                element = APP_INPUTS["numbers"]["e"]["character"]
            self.equation.set(self.equation.get() + element)

    def auxiliary_evaluate(self):
        try:
            expression = "".join(self.expression)
            print(expression)
            self.solution.set(str(float(sp.sympify(expression).evalf())))
        except Exception as e:
            print(e)
            self.solution.set("Error")


if __name__ == "__main__":
    mode = "dark" if dd.isDark() else "light"
    calculator = Calculator(mode)
