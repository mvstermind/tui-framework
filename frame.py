"""Module for creating tui frames and displaying data inside of them"""

from re import error
from typing import Dict
import sys


class Frame:
    """Class responsible for printing out tui frames using UTF-8 encoded characters"""

    DEFAULT: Dict[str, str] = {
        "horizontal": "━",
        "vertical": "┃",
        "top-left": "┏",
        "top-right": "┓",
        "bottom-left": "┗",
        "bottom-right": "┛",
    }

    def __init__(
        self, height: int, width: int, data: str = "", style: Dict[str, str] = DEFAULT
    ) -> None:
        """Data required to create a frame, including custom styling parts"""

        self.frame_height = height
        self.frame_width = width
        self.frame_data = data if data is not None else ""
        self.style = style
        self.__frame_data_text = []
        self.__frame_data_row = []

    def add_data(self, text: str, row: int, position: str = "") -> None:
        """Add data to total list of text to display on the terminal screen"""
        if row < self.frame_width - 2:
            self.__frame_data_text.append(text)
            self.__frame_data_row.append(row)
        else:
            print(
                error(
                    f"Error: text too long to fit into the frame: {len(text)} recieved"
                    f", can fit text of lenght: {self.frame_width}"
                )
            )
            sys.exit(1)

    def print_gathered_data(self) -> None:
        """Return to the user list of given input and its coresponding row"""
        for key, _ in enumerate(self.__frame_data_text):
            print(
                f"text: {self.__frame_data_text[key]} is in row: {self.__frame_data_row[key]}"
            )

    def display_frame(self) -> None:
        """Create and display frame using components from __init__"""
        self.__print_top_part()

        for row in range(self.frame_height):
            print(self.style["vertical"], end="")

            if row in self.__frame_data_row:
                text_index = self.__frame_data_row.index(row)
                text = self.__frame_data_text[text_index]
                print(text, end="")
                print(" " * (self.frame_width - len(text)), end="")
                print(self.style["vertical"])
            else:
                print(" " * (self.frame_width), end="")
                print(self.style["vertical"])

        self.__print_bot_part()

    def __print_top_part(self) -> None:
        """display top part of the frame to the screen"""
        print(self.style["top-left"], end="")
        print(self.style["horizontal"] * self.frame_width, end="")
        print(self.style["top-right"])

    def __print_bot_part(self) -> None:
        """display bottom part of the frame on the screen"""
        print(self.style["bottom-left"], end="")
        print("━" * self.frame_width, end="")
        print(self.style["bottom-right"])


if __name__ == "__main__":
    frame: Frame = Frame(height=4, width=10)
    frame.add_data(row=1, text="test")
    frame.add_data(row=2, text="test1")
    frame.display_frame()
    frame.print_gathered_data()
