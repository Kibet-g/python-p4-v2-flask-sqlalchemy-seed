#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    # Create and initialize a Faker instance
    fake = Faker()

    # Delete all rows in the "pets" table
    Pet.query.delete()

    # List of possible pet species
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Generate 10 random pets
    pets = [
        Pet(name=fake.first_name(), species=rc(species)) 
        for _ in range(10)
    ]

    # Insert all generated pets into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()

    print("Database seeded successfully with 10 pets!")
