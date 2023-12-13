from latex.latex import LaTeX
import os


class Book:
    name: str = ""
    author: str = ""
    page_number: str = ""

    def __init__(self, name: str, author: str, page_number: str):
        self.name = name
        self.author = author
        self.page_number = page_number


def read_books_from_file(file_path: str) -> (int, list[Book]):
    with open(file_path, "rb") as file:
        buffer = file.read().decode("utf-8")

        result = buffer.split("\r\n\r\n")

        year = result[0]
        content = result[1]

        content = content.split("\r\n")
        books = [
            Book(b.split(";")[0], b.split(";")[1], b.split(";")[2]) for b in content
        ]

        return (year, books)


def main():
    latex = LaTeX()

    latex.set_document_class("article")
    latex.set_document_class_options(["a4paper", "twoside"])
    latex.set_title("Lista de Livros Lidos")
    latex.set_author("Gustavo Azevedo Naldoni")

    latex.document_class()
    latex.input("packages.tex")
    latex.use_package("babel", ["brazil"])
    latex.title()
    latex.author()

    latex.begin_document()

    latex.page_style("fancy")
    latex.generic_command(r"\fancyhead{}")
    latex.generic_command(r"\fancyhead[RO,LE]{Lista de livros lidos}")
    latex.generic_command(r"\fancyfoot{}")
    latex.generic_command(r"\fancyfoot[LE,RO]{Página \thepage}")
    latex.generic_command(
        r"\fancyfoot[LO,CE]{\copyright \hspace{0.10cm} Gustavo Azevedo Naldoni}"
    )

    latex.make_title()
    latex.table_of_contents()
    latex.new_page()

    year, books = read_books_from_file("./examples/books/books.txt")

    latex.section(f"{year}")

    total_pages = 0

    latex.begin_enumerate()

    for book in books:
        latex.item(f"\emph{{{book.name}}} - {book.author} - {book.page_number} páginas")
        total_pages += int(book.page_number)

    latex.end_enumerate()

    latex.begin_center()
    latex.generic_command(f"\\textbf{{Total de páginas: {total_pages}}}")
    latex.end_center()

    latex.end_document()

    latex.save_pdf_file("./examples/books/books.tex", "./examples/books")


if __name__ == "__main__":
    main()
