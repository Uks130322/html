"""Module with classes for print HTML-documents"""


class Paragraph:
    """Paragraph of HTML-document"""
    def __init__(self, text=""):
        """Creating paragraph"""
        self.p = text

    def __str__(self):
        """Print the paragraph in needed format"""
        return f"<p>\n{self.p}\n</p"


class Body(Paragraph):
    """Body of HTML-document, including paragraph"""

    def __init__(self, body_text, subelement=str(Paragraph())):
        """Creating body"""
        super().__init__()
        self.body = body_text
        self.subelement = subelement

    def __str__(self):
        """Print the body in needed format"""
        return f"<body>\n{self.body}\n{self.subelement}\n</body>"


class HTML(Body):
    """Whole HTML-document"""

    def __init__(self, subelement):
        """Creating document"""
        super().__init__(body_text="")
        self.subelement = subelement

    def __str__(self):
        """Print the body in needed format"""
        return f"<html>\n{self.subelement}\n</html>"
