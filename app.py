from __init__ import setup_app

app = setup_app(test_config=False)

# Runs the app through setup_app ensuring testing config is false
if __name__ == '__main__':
    testing=False
    app.run(debug=True)