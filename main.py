"""Convert the included kitten image text into a verified PNG output."""

import base64
import os
from pathlib import Path


def emit_artwork():
    text_file = Path(__file__).resolve().parent / "entry.png.b64"
    png_data = base64.b64decode(text_file.read_text().strip())
    signature = bytes((137, 80, 78, 71, 13, 10, 26, 10))
    if not png_data.startswith(signature):
        raise ValueError(f"Decoded artwork has no PNG signature: {text_file}")
    if len(png_data) > 1048576:
        raise ValueError(f"Decoded artwork is larger than 1048576 bytes: {len(png_data)}")
    end_marker = bytes((73, 69, 78, 68, 174, 66, 96, 130))
    if not png_data.endswith(end_marker):
        raise ValueError(f"Decoded artwork is missing the PNG IEND chunk: {text_file}")

    output_folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_folder.mkdir(parents=True, exist_ok=True)
    (output_folder / "entry.png").write_bytes(png_data)


if __name__ == "__main__":
    emit_artwork()
