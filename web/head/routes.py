from web.head import bp
from flask import render_template
from src.sqliter import Database
from .tools import total
db = Database()


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    sheets = db.get_sheets()
    count = total(sheets)
    return render_template('index.html', sheets=sheets, count=count)



