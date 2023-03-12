import random

"""Word Finder: finds random words from a dictionary."""
 
class WordFinder:
    """
    A class that reads a file containing a list of words and provides a method for returning a random word.

    >>> wf = WordFinder("words.txt")
    235887 words read

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True
    """

    def __init__(self, file_path):
        """
        Read the file at the given file path and initialize the words list.

        >>> wf = WordFinder("words.txt")
        235887 words read

        """
        self.file_path = file_path
        with open(file_path, 'r') as file:
            self.words = file.read().split() 
        self.num_words = len(self.words)
        print(f"{self.num_words} words read")

    def random(self):
        """
        Return a random word from the list of words.

        >>> wf = WordFinder("words.txt")
        235887 words read

        >>> word = wf.random()
        >>> word in wf.words
        True

        """
        return random.choice(self.words)
    
    def __repr__(self):
        """Return string representation of the WordFinder instance."""
        return f"<WordFinder total_words={len(self.words)} file_path={self.file_path}>"

class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random non-comment words from a dictionary.
    
    SpecialWordFinder is a subclass of WordFinder that only returns non-comment words 
    from the provided word list.
    
    >>> swf = SpecialWordFinder("words.txt")
    235887 words read
    
    >>> swf.random()
    'abstainer'
    
    >>> swf.random()
    'duplications'
    
    >>> swf.random() 
    'funkias'
    
    >>> swf.random()
    'enchain'
    """
    
    # def __init__(self, path):
    #     """Initialize the SpecialWordFinder instance.
        
    #     Read words from a file and store them in a list. 
        
    #     """
    #     super().__init__(path)
        
    #     # remove the commented and empty lines from the list of words
    #     self.words = [word.strip() for word in self.words if word.strip() and not word.startswith('#')]
    #     self.num_words = len(self.words)
    #     print(f"{self.num_words} words read")
    def __init__(self, path):
        """
        Read the file at the given file path and initialize the words list.

        Exclude any commented or empty lines from the list of words.

        >>> swf = SpecialWordFinder("words.txt")
        235886 words read
        """
        self.file_path = path
        self.num_words = 0
        with open(self.file_path, 'r') as file:
            self.words = []
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    self.words.append(line)
                    self.num_words += 1

        print(f"{self.num_words} words read")

    def random(self):
        """Return a random non-comment word from the list of words."""
        return random.choice(self.words)

    def __repr__(self):
        """Return string representation of the SpecialWordFinder instance."""
        return f"<SpecialWordFinder num_words={self.num_words} total_words={len(self.words)} file_path={self.file_path}>"
 