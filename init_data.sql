CREATE TABLE item (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

INSERT INTO item (name, description) VALUES ('Test Item 1', 'This is the first test item');
INSERT INTO item (name, description) VALUES ('Test Item 2', 'This is the second test item');
INSERT INTO item (name, description) VALUES ('Test Item 3', 'This is the third test item');

