#!/usr/bin/env python3
"""Test blog generation for all clients"""

import requests
import json
import time

API_URL = "http://100.111.33.88:5680"

def test_all_clients():
    """Test blog generation for each client"""
    
    # Get all clients
    response = requests.get(f"{API_URL}/clients")
    clients_data = response.json()
    
    if isinstance(clients_data, dict) and 'clients' in clients_data:
        client_names = clients_data['clients']
    else:
        client_names = clients_data
    
    print(f"Found {len(client_names)} clients")
    print("-" * 50)
    
    success_count = 0
    failed_clients = []
    
    for i, client_name in enumerate(client_names, 1):
        print(f"\n[{i}/{len(client_names)}] Testing: {client_name}")
        
        # Get client details
        response = requests.get(f"{API_URL}/client/{client_name}")
        if response.status_code != 200:
            print(f"  ❌ Failed to get client details: {response.status_code}")
            failed_clients.append(client_name)
            continue
            
        client_data = response.json()
        
        # Generate blog post
        try:
            response = requests.post(f"{API_URL}/generate-blog", json=client_data)
            if response.status_code == 200:
                blog_data = response.json()
                print(f"  ✅ Blog generated successfully!")
                print(f"     Title: {blog_data['title'][:60]}...")
                print(f"     Length: {blog_data['metadata']['word_count']} words")
                success_count += 1
            else:
                print(f"  ❌ Failed to generate blog: {response.status_code}")
                failed_clients.append(client_name)
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
            failed_clients.append(client_name)
        
        # Small delay to avoid overwhelming the API
        time.sleep(1)
    
    # Summary
    print("\n" + "=" * 50)
    print(f"SUMMARY:")
    print(f"  Total clients: {len(client_names)}")
    print(f"  Successful: {success_count}")
    print(f"  Failed: {len(failed_clients)}")
    
    if failed_clients:
        print(f"\nFailed clients:")
        for client in failed_clients:
            print(f"  - {client}")
    
    return success_count == len(client_names)

if __name__ == "__main__":
    print("Blog Automation API Test")
    print("=" * 50)
    
    # Test API connection
    try:
        response = requests.get(f"{API_URL}/")
        print(f"API Status: ✅ Online")
    except:
        print(f"API Status: ❌ Offline")
        print(f"Make sure the API is running at {API_URL}")
        exit(1)
    
    # Run tests
    success = test_all_clients()
    
    if success:
        print("\n✅ All tests passed! Ready for n8n workflow.")
    else:
        print("\n⚠️  Some tests failed. Check the logs above.")