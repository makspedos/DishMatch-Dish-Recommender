from flask import Blueprint, render_template, request

culinary_bp = Blueprint('culinary', __name__, template_folder='templates', static_folder='static')

@culinary_bp.route('/', methods=['GET'])
def form_find():
    value = request.args.get('search-value')
    return render_template('html/index.html', value=value)
