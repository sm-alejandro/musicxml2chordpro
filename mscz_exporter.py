import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def mscz2musicxml(input_path: Path, output_path: Path | None):
    "Converts musescore sheet to xml"
    output_path = Path(output_path) or input_path.with_suffix(".musicxml")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [os.getenv("MUSESCORE_EXECUTABLE"), input_path, "-o", output_path], check=True
    )
    return output_path


def mscz2pdf(input_path: Path, output_path: Path | None):
    "Converts musescore sheet to pdf"
    output_path = output_path or input_path.with_suffix(".pdf")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [os.getenv("MUSESCORE_EXECUTABLE"), input_path, "-o", output_path],
        check=True,
    )
    return output_path


if __name__ == "__main__":
    mscz2musicxml(Path(sys.argv[1]), None)
    mscz2pdf(Path(sys.argv[1]), None)
