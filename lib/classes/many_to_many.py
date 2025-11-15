class Article:
    # Track all articles created for the Article.all class variable
    all = []
    
    def __init__(self, author, magazine, title):
        # Set author and magazine (both mutable)
        self.author = author
        self.magazine = magazine
        # Use private attribute with property to make title immutable
        self._title = None
        self.title = title
        # Add to all articles list
        Article.all.append(self)
    
    @property
    def title(self):
        """Returns the article's title"""
        return self._title
    
    @title.setter
    def title(self, value):
        # Validate title: must be str and between 5-50 characters
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            return
        self._title = value
    
    @property
    def author(self):
        """Returns the author object for this article"""
        return self._author
    
    @author.setter
    def author(self, value):
        # Author must be of type Author and is mutable
        if not isinstance(value, Author):
            return
        self._author = value
    
    @property
    def magazine(self):
        """Returns the magazine object for this article"""
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        # Magazine must be of type Magazine and is mutable
        if not isinstance(value, Magazine):
            return
        self._magazine = value

class Author:
    def __init__(self, name):
        # Use private attribute with property to make name immutable
        self._name = None
        self.name = name
    
    @property
    def name(self):
        """Returns the author's name"""
        return self._name
    
    @name.setter
    def name(self, value):
        # Validate name: must be str and length > 0
        # Prevent reassignment after initial creation using hasattr
        if hasattr(self, '_name') and self._name is not None:
            return
        if not isinstance(value, str) or len(value) == 0:
            return
        self._name = value

    def articles(self):
        # Return a list of all articles written by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Return a unique list of magazines the author has contributed to
        magazines = [article.magazine for article in self.articles()]
        # Remove duplicates while preserving list type
        return list(set(magazines))

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    # Track all magazines created for potential future use
    all = []
    
    def __init__(self, name, category):
        # Initialize with name and category (both mutable)
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        """Returns the magazine's name"""
        return self._name
    
    @name.setter
    def name(self, value):
        # Validate name: must be str and between 2-16 characters
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            return
        self._name = value
    
    @property
    def category(self):
        """Returns the magazine's category"""
        return self._category
    
    @category.setter
    def category(self, value):
        # Validate category: must be str and length > 0
        if not isinstance(value, str) or len(value) == 0:
            return
        self._category = value

    def articles(self):
        # Return a list of all articles published by this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Return a unique list of authors who have written for this magazine
        authors = [article.author for article in self.articles()]
        # Remove duplicates while preserving list type
        return list(set(authors))

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass