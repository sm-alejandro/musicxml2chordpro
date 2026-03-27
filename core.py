import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

from musicxml2chordpro.xml2pro import XML2Pro

load_dotenv()


def mscz2musicxml(input_path: Path, output_path: Path | None):
    output_path = output_path or input_path.with_suffix(".musicxml")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [os.getenv("MUSESCORE_EXECUTABLE"), input_path, "-o", output_path], check=True
    )
    return output_path


def mscz2pdf(input_path: Path, output_path: Path | None):
    output_path = output_path or input_path.with_suffix(".pdf")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [os.getenv("MUSESCORE_EXECUTABLE"), input_path, "-o", output_path],
        check=True,
    )
    return output_path


def musicxml2pro(input_path: Path, output_path: Path | None):
    converter = XML2Pro()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path = converter.convert_file(input_path, output_path)
    return output_path


def pro2pdf(input_path: Path, output_path: Path | None):
    output_path = output_path or input_path.with_suffix(".pdf")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["chordpro", input_path, "-o", output_path],
        check=False,
    )


if __name__ == "__main__":
    mscz2musicxml(Path(sys.argv[1]), None)
    mscz2pdf(Path(sys.argv[1]), None)
    pro: Path = musicxml2pro(Path(sys.argv[1]), None)
    pro2pdf(pro, None)
    pro2pdf(pro, None)
