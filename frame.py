from typing import Dict


class Frame:
    STYLE: Dict[str, str] = {
        "horizontal": "━",
        "vertical": "┃",
        "top-left": "┏",
        "top-right": "┓",
        "bottom-left": "┗",
        "bottom-right": "┛",
        "corners": "*",
    }

    def __init__(
        self, height: int, width: int, data: str = "", style: Dict[str, str] = STYLE
    ) -> None:
        """Data required to create a frame, including custom styling parts"""
        self.frame_height = height
        self.frame_width = width
        self.frame_data = data
        self.style = style

    def display_frame(self):
        """Create frame using components from __init__"""
        self.__print_top_part()

        for _ in range(self.frame_height):
            print(self.style["vertical"], end="")
            for _ in range(self.frame_width):
                print(" ", end="")
            print(self.style["vertical"])

        self.__print_bot_part()

    def __print_top_part(self):
        """display top part of the frame to the screen"""
        print(self.style["top-left"], end="")
        for _ in range(self.frame_width):
            print(self.style["horizontal"], end="")
        print(self.style["top-right"])

    def __print_bot_part(self):
        """display bottom part of the frame on the screen"""
        print(self.style["bottom-left"], end="")
        for _ in range(self.frame_width):
            print("━", end="")
        print(self.style["bottom-right"])


if __name__ == "__main__":
    frame: Frame = Frame(height=4, width=10)
    frame.display_frame()
