from cool_editor import create_app
from cool_editor.config import DevelopmentConfig

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    with app.app_context():
        app.run()
