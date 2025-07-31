#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not ANTHROPIC_API_KEY:
    print("ANTHROPIC_API_KEY not found in environment variables")
    print("Make sure you have a .env file with your API key")
    sys.exit(1)

def test_anthropic_connection():
    """Test Anthropic API connection - FREE operation + small paid test"""
    try:
        client = Anthropic(api_key=ANTHROPIC_API_KEY)
        
        # Test 1: List models (FREE operation)
        print("Testing API key validity...")
        models = client.models.list()
        print("API key is valid and working!")
        print(f"   Available models: {len(models.data)} models")
        
        # Show some available models
        model_names = [m.id for m in models.data[:5]]
        print(f"   Sample models: {model_names}")
        
        # Test 2: Small paid test (very cheap - ~$0.0001)
        print("\nTesting credits with minimal completion...")
        response = client.messages.create(
            model="claude-3-haiku-20240307",  # Cheapest model
            max_tokens=1,
            messages=[{"role": "user", "content": "Hi"}]
        )
        print("Credits available! Paid operations work.")
        print(f"   Response: '{response.content[0].text}'")
        
        print("\nYour Anthropic API key is working and you have credits!")
        
    except Exception as e:
        print(f"API key test failed: {e}")
        if "invalid_api_key" in str(e).lower() or "authentication" in str(e).lower():
            print("   This means your API key is invalid or expired.")
        elif "quota" in str(e).lower() or "billing" in str(e).lower():
            print("   This means you've exceeded your quota or have no credits.")
        sys.exit(1)

if __name__ == "__main__":
    test_anthropic_connection() 