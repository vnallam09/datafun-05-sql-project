SELECT
    books.book_id,
    books.title,
    books.publication_year,
    authors.author_id,
    authors.name AS author_name
FROM books
INNER JOIN authors
    ON books.author_id = authors.author_id;