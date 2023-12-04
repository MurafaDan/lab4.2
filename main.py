class WritingTool:
    def write(self):
        print("Writing tool writes.")

    def public_method(self):
        print("Public method of WritingTool.")

    def _protected_method(self):
        print("Protected method of WritingTool.")

    def __private_method(self):
        print("Private method of WritingTool.")


class Pencil(WritingTool):
    def write(self):
        print("Pencil draws.")

    def pencil_method(self):
        print("Specific method for Pencil.")


class Pen(WritingTool):
    def write(self):
        print("Pen writes.")

    def pen_method(self):
        print("Specific method for Pen.")


class GelPen(Pen):
    def write(self):
        print("Gel pen writes.")

    def gel_pen_method(self):
        print("Specific method for Gel Pen.")


def main():
    pencil = Pencil()
    pen = Pen()
    gel_pen = GelPen()

    pencil.write()
    pen.write()
    gel_pen.write()

    pencil.public_method()

if __name__ == "__main__":
    main()