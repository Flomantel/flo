from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
    #gunicorn app:run(port=8080, debug=True)
