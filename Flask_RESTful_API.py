from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to-do-database.db'
db = SQLAlchemy(app)



class ToDoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    importance = db.Column(db.Integer, nullable=False)
     
    def __rppr__(self):
        print(f"id =  {self.id}, task =  {self.task}, importance = , {self.importance}")
     


parser = reqparse.RequestParser()
parser.add_argument('Desc', type=str, help='Description of Task', required = True)
parser.add_argument('Importance', type=int, help='Level of Importance', required = True)


resource_fields = {
	'id': fields.Integer,
	'task': fields.String,
	'importance': fields.Integer
}

class TaskModel(Resource):

    @marshal_with(resource_fields)
    def get(self, id):

        result = ToDoModel.query.filter_by(id=id).first()

        if not result:
            abort(404, message="Could not find a task with that id")
        return result
    

    @marshal_with(resource_fields)
    def put(self, id):
        #args = parser.parse_args(strict=True)

        result = ToDoModel.query.filter_by(id=id).first()

        if result:
            abort(404, message="A task already exists with that ID")


        entry = ToDoModel(id = id, task = request.form["Desc"], importance = request.form["Importance"])

        db.session.add(entry)
        db.session.commit()

        return entry, 201

    @marshal_with(resource_fields)
    def patch(self, id):
        #args = parser.parse_args()

        result = ToDoModel.query.filter_by(id=id).first()

        if not result:
            abort(404, message="Task doesn't exist, cannot update")


        result.ids = id
        result.task = request.form["Desc"]
        result.importance = request.form["Importance"]

        db.session.commit()

        return result, 201



    @marshal_with(resource_fields)
    def delete(self, id):

        #args = parser.parse_args()

        result = ToDoModel.query.filter_by(id=id).first()

        if not result:
            abort(404, message="Task doesn't exist, cannot delte")

        
        db.session.delete(result)
        db.session.commit()
        
        return 201



api.add_resource(TaskModel, '/id/<int:id>')


if __name__ == "__main__":
        
    app.run(debug=True)

    #with app.app_context():
        #db.create_all()  
        #app.run(debug=True)

