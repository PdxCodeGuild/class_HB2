class Reader:

    def __init__(self, book_file):
        self.book_file = book_file
        self.text = ''

    def load(self):
        """
        1) open 'file' with option 'r' for read
        2) get the text from the file
        """
        with open(self.book_file, "r") as f_read:
            self.text = f_read.read()

        return self.text

    def edit(self, new_text):
        """
        1) open file with open 'w' for write
        2) take in additional text & concat onto existing file
        3) save to the file
        """
        with open(self.book_file, "a") as f_write:
            f_write.write(new_text)

    def replace(self, new_text):
        with open(self.book_file, "w") as f_write:
            f_write.write(new_text)

    def print(self):
        """
        print the text
        """


def main():
    text = Reader('/Users/sb/Desktop/class_HB2/1 Python/docs/class_code_examples/fileIO/book.txt')  # create an instance of our class
    text.load()
    while True:
        command = input('Enter a command: ')
        if command == 'save':
            new_text = input('add new text: ')
            text.save(new_text)
        elif command == 'print':
            print('heeey')
        else:
            print('Command not recognized')


if __name__ == "__main__":
    main()