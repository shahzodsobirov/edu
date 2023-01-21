from .database import *
from app import *


@app.route('/')
def hello_world():  # put application's code here
    return render_template("home.html")


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


class Schools:
    def __init__(self):
        self.name = ch(['Shahzod', 'Akbar', 'Akram', 'Alisher', 'Aziz', 'Bilol', 'Begzod', 'Sardor', 'Asad', 'Muhammad',
                        'Ulugbek'])
        self.surname = ch(
            ['Shahzod', 'Akbar', 'Akram', 'Alisher', 'Aziz', 'Bilol', 'Begzod', 'Sardor', 'Asad', 'Muhammad',
             'Ulugbek'])
        self.age = rd(7, 18)
        self.attendance = rd(20, 90)
        self.score = rd(20, 90)
        self.id = rd(100000, 199999)


data = {
    "schools": []
}

for i in range(50):
    data['schools'].append(Schools().__dict__)

# input(data)
write(data, 'package.json')
pprint(data)


# pprint(read('package.json'))
# input()


@app.route('/list_of_readers')
def list_of_readers():
    # for r in read('package.json')['schools']:
    # print(r)
    return render_template("list of readers.html", schools=read('package.json'))


@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        info = {
            'name': '',
            'surname': '',
            'age': '',
            'attendance': '',
            'score': '',
            'id': ''
        }

        search = int(request.form.get("search"))
        for user in read('package.json')['schools']:
            print("user")
            if search == user['id']:
                print(True)
                info['name'] = user['name']
                info['surname'] = user['surname']
                info['age'] = user['age']
                info['attendance'] = user['attendance']
                info['score'] = user['score']
                info['id'] = user['id']
        print(info)
        return render_template("search.html", info=info)
