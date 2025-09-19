"""
Database seeder to populate MongoDB with initial data
"""
import asyncio
from datetime import datetime
from .database import connect_to_mongo, get_database
from .models import Destination, Homestay, Guide, Handicraft, Itinerary

async def seed_destinations():
    """Seed destinations data"""
    database = get_database()
    if database is None:
        return
    
    destinations_data = [
        {
            "name": "Ranchi",
            "state": "Jharkhand",
            "description": "Capital city of Jharkhand, known for its waterfalls and tribal culture",
            "attractions": ["Hundru Falls", "Tagore Hill", "Rock Garden", "Patratu Valley", "Jonha Falls"],
            "popular_places": ["Hundru Falls", "Tagore Hill", "Rock Garden"],
            "image_url": "https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg",
            "coordinates": {"lat": 23.3441, "lng": 85.3096},
            "best_time_to_visit": "October to March",
            "climate": "Tropical"
        },
        {
            "name": "Deoghar",
            "state": "Jharkhand", 
            "description": "Sacred city known for Baidyanath Temple and spiritual significance",
            "attractions": ["Baidyanath Temple", "Tapovan", "Trikuta Hills", "Nandan Pahar", "Shivganga"],
            "popular_places": ["Baidyanath Temple", "Tapovan", "Trikuta Hills"],
            "image_url": "https://images.pexels.com/photos/161401/fushimi-inari-taisha-shrine-kyoto-japan-temple-161401.jpeg",
            "coordinates": {"lat": 24.4889, "lng": 86.7031},
            "best_time_to_visit": "July to March",
            "climate": "Tropical"
        },
        {
            "name": "Jamshedpur",
            "state": "Jharkhand",
            "description": "Steel city with beautiful parks and industrial heritage",
            "attractions": ["Jubilee Park", "Dimna Lake", "Tata Steel Zoological Park", "Dalma Wildlife Sanctuary", "Bhimbandh Wildlife Sanctuary"],
            "popular_places": ["Jubilee Park", "Dimna Lake", "Tata Steel Zoological Park"],
            "image_url": "https://images.pexels.com/photos/1386604/pexels-photo-1386604.jpeg",
            "coordinates": {"lat": 22.8046, "lng": 86.2029},
            "best_time_to_visit": "October to March",
            "climate": "Tropical"
        }
    ]
    
    # Clear existing destinations
    await database.destinations.delete_many({})
    
    # Insert new destinations
    for dest_data in destinations_data:
        destination = Destination(**dest_data)
        await database.destinations.insert_one(destination.dict())

async def seed_homestays():
    """Seed homestays data"""
    database = get_database()
    if database is None:
        return
    
    homestays_data = [
        {
            "name": "Village Heritage Stay",
            "location": "Ranchi Hills",
            "description": "Experience authentic tribal culture in a traditional village setting",
            "price_per_night": 1200.0,
            "amenities": ["WiFi", "Local Meals", "Cultural Tours", "Parking"],
            "host_name": "Sunita Devi",
            "host_phone": "+91-9876543210",
            "coordinates": {"lat": 23.3441, "lng": 85.3096},
            "images": ["https://images.pexels.com/photos/1374125/pexels-photo-1374125.jpeg"]
        },
        {
            "name": "Eco Tribal Retreat",
            "location": "Netarhat",
            "description": "Sustainable living experience with organic farming and nature walks",
            "price_per_night": 1800.0,
            "amenities": ["Organic Garden", "Nature Walks", "Tribal Cuisine", "Eco-friendly"],
            "host_name": "Ravi Kumar",
            "host_phone": "+91-9876543211",
            "coordinates": {"lat": 23.5000, "lng": 84.5000},
            "images": ["https://images.pexels.com/photos/1029599/pexels-photo-1029599.jpeg"]
        }
    ]
    
    # Clear existing homestays
    await database.homestays.delete_many({})
    
    # Insert new homestays
    for homestay_data in homestays_data:
        homestay = Homestay(**homestay_data)
        await database.homestays.insert_one(homestay.dict())

async def seed_guides():
    """Seed guides data"""
    database = get_database()
    if database is None:
        return
    
    guides_data = [
        {
            "name": "Arjun Singh",
            "speciality": "Wildlife & Tribal Culture",
            "languages": ["Hindi", "English", "Santhali"],
            "experience_years": 8,
            "phone": "+91-9876543212",
            "email": "arjun@example.com",
            "description": "Expert in wildlife photography and tribal culture with 8 years of experience",
            "price_per_day": 800.0
        },
        {
            "name": "Meera Kumari",
            "speciality": "Heritage & Temples",
            "languages": ["Hindi", "English"],
            "experience_years": 5,
            "phone": "+91-9876543213",
            "email": "meera@example.com",
            "description": "Specialized in heritage tours and temple visits with deep local knowledge",
            "price_per_day": 600.0
        }
    ]
    
    # Clear existing guides
    await database.guides.delete_many({})
    
    # Insert new guides
    for guide_data in guides_data:
        guide = Guide(**guide_data)
        await database.guides.insert_one(guide.dict())

async def seed_handicrafts():
    """Seed handicrafts data"""
    database = get_database()
    if database is None:
        return
    
    handicrafts_data = [
        {
            "name": "Tribal Dokra Art",
            "description": "Handcrafted bronze figurine using ancient lost-wax casting technique",
            "price": 2500.0,
            "category": "Metal Art",
            "artist_name": "Kailash Mahato",
            "artist_phone": "+91-9876543214",
            "images": ["https://images.pexels.com/photos/1070945/pexels-photo-1070945.jpeg"],
            "materials_used": ["Bronze", "Clay", "Wax"]
        },
        {
            "name": "Sohrai Painting",
            "description": "Traditional tribal wall art depicting nature and animals",
            "price": 1200.0,
            "category": "Painting",
            "artist_name": "Baua Devi",
            "artist_phone": "+91-9876543215",
            "images": ["https://images.pexels.com/photos/1045114/pexels-photo-1045114.jpeg"],
            "materials_used": ["Natural Colors", "Rice Paste", "Clay"]
        }
    ]
    
    # Clear existing handicrafts
    await database.handicrafts.delete_many({})
    
    # Insert new handicrafts
    for handicraft_data in handicrafts_data:
        handicraft = Handicraft(**handicraft_data)
        await database.handicrafts.insert_one(handicraft.dict())

async def seed_itineraries():
    """Seed itineraries data"""
    database = get_database()
    if database is None:
        return
    
    itineraries_data = [
        {
            "title": "3-Day Wildlife Adventure",
            "description": "Explore the rich wildlife of Jharkhand with expert guides",
            "duration_days": 3,
            "places": ["Betla National Park", "Palamau Tiger Reserve", "Hazaribagh Wildlife Sanctuary"],
            "highlights": ["Tiger Spotting", "Bird Watching", "Nature Photography", "Jungle Safari"],
            "difficulty_level": "Medium",
            "price_estimate": 5000.0
        },
        {
            "title": "Cultural Heritage Trail",
            "description": "Discover the rich cultural heritage and traditions of Jharkhand",
            "duration_days": 5,
            "places": ["Baidyanath Temple", "Tagore Hill", "Tribal Villages", "Craft Centers"],
            "highlights": ["Temple Visits", "Tribal Interactions", "Craft Workshops", "Cultural Performances"],
            "difficulty_level": "Easy",
            "price_estimate": 8000.0
        }
    ]
    
    # Clear existing itineraries
    await database.itineraries.delete_many({})
    
    # Insert new itineraries
    for itinerary_data in itineraries_data:
        itinerary = Itinerary(**itinerary_data)
        await database.itineraries.insert_one(itinerary.dict())

async def seed_all_data():
    """Seed all data into the database"""
    print("🌱 Starting database seeding...")
    
    await connect_to_mongo()
    
    try:
        await seed_destinations()
        print("✅ Destinations seeded")
        
        await seed_homestays()
        print("✅ Homestays seeded")
        
        await seed_guides()
        print("✅ Guides seeded")
        
        await seed_handicrafts()
        print("✅ Handicrafts seeded")
        
        await seed_itineraries()
        print("✅ Itineraries seeded")
        
        print("🎉 Database seeding completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during seeding: {e}")
    finally:
        from .database import close_mongo_connection
        await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(seed_all_data())
