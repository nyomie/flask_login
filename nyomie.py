# Main application module

from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    """
    Application entry point
    """
    use_debugger = False
    app.run(debug=False)
