# Obarly - E-commerce Website

A Flask-based e-commerce website with MongoDB Atlas integration.

## Features
- Product catalog
- User authentication
- Shopping cart
- Order management
- Admin dashboard

## Tech Stack
- Flask
- MongoDB Atlas
- Python
- HTML/CSS/JavaScript

## Local Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file with:
   ```
   MONGODB_URI=mongodb+srv://nik84810:Niku_2004@obarly.xwq8r3k.mongodb.net/
   DATABASE_NAME=Inventory
   SECRET_KEY=your-secret-key-here
   ```
5. Run the application:
   ```bash
   python main.py
   ```

## Deployment

The application is deployed on Render. To deploy:

1. Push changes to GitHub
2. Render will automatically deploy the latest version
3. Environment variables are managed in Render dashboard

## Environment Variables

- `MONGODB_URI`: MongoDB Atlas connection string
- `DATABASE_NAME`: Database name (default: Inventory)
- `SECRET_KEY`: Flask secret key for session management

## Security Notes

- Never commit .env file
- Keep MongoDB credentials secure
- Use environment variables in production
