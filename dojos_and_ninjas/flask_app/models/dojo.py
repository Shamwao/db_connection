from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo: 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result

    @classmethod 
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos = []
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        for d in result:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(result[0])
        for row in result:
            ninja_data = {
                "id": row['ninjas.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
