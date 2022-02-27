from flask import Flask
from flask_restful import Api,Resource,abort,reqparse
from flask_cors import CORS

sample_data_fruit = {
    'apple': 'red',
    'banana': 'yellow',
    'peach': 'pink' 
}
sample_data_animal = {
    'giraffe': 'yellow',
    'flamingo': 'pink',
    'crow' : 'black'
}
app = Flask(__name__)
api = Api(app)
CORS(app,supports_credentials=True)

class Sample(Resource):
    def get(self):
        parser =reqparse.RequestParser()
        parser.add_argument("fruit")
        parser.add_argument("animal")
        args = parser.parse_args()
        return {"data":{
            "fruit_color":sample_data_fruit.get(args["fruit"],'no data'),
            "animal_color":sample_data_animal.get(args["animal"],'no data')
        } }

api.add_resource(Sample,"/")

if __name__ == "__main__":
    #app.run(host='127.0.0.1',port=8888)
    app.run()