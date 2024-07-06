"""Module for creating tui frames and displaying data inside of them"""

from re import error
from typing import Dict
import sys


class Frame:
    """Class responsible for printing out tui frames using UTF-8 encoded characters"""

    DEFAULT: Dict[str, str] = {
        "horizontal": "━",
        "vertical": "┃",
        "top_left": "┏",
        "top_right": "┓",
        "bottom_left": "┗",
        "bottom_right": "┛",
    }

    def __init__(
        self, height: int, width: int, style: Dict[str, str] = DEFAULT
    ) -> None:
        """Data required to create a frame, including custom styling parts"""

        self.frame_height = height
        self.frame_width = width
        self.style = style
        self.__frame_data_text = []
        self.__frame_data_row = []

    def add_content(self, text: str, row: int, position: str = "left") -> None:
        """Add data to total list of text to display on the terminal screen"""
        if not row >= self.frame_height:
            self.__frame_data_text.append(text)
            self.__frame_data_row.append(row)
            self.position = position  # left, center, right avilable
        else:
            print(
                error(
                    f"Error: given row '{row}' for input '{text}' won't fit inside frame "
                )
            )
            sys.exit(1)

    def remove_content(self):
        """Clears all of data inside the frame"""
        self.__frame_data_text = []
        self.__frame_data_row = []

    def print_gathered_data(self) -> None:
        """Return to the user list of given input and its coresponding row"""
        for key, _ in enumerate(self.__frame_data_text):
            print(
                f"text: {self.__frame_data_text[key]} is in row: {self.__frame_data_row[key]}"
            )

    def display_frame(self) -> None:
        """Create and display frame using components from __init__"""
        if self.position == "left" or None:
            self.__left_align()

        if self.position == "center":
            self.__center()

    # row aligmnent methods
    def __left_align(self):
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

    def __center(self):
        self.__print_top_part()

        for row in range(self.frame_height):
            print(self.style["vertical"], end="")

            if row in self.__frame_data_row:
                text_index = self.__frame_data_row.index(row)
                text = self.__frame_data_text[text_index]
                padding_left = (self.frame_width - len(text)) // 2
                padding_right = self.frame_width - len(text) - padding_left
                print(" " * padding_left, end="")
                print(text, end="")
                print(" " * padding_right, end="")
                print(self.style["vertical"])
            else:
                print(" " * self.frame_width, end="")
                print(self.style["vertical"])
        self.__print_bot_part()

    # frame building components
    def __print_top_part(self) -> None:
        """display top part of the frame to the screen"""
        print(self.style["top_left"], end="")
        print(self.style["horizontal"] * self.frame_width, end="")
        print(self.style["top_right"])

    def __print_bot_part(self) -> None:
        """display bottom part of the frame on the screen"""
        print(self.style["bottom_left"], end="")
        print(self.style["horizontal"] * self.frame_width, end="")
        print(self.style["bottom_right"])

    # customize style
    def custom_style(
        self,
        horizontal: str,
        vertical: str,
        top_left: str,
        top_right: str,
        bottom_left: str,
        bottom_right: str,
        corners="",
    ):
        """Create custom style for changing view of displayed frame"""
        self.style = {
            "horizontal": horizontal,
            "vertical": vertical,
            "top_left": top_left,
            "top_right": top_right,
            "bottom_left": bottom_left,
            "bottom_right": bottom_right,
            "corners": corners,
        }

    def clear_style(self):
        """Chanegs custom made style to default one"""
        self.style = self.DEFAULT


if __name__ == "__main__":
    frame: Frame = Frame(height=4, width=10)
    frame.add_content(row=1, text="test", position="center")
    # frame.custom_style(
    #     horizontal="0",
    #     vertical="o",
    #     top_left="*",
    #     bottom_right="*",
    #     top_right="*",
    #     bottom_left="*",
    # )
    # frame.clear_style()
    frame.display_frame()
