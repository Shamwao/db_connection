from operator import truediv
from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data ['created_at']
        self.upated_at = data ['updated_at']
    
    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['first_name']) < 1:
            flash("First name required.")
            is_valid = False
        if len(user['last_name']) < 1:
            flash("Last name required.")
            is_valid = False
        if len(user['email']) < 1 :
            flash("Email required")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_email(user):
        is_valid=True
        if not EMAIL_REGEX.match(user['email']):
            flash("Valid email address required")
            is_valid = False
        return is_valid
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL('users').query_db(query)
        users = []
        for u in result:
            users.append( cls(u) )                       
        return users
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users').query_db(query, data)
        return result[0]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        result = connectToMySQL('users').query_db(query, data)
        return result

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users').query_db(query, data)
        return result

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query, data)
