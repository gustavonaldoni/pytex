# from latex.latex import LaTeX

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
        
        result = buffer.split('\r\n\r\n')
        
        year = result[0]
        content = result[1]
        
        content = content.split('\r\n')
        books = [Book(b.split(';')[0], b.split(';')[1], b.split(';')[2]) for b in content]

        return (year, books)   

def main():
    year, books = read_books_from_file("./examples/books/books.txt")

if __name__ == "__main__":
    main()