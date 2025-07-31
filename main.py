from flask import Flask,request, jsonify
from flask_cors import CORS , cross_origin
from nexus_final_approach import final_process
from nexus_final_approach_user import user_login , user_registration , save_user_history , get_user_history

app = Flask(__name__)
CORS(app , resources={r"/":{"origins":"*"}})


@app.route("/")
def main():
    return "hello world"

@app.route("/home")
@cross_origin()
def home():
    return "First Page"


@app.route("/v1/login", methods=["POST"])
@cross_origin()
def user_login_():
    print("login")
    body = request.get_json()
    return user_login(body['username'],body['password'])

@app.route("/v1/register", methods=["POST"])
@cross_origin()
def user_register():
    print("register")
    body = request.get_json()
    return user_registration(body['username'],body['password'])

@app.route("/v1/get_history", methods=["POST"])
@cross_origin()
def user_history():
    print("history")
    body = request.get_json()
    return get_user_history(body['user_id'])


@app.route("/v1/prediction", methods=["POST"])
@cross_origin()
def final_result():
    print("main")
    uploaded_file = request.files['video']
    print(request.form)
    user_id = request.form['user_id']
    if uploaded_file:
        uploaded_file.save('yasiru/my_video.mp4')
    prediction = final_process(request.form)
    save_user_history(user_id,prediction)
    return prediction


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
