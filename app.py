from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Initialize the Flask app
app = Flask(__name__)

# Set up Gemini API Key (use your actual API key)
os.environ["GOOGLE_API_KEY"] = "AIzaSyCU4mbVJYBUWIGJL_0jAWZlVNwnReJw1_c"

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user input and request content from Gemini AI
@app.route('/generate', methods=['POST'])
def generate_content():
    # Get the user input from the form
    user_input = request.form['prompt']

    try:
        # Generate content from the Gemini model based on user input
        response = model.generate_content(user_input)
        generated_text = response.text  # Get the generated content

        # Return the response to the front-end (as a success)
        return render_template('index.html', prompt=user_input, response=generated_text)

    except Exception as e:
        # Handle any errors from the API call
        return render_template('index.html', prompt=user_input, response=f"Error: {str(e)}")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
