#!/usr/bin/env python3
"""
Simple Blog Automation API for May Marketing SEO
Mock API for testing Railway deployment
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

# Mock client data for May Marketing SEO
CLIENTS = {
    "May Marketing SEO": {
        "industry": "Digital Marketing",
        "location": "Lebanon, OH",
        "services": ["SEO", "Web Design", "Content Marketing"],
        "blog_collection_id": "may-marketing-blog"
    },
    "Cowboy Property Restoration": {
        "industry": "Property Restoration",
        "location": "Cincinnati, OH",
        "services": ["Water Damage", "Fire Damage", "Mold Remediation"],
        "blog_collection_id": "cowboy-restoration-blog"
    },
    "Pool Scouts Dayton": {
        "industry": "Pool Services",
        "location": "Dayton, OH",
        "services": ["Pool Cleaning", "Maintenance", "Repairs"],
        "blog_collection_id": "pool-scouts-blog"
    },
    "Mastercraft Home Remodeling": {
        "industry": "Home Remodeling",
        "location": "Northern Kentucky",
        "services": ["Kitchen Remodeling", "Bathroom Remodeling", "Additions"],
        "blog_collection_id": "mastercraft-blog"
    },
    "Scheffer Contracting": {
        "industry": "Construction",
        "location": "Cincinnati, OH",
        "services": ["Commercial Construction", "Residential Construction", "Renovations"],
        "blog_collection_id": "scheffer-blog"
    },
    "RGV Roofing": {
        "industry": "Roofing",
        "location": "Rio Grande Valley, TX",
        "services": ["Roof Installation", "Roof Repair", "Storm Damage"],
        "blog_collection_id": "rgv-roofing-blog"
    },
    "Inception Pools": {
        "industry": "Pool Construction",
        "location": "Austin, TX",
        "services": ["Pool Design", "Pool Construction", "Outdoor Living"],
        "blog_collection_id": "inception-pools-blog"
    }
}

@app.route('/')
def home():
    """API documentation"""
    return jsonify({
        "service": "Blog Automation API",
        "status": "ready",
        "version": "1.0",
        "clients": len(CLIENTS),
        "endpoints": {
            "GET /": "This documentation",
            "GET /health": "Health check",
            "GET /clients": "List all clients",
            "GET /client/<name>": "Get client details",
            "POST /generate-blog": "Generate a blog post for a client"
        }
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/clients')
def get_clients():
    """Get list of all clients"""
    return jsonify({
        "clients": list(CLIENTS.keys()),
        "count": len(CLIENTS)
    })

@app.route('/client/<name>')
def get_client(name):
    """Get details for a specific client"""
    if name in CLIENTS:
        client_data = CLIENTS[name].copy()
        client_data["name"] = name
        return jsonify(client_data)
    return jsonify({"error": "Client not found"}), 404

@app.route('/generate-blog', methods=['POST'])
def generate_blog():
    """Generate a blog post for a client"""
    data = request.json or {}
    client_name = data.get('name', 'Unknown Client')
    
    # Blog topic templates
    topic_templates = [
        "Top {year} Trends in {industry}",
        "How to Choose the Right {service} Provider in {location}",
        "Common {industry} Mistakes to Avoid",
        "The Benefits of Professional {service}",
        "Understanding {industry} Best Practices",
        "{season} {service} Tips for Homeowners",
        "Why {location} Businesses Choose Professional {service}",
        "The Complete Guide to {service} in {year}"
    ]
    
    # Generate blog content
    client_info = CLIENTS.get(client_name, {})
    industry = client_info.get("industry", "Business")
    service = random.choice(client_info.get("services", ["Services"]))
    location = client_info.get("location", "Your Area")
    
    # Current date info
    now = datetime.now()
    season = ["Winter", "Spring", "Summer", "Fall"][(now.month-1)//3]
    year = now.year
    
    # Select and format topic
    topic_template = random.choice(topic_templates)
    topic = topic_template.format(
        year=year,
        season=season,
        industry=industry,
        service=service,
        location=location
    )
    
    # Generate mock blog content
    blog_content = f"""# {topic}

In today's competitive market, businesses in {location} need to stay ahead of the curve when it comes to {industry.lower()}. At {client_name}, we understand the unique challenges faced by local businesses and homeowners.

## Introduction

{service} is more than just a service—it's an investment in your property's future. Whether you're a homeowner or business owner in {location}, understanding the importance of professional {service.lower()} can save you time, money, and stress.

## Key Benefits

1. **Professional Expertise**: Our team brings years of experience in {industry.lower()}.
2. **Local Knowledge**: We understand the specific needs of {location} properties.
3. **Quality Guarantee**: All our {service.lower()} services come with comprehensive warranties.
4. **Cost-Effective Solutions**: Professional service prevents costly future repairs.

## Why Choose {client_name}?

As a leading {industry.lower()} company in {location}, we pride ourselves on:

- Exceptional customer service
- Transparent pricing
- Timely project completion
- Licensed and insured professionals
- State-of-the-art equipment and techniques

## Conclusion

Don't wait until small issues become major problems. Contact {client_name} today for a free consultation and discover why we're {location}'s trusted choice for {service.lower()}.

Call us today or visit our website to schedule your appointment!
"""
    
    return jsonify({
        "success": True,
        "title": topic,
        "content": blog_content.strip(),
        "metadata": {
            "client": client_name,
            "industry": industry,
            "service": service,
            "location": location,
            "generated_at": datetime.now().isoformat(),
            "word_count": len(blog_content.split()),
            "reading_time": f"{len(blog_content.split()) // 200} min",
            "seo_keywords": [
                f"{service} {location}",
                f"{industry} services",
                f"Professional {service}",
                f"{location} {industry}"
            ]
        }
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5680))
    app.run(host="0.0.0.0", port=port, debug=False)