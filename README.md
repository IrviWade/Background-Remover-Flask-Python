# Background Remover Flask Python 🖼️

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A web application built with Flask that removes backgrounds from images using the rembg library.

## 📜 About
This project implements a simple web interface for removing backgrounds from images. It demonstrates how to integrate the rembg library with Flask to create a functional background removal tool. The application is designed to be user-friendly and efficient for processing images.

## ✨ Features
- Web-based interface for easy access
- Supports multiple image formats
- Fast processing using rembg library
- Responsive design for various devices
- Direct download of processed images

## 🚀 Quick Start

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fahadelahikhan/Background-Remover-Flask-Python.git
   cd Background-Remover-Flask-Python
   ```

2. Install required dependencies:
   ```bash
   pip install flask rembg pillow
   ```

3. Run the application:
   ```bash
   python app.py
   ```

### Basic Usage
```python
# The application provides a web interface for background removal
# Open your browser and navigate to http://localhost:4000
# Upload an image and click "Remove Background"
# The processed image will be displayed with background removed
```

### Example Usage
```python
# Example using the web interface:
# 1. Open the application in your browser
# 2. Select an image file (e.g., "input.jpg")
# 3. Click "Remove Background"
# 4. Download the processed image
```

## 📖 Documentation
### How It Works
The application uses the rembg library to remove backgrounds from images. The process involves:
1. Uploading an image through the web interface
2. Processing the image with rembg's background removal algorithm
3. Converting the processed image to a base64 encoded string for display
4. Providing a download link for the processed image

## ⚖️ License
Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

> **Note**: This implementation is for educational purposes. The background removal quality depends on the rembg library's capabilities.
