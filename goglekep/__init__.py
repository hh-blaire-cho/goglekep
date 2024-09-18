from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()


def create_app():
    print("run: create_app()")
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'qwerty'
    if app.config['DEBUG'] == True:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
        app.config['TEMPLATES_AUTO_RELOAD'] = True

    # CSRF INIT
    csrf.init_app(app)

    # ROUTE INIT
    from goglekep.routes import base_route
    app.register_blueprint(base_route.bp)

    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404

    from goglekep.forms.auth_form import LoginForm, RegisterForm

    @app.route("/auth/login", methods=["GET", "POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            # TODO: impl list below
            # 1) 유저조회
            # 2) 존재하는 유저 인지 체크
            # 3) 패스워드 정합확인
            # 3) 로그인 유지(세션)
            user_id = form.data.get('user_id')
            password = form.data.get('password')
            return f'ID: {user_id}</br>PW: {password}'
        else:
            pass  # TODO: 에러컨트롤
        return render_template('login.html', form=form)

    @app.route("/auth/register", methods=["GET", "POST"])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            # TODO: impl list below
            # 1) 유저조회
            # 2) 유저 이미 존재하는지 체크
            # 3) 없으면 유저 생성
            # 4) 로그인 유지(세션)
            user_id = form.data.get('user_id')
            password = form.data.get('password')
            repassword = form.data.get('repassword')
            nickname = form.data.get('nickname')
            return f'ID: {user_id}</br>PW: {password}</br>NICKNAME: {nickname}'
        else:
            pass  # TODO: 에러컨트롤
        return render_template('register.html', form=form)

    @app.route("/auth/logout")
    def logout():
        # TODO: impl
        return "logging out..."

    return app
