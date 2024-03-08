# Python-OCR-Project - In Progress

This project is designed to scan driver's license (DL) images from a webcam and display the extracted details on the front-end. It utilizes React for the front-end, Flask for the backend, and Pytesseract along with EasyOCR for optical character recognition (OCR).

## Usage
1) Allow the application to access your webcam.
2) Hold a driver's license in front of the webcam.
3) Click the "S" button to capture an image.
4) The application will perform OCR on the image and display the extracted details on the front-end.

## Technologies Used
- React: Front-end user interface development.
- Flask: Backend server to handle image processing and OCR.
- Pytesseract: Python library for OCR.
- EasyOCR: Python library for more advanced OCR capabilities.

## Dependencies
- Install Pytesseract in the same directory as ocr_scanner.py

## Project Structure
1) OCR Scripts - ocr_scanner.py, along with sample1 & sample4 images form the OCR detection part of the project
2) Backend - DLScannerAPI folder contains api.py, along with .flaskenv to form the Flask backend of the project
3) Frontend - dlscannerapp folder contains the source files for the React front-end of the project
