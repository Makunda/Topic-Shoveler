##
# -- ************************************** "file"
#
# CREATE TABLE IF NOT EXISTS "file"
# (
#  "id"            SERIAL PRIMARY KEY,
#  "name"          text NOT NULL,
#  "relative_path" text NOT NULL,
#  "extension"     text NOT NULL,
#  "comments"      text NOT NULL,
#  "size"          text NULL,
#  "hash"          text NULL,
#  "content"       bytea NULL
# );


class FileModel:
    """
        Model representing a file
    """
    name: str
    relative_path: str
    extension: str
    comments: str
    size: int
    hash_sum: str
    content: str

