from flask import Flask

app = Flask(__name__)

@app.route('/Post/<string:date>')
def Post(date):
    file2 = open("MyFile.txt", "r+")
    date=date.replace('-', '/')
    print("this i date",date)
    for line in file2:
        if date in line:
            file2.close()
            return "{ Date Is Present : %s} " % date
    file2.close()
    return "{ Date Not Present : Null }"

if __name__ == "__main__":
    app.run(debug=True)