# Background Remover Flask Python 🖼️

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A web application built with Flask that removes backgrounds from images using the rembg library.

## 📜 About
This project provides a user-friendly web interface for removing backgrounds from images. It leverages the rembg library for efficient background removal and supports multiple image formats. The application is designed to be responsive, accessible, and easy to use.

## ✨ Features
- Web-based interface for seamless image uploads
- Supports JPG, PNG, GIF, and BMP image formats
- Fast and reliable background removal using rembg
- Responsive design compatible with desktop and mobile devices
- Displays processed images with an option to download

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fahadelahikhan/Background-Remover-Flask-Python.git
   cd Background-Remover-Flask-Python
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Open your browser and navigate to `http://localhost:4000`.

### Usage
- Access the web interface at `http://localhost:4000`
- Upload an image by clicking "Choose file" or dragging and dropping
- Click "Remove Background" to process the image
- View the processed image and download the result

## 📖 Project Structure
```
Background-Remover-Flask-Python/
├── main.py                # Main application code
├── templates/
│   └── index.html         # HTML template for the web interface
├── requirements.txt       # Project dependencies
├── LICENSE.txt            # MIT License file
├── .gitignore             # Git ignore file
└── README.md              # Project documentation
```

## 📋 Requirements
See [requirements.txt](requirements.txt) for a complete list of dependencies.

## ⚙️ Deployment
For production deployment, use a WSGI server like Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:4000 main:create_app
```

Set the `PORT` environment variable for custom port configuration:
```bash
export PORT=8080  # On Windows: set PORT=8080
```

## 🛠️ Troubleshooting
- Ensure all dependencies are installed correctly.
- Verify that the uploaded image is in a supported format (JPG, PNG, GIF, BMP).
- Check the console for error messages if processing fails.

## ⚖️ License
Distributed under the MIT License. See [LICENSE.txt](LICENSE.txt) for details.

---

> **Note**: The quality of background removal depends on the rembg library's capabilities. For best results, use high-quality images with clear foregrounds.