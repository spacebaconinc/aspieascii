import random

class CartoonCharacter:
    def __init__(self):
        self.heads = [
            "  ---  ",
            " .---. ",
            " o---o ",
            " '---' ",
        ]
        
        self.eyes = [
            "| o o |",
            "| - - |",
            "| > < |",
            "| . . |",
        ]
        
        self.mouths = [
            "|  -  |",
            "|  ~  |",
            "| ___ |",
            "|     |",
        ]

        self.necks = [
            "   |   ",
            "   !   ",
            "   i   "
        ]

        self.chests = [
            " /---\\ ",
            "/-----\\",
            " \\---/ "
        ]

        self.torsos = [
            "  |-|  ",
            "  | |  ",
            "  |!|  "
        ]

        self.arms = [
            "/|   |\\",
            "\\|   |/",
            " |   | "
        ]

        self.hands = [
            " |---| ",
            " |-|-| ",
            " | | | "
        ]

        self.shoulders = [
            "/     \\",
            "\\     /",
            "       "
        ]

        self.waists = [
            "  |-|  ",
            "  |!|  ",
            "  | |  "
        ]

        self.thighs = [
            " / \\  ",
            "/   \\",
            "     "
        ]

        self.legs = [
            " | |  ",
            " |!|  ",
            " |-|  "
        ]

        self.feet = [
            " |\"|  ",
            " |'|  ",
            " |_|  "
        ]

    def generate_character(self):
        parts = [
            random.choice(self.heads),
            random.choice(self.eyes),
            random.choice(self.mouths),
            random.choice(self.necks),
            random.choice(self.chests),
            random.choice(self.torsos),
            random.choice(self.arms),
            random.choice(self.hands),
            random.choice(self.shoulders),
            random.choice(self.waists),
            random.choice(self.thighs),
            random.choice(self.legs),
            random.choice(self.feet)
        ]
        
        return "\n".join(parts)

def generate_ascii_cartoon(width, height):
    character = CartoonCharacter()
    art = "\n".join([" " * ((width - 7) // 2) + character.generate_character() for _ in range(height // 13)])
    return art

if __name__ == "__main__":
    width = int(input("Enter the width of the ASCII cartoon area: "))
    height = int(input("Enter the height of the ASCII cartoon area: "))
    print(generate_ascii_cartoon(width, height))
