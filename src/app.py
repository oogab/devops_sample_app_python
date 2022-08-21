from flask import Flask, jsonify, request

def create_app():
  app = Flask(__name__)

  @app.route("/healthz")
  def healthz():
    return {
      "status": 200,
      "message": "healthy"
    }

  @app.route("/hello")
  def hello():
    print("hello world")
    return jsonify({"message": "Hello world !!\n"}), 200

  @app.route("/hello/<username>")
  def hello_user(username):
    print("username: ", username)
    return jsonify({"message": "Hello %s\n" % username}), 200

  return app


if __name__ == "__main__":
  app = create_app()
  app.run(host='0.0.0.0', port=8080)
