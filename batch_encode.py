import base64
import os

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def batch_encode_images_to_base64(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(input_folder, filename)
            encoded_string = encode_image_to_base64(image_path)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            with open(output_path, "w") as output_file:
                output_file.write(encoded_string)

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing images: ")
    output_folder = input("Enter the path to the folder where you want to save the Base64 encoded files: ")
    batch_encode_images_to_base64(input_folder, output_folder)
    print("Encoding complete.")