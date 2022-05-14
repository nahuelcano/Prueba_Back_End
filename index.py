from App import Database, app
from Utils.db import db
from sqlalchemy_utils import create_database, database_exists
##CHEQUEO DE DATA BASE
with app.app_context():
    if not database_exists(Database):
        create_database(Database)
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
