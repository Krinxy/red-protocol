# Path Traversal

Goal: write a file outside the intended temp directory via upload. `file.filename` is used
unchecked in `temp_path / file.filename` (`loader/loader_api.py:294,464`).

Try: a filename like `../../etc/somefile`.

Success: the file lands outside the expected directory, or overwrites an existing one.
