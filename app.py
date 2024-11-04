from flask import Flask, render_template, request
import openai


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request

    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    if request.method == "POST":
        print("POST request received at /api")

    #return render_template("temp.html")
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()

