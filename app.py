from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ---------------------- MODELS ----------------------
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(50), nullable=False)


# ---------------------- ROUTES ----------------------
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        blood_group = request.form["blood_group"]
        phone = request.form["phone"]
        city = request.form["city"]

        new_donor = Donor(
            name=name,
            age=age,
            blood_group=blood_group,
            phone=phone,
            city=city
        )
        db.session.add(new_donor)
        db.session.commit()

        return redirect(url_for("register_success"))

    return render_template("register.html")


@app.route("/register/success")
def register_success():
    return render_template("register_success.html")


@app.route('/search', methods=["GET", "POST"])
def search():
    donors = []
    if request.method == "POST":
        blood_group = request.form["blood_group"]
        city = request.form["city"]

        donors = Donor.query.filter_by(
            blood_group=blood_group,
            city=city
        ).all()

    return render_template("search.html", donors=donors)


# ---------------------- MAIN ----------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
