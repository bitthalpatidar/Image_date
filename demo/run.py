from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

file2= open("MyFile1.txt", "r+")
def post(self, date):
    for line in file2:
        if date in line:
            file2.close()
            return "{ Date Is Present : %s} " % date
    file2.close()
    return "{ Date Not Present : Null }"


api.add_resource(Post, "/user/<string:name>")

app.run(debug=True)