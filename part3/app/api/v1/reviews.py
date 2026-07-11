from jsonschema.validators import validate

from app.services import facade
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource, fields

api = Namespace("reviews", description="Review operations")

# Define the review model for input validation and documentation
review_model = api.model(
    "Review",
    {
        "text": fields.String(required=True, description="Text of the review"),
        "rating": fields.Integer(
            required=True, description="Rating of the place (1-5)"
        ),
        "place_id": fields.String(required=True, description="ID of the place"),
    },
)


@api.route("/")
class ReviewList(Resource):
    @jwt_required()
    @api.expect(review_model, validate=True)
    @api.response(201, "Review successfully created")
    @api.response(400, "Invalid input data")
    @api.response(404, "Place or User not found")
    def post(self):
        """Register a new review"""
        review_data = api.payload
        place = facade.get_place(review_data["place_id"])
        user_id = get_jwt_identity()

        if not place:
            return {"error": "place not found"}, 404
        
        if place.owner_id == user_id:
            return {"error": "You cannot review your own place"}, 400

        reviews = facade.get_reviews_by_place(place.id)

        for review in reviews:
            if review.user_id == user_id:
                return {"error": "You have already reviewed this place"}, 400

        try:
            review_data["user_id"] = user_id 
            review = facade.create_review(review_data)
        except ValueError as e:
            return {"error": str(e)}, 400

        return review.as_dict(), 200

    @api.response(200, "List of reviews retrieved successfully")
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = []
        for review in facade.get_all_reviews():
            reviews.append(
                {
                    "id": review.id,
                    "text": review.text,
                    "rating": review.rating,
                }
            )

        return reviews, 200


@api.route("/<review_id>")
class ReviewResource(Resource):
    @api.response(200, "Review details retrieved successfully")
    @api.response(404, "Review not found")
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        print(review)
        if not review:
            return {"error": "review not found"}, 404

        return review.as_dict(), 200

    @jwt_required()
    @api.expect(review_model)
    @api.response(200, "Review updated successfully")
    @api.response(404, "Review not found")
    @api.response(400, "Invalid input data")
    @api.response(403, "Unauthorized")
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload
        user_id = get_jwt_identity()
        review = facade.get_review(review_id)

        if not review:
            return {"error": "Review not found"}, 404

        if review.user_id != user_id:
            return {"error": "Unauthorized action"}, 403

        try:
            review_data["user_id"] = user_id 
            facade.update_review(review_id, review_data)
        except ValueError as e:
            return {"error": str(e)}, 400

        return {"message": "review updated sucessfully"}, 200

    @api.response(200, "Review deleted successfully")
    @api.response(404, "Review not found")
    def delete(self, review_id):
        """Delete a review"""
        review = facade.get_review(review_id)

        if not review:
            return {"error": "review not found"}, 404

        facade.delete_review(review_id)
        return {"message": "review deleted sucessfully"}, 200
