import os
import base64
from io import BytesIO
from flask import Flask, render_template, request
from rembg import remove
from PIL import Image


class ImageProcessor:
    """Handles image processing operations for background removal"""

    def __init__(self):
        self.processed_data = None

    def remove_background(self, uploaded_file):
        """
        Process uploaded image to remove background

        Args:
            uploaded_file: File object from Flask request

        Returns:
            bool: True if processing successful, False otherwise
        """
        try:
            # Open and process the uploaded image
            original_image = Image.open(uploaded_file.stream)
            processed_image = remove(original_image)

            # Convert processed image to base64 for web display
            buffer = BytesIO()
            processed_image.save(buffer, format="PNG")
            buffer.seek(0)

            # Encode image data
            self.processed_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
            return True

        except Exception as error:
            print(f"Image processing failed: {error}")
            self.processed_data = None
            return False

    def get_processed_data(self):
        """Return the processed image data"""
        return self.processed_data


def create_app():
    """Application factory function"""
    flask_app = Flask(__name__)

    @flask_app.route("/", methods=["GET", "POST"])
    def home():
        """Main route handler for image upload and processing"""
        processor = ImageProcessor()

        if request.method == "POST":
            uploaded_file = request.files.get("image")
            if uploaded_file:
                processor.remove_background(uploaded_file)

        return render_template("index.html", image_data=processor.get_processed_data())

    return flask_app


def main():
    """Main application entry point"""
    application = create_app()

    # Get port from the environment variable or use default
    server_port = int(os.environ.get("PORT", 4000))

    # Run the Flask application
    application.run(
        host="0.0.0.0",
        port=server_port,
        debug=False
    )


if __name__ == "__main__":
    main()