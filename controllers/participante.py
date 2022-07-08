from flask_restful import Resource


class ParticipanteController(Resource):
    # esta clase se comportará como un controlador, es decir, que si definimos un método llamado get
    def get(self):
        return {
            'message': 'Ingreso al get'
        }
