# Tourism India Backend

A FastAPI backend for the Tourism India mobile application with MongoDB database integration.

## Features

- **Authentication**: JWT-based authentication with role-based access control
- **Destinations**: Manage tourist destinations with detailed information
- **Marketplace**: Homestays, guides, and handicrafts
- **Itineraries**: Pre-planned travel itineraries
- **AI Assistant**: Chat-based travel assistance
- **MongoDB**: NoSQL database for flexible data storage

## Prerequisites

- Python 3.8+
- MongoDB 4.4+
- pip (Python package manager)

## Quick Setup

### Option 1: Automated Setup
```bash
cd backend
python setup_database.py
```

### Option 2: Manual Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start MongoDB**
   - **Windows**: `net start MongoDB`
   - **macOS**: `brew services start mongodb-community`
   - **Linux**: `sudo systemctl start mongod`

3. **Seed Database**
   ```bash
   python -m app.seed_data
   ```

4. **Start Server**
   ```bash
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `POST /auth/dummy-login` - Dummy login for testing
- `GET /auth/me` - Get current user info

### Destinations
- `GET /destinations` - List all destinations
- `GET /destinations/{id}` - Get specific destination
- `POST /destinations` - Create destination (Admin)

### Marketplace
- `GET /marketplace/homestays` - List homestays
- `GET /marketplace/guides` - List guides
- `GET /marketplace/handicrafts` - List handicrafts

### Itineraries
- `GET /itineraries` - List itineraries
- `GET /itineraries/{id}` - Get specific itinerary

### Assistant
- `POST /assistant/chat` - Chat with AI assistant

## Database Schema

### Collections
- `users` - User accounts and profiles
- `destinations` - Tourist destinations
- `homestays` - Accommodation listings
- `guides` - Local guide profiles
- `handicrafts` - Local craft products
- `itineraries` - Travel itineraries
- `bookings` - User bookings
- `reviews` - User reviews and ratings

## Environment Variables

Create a `.env` file in the backend directory:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=tourism_india
SECRET_KEY=your-secret-key-here
```

## Testing

### Dummy Login Credentials
- **Tourist**: `tourist@example.com` / `tourist123`
- **Guide**: `guide@example.com` / `guide123`
- **Business**: `business@example.com` / `business123`
- **Admin**: `admin@example.com` / `admin123`

### Test API
```bash
# Health check
curl http://localhost:8000/health

# Get destinations
curl http://localhost:8000/destinations

# Dummy login
curl -X POST http://localhost:8000/auth/dummy-login \
  -H "Content-Type: application/json" \
  -d '{"email": "tourist@example.com", "password": "tourist123", "role": "tourist"}'
```

## Development

### Project Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app
│   ├── database.py          # MongoDB connection
│   ├── models.py            # Pydantic models
│   ├── auth.py              # Authentication utilities
│   ├── seed_data.py         # Database seeder
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Authentication routes
│       ├── destinations.py  # Destination routes
│       ├── marketplace.py   # Marketplace routes
│       ├── itineraries.py   # Itinerary routes
│       └── assistant.py     # AI assistant routes
├── requirements.txt
├── setup_database.py
└── README.md
```

### Adding New Features
1. Create models in `models.py`
2. Add routes in appropriate router file
3. Update database seeder if needed
4. Test with API endpoints

## Troubleshooting

### MongoDB Connection Issues
- Ensure MongoDB is running: `mongosh` or `mongo`
- Check connection string in `database.py`
- Verify MongoDB service is started

### Import Errors
- Install dependencies: `pip install -r requirements.txt`
- Check Python path and virtual environment

### Database Errors
- Clear database: `mongosh tourism_india --eval "db.dropDatabase()"`
- Re-seed database: `python -m app.seed_data`

## Production Deployment

1. Set secure `SECRET_KEY` in environment
2. Use production MongoDB instance
3. Configure proper CORS settings
4. Set up SSL/TLS certificates
5. Use process manager (PM2, systemd)
6. Set up monitoring and logging

## License

MIT License - see LICENSE file for details
