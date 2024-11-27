from flask import Flask, request, jsonify, render_template, session
import tensorflow as tf
from PIL import Image
import io

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For session storage

# Load a pre-trained model (e.g., MobileNetV2)
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Function to process and predict the image
def predict_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    
    # Convert image to RGB format to ensure 3 channels
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    img = img.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    label, confidence = decoded_predictions[0][0][1], decoded_predictions[0][0][2]
    return label, confidence

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    image_bytes = file.read()
    label, confidence = predict_image(image_bytes)

    # Convert confidence to a Python float for JSON serialization
    confidence = float(confidence)

    # Store prediction in session for follow-up questions
    session['last_prediction'] = {"label": label, "confidence": confidence}

    return jsonify({"prediction": label, "confidence": round(confidence, 2)})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message').lower()

    # Retrieve the last prediction from the session
    last_prediction = session.get('last_prediction')
    if not last_prediction:
        return jsonify({"response": "Please upload an image for me to analyze first."})

    label = last_prediction["label"]
    confidence = last_prediction["confidence"]

    # Basic responses about the predicted image
    if "what is it" in user_message or "what's in the image" in user_message:
        bot_response = f"The image likely contains a '{label}' with a confidence of {confidence:.2f}."
    elif "tell me more" in user_message:
        bot_response = f"The object is identified as a '{label}', typically associated with {get_additional_info(label)}."
    elif "confidence" in user_message:
        bot_response = f"My confidence in this prediction is {confidence:.2f}."
    else:
        bot_response = "I'm not sure how to answer that about the image. Can you clarify?"

    return jsonify({"response": bot_response})

@app.route('/')
def home():
    return render_template('hack.html')

# Function to provide additional information about an object (basic implementation)
def get_additional_info(label):
    info = {
        "dog": "a domesticated animal often kept as a pet.",
        "cat": "a small carnivorous mammal known for its agility and companionship.",
        "car": "a motor vehicle with wheels, used for transportation.",
        # Add more context for other labels as needed
    }
    return info.get(label.lower(), "an interesting object.")

if __name__ == '__main__':
    app.run(debug=True)
