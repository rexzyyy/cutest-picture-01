"""Turn the bundled image string into a checked PNG file."""

import base64
import os
from pathlib import Path


def write_picture():
    encoded_path = Path(__file__).resolve().parent / "entry.png.b64"
    image_bytes = base64.b64decode(encoded_path.read_text().strip())
    png_marker = bytes((137, 80, 78, 71, 13, 10, 26, 10))
    if not image_bytes.startswith(png_marker):
        raise ValueError(f"Decoded picture is not a PNG: {encoded_path}")
    if len(image_bytes) > 1048576:
        raise ValueError(f"Decoded PNG exceeds 1048576 bytes: {len(image_bytes)}")

    target_folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_folder.mkdir(parents=True, exist_ok=True)
    (target_folder / "entry.png").write_bytes(image_bytes)


if __name__ == "__main__":
    write_picture()
