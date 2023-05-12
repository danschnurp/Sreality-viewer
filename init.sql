CREATE DATABASE sreality;

\c sreality

DROP TABLE IF EXISTS results;

CREATE TABLE results (
     url_part TEXT,
    title TEXT,
   img TEXT
);

