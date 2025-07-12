# @Filename: pet.py
# @Author: codists
# @Created: 2025-07-12 15:55:21
"""
flask-smorest demo
"""

# response 采用原始式
import marshmallow as ma
from flask_smorest import Blueprint, abort
from flask.views import MethodView

class ItemNotFoundError(Exception):
    """Custom exception for when a pet is not found."""
    pass

class Pet:
    _pets = []
    _id_counter = 1

    def __init__(self, name):
        self.id = Pet._id_counter
        self.name = name
        Pet._id_counter += 1

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    @classmethod
    def get(cls, filters=None):
        if not filters or not filters.get("name"):
            return [pet.to_dict() for pet in cls._pets]
        return [
            pet.to_dict()
            for pet in cls._pets
            if pet.name == filters["name"]
        ]

    @classmethod
    def get_by_id(cls, pet_id):
        for pet in cls._pets:
            if pet.id == int(pet_id):
                return pet
        raise ItemNotFoundError()

    @classmethod
    def create(cls, name):
        pet = Pet(name=name)
        cls._pets.append(pet)
        return pet.to_dict()

    def update(self, data):
        self.name = data.get("name", self.name)

    def commit(self):
        # No-op for in-memory
        pass

    @classmethod
    def delete(cls, pet_id):
        pet = cls.get_by_id(pet_id)
        cls._pets.remove(pet)



class PetSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String()

class PetQueryArgsSchema(ma.Schema):
    name = ma.fields.String()

bp = Blueprint("pets", "pets", url_prefix="/api/pets", description="Operations on pets")


@bp.route("/")
class Pets(MethodView):
    @bp.arguments(PetQueryArgsSchema, location="query")
    @bp.response(200, PetSchema(many=True))
    def get(self, args):
        """List pets"""
        return Pet.get(filters=args)

    @bp.arguments(PetSchema)
    @bp.response(201, PetSchema)
    def post(self, new_data):
        """Add a new pet"""
        print(111)
        item = Pet.create(**new_data)
        return item


@bp.route("/<pet_id>")
class PetsById(MethodView):
    @bp.response(200, PetSchema)
    def get(self, pet_id):
        """Get pet by ID"""
        try:
            item = Pet.get_by_id(pet_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        return item

    @bp.arguments(PetSchema)
    @bp.response(200, PetSchema)
    def put(self, update_data, pet_id):
        """Update existing pet"""
        try:
            item = Pet.get_by_id(pet_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        item.update(update_data)
        item.commit()
        return item

    @bp.response(204)
    def delete(self, pet_id):
        """Delete pet"""
        try:
            Pet.delete(pet_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

# response 采用封装式
# # @Filename: pet.py
# # @Author: codists
# # @Created: 2025-07-12 15:55:21
#
# import marshmallow as ma
# from flask_smorest import Blueprint, abort
# from flask.views import MethodView
#
#
# class ItemNotFoundError(Exception):
#     """Custom exception for when a pet is not found."""
#     pass
#
#
# class Pet:
#     _pets = []
#     _id_counter = 1
#
#     def __init__(self, name):
#         self.id = Pet._id_counter
#         self.name = name
#         Pet._id_counter += 1
#
#     def to_dict(self):
#         return {"id": self.id, "name": self.name}
#
#     @classmethod
#     def get(cls, filters=None):
#         if not filters or not filters.get("name"):
#             return [pet.to_dict() for pet in cls._pets]
#         return [
#             pet.to_dict()
#             for pet in cls._pets
#             if pet.name == filters["name"]
#         ]
#
#     @classmethod
#     def get_by_id(cls, pet_id):
#         for pet in cls._pets:
#             if pet.id == int(pet_id):
#                 return pet
#         raise ItemNotFoundError()
#
#     @classmethod
#     def create(cls, name):
#         pet = Pet(name=name)
#         cls._pets.append(pet)
#         return pet.to_dict()
#
#     def update(self, data):
#         self.name = data.get("name", self.name)
#
#     def commit(self):
#         # No-op for in-memory
#         pass
#
#     @classmethod
#     def delete(cls, pet_id):
#         pet = cls.get_by_id(pet_id)
#         cls._pets.remove(pet)
#
#
# # =========================
# # Schema definitions
# # =========================
#
# class PetSchema(ma.Schema):
#     id = ma.fields.Int(dump_only=True)
#     name = ma.fields.String()
#
#
# class PetQueryArgsSchema(ma.Schema):
#     name = ma.fields.String()
#
#
# class WrappedResponseSchema(ma.Schema):
#     code = ma.fields.Int()
#     message = ma.fields.String(allow_none=True)
#     data = ma.fields.Nested(PetSchema, allow_none=True)
#
#
# class WrappedListResponseSchema(ma.Schema):
#     code = ma.fields.Int()
#     message = ma.fields.String(allow_none=True)
#     data = ma.fields.List(ma.fields.Nested(PetSchema))
#
#
# # =========================
# # Response formatting helpers
# # =========================
#
# def make_response(data=None, code=200, message=None):
#     return {"code": code, "message": message, "data": data}, code
#
#
# def handle_item_not_found():
#     abort(404, message="Item not found.", data={"code": 404, "message": "Item not found.", "data": None})
#
#
# # =========================
# # Blueprint and Views
# # =========================
#
# bp = Blueprint("pets", "pets", url_prefix="/api/pets", description="Operations on pets")
#
#
# @bp.route("/")
# class Pets(MethodView):
#     @bp.arguments(PetQueryArgsSchema, location="query")
#     @bp.response(200, WrappedListResponseSchema)
#     def get(self, args):
#         """List pets"""
#         pets = Pet.get(filters=args)
#         return make_response(pets)
#
#     @bp.arguments(PetSchema)
#     @bp.response(201, WrappedResponseSchema)
#     def post(self, new_data):
#         """Add a new pet"""
#         item = Pet.create(**new_data)
#         return make_response(item, code=201)
#
#
# @bp.route("/<pet_id>")
# class PetsById(MethodView):
#     @bp.response(200, WrappedResponseSchema)
#     def get(self, pet_id):
#         """Get pet by ID"""
#         try:
#             item = Pet.get_by_id(pet_id)
#         except ItemNotFoundError:
#             return handle_item_not_found()
#         return make_response(item.to_dict())
#
#     @bp.arguments(PetSchema)
#     @bp.response(200, WrappedResponseSchema)
#     def put(self, update_data, pet_id):
#         """Update existing pet"""
#         try:
#             item = Pet.get_by_id(pet_id)
#         except ItemNotFoundError:
#             return handle_item_not_found()
#         item.update(update_data)
#         item.commit()
#         return make_response(item.to_dict())
#
#     @bp.response(204, WrappedResponseSchema)
#     def delete(self, pet_id):
#         """Delete pet"""
#         try:
#             Pet.delete(pet_id)
#         except ItemNotFoundError:
#             return handle_item_not_found()
#         return make_response(None, code=204)
