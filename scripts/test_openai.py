#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("OPENAI_API_KEY not found in environment variables")
    print("Make sure you have a .env.local file with your API key")
    sys.exit(1)

def test_openai_connection():
    """Test OpenAI API connection - FREE operation + small paid test"""
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        # Test 1: List models (FREE operation)
        print("Testing API key validity...")
        models = client.models.list()
        print("API key is valid and working!")
        print(f"   Available models: {len(models.data)} models")
        
        # Show some available models
        model_names = [m.id for m in models.data[:5]]
        print(f"   Sample models: {model_names}")
        
        # Test 2: Small paid test (very cheap - ~$0.0001)
        print("\n💰 Testing credits with minimal completion...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=1
        )
        print("Credits available! Paid operations work.")
        print(f"   Response: '{response.choices[0].message.content}'")
        
        print("\nYour OpenAI API key is working and you have credits!")
        
    except Exception as e:
        print(f"API key test failed: {e}")
        if "invalid_api_key" in str(e).lower():
            print("   This means your API key is invalid or expired.")
        elif "quota" in str(e).lower() or "billing" in str(e).lower():
            print("   This means you've exceeded your quota or have no credits.")
        sys.exit(1)

if __name__ == "__main__":
    test_openai_connection() 