#!/usr/bin/env python
"""
Script to initialize admin user in the database
Run this once to create an admin account
"""

from app import app
from Application.models import User, db

def init_admin():
    with app.app_context():
        # Check if admin already exists
        admin_exists = User.query.filter_by(type='admin').first()
        
        if admin_exists:
            print(f"Admin user already exists: {admin_exists.username}")
            return
        
        # Create admin user
        admin_user = User(
            username='admin',
            email='admin@ecard.com',
            password='admin123',
            type='admin'
        )
        
        db.session.add(admin_user)
        db.session.commit()
        
        print("✓ Admin user created successfully!")
        print(f"  Username: admin")
        print(f"  Password: admin123")
        print(f"  Email: admin@ecard.com")

if __name__ == '__main__':
    init_admin()
