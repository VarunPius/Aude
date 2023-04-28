from pathlib import Path
from PIL import Image


def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False


def convert_webp(source, destination_dir):
    """Convert image from webp.
    Args: source (pathlib.Path): Path to source image
    Returns: pathlib.Path: path to new image
    """
    dest_filename = source.with_suffix(".jpg").name     #converts webp suffix to jpg and then gets filename
    destination = destination_dir.joinpath(dest_filename)   # final location
    
    #src_filename = Path(dest_filename).name
    #print(src_filename, destination)

    image = Image.open(source)  # Open image
    image.convert("RGB")
    image.save(destination)  # Convert image to webp
    return destination


def main():
    data_dir = Path("Data")
    source_dir = data_dir.joinpath('Native')
    destination_dir = data_dir.joinpath('Modified')
    paths = source_dir.glob("*.webp")

    for path in paths:
        print("Processing: ", path)
        webp_path = convert_webp(path, destination_dir)
        print("Image converted:", webp_path)

main()
