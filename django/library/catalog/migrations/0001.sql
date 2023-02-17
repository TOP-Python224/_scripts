BEGIN;
--
-- Create model Author
--
CREATE TABLE "catalog_author" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
--
-- Create model Book
--
CREATE TABLE "catalog_book" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(100) NOT NULL,
    "author_id" smallint NOT NULL
        REFERENCES "catalog_author" ("id") DEFERRABLE INITIALLY DEFERRED
);
--
-- Create model Publisher
--
CREATE TABLE "catalog_publisher" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(50) NOT NULL
);

CREATE TABLE "catalog_publisher_authors" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "publisher_id" smallint NOT NULL
        REFERENCES "catalog_publisher" ("id") DEFERRABLE INITIALLY DEFERRED,
    "author_id" smallint NOT NULL
        REFERENCES "catalog_author" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE "catalog_publisher_books" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "publisher_id" smallint NOT NULL
        REFERENCES "catalog_publisher" ("id") DEFERRABLE INITIALLY DEFERRED,
    "book_id" smallint NOT NULL
        REFERENCES "catalog_book" ("id") DEFERRABLE INITIALLY DEFERRED
);


CREATE INDEX "catalog_book_author_id_b0849980" ON "catalog_book" ("author_id");
CREATE UNIQUE INDEX "catalog_publisher_authors_publisher_id_author_id_8a8689be_uniq" ON "catalog_publisher_authors" ("publisher_id", "author_id");
CREATE INDEX "catalog_publisher_authors_publisher_id_1e577bed" ON "catalog_publisher_authors" ("publisher_id");
CREATE INDEX "catalog_publisher_authors_author_id_7c16aa21" ON "catalog_publisher_authors" ("author_id");
CREATE UNIQUE INDEX "catalog_publisher_books_publisher_id_book_id_ad6e0645_uniq" ON "catalog_publisher_books" ("publisher_id", "book_id");
CREATE INDEX "catalog_publisher_books_publisher_id_11f076ec" ON "catalog_publisher_books" ("publisher_id");
CREATE INDEX "catalog_publisher_books_book_id_c90a676e" ON "catalog_publisher_books" ("book_id");
COMMIT;
