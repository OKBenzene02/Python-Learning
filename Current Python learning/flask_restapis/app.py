import json
import flask
from flask import Flask, abort
from flask_restful import Api, reqparse, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trails.db'
db = SQLAlchemy(app)
BASE = "http://127.0.0.1:5000/"

# Orders Database for storing the incoming orders
class TrailsDB(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    product1 = db.Column(db.String(100), nullable=True)
    product2 = db.Column(db.String(100), nullable=True)
    product3 = db.Column(db.String(100), nullable=True)
    pincode = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.String(), nullable=False)
    timeslots = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Trails [Unique ID={self.id}, UserID = {self.user_id}, Product1 = {self.product1}, " \
               f"Product2 = {self.product2}, Product3 = {self.product3}, Pincode = {self.pincode}, " \
               f"Date={self.date}, Timeslots={self.timeslots}]"


# Slots Database is for storing Products and their respective details of availability, timeslots, orders and date
class SlotsDB(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    timeslots = db.Column(db.String(), nullable=False)
    available = db.Column(db.String(), nullable=False)
    avail_count = db.Column(db.Integer(), nullable=False)
    order_one = db.Column(db.Integer(), nullable=True)
    order_two = db.Column(db.Integer(), nullable=True)
    order_three = db.Column(db.Integer(), nullable=True)

    def __repr__(self):
        return f"Slots [Unique ID={self.id}, Product = {self.product}, " \
               f"Date = {self.date}, Timeslots={self.timeslots}, Availability = {self.available} " \
               f"Count = {self.avail_count}, Order1 = {self.order_one}, Order2 = {self.order_two}" \
               f"Order3 = {self.order_three}]"

# Pincode database for calculating the distance and classifying the zone for the incoming orders based on their respective match
# in the Orders Database. When ever a new product is received in the Orders Database based on the product name, and its available
# timeslots we give out the list of products that can be accommodated.
class PincodeDB(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    pincode1 = db.Column(db.Integer(), nullable=False)
    pincode2 = db.Column(db.Integer(), nullable=False)
    distance = db.Column(db.Integer(), nullable=False)
    zone = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f"Pincode [Unique ID={self.id}, Pincode1 = {self.pincode1}, " \
               f"Pincode2 = {self.pincode2}, Distance = {self.distance}, Zone = {self.zone}]"

# Requested arguments that can be parsed from the incoming json data from the testapi file.
add_details_args = reqparse.RequestParser()

# Unique id's for tables Orders Table, Slots Table, Pincode Table
add_details_args.add_argument("orderid", type=int, help="Primary ID")

# Here userid can be multiple users ordering different or same product
add_details_args.add_argument("user_id", type=int, help="User ID")

add_details_args.add_argument("slotid", type=int, help="Slot ID")
add_details_args.add_argument("pinid", type=int, help="Pincode ID")

# Product arguments that are created for various tables
add_details_args.add_argument("product", type=str, help="Product in Order details")
add_details_args.add_argument("product1", type=str, help="Product ID")
add_details_args.add_argument("product2", type=str, help="Product ID")
add_details_args.add_argument("product3", type=str, help="Product ID")

# Pincode arguments for the pincode table
add_details_args.add_argument("pincode", type=int, help="Pincode")
add_details_args.add_argument("pincode1", type=int, help="Pincode 1 Capture")
add_details_args.add_argument("pincode2", type=int, help="Pincode 2 Capture")
add_details_args.add_argument("date", type=str, help="Date of Product Trial")
add_details_args.add_argument("zone", type=int, help='Zone as per the pin codes')

# Required details for a product to be classified as different from other products
add_details_args.add_argument("timeslots", type=str, help="Time slots to try the product")
add_details_args.add_argument("distance", type=int, help="Distance between two pincodes")
add_details_args.add_argument("available", type=str, help="Availability of the product")
add_details_args.add_argument("avail_count", type=int, help="Number of trail products")
add_details_args.add_argument("orderone", type=int, help="First order of the trail product")
add_details_args.add_argument("ordertwo", type=int, help="Second order of the trail product")
add_details_args.add_argument("orderthree", type=int, help="Third order of the trail product")
add_details_args.add_argument('placedID', type=int, help='Order ID created when a new order is placed')

# Marshal fields for current implementation is not required...... these serialize the json outputs
resource_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "product": fields.String,
    "pincode": fields.Integer,
    "date": fields.String,
    "timeslots": fields.String,
    "zone": fields.Integer,
}

# CRUD methods
class TrailsAPI(Resource):
    # @marshal_with(resource_fields)
    def get(self, user_id, product_id, pincode):

        # Set of conditions for error handling a request.
        if len(product_id) > 100: abort(500, 'Chars too long to process....')

        product_list = product_id.split(',')
        if len(product_list) > 3: abort(500, "More than 3 Products were requested....")

        # When a user requests for multiple products, we use split method to create a list of products.
        # for ex- request -
        # http://127.0.0.1:5000/shopify/2/Apple_iPhone_14 Pro Max_512GB_Gold,Oppo_f21s-pro 5g,vivo-Y72-5G-8-128-Black/500007
        # now the address is parsed such that [2, - incoming user-id
        # [Apple_iPhone_14 Pro Max_512GB_Gold, Oppo_f21s-pro 5g, vivo-Y72-5G-8-128-Black], - products of request user
        # 500007 - pincode of the requested user]
        products = list()
        products_list = product_id.split(',')

        # Based on the requested product we create a list of all the products and their details from the Slots table
        products.extend(SlotsDB.query.filter(SlotsDB.product.in_(product_list)).all())

        if not products:
            abort(404, "Data not found")

        # When multiple orders are received.
        # Case - 1 when Orders table is empty we tend to give out all the possible details regarding the products
        # Case - 2 when second order is received we need to check
        # if the current pincode starts with a specified digit and get all the pin-codes that start with that
        # starting digit. After getting those records check for the distance and give out the date and timeslots for the
        # required request.

        firstdigit = int(str(pincode)[0])
        zone = 0
        similar_pincodes = PincodeDB.query.filter(PincodeDB.pincode1.startswith(firstdigit)).all()
        if similar_pincodes:
            for pincodes in similar_pincodes:
                if pincodes.pincode1 <= pincode <= pincodes.pincode2:
                    zone = pincodes.zone
                    print("Current zone ", zone)
                    break

            print("Yes there are records that have pincodes in this range......")

        # JSON serializing with conditions for specific cases
        serialized_products = []
        # This loop is for traversing all the products that were retrieved from the Slots table that matches the incoming request.
        for i, product in enumerate(products):
            date = None
            product.timeslots = product.timeslots
            product.avail_count = product.avail_count
            product.available = product.available
            product.order_one = product.order_one
            product.order_two = product.order_two
            product.order_three = product.order_three

            # Checking if the current zone is 1 based on their pincode.
            if int(zone) == 1:
                date = "D1"
                product.timeslots = product.timeslots if product.available == 'yes' else 'no'

            # This condition is executed when the zone is farther from the orders available in the Orders Table
            else:
                date = "D" + str(zone - 1)
                product.avail_count = 3
                product.order_one, product.order_two, product.order_three = [None] * 3
                product.available = 'yes'
                if i == 0:
                    product.timeslots = 'no'
                    product.available = 'no'
                    product.order_one, product.order_two, product.order_three = ["Not available"] * 3

            serialized_product = {
                "product": product.product,
                "date": date,
                "timeslots": product.timeslots,
                "available": product.available,
                "avail_count": product.avail_count,
                "order_one": product.order_one,
                "order_two": product.order_two,
                "order_three": product.order_three
            }
            serialized_products.append(serialized_product)

        return serialized_products

    # @marshal_with(resource_fields)
    def put(self, user_id, product_id, pincode):

        # Parsing the incoming data requests
        args = add_details_args.parse_args()

        # When same data is being added to the database we stop that request from being added by aborting it
        user_id = TrailsDB.query.filter_by(id=user_id).first()
        if user_id:
            abort(409, "User already added......")

        slots_id = SlotsDB.query.filter_by(id=args['slotid']).first()
        if slots_id:
            abort(409, "Slot already already added......")

        pinid = PincodeDB.query.filter_by(id=args['pinid']).first()
        if pinid:
            abort(409, "Pincode already added......")

        # Adding the pincode, timeslots, products details to the Orders database by considering multiple products
        # These set of conditions check whether the incoming request was given for one product or two products or three products.
        # after execution of these conditions we try to add the incoming request to the database.
        details, slots, pincodedb = None, None, None
        products_list = product_id.split(',')
        if len(products_list) > 2: product_one, product_two, product_three = products_list
        elif len(products_list) == 2: product_one, product_two = products_list; product_three = None
        else: product_one = products_list[0]; product_two = None; product_three = None
        print(products_list)

        # Adding Order details to the Database
        # These specific conditions are triggered when parsed requests contain the available data.

        # For classifying the incoming request as to store the data in Orders Table we use "User id", "Products requested" and
        # "Pincode of the request".
        if args['user_id'] and products_list and pincode:
            details = TrailsDB(id=user_id, user_id=args['user_id'],
                               product1=product_one,
                               product2=product_two, product3=product_three, pincode=args['pincode'],
                               date=args['date'], timeslots=args['timeslots'])
            for prod_slots in products_list:
                slot = SlotsDB.query.filter_by(product=prod_slots, timeslots=args['timeslots']).first()

                # Check for the records that have a specific pincode which falls in the range
                # If the pincode does not fall in that range then give out the default pincodes
                if slot and slot.avail_count != 0:
                    slot.avail_count -= 1
                    if not slot.order_one:
                        slot.order_one = args['placedID']
                        print("Order 1 is placed........")
                    elif not slot.order_two:
                        slot.order_two = args['placedID']
                        print("Order 2 is placed........")
                    else:
                        slot.order_three = args['placedID']
                        print("Order 3 is placed........")
                if slot and slot.avail_count == 0:
                    slot.available = "no"
                    print("Slot is not available..........")
            db.session.add(details)
            print("Order Details Have been added.......")

        # Adding Slots to the Database this condition is classified for adding the data for Slots table. This condition
        # checks for any one of the products availability and their slot id with order id's
        if args['orderone'] or args['ordertwo'] or args['orderthree'] or args['available'] and args['slotid']:
            slots = SlotsDB(id=args['slotid'], product=args['product'], date=args['date'], timeslots=args['timeslots'],
                            available=args['available'], avail_count=args['avail_count'], order_one=args['orderone'],
                            order_two=args['ordertwo'], order_three=args['orderthree'])
            db.session.add(slots)
            print("Slots Have been added.......")

        # Adding Pincode details to the Database this condition is classified for adding the data for Pincode table. This
        # condition is triggered when pin-codes and their pin-code ids are satisfied
        if args['pincode1'] and args['pincode2'] and args['pinid']:
            pincodedb = PincodeDB(id=args['pinid'], pincode1=args['pincode1'], pincode2=args['pincode2'],
                                  distance=args['distance'], zone=args['zone'])
            db.session.add(pincodedb)
            print("Pincodes Have been added............")
        db.session.commit()
        return f"details {details}\nslots {slots}\npincode {pincodedb}", 201

    # This method is not implemented completely.......
    def delete(self, user_id, product_id, pincode):
        user = TrailsDB.query.filter_by(user_id=user_id).first()
        if not user: abort(404, message="Requested User is not found....")
        db.session.delete(user)
        db.session.commit()
        return "Deleted successfully...", 404


api.add_resource(TrailsAPI, '/shopify/<int:user_id>/<string:product_id>/<int:pincode>')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
