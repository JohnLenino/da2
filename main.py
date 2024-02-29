from flask import Flask

from data.news import News
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)

    db_sess.commit()

    user = User()
    user.surname = 'aboba'
    user.name = 'bebrovich'
    user.age = 42
    user.position = 'moron'
    user.speciality = 'moron'
    user.address = 'module_2'
    user.email = 'moron@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)

    db_sess.commit()

    user = User()
    user.surname = 'e'
    user.name = 'a'
    user.age = 21
    user.position = 'servant'
    user.speciality = 'ggg'
    user.address = 'module_4'
    user.email = 'ggg@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)

    db_sess.commit()

    user = User()
    user.surname = 'ee'
    user.name = 'aa'
    user.age = 2121
    user.position = 'servant2'
    user.speciality = 'ggkg'
    user.address = 'module_78'
    user.email = 'ggfg@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)

    db_sess.commit()


if __name__ == '__main__':
    main()
