from app.services import facade
from flask_restx import Namespace, Resource, fields

api = Namespace("amenities", description="Amenity operations")

# Define the amenity model for input validation and documentation
amenity_model = api.model(
    "Amenity", {"name": fields.String(required=True, description="Name of the amenity")}
)


@api.route("/")
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, "Amenity successfully created")
    @api.response(400, "Invalid input data")
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload

        try:
            new_amenity = facade.create_amenity(amenity_data)
        except ValueError as e:
            return {"error": str(e)}, 400

        return new_amenity.as_dict(), 201

    @api.response(200, "List of amenities retrieved successfully")
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = [a.as_dict() for a in facade.get_all_amenities()]
        return amenities


@api.route("/<amenity_id>")
class AmenityResource(Resource):
    @api.response(200, "Amenity details retrieved successfully")
    @api.response(404, "Amenity not found")
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)

        if not amenity:
            return {"error": "amenity not found"}, 404

        return amenity.as_dict(), 200

    @api.expect(amenity_model, validate=True)
    @api.response(200, "Amenity updated successfully")
    @api.response(404, "Amenity not found")
    @api.response(400, "Invalid input data")
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data = api.payload
        name = amenity_data.get("name")

        if not name.strip():
            return {"error": "Name cannot be empty"}, 400

        if len(name) > 50:
            return {"error": "Name has a maximum length of 50 characters"}, 400

        amenity = facade.update_amenity(amenity_id, amenity_data)

        if not amenity:
            return {"error": "amenity not found"}, 404

        return amenity.as_dict(), 200
