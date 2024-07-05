from re import error
from typing import Dict
import sys


class Frame:
    DEFAULT: Dict[str, str] = {
        "horizontal": "━",
        "vertical": "┃",
        "top-left": "┏",
        "top-right": "┓",
        "bottom-left": "┗",
        "bottom-right": "┛",
        "corners": "*",
    }

    def __init__(
        self, height: int, width: int, data: str = "", style: Dict[str, str] = DEFAULT
    ) -> None:
        """Data required to create a frame, including custom styling parts"""
        self.frame_height = height
        self.frame_width = width
        self.frame_data = data
        self.style = style
        self.frame_data_list = []

    def add_data(self, text: str, row: int):
        """adds data to total list of things for display"""
        if row < self.frame_width - 2:
            self.frame_data_list.append({row: text})
        else:
            print(
                error(
                    f"Error: text too long to fit into the frame: {len(text)} recieved"
                    f", can fit text of lenght: {self.frame_width}"
                )
            )
            sys.exit(1)

    def print_gathered_data(self):
        print(self.frame_data_list)

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
    frame: Frame = Frame(height=4, width=1)
    frame.add_data(row=3, text="teksciwo")
    frame.add_data(row=1, text="chujajaja")
    frame.display_frame()
    frame.print_gathered_data()
