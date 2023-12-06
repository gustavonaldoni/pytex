class LaTeX:
    _document_class: str = "article"
    _document_class_options: list[str] = []
    _title: str = "Default LaTeX Title"
    _author: str = "Default LaTeX Author"
    _date: str = r"\today"
    
    document: str = ""

    def set_document_class(self, new_document_class: str):
        self._document_class = new_document_class

    def get_document_class(self) -> str:
        return self._document_class

    def set_title(self, new_title: str):
        self._title = new_title

    def get_title(self) -> str:
        return self._title

    def set_author(self, new_author: str):
        self._author = new_author

    def get_title(self) -> str:
        return self._title

    def document_class(self):
        self.document += f"\\documentclass{{{self._document_class}}}\n"

    def title(self):
        self.document += f"\\title{{{self._title}}}\n"

    def author(self):
        self.document += f"\\author{{{self._author}}}\n"

    def date(self):
        self.document += f"\\date{{{self._date}}}\n"

    def input(self, arquivo: str):
        self.document += f"\\input{{{arquivo}}}\n"

    def make_title(self):
        self.document += f"\\maketitle\n"

    def new_page(self):
        self.document += f"\\newpage\n"

    def table_of_contents(self):
        self.document += f"\\tableofcontents\n"

    def section(self, section_title: str):
        self.document += f"\\section{{{section_title}}}\n"

    def enumerate(self, items: list):
        command = f"\\begin{{enumerate}}\n"

        for item in items:
            command += f"\\item {item}\n"

        command += f"\\end{{enumerate}}\n"

        self.document += command

    def begin_enumerate(self):
        self.document += f"\\begin{{enumerate}}\n"

    def end_enumerate(self):
        self.document += f"\\end{{enumerate}}\n"

    def itemize(self, items: list):
        command = f"\\begin{{itemize}}\n"

        for item in items:
            command += f"\\item {item}\n"

        command += f"\\end{{itemize}}\n"

        self.document += command

    def begin_itemize(self):
        self.document += f"\\begin{{itemize}}\n"

    def end_itemize(self):
        self.document += f"\\end{{itemize}}\n"

    def begin_document(self):
        self.document += f"\\begin{{document}}\n"

    def end_document(self):
        self.document += f"\\end{{document}}\n"

    def begin_multicols(self, number_of_columns):
        self.document += f"\\begin{{multicols}}{{{number_of_columns}}}\n"

    def end_multicols(self):
        self.document += f"\\end{{multicols}}\n"

    def save_tex_file(self, file_path: str):
        with open(file_path, "wb") as file:
            file.write(self.document.encode("utf-8"))
            
    def save_pdf_file(self, file_path: str):
        pass
