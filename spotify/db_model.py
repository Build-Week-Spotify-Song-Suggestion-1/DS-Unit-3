from flask_sqalchemy import SQAlchemy

DB = SQAlchemy

class SongTitle(DB.Model):
    id = DB.Column(DB.String(30), primary_key=True)
    name = DB.Column(DB.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<SongTitle %r>' % self.name

class Tempo(DB.Model):
    id = DB.Column(DB.String(30), primary_key=True)
    tempo = DB.Column(DB.Float, nullable=False)
    songtitle = DB.relationship('SongTitle', backref=DB.backref('tempo', lazy=True))

    def __repr__(self):
        return '<Tempo %r>' % self.tempo