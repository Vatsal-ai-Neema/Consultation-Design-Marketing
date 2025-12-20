import os
from PIL import Image
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, Project, Client, Contact, Subscriber
from flask_admin.form import FileUploadField
from wtforms import StringField

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def crop_and_save(image_file):
    filename = secure_filename(image_file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)

    img = Image.open(image_file)

    # FIX: Convert RGBA / P mode images to RGB
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img = img.resize((450, 350))
    img.save(path, format="JPEG")

    return filename

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)

with app.app_context():
    db.create_all()

admin = Admin(app, name="Admin Panel")
class ProjectAdmin(ModelView):
    form_extra_fields = {
        'image_upload': FileUploadField(
            'Upload Image',
            base_path='static/uploads',
            relative_path='uploads/'
        ),
        'image_url': StringField('Image URL')
    }

    def on_model_change(self, form, model, is_created):
        if form.image_upload.data:
            model.image = crop_and_save(form.image_upload.data)
        elif form.image_url.data:
            model.image = form.image_url.data


class ClientAdmin(ModelView):
    form_extra_fields = {
        'image_upload': FileUploadField(
            'Upload Image',
            base_path='static/uploads',
            relative_path='uploads/'
        ),
        'image_url': StringField('Image URL')
    }

    def on_model_change(self, form, model, is_created):
        if form.image_upload.data:
            model.image = crop_and_save(form.image_upload.data)
        elif form.image_url.data:
            model.image = form.image_url.data

admin.add_view(ProjectAdmin(Project, db.session))
admin.add_view(ClientAdmin(Client, db.session))
admin.add_view(ModelView(Contact, db.session))
admin.add_view(ModelView(Subscriber, db.session))

@app.route("/", methods=["GET"])
def index():
    projects = Project.query.all()
    clients = Client.query.all()

    return render_template(
        "index.html",
        projects=projects,
        clients=clients
    )

@app.route("/contact", methods=["POST"])
def contact():
    data = request.form
    c = Contact(
        name=data["name"],
        email=data["email"],
        mobile=data["mobile"],
        city=data["city"]
    )
    db.session.add(c)
    db.session.commit()
    return redirect("/")

@app.route("/subscribe", methods=["POST"])
def subscribe():
    s = Subscriber(email=request.form["email"])
    db.session.add(s)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run()
