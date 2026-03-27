import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def mscz2musicxml(filepath: Path):
    "Converts musescore sheet to xml"
    musicxml_file = filepath.with_suffix(".musicxml")
    subprocess.run(
        [os.getenv("MUSESCORE_EXECUTABLE"), filepath, "-o", musicxml_file], check=True
    )
    return musicxml_file


def mscz2pdf(filepath: Path):
    "Converts musescore sheet to pdf"
    pdf_file = filepath.with_suffix(".pdf")
    subprocess.run(
        [os.getenv("MUSESCORE_EXECUTABLE"), filepath, "-o", pdf_file],
        check=True,
    )
    return pdf_file


if __name__ == "__main__":
    mscz2xml(Path(sys.argv[1]))
    mscz2pdf(Path(sys.argv[1]))
