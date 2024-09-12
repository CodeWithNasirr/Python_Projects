import cv2

def resize_image(input_path, output_path, new_size):
    """
    Resize an image to the specified dimensions using OpenCV.

    Parameters:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the resized image.
        new_size (tuple): Desired size as a tuple (width, height).
    """
    try:
        # Read the input image
        img = cv2.imread(input_path)
        # Resize the image
        resized_img = cv2.resize(img, new_size,cv2.INTER_AREA)
        # Save the resized image
        cv2.imwrite(output_path, resized_img)
        print("Image resized successfully!")
    except Exception as e:
        print(f"Unable to resize image: {str(e)}")

# Example usage:
input_image_path = "IMG.jpg"
output_image_path = "resized_image.jpg"
new_size = (1708, 2560)  # Set the desired dimensions


resize_image(input_image_path, output_image_path, new_size)
