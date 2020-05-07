from flask.cli import FlaskGroup

from ormuco import app, db

cli = FlaskGroup(app)

@cli.command("init_db")
def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    cli()
