import os
from .utils import deco

class FileReader:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._lines = self._read_lines()

    def _read_lines(self):
        with open(self._file_path, 'r') as f:
            for line in f:
                yield line.strip()

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        if not os.path.exists(value):
            raise FileNotFoundError("File not found.")
        self._file_path = value
        self._lines = self._read_lines()

    @staticmethod
    def description():
        return "Reads a file line by line using a generator."

    @classmethod
    def from_file(cls, file_path):
        return cls(file_path)

    def __str__(self):
        return f"<FileReader reading: {self.file_path}>"

    def __add__(self, other):
        new_file = 'combined.txt'
        with open(new_file, 'w') as f:
            f.writelines([line + '\n' for line in self._lines])
            f.writelines([line + '\n' for line in other._lines])
        return FileReader(new_file)

    @deco('green')
    def preview(self, lines=3):
        print("\n".join([line for _, line in zip(range(lines), self._read_lines())]))


class AdvancedFileReader(FileReader):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def __str__(self):
        return f"<AdvancedFileReader: {self.file_path}>"

    def concat_files(self, *file_paths):
        with open('multi_combined.txt', 'w') as f:
            for path in file_paths:
                with open(path, 'r') as file:
                    f.write(file.read())
        return AdvancedFileReader('multi_combined.txt')
