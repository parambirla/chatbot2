from flask import Flask, render_template, request
import openai
import os


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request

    global conversation_history

    #personality = Conscientiousness
    message = request.json.get("message") + ' . (Respond to this assuming "Conscientiousness" personality trait without revealing "Conscientiousness" statement in response) '

    conversation_history.append({"role": "user", "content": message})
    # Send the message to OpenAI's API and receive the response
    if request.method == "POST":
        print("POST request received at /api")

    #return render_template("temp.html")
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        #messages=[{"role": "user", "content": message}]
        messages=conversation_history 
    )
    if completion.choices[0].message!=None:
        assistant_reply = completion.choices[0].message['content']
        conversation_history.append({"role": "assistant", "content": assistant_reply})
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()

