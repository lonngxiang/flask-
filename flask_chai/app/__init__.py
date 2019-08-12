from flask import Flask

from app.ext import init_ext
from app.settings import envs
from app.views import init_first_blue


def creat_app():
    app = Flask(__name__,template_folder="../templates")
    #初始化app
    app.config.from_object(envs.get("develop"))
    #初始化蓝图 路由
    init_first_blue(app)
    #初始化第三方库
    init_ext(app)


    return app