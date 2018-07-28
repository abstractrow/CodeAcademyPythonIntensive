'''
Project: Tome Rater
Author: Alfonso Camblor

Note: Hello, there is something i would like to fix.

When I have a constructor error, I don't really know how to handle it. I saw that __del__ with the variable you have created would fix it, but I haven't seen that variable
in this course, so I have decided to equal the inner variables to my own error values.
'''

#User object
class User(object):
    def __init__(self, name, email):
        if type(name) == str and type(email) == str and '@' in email and ('.com' in email or '.edu' in email or '.org' in email):
            self.name = name #string
            self.email = email #string
            self.books = {} #dictionary
        else:
            print("User's constructor error")
            self.name = "Error" #string
            self.email = "Error" #string
            self.books = {} #dictionary

    def get_email(self):
        try:
            return self.email
        except:
            print("User get email error")

    def change_email(self, address):
        if type(address) == str:
            self.email = address
            print(self.name + "'s email has been changed to " + self.email)
        else:
            print("User's email change error")

    def __repr__(self):
        try:
            return self.name + ", email: " + self.email + " - Books read: " + str(len(self.books))
        except:
            return "printing user error"

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        if (type(book) == Book or type(book) == Fiction or type(book) == Non_Fiction) and ((type(rating) == int and rating >= 0 and rating <= 4) or rating == None):
            if book in self.books:
                print(self.name + " has already read this book. Updating the rating.")
                self.books[book] = rating
            else:
                print("Adding "+ book.title +" to " + self.name + " library. Adding the rating.")
                self.books[book] = rating
        else:
            print("Read book error")

    def get_average_rating(self):
        sum = 0
        n = 0
        for rating in self.books.values():
            if rating != None:
                sum += rating
                n += 1
            else:
                continue

        if sum == 0 and n == 0:
            return 0
        else:
            return sum / n

    def	__hash__(self):
        return	hash((self.name, len(self.books)))

    def read_books(self):
        return len(self.books)


#Book object
class Book(object):
    def __init__(self, title, isbn, price=0.0):
        if type(title) == str and type(isbn) == int and type(price) == float:
            self.title = title #string
            self.isbn = isbn #number
            self.price = price
            self.ratings = [] #list
        else:
            print("Book's constructor error")
            self.title = "Error" #string
            self.isbn = -1 #number
            self.ratings = [] #list

    def get_title(self):
        try:
            return self.title
        except:
            print("Get title error")

    def get_isbn(self):
        try:
            return self.isbn
        except:
            print("Get isbn error")

    def set_isbn(self, new_isbn):
        try:
            self.isbn = new_isbn
            print(self.title + " ISBN has been updated to " + str(self.isbn))
        except:
            print("Set book isbn error")

    def add_rating(self, rating):
        if (type(rating) == int and rating >= 0 and rating <= 4) or rating == None:
            self.ratings.append(rating)
        else:
            print("Add rating error")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        sum = 0
        n = 0
        for rating in self.ratings:
            if rating != None:
                sum += rating
                n += 1
        if sum == 0 and n == 0:
            return 0
        else:
            return sum / n

    def	__hash__(self):
        return	hash((self.title, self.isbn))

    def __repr__(self):
        try:
            return self.title + " with ISBN " + str(self.isbn)
        except:
            return "Printing Book error"



class Fiction(Book):
    def __init__(self, title, author, isbn):
        if type(author) == str: 
            super().__init__(title, isbn)
            self.author = author
        else:
            print("Fiction constructor error")
            super().__init__("Error", -1)
            self.author = "Error"

    def get_author(self):
        try:
            return self.author
        except:
            print("Get Fiction author error")

    def __repr__(self):
        try:
            return self.title + " by " + self.author
        except:
            return "Printing Fiction book error"


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        try:
            super().__init__(title, isbn)
            self.subject = subject
            self.level = level
        except:
            print("Non Fiction constructor error")
            super().__init__("Error", -1)
            self.subject = "Error"
            self.level = "Error"

    def get_subject(self):
        try:
            return self.subject
        except:
            print("Non Fiction get subject error")

    def get_level(self):
        try:
            return self.level
        except:
            print("Non Fiction get level error")

    def __repr__(self):
        try:
            return self.title + ", a " + self.level + " manual on " + self.subject
        except:
            return "Printing Non Fiction book error"


class TomeRater():
    def __init__(self):
        self.users = {} #email: user_object
        self.books = {} #book:n_users
        
    def create_book(self, title, isbn):
        if type(title) == str and type(isbn) == int:
            for book in self.books.keys():
                if book.isbn == isbn:
                    print("This ISBN already exists.")
                    return None

            return Book(title, isbn)
        else:
            print("You can't create a book with this input")

    def create_novel(self, title, author, isbn):
        if type(title) == str and type(author) == str and type(isbn) == int:
            for book in self.books.keys():
                if book.isbn == isbn:
                    print("This ISBN already exists.")
                    return None

            new_book = Fiction(title, author, isbn)
            self.books[new_book] = 0

            return new_book
        else:
            print("You can't create a book with this input")

    def create_non_fiction(self, title, subject, level, isbn):
        if type(title) == str and type(subject) == str and type(level) == str and type(isbn) == int:
            for book in self.books.keys():
                if book.isbn == isbn:
                    print("This ISBN already exists.")
                    return None

            new_book = Non_Fiction(title, subject, level, isbn)
            self.books[new_book] = 0

            return new_book
        else:
            print("You can't create a book with this input")

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email)
        if type(user) == User and (type(book) == Book or type(book) == Fiction or type(book) == Non_Fiction):
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("Adding book error.")

    def add_user(self, name, email, user_books = None):
        for user_email in self.users.keys():
            if user_email == email:
                print("That email already exists")
                return None
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most = 0
        for book, readers in self.books.items():
            if readers > most:
                most = readers
                most_read = book
        return most_read

    def highest_rated_book(self):
        temp = 0.0
        most = 0.0
        for book in self.books.keys():
            temp = book.get_average_rating()
            if temp > most:
                most = temp
                highest_rated = book

        return highest_rated

    def most_positive_user(self):
        temp = 0.0
        most = 0.0
        for user in self.users.values():
            temp = user.get_average_rating()
            if temp > most:
                most = temp
                most_positive = user
        return most_positive

    def get_n_most_read_books(self, num):
        n = 0
        most_read = []
        temp_dict = {}

        for book, views in self.books.items():
            temp_dict[book] = views
        
        while n < num:
            temp_max_view = max(temp_dict, key = temp_dict.get)
            temp_dict.pop(temp_max_view)
            most_read.append(temp_max_view)
            n += 1

        return most_read

    #I got a not hashable error here if I try to do the same as get_n_most_read-books
    def get_n_most_prolific_readers(self, num):
        n = 0
        most_prolific = []
        temp_list_1 = []
        temp_list_2 = []
        temp_value = 0
        temp_index = -1

        for user in self.users.values():
            temp_list_1.append(user.name)
            temp_list_2.append(user.read_books())

        while n < num and len(most_prolific) < len(self.users):
            #We obtain the value, name and index for both lists of the user with max read books
            temp_value = max(temp_list_2)
            temp_index = temp_list_2.index(temp_value)
            temp_name = temp_list_1[temp_index]
            #We append the output of that 3 lines to the return list
            most_prolific.append(temp_name)
            #We remove from the lists the elements we used every iteration
            temp_list_1.remove(temp_name)
            temp_list_2.remove(temp_value)
            n += 1

        return most_prolific

    def get_n_most_expensive_books(self, num):
        n = 0
        most_expensive = []
        temp_dict = {}

        for book in self.books:
            temp_dict[book] = book.price
        
        while n < num:
            temp_max_price = max(temp_dict, key = temp_dict.get)
            temp_dict.pop(temp_max_price)
            most_expensive.append(temp_max_price)
            n += 1

        return most_expensive

    def get_worth_of_user(self, user_email):
        if user_email in self.users:
            sum = 0
            temp_user = self.users[user_email]
            for book in temp_user.books:
                sum += book.price
            return sum

        else:
            print("No user with that email.")
            return 0

    #I decided to print the most 3 of every most_n function I wrote
    def __repr__(self):
        most_read = str(self.get_n_most_read_books(3))
        most_prolific = str(self.get_n_most_prolific_readers(3))
        most_expensive = str(self.get_n_most_expensive_books(3))

        return "Most read books:\n" + most_read + "\nMost prolific readers:\n" + most_prolific + "\nMost expensive books:\n" + most_expensive

    def __eq__(self, other_tomerater):
        #We will need to compare both first argument with second argument
        for email in self.users:
            if email not in other_tomerater.users:
                return False
        for book in self.books:
            if book not in other_tomerater.books:
                return False
        #and second argument with first argument
        for email in other_tomerater.users:
            if email not in self.users:
                return False
        for book in other_tomerater.books:
            if book not in self.books:
                return False
        #If everything is equal, they are so.
        return True
