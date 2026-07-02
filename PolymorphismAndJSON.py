import json

class Book():

    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def show_info(self):
        print(f'Tên sách: {self.title}')
        print(f'Tác giả: {self.author}')

    def to_dict(self):
        return {
            "type": type(self).__name__,
            "title": self.title,
            "author": self.author
        }

class Novel(Book):

    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def show_info(self):
        print(f'Tên sách: {self.title}')
        print(f'Tác giả: {self.author}')
        print(f'Thể loại: {self.genre}')

    def to_dict(self):
        data = super().to_dict()
        data["genre"] = self.genre
        return data
        

class Comic(Book):

    def __init__(self, title, author, illustrator):
        super().__init__(title, author)
        self.illustrator = illustrator

    def show_info(self):
        print(f'Tên sách: {self.title}')
        print(f'Tác giả: {self.author}')
        print(f'Họa sĩ: {self.illustrator}')

    def to_dict(self):
        data = super().to_dict()
        data["illustrator"] = self.illustrator
        return data
    
def save_data(ten_file, dict):
    with open(ten_file, 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii= False, indent = 4)

def load_data(ten_file):
    with open(ten_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        books = []
        for item in data:
            if item["type"] == "Novel":
                book = Novel(
                    item["title"],
                    item["author"],
                    item["genre"]
                )
                books.append(book)
            elif item["type"] == "Comic":
                book = Comic(
                    item["title"],
                    item["author"],
                    item["illustrator"]
                )
                books.append(book)   

        return books

n1 = Novel("Cổ Chân Nhân", "Cổ Chân Nhân", "Huyền huyễn")
c1 = Comic("Chiêu Hồng Nguyệt", "Phạm Minh Khai", "Phạm Minh Khai")
books = [n1, c1]
books_dict = []
for book in books:
    book = book.to_dict()
    books_dict.append(book)
save_data("books.json", books_dict)

books = load_data("books.json")
for book in books:
    book = book.to_dict()
    books_dict.append(book)
print(books_dict)