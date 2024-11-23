--- 
It's just a basic Image Classifier, It classify about the **Animals Picture** more acuurately than the other still in Changes.
---
---

# 🖼️ Image Classifier & Chatbot

Welcome to the **Image Classifier & Chatbot**! This Flask-based web application allows you to upload images, classify them using a pre-trained MobileNetV2 model, and engage in a chatbot conversation to learn more about the predictions. 🎉

---

## 🚀 Features

- **Image Classification**: Upload an image, and the app will classify it using the MobileNetV2 model trained on ImageNet.
- **Chatbot Interaction**: Ask questions about the image, its classification, and the prediction confidence.
- **Session Storage**: Keeps track of the last prediction for enhanced chatbot interaction.
- **Web Interface**: Simple and user-friendly interface for uploading images and interacting with the chatbot.

---

## 🛠️ Installation and Setup

### 1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/image-classifier-chatbot.git
   cd image-classifier-chatbot
   ```

### 2. **Install Required Packages**

   The following Python packages are required for the application to run:  
   - **Flask**: For creating the web application.  
   - **tensorflow**: For the pre-trained MobileNetV2 model.  
   - **Pillow**: For image processing.  

   Install them using the command:
   ```bash
   pip install flask tensorflow pillow
   ```

   Alternatively, install all dependencies at once using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

   Example `requirements.txt`:
   ```
   Flask==2.3.3
   tensorflow==2.14.0
   Pillow==10.0.0
   ```

### 3. **Run the Application**
   ```bash
   python app.py
   ```

### 4. **Access the Web App**
   Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 📋 How to Use

1. **Upload an Image**:
   - Use the web interface to upload an image or send it programmatically via a tool like Postman to the `/predict` endpoint.
   - Example using `curl`:
     ```bash
     curl -X POST -F "file=@path/to/image.jpg" http://127.0.0.1:5000/predict
     ```

2. **Chat with the Bot**:
   - Ask questions about the image by sending a JSON payload to the `/chat` endpoint.
   - Example using `curl`:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"message": "What is it?"}' http://127.0.0.1:5000/chat
     ```

---

## 🏗️ Code Overview

### **Main Components**
1. **Image Upload and Classification**:
   - The `/predict` endpoint accepts an image, processes it, and predicts its label and confidence using MobileNetV2.

2. **Chatbot**:
   - The `/chat` endpoint allows the user to ask questions about the most recently classified image.

3. **Home Route**:
   - The `/` endpoint serves the HTML interface for the app.

---

## 🧠 Pre-trained Model: MobileNetV2

This app leverages TensorFlow's `MobileNetV2`, a lightweight deep learning model, for quick and efficient image recognition.

---

## 🎯 Example Use Cases

- Educational tools for explaining image classification.
- Fun image recognition game with chatbot interaction.
- Quick identification of objects in uploaded images.

---

## 🌟 Future Enhancements

- Add support for multiple image uploads.
- Expand the chatbot's contextual responses.
- Integrate more pre-trained models for diverse use cases.
- Build a more dynamic frontend for enhanced user experience.

---

## 🧑‍💻 Contributions

Feel free to open issues or submit pull requests to improve the app. Contributions are always welcome! 🛠️

---

## 📜 License

This project is licensed under the MIT License.

---

Happy coding! 💻✨
