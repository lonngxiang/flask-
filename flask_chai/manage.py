from flask_migrate import MigrateCommand
from flask_script import Manager

from flask import Flask

from app import creat_app

app = creat_app()


manager = Manager(app)
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    manager.run()
