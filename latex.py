class LaTeX:
    _document_class: str = "article"
    _document_class_options: list[str] = []
    _title: str = "Default LaTeX Title"
    _author: str = "Default LaTeX Author"
    _date: str = r"\today"

    _document: str = ""

    def set_document_class(self, document_class: str):
        self._document_class = document_class

    def get_document_class(self) -> str:
        return self._document_class

    def set_document_class_options(self, document_class_options: list[str]):
        self._document_class_options = document_class_options

    def get_document_class_options(self) -> list[str]:
        return self._document_class_options

    def set_title(self, title: str):
        self._title = title

    def get_title(self) -> str:
        return self._title

    def set_author(self, author: str):
        self._author = author

    def get_title(self) -> str:
        return self._title

    def set_document(self, document: str):
        self._document = document

    def get_document(self) -> str:
        return self._document

    def append_to_document(self, text: str):
        self._document += text

    def document_class(self):
        options = ", ".join(self.get_document_class_options())
        command = f"\\documentclass[{options}]{{{self._document_class}}}\n"

        self.append_to_document(command)

    def title(self):
        command = f"\\title{{{self._title}}}\n"
        self.append_to_document(command)

    def author(self):
        command = f"\\author{{{self._author}}}\n"
        self.append_to_document(command)

    def date(self):
        command = f"\\date{{{self._date}}}\n"
        self.append_to_document(command)

    def input(self, arquivo: str):
        command = f"\\input{{{arquivo}}}\n"
        self.append_to_document(command)

    def make_title(self):
        command = f"\\maketitle\n"
        self.append_to_document(command)

    def new_page(self):
        command = f"\\newpage\n"
        self.append_to_document(command)

    def table_of_contents(self):
        command = f"\\tableofcontents\n"
        self.append_to_document(command)

    def section(self, section_title: str):
        command = f"\\section{{{section_title}}}\n"
        self.append_to_document(command)

    def enumerate(self, items: list):
        command = f"\\begin{{enumerate}}\n"

        for item in items:
            command += f"\\item {item}\n"

        command += f"\\end{{enumerate}}\n"

        self.append_to_document(command)

    def begin_enumerate(self):
        command = f"\\begin{{enumerate}}\n"
        self.append_to_document(command)

    def end_enumerate(self):
        command = f"\\end{{enumerate}}\n"
        self.append_to_document(command)

    def itemize(self, items: list):
        command = f"\\begin{{itemize}}\n"

        for item in items:
            command += f"\\item {item}\n"

        command += f"\\end{{itemize}}\n"

        self.append_to_document(command)

    def begin_itemize(self):
        command = f"\\begin{{itemize}}\n"
        self.append_to_document(command)

    def end_itemize(self):
        command = f"\\end{{itemize}}\n"
        self.append_to_document(command)

    def begin_document(self):
        command = f"\\begin{{document}}\n"
        self.append_to_document(command)

    def end_document(self):
        command = f"\\end{{document}}\n"
        self.append_to_document(command)

    def begin_multicols(self, number_of_columns):
        command = f"\\begin{{multicols}}{{{number_of_columns}}}\n"
        self.append_to_document(command)

    def end_multicols(self):
        command = f"\\end{{multicols}}\n"
        self.append_to_document(command)

    def save_tex_file(self, file_path: str):
        with open(file_path, "wb") as file:
            file.write(self.get_document().encode("utf-8"))

    def save_pdf_file(self, file_path: str):
        pass
