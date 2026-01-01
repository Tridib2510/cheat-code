from dotenv import load_dotenv
load_dotenv()
import cloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

def upload_image(image_path):
    try:
        response = cloudinary.uploader.upload(
            image_path,
            folder="uploads",      
            resource_type="image"
        )

        print("Upload successful!")
        print("Image URL:", response["secure_url"])
        return response

    except Exception as e:
        print("Upload failed:", e)
        return None
    
if __name__ == "__main__":
    image_path = r"C:\Users\Tridib Roy Chowdhury\OneDrive\Desktop\CODING\CheatCode\screenshots\shot.png"
    upload_image(image_path)