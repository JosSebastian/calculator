APP_SIZE_WIDTH = 375
APP_SIZE_HEIGHT = 625
APP_SIZE = f"{APP_SIZE_WIDTH}x{APP_SIZE_HEIGHT}"

APP_LAYOUT_COLUMNS = 4
APP_LAYOUT_ROWS = 10

APP_FONT_STYLE = "Microsoft YaHei"
APP_FONT_SIZE = {
    "small": 18,
    "medium": 27,
    "large": 36,
}

APP_COLORS = {
    "white": "#f3f3f3",
    "black": "#202020",
    "light_gray": {
        "fg": ("#d4d4d2", "#505050"),
        "hover": ("#686868", "#686868"),
        "text": ("#202020", "#f3f3f3"),
    },
    "dark_gray": {
        "fg": ("#3a3a3a", "#f3f3f3"),
        "hover": ("#202020", "#686868"),
        "text": ("#f3f3f3", "#202020"),
    },
    "orange": {
        "fg": ("#ff8000", "#ff9d00"),
        "hover": ("#ff9d00", "#ff8000"),
        "text": ("#202020", "#f3f3f3"),
    },
    "orange_highlight": {
        "fg": ("#ffcc00", "#202020"),
        "hover": ("#ffa000", "#202020"),
        "text": ("#202020", "#f3f3f3"),
    },
}

APP_OUTPUTS = {
    "equation": {"row": 0, "col": 0, "span": 4},
    "solution": {"row": 1, "col": 0, "span": 4},
}

APP_INPUTS = {
    "utilities": {
        "inverse": {"row": 2, "col": 0, "span": 1, "character": "INV"},
        "angle": {"row": 2, "col": 1, "span": 1, "character": "RAD"},
        "absolute_value": {"row": 2, "col": 1, "span": 1, "character": "| |"},
        "clear_entry": {"row": 2, "col": 2, "span": 1, "character": "CE"},
        "clear_entries": {"row": 2, "col": 3, "span": 1, "character": "C"},
        "open_parenthesis": {"row": 3, "col": 0, "span": 1, "character": "("},
        "close_parenthesis": {"row": 3, "col": 1, "span": 1, "character": ")"},
        "invert": {"row": 3, "col": 2, "span": 1, "character": "±"},
    },
    "numbers": {
        "0": {"row": 9, "col": 0, "span": 2, "character": "0"},
        ".": {"row": 9, "col": 2, "span": 1, "character": "."},
        "1": {"row": 8, "col": 0, "span": 1, "character": "1"},
        "2": {"row": 8, "col": 1, "span": 1, "character": "2"},
        "3": {"row": 8, "col": 2, "span": 1, "character": "3"},
        "4": {"row": 7, "col": 0, "span": 1, "character": "4"},
        "5": {"row": 7, "col": 1, "span": 1, "character": "5"},
        "6": {"row": 7, "col": 2, "span": 1, "character": "6"},
        "7": {"row": 6, "col": 0, "span": 1, "character": "7"},
        "8": {"row": 6, "col": 1, "span": 1, "character": "8"},
        "9": {"row": 6, "col": 2, "span": 1, "character": "9"},
        "pi": {"row": 5, "col": 0, "span": 1, "character": "π", "operator": "pi"},
        "i": {"row": 5, "col": 1, "span": 1, "character": "i", "operator": "I"},
        "e": {"row": 5, "col": 2, "span": 1, "character": "e", "operator": "E"},
    },
    "operators": {
        "unary": ["log", "sin", "cos", "tan", "asin", "acos", "atan"],
        "binary": ["exp", "div", "mul", "sub", "add"],
        "log": {"row": 3, "col": 3, "span": 1, "character": "log", "operator": "log"},
        "exp": {"row": 4, "col": 3, "span": 1, "character": "^", "operator": "**"},
        "div": {"row": 5, "col": 3, "span": 1, "character": "÷", "operator": "/"},
        "mul": {"row": 6, "col": 3, "span": 1, "character": "x", "operator": "*"},
        "sub": {"row": 7, "col": 3, "span": 1, "character": "-", "operator": "-"},
        "add": {"row": 8, "col": 3, "span": 1, "character": "+", "operator": "+"},
        "equ": {"row": 9, "col": 3, "span": 1, "character": "=", "operator": "="},
        "sin": {"row": 4, "col": 0, "span": 1, "character": "sin", "operator": "sin"},
        "cos": {"row": 4, "col": 1, "span": 1, "character": "cos", "operator": "cos"},
        "tan": {"row": 4, "col": 2, "span": 1, "character": "tan", "operator": "tan"},
        "asin": {
            "row": 4,
            "col": 0,
            "span": 1,
            "character": "sin⁻¹",
            "operator": "asin",
        },
        "acos": {
            "row": 4,
            "col": 1,
            "span": 1,
            "character": "cos⁻¹",
            "operator": "acos",
        },
        "atan": {
            "row": 4,
            "col": 2,
            "span": 1,
            "character": "tan⁻¹",
            "operator": "atan",
        },
    },
}
