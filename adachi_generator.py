from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def new_file_name(file_name: str, bottom_text: str):
    """
    Get the new file name given the original `file_name` and `bottom_text` input
    """
    separated = file_name.rsplit('.', 1)
    return separated[0] + "-adachi-" + bottom_text.lower() + '.' + separated[1]

def center_size(frame_size: int, inner_size: int):
    """
    Return the appropriate coordinate to place an inner element of `inner_size`
    inside a frame of `frame_size` such that the inner element will be centered.
    """
    return frame_size / 2 - inner_size / 2

def adachify(file_name: str, bottom_text: str):
    """
    Open an image located in `file_name` and add `bottom_text`.
    """
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    original = Image.open(file_name)
    font_size = original.size[1]//8

    new_size = (original.size[0], original.size[1] + font_size) # size of the output image
    new = Image.new(original.mode, new_size, WHITE)
    new.paste(original, (0, 0))
    draw = ImageDraw.Draw(new)
    font = ImageFont.truetype("COMIC.TTF", font_size)
    text_coordinates = (
        center_size(new_size[0], font.getlength(bottom_text)),
        new_size[1] - font_size * 1.2 # Cuts off otherwise, yes it's weird
    )
    draw.text(text_coordinates, bottom_text, RED, font)
    new.save(new_file_name(file_name, bottom_text))

def main():
    file_path = input("Enter file path: ")
    bottom_text = input("Bottom text: ")
    adachify(file_path, bottom_text)

if __name__ == "__main__":
    main()