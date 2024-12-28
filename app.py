from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def form_find():
    value = request.args.get('search-value')
    return render_template('html/index.html', value=value)

if __name__ == '__main__':
    app.run(debug=True)
