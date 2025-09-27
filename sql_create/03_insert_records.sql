-- Insert records into the authors table first
INSERT INTO authors (author_id, name, birth_year, nationality) VALUES
    ('AUTHOR_001', 'J.K. Rowling', 1965, 'British'),
    ('AUTHOR_002', 'George Orwell', 1903, 'British'),
    ('AUTHOR_003', 'Harper Lee', 1926, 'American'),
    ('AUTHOR_004', 'Jane Austen', 1775, 'British'),
    ('AUTHOR_005', 'F. Scott Fitzgerald', 1896, 'American'),
    ('AUTHOR_006', 'Gabriel García Márquez', 1927, 'Colombian'),
    ('AUTHOR_007', 'Chinua Achebe', 1930, 'Nigerian');

-- Insert records into the books table
-- And include foreign key references to the authors table
-- IMPORTANT: No tic marks inside a string, use two single quotes to escape a single quote
INSERT INTO books (book_id, title, genre, publication_year, author_id) VALUES
    ('BOOK_001', 'Harry Potter and the Sorcerer''s Stone', 'Fantasy', 1997, 'AUTHOR_001'),
    ('BOOK_002', 'Harry Potter and the Chamber of Secrets', 'Fantasy', 1998, 'AUTHOR_001'),
    ('BOOK_003', '1984', 'Dystopian', 1949, 'AUTHOR_002'),
    ('BOOK_004', 'Animal Farm', 'Political Satire', 1945, 'AUTHOR_002'),
    ('BOOK_005', 'To Kill a Mockingbird', 'Fiction', 1960, 'AUTHOR_003'),    
    ('BOOK_006', 'Pride and Prejudice', 'Romance', 1813, 'AUTHOR_004'),
    ('BOOK_007', 'Sense and Sensibility', 'Romance', 1811, 'AUTHOR_004'),
    ('BOOK_008', 'The Great Gatsby', 'Tragedy', 1925, 'AUTHOR_005'),
    ('BOOK_009', 'One Hundred Years of Solitude', 'Magic Realism', 1967, 'AUTHOR_006'),
    ('BOOK_010', 'Love in the Time of Cholera', 'Romance', 1985, 'AUTHOR_006'),
    ('BOOK_011', 'Things Fall Apart', 'Historical Fiction', 1958, 'AUTHOR_007'),
    ('BOOK_012', 'No Longer at Ease', 'Fiction', 1960, 'AUTHOR_007'),
    ('BOOK_013', 'Chronicle of a Death Foretold', 'Novella', 1981, 'AUTHOR_006');


