# -*-encoding=utf-8-*-


from flask import Flask, render_template, request, make_response, redirect, flash, get_flashed_messages
import logging

from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'
app.secret_key = 'ben'


@app.route('/index')
@app.route('/')
def index():
    res = ''
    for msg in get_flashed_messages():
        res = res + msg + '<br>'

    res = res + 'hello'

    return res


@app.route('/profile/<int:uid>/', methods=['get', 'post'])
def profile(uid):
    colors = ('red', 'green')
    infos = {'nowcoder': 'abc', 'google': 'def'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)


@app.route('/request')
def request_demo():
    key = request.args.get('key', 'defaultkey')
    res = request.args.get('key', 'defaultkey') + '<br>'

    for property in dir(request):
        res = res + str(property) + '|==|' + str(eval('request.' + property)) + '<br>'
    response = make_response(res)
    response.set_cookie('nowcoderid', key)
    response.status = '404'

    return response


@app.route('/newpath')
def newpath():
    return 'newpath'


@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath', code=code)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', url=request.url)


@app.route('/admin')
def admin():
    key = request.args.get('key')
    if key == 'admin':
        return 'hello admin'
    else:
        raise Exception()


@app.route('/login')
def login():
    app.logger.info('log success')
    flash('登录成功')
    return 'ok'


@app.route('/log/<level>/<msg>')
def log(level, msg):
    dict = {'warn': logging.WARN, 'error': logging.ERROR, 'info': logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level], msg)

    return 'logged:' + msg


def set_logger():
    info_file_handler = RotatingFileHandler("../log/info.txt")
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler("../log/warn.txt")
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler("../log/error.txt")
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


if __name__ == "__main__":
    set_logger()
    app.run(debug=True)
