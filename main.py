from flask import make_response

from data.users import User
from data import db_session
from flask_login import LoginManager, login_user
from forms.user import LoginForm
from flask import Flask, request, render_template, redirect


app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

def main():
    db_session.global_init("db/blogs.db")
    # user = User()
    # user.surname = 'Scott'
    # user.name = 'Ridley'
    # user.age = 21
    # user.position = 'captain'
    # user.speciality = 'research engineer'
    # user.address = 'module_1'
    # user.email = 'scott_chief@mars.org'
    # user.hashed_password = '123456'
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    #
    # db_sess.commit()
    #
    # user = User()
    # user.surname = 'aboba'
    # user.name = 'bebrovich'
    # user.age = 42
    # user.position = 'moron'
    # user.speciality = 'moron'
    # user.address = 'module_2'
    # user.email = 'moron@mars.org'
    # user.hashed_password = 'cstyler'
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    #
    # db_sess.commit()
    #
    # user = User()
    # user.surname = 'e'
    # user.name = 'a'
    # user.age = 21
    # user.position = 'servant'
    # user.speciality = 'ggg'
    # user.address = 'module_4'
    # user.email = 'ggg@mars.org'
    # user.hashed_password = 'kotiki'
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    #
    # db_sess.commit()



@app.route("/")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            response = make_response(redirect("/"))
            response.set_cookie('name', user.name, max_age=60 * 60 * 24)
            return response
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')

