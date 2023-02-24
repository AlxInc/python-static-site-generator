from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        extension = self.extension
        return True if self.extension in extension else False

    def parse(self, path: Path, source: Path, dest: Path) -> Path:
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext='.html'):
        full_path = f'{dest}/{path.with_suffix(ext).name}'
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, source(dest/path))

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path) -> Path:
        Parser.copy(path, source, dest)
