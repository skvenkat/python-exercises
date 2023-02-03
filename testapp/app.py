from importlib_resources import files
from importlib import resources
from pkgutil import get_data

import pandas as pd

def get_data(filepath):
    """Get book data from the csv file"""
    return pd.read_csv(filepath)

def main():
    #with resources.as_file(
    #    "author_book_publisher.csv"
    #) as file_path:
    #    data = get_data(file_path)
    
    #with open("author_book_publisher.csv") as dfd:
    #    data = get_data(dfd)
    
    csvdata = files('data').joinpath('author_book_publisher.csv').read_text()
    print(csvdata)

    books_by_publisher = get_books_by_publisher(data, ascending=False)
    for publisher, total_books in books_by_publisher.items():
        print(f"Publisher: {publisher}, total books: {total_books}")
    print()

    authors_by_publisher = get_authors_by_publishers(data, ascending=False)
    for publisher, total_authors in authors_by_publisher.items():
        print(f"Publisher: {publisher}, total authors: {total_authors}")
    print()

    output_author_hierarchy(data)

    data = add_new_book(
        data,
        author_name="Stephen King",
        book_title="The Stand",
        publisher_name="Random House",
    )

    output_author_hierarchy(data)


if __name__ == '__main__':
    main()
