-- ************************************** "file"

CREATE TABLE IF NOT EXISTS "file"
(
 "id"            SERIAL PRIMARY KEY,
 "name"          text NOT NULL,
 "relative_path" text NOT NULL,
 "extension"     text NOT NULL,
 "comments"      text NOT NULL,
 "size"          text NULL,
 "hash"          text NULL,
 "content"       bytea NULL
);


