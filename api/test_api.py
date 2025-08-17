"""
API Testing Script
=================

This script can be used to test the API endpoints.
Run this script to verify that all endpoints are working correctly.

Usage:
    python test_api.py
"""

import requests
import json
from typing import Dict, Any

# Base URL for the API
BASE_URL = "http://localhost:8000/api"

def test_endpoint(url: str, name: str) -> Dict[str, Any]:
    """
    Test a single endpoint and return the result
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return {
                "status": "success",
                "name": name,
                "url": url,
                "status_code": response.status_code,
                "data_length": len(response.text)
            }
        else:
            return {
                "status": "error",
                "name": name,
                "url": url,
                "status_code": response.status_code,
                "error": f"HTTP {response.status_code}"
            }
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "name": name,
            "url": url,
            "error": str(e)
        }

def test_all_endpoints():
    """
    Test all API endpoints
    """
    endpoints = [
        # API Overview
        (f"{BASE_URL}/", "API Overview"),
        
        # All Data
        (f"{BASE_URL}/all-data/", "All Data"),
        
        # Articles
        (f"{BASE_URL}/articles/", "Articles"),
        (f"{BASE_URL}/article-categories/", "Article Categories"),
        (f"{BASE_URL}/article-tags/", "Article Tags"),
        
        # WebConfig
        (f"{BASE_URL}/web-settings/", "Web Settings"),
        (f"{BASE_URL}/my-documents/", "My Documents"),
        (f"{BASE_URL}/social-links/", "Social Links"),
        
        # Pages
        (f"{BASE_URL}/pages/hero/", "Pages Hero"),
        (f"{BASE_URL}/pages/about/", "Pages About"),
        (f"{BASE_URL}/pages/certificate/", "Pages Certificate"),
        (f"{BASE_URL}/pages/project/", "Pages Project"),
        (f"{BASE_URL}/pages/call-to-action/", "Pages Call to Action"),
        (f"{BASE_URL}/pages/header-experience/", "Pages Header Experience"),
        (f"{BASE_URL}/pages/skills/", "Pages Skills"),
        (f"{BASE_URL}/pages/article/", "Pages Article"),
        (f"{BASE_URL}/pages/contact/", "Pages Contact"),
        
        # Contact
        (f"{BASE_URL}/contact/forms/", "Contact Forms"),
        (f"{BASE_URL}/contact/information/", "Contact Information"),
        
        # Portfolio
        (f"{BASE_URL}/portfolio/certificates/", "Portfolio Certificates"),
        (f"{BASE_URL}/portfolio/project-categories/", "Portfolio Project Categories"),
        (f"{BASE_URL}/portfolio/projects/", "Portfolio Projects"),
        (f"{BASE_URL}/portfolio/project-images/", "Portfolio Project Images"),
        (f"{BASE_URL}/portfolio/experiences/", "Portfolio Experiences"),
        (f"{BASE_URL}/portfolio/achievement-experiences/", "Portfolio Achievement Experiences"),
        (f"{BASE_URL}/portfolio/skills-categories/", "Portfolio Skills Categories"),
        (f"{BASE_URL}/portfolio/skills/", "Portfolio Skills"),
    ]
    
    print("🚀 Testing API Endpoints...")
    print("=" * 50)
    
    results = []
    success_count = 0
    error_count = 0
    
    for url, name in endpoints:
        result = test_endpoint(url, name)
        results.append(result)
        
        if result["status"] == "success":
            print(f"✅ {name}: OK ({result['data_length']} chars)")
            success_count += 1
        else:
            print(f"❌ {name}: ERROR - {result.get('error', 'Unknown error')}")
            error_count += 1
    
    print("=" * 50)
    print(f"📊 Results: {success_count} successful, {error_count} failed")
    
    if error_count == 0:
        print("🎉 All endpoints are working correctly!")
    else:
        print("⚠️  Some endpoints failed. Check the errors above.")
    
    return results

def test_specific_endpoint(endpoint: str):
    """
    Test a specific endpoint and show detailed response
    """
    url = f"{BASE_URL}/{endpoint}/"
    print(f"🔍 Testing: {url}")
    print("=" * 50)
    
    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Content Type: {response.headers.get('content-type', 'Unknown')}")
        print(f"Response Length: {len(response.text)} characters")
        print("\nResponse Preview:")
        print("-" * 30)
        
        # Try to format JSON response
        try:
            json_data = response.json()
            print(json.dumps(json_data, indent=2)[:1000] + "..." if len(json.dumps(json_data, indent=2)) > 1000 else "")
        except json.JSONDecodeError:
            print(response.text[:500] + "..." if len(response.text) > 500 else response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🧪 API Testing Tool")
    print("=" * 50)
    
    # Test all endpoints
    results = test_all_endpoints()
    
    print("\n" + "=" * 50)
    print("🔍 Detailed Testing Options:")
    print("1. Test all endpoints (default)")
    print("2. Test specific endpoint")
    print("3. Test all-data endpoint in detail")
    
    choice = input("\nEnter your choice (1-3) or press Enter to exit: ").strip()
    
    if choice == "2":
        endpoint = input("Enter endpoint name (e.g., 'articles', 'portfolio/projects'): ").strip()
        test_specific_endpoint(endpoint)
    elif choice == "3":
        test_specific_endpoint("all-data")
    elif choice == "1":
        print("✅ All endpoints have been tested above.")
    else:
        print("👋 Goodbye!") 