from __future__ import annotations
import fnmatch
from pathlib import Path
import re
import zipfile
from abc import ABC, abstractmethod
# Управление объектами (страница 203)


# class ZipReplace:
#     def __init__(self, archive: Path, pattern: str, find: str, replace: str) -> None:
#         self.archive_path = archive
#         self.pattern = pattern
#         self.find = find
#         self.replace = replace

#     def find_and_replace(self) -> None:
#         input_path, output_path = self.make_backup()

#         with zipfile.ZipFile(output_path, 'w') as output:
#             with zipfile.ZipFile(input_path) as input:
#                 self.copy_and_transform(input, output)

#     def make_backup(self) -> tuple[Path, Path]:
#         input_path = self.archive_path.with_suffix(
#             f"{self.archive_path.suffix}.old")
#         output_path = self.archive_path
#         self.archive_path.rename(input_path)
#         return input_path, output_path

#     def copy_and_transform(self, input: zipfile.ZipFile, output: zipfile.ZipFile) -> None:
#         for item in input.infolist():
#             extracted = Path(input.extract(item))
#             if (not item.is_dir() and fnmatch.fnmatch(item.filename, self.pattern)):
#                 print(f"Transform {item}")
#                 input_text = extracted.write_text(output_text)
#                 output_text = re.sub(self.find, self.replace, input_text)
#                 extracted.write_text(output_text)
#             else:
#                 print(f"Ignore {item}")
#             output.write(extracted, item.filename)
#             extracted.unlink()
#             for parent in extracted.parents:
#                 if parent == Path.cwd():
#                     break
#                 parent.rmdir()


# if __name__ == "__main__":
#     sample_zip = Path("sample.zip")
#     zr = ZipReplace(sample_zip, '*.md', 'xyzzy', "plover's egg")
#     zr.find_and_replace()

class ZipProcessor(ABC):
    def __init__(self, archive: Path) -> None:
        self.archive_path = archive
        self.pattern: str

    def process_files(self, pattern: str) -> None:
        self._pattern = pattern

        input_path, output_path = self.make_backup()

        with zipfile.ZipFile(output_path, 'w') as output:
            with zipfile.ZipFile(input_path) as input:
                self.copy_and_transform(input, output)

    def make_backup(self) -> tuple[Path, Path]:
        input_path = self.archive_path.with_suffix(
            f"{self.archive_path.suffix}.old")
        output_path = self.archive_path
        self.archive_path.rename(input_path)
        return input_path, output_path

    def copy_and_transform(self, input: zipfile.ZipFile, output: zipfile.ZipFile) -> None:
        for item in input.infolist():
            extracted = Path(input.extract(item))
            if self.matches(item):
                print(f"Transform {item}")
                self.transform(extracted)
            else:
                print(f"Ignore {item}")
            output.write(extracted, item.filename)
            self.remove_under_cwd(extracted)

    def matches(self, item: zipfile.ZipInfo) -> bool:
        return (not item.is_dir() and fnmatch.fnmatch(item.filename, self._pattern))

    def remove_under_cwd(self, extracted: Path) -> None:
        extracted.unlink()
        for parent in extracted.parents:
            if parent == Path.cwd():
                break
            parent.rmdir()


class TextTweaker(ZipProcessor):
    def __init__(self, archive: Path) -> None:
        super().__init__(archive)
        self.find: str
        self.replace: str

    def find_and_replace(self, find: str, replace: str) -> "TextTweaker":
        self.find = find
        self.replace = replace
        return self

    def transform(self, extracted: Path) -> None:
        input_text = extracted.read_text()
        output_text = re.sub(self.find, self.replace, input_text)
        extracted.write_text(output_text)
