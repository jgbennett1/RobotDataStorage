from flask import Flask, request, jsonify
import json
import traceback

app = Flask(__name__)

@app.route('/', methods=['POST'])
def submit_data():
    try:
        # Get the JSON data from the POST request
        data = str(request.get_data())
        data = data[2:len(data)-1]

        file = open("data/currentID.txt", "r")  # read mode
        id = file.read()
        file.close()

        if "UserID" in data:
            id = data[10:23]
            file = open("data/currentID.txt", "w")  # write mode
            file.write(id)
            file.close()

        if id == "":
            filepath = "data/data.json"
        else:
            filepath = "data/"+id+".json"

        file = open(filepath, "a")  # append mode
        file.write(data)
        file.close()

        return jsonify({"message": "Data submitted successfully"}), 201

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e.with_traceback)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5502)
