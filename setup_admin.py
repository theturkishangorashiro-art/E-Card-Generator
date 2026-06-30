#!/usr/bin/env python
"""
Direct database setup script for admin user
Run this once to create admin credentials directly in the database
"""

from app import app
from Application.models import User, db

def setup_admin_user():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Check if admin already exists
        admin_user = User.query.filter_by(type='admin').first()
        
        if admin_user:
            print(f"✓ Admin user already exists!")
            print(f"  Username: {admin_user.username}")
            print(f"  Email: {admin_user.email}")
            return
        
        # Create new admin user
        new_admin = User(
            username='admin',
            email='admin@ecard.com',
            password='admin@123',
            type='admin'
        )
        
        db.session.add(new_admin)
        db.session.commit()
        
        print("✓ Admin user created successfully in database!")
        print("\n" + "="*50)
        print("Admin Login Credentials:")
        print("="*50)
        print(f"Username: admin")
        print(f"Password: admin@123")
        print(f"Email:    admin@ecard.com")
        print("="*50)
        print("\nYou can now:")
        print("1. Go to http://localhost:5000/login")
        print("2. Enter username: admin")
        print("3. Enter password: admin@123")
        print("4. You will be redirected to /admin dashboard")

if __name__ == '__main__':
    setup_admin_user()
