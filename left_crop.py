import os
from PIL import Image

def crop_image_from_bottom_left(input_path, output_path, new_width=500, new_height=300):
    """
    Crop an image to a specific resolution based on the bottom left corner, then save it to a new folder.

    Args:
    input_path (str): Path to the input image.
    output_path (str): Path where the new folder will be created and the cropped image will be saved.
    new_width (int): New width of the image.
    new_height (int): New height of the image.
    """

    with Image.open(input_path) as img:
        # Calculate the top-left point of the cropping box
        left = 0
        top = img.height - new_height

        # Crop the image based on the bottom left corner
        img_cropped = img.crop((left, top, left + new_width, top + new_height))
        img_cropped.save(output_path)

def process_folder(input_folder, output_folder):
    """
    Process all images in the input folder, cropping them and saving the results in the output folder.

    Args:
    input_folder (str): Path to the folder containing input images.
    output_folder (str): Path to the folder where cropped images will be saved.
    """

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            crop_image_from_bottom_left(input_path, output_path)

# Example usage
if __name__ == "__main__":
    input_folder = 'C:/Users/Intern/Documents/Data_Collecton_Chamodya/20231211/images/0/Right Rurn'
    output_folder = 'C:/Users/Intern/Documents/Data_Collecton_Chamodya/20231211/images/0/left_turns'
    process_folder(input_folder, output_folder)
