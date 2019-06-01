from app import db


groups_subscriptions = db.Table("groups_subscriptions",
    db.Column("username", db.String(40), db.ForeignKey('user.username')),
    db.Column("groupname", db.String(15), db.ForeignKey('group.id'))
)


teachers_subscriptions = db.Table("teachers_subscriptions",
    db.Column("username", db.String(40), db.ForeignKey('user.username')),
    db.Column("teachername", db.String(15), db.ForeignKey('teacher.id'))
)


class User(db.Model):
    __tablename__ = "user"

    username = db.Column(db.String(40), primary_key=True)
    
    saved_groups = db.relationship('Group', secondary=groups_subscriptions)
    saved_teachers = db.relationship('Teacher', secondary=teachers_subscriptions)

    def __init__(self, name):
        username = name

    def __repr__(self):
        return '@{}'.format(self.username)


class Group(db.Model):
    __tablename__ = "group"

    code = db.Column(db.String(15), primary_key=True)
    course = db.Column(db.Integer)

    children = db.relationship("Lesson")


class Subject(db.Model):
    __tablename__ = "subject"

    short_name = db.Column(db.String(15), primary_key=True)
    name = db.Column(db.String(70))

    def __repr__(self):
        return '{}'.format(self.name)


class Lesson(db.Model):
    __tablename__ = "lesson"

    short_name = db.Column(db.String(15), primary_key=True)
    code = db.Column(db.String(15), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    type_of_lesson = db.Column(db.String(15), primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)
    start = db.Column(db.DateTime, primary_key=True)
    classroom = db.Column(db.String(15))
    end = db.Column(db.DateTime)

    def __repr__(self):
        return '{}-{}-{}'.format(self.short_name, self.code, self.date)


class Teacher(db.Model):
    __tablename__ = "teacher"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), unique=True)


class Term(db.Model):
    __tablename__ = "term"

    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
