from app import web_app

@web_app.route('/')
def index():
    return "Perfect Tempo"
