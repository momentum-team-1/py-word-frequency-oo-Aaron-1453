import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename.open()

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        contents = self.filename.read()
        return contents


class WordList:
    def __init__(self, text):
        self.text = text

    def extract_words(self):
        words = self.text.lower().split()
        return [word.strip(string.punctuation) for word in words]

    def remove_stop_words(self):
        return [
            word
            for word in self.extract_words()
            if not word in STOP_WORDS]

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        freqs = {
            # I only barely understand these lines and why they work##
            word: self.remove_stop_words().count(word)
            for word in self.remove_stop_words()
        }
        alpha_freqs = dict(sorted(freqs.items()))
        return dict(sorted(alpha_freqs.items(), key=lambda seq: seq[1], reverse=True))


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        top_ten = []

        """
       Prints out a frequency chart of the top 10 items
       in our frequencies data structure.
       Example:
         her | 33   *********************************
       which | 12   ************
         all | 12   ************
        they | 7    *******
       their | 7    *******
         she | 7    *******
        them | 6    ******
        such | 6    ******
      rights | 6    ******
       right | 6    ******
       """


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
