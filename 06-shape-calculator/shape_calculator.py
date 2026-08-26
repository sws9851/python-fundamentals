class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, new_width: int) -> None:
        self.width = new_width

    def set_height(self, new_height: int) -> None:
        self.height = new_height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape: "Rectangle") -> int:
        # floor each side separately: no rotations, and a shape that is too wide
        # fits zero times however much vertical room is left over
        return (self.height // shape.height) * (self.width // shape.width)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def set_side(self, new_side: int) -> None:
        self.width = new_side
        self.height = new_side

    def set_width(self, new_side: int) -> None:
        self.set_side(new_side)

    def set_height(self, new_side: int) -> None:
        self.set_side(new_side)

    def __repr__(self) -> str:
        return f"Square(side={self.width})"


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
