import pytest
from file_reader.reader import FileReader, AdvancedFileReader
import os

@pytest.fixture
def temp_files(tmp_path):
    f1 = tmp_path / "file1.txt"
    f2 = tmp_path / "file2.txt"
    f1.write_text("Line1\nLine2\n")
    f2.write_text("More1\nMore2\n")
    return str(f1), str(f2)

def test_file_reader(temp_files):
    file1, _ = temp_files
    reader = FileReader(file1)
    assert reader.file_path == file1
    assert isinstance(next(reader._read_lines()), str)

def test_add_operator(temp_files):
    file1, file2 = temp_files
    r1 = FileReader(file1)
    r2 = FileReader(file2)
    combined = r1 + r2
    assert os.path.exists(combined.file_path)

def test_advanced_concat(temp_files):
    file1, file2 = temp_files
    afr = AdvancedFileReader(file1)
    combined = afr.concat_files(file1, file2)
    assert os.path.exists(combined.file_path)
