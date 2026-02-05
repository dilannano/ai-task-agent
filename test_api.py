"""
Simple test script to verify the API works correctly
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("🏥 Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_tasks():
    """Test tasks list endpoint"""
    print("📋 Testing tasks endpoint...")
    response = requests.get(f"{BASE_URL}/tasks")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_summarize():
    """Test summarization task"""
    print("📝 Testing summarize task...")
    data = {
        "task": "summarize",
        "input_text": """
        Artificial Intelligence (AI) is transforming the world in unprecedented ways.
        From healthcare to finance, AI systems are helping humans make better decisions,
        automate repetitive tasks, and unlock new possibilities. Machine learning, a 
        subset of AI, enables computers to learn from data without explicit programming.
        Deep learning, which uses neural networks, has achieved remarkable breakthroughs
        in image recognition, natural language processing, and game playing.
        """,
        "max_tokens": 200
    }
    
    response = requests.post(f"{BASE_URL}/process", json=data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Task: {result['task']}")
        print(f"Result: {result['result']}")
        print(f"Tokens Used: {result['tokens_used']}\n")
    else:
        print(f"Error: {response.text}\n")

def test_interview_prep():
    """Test interview prep task"""
    print("💼 Testing interview prep task...")
    data = {
        "task": "interview prep",
        "input_text": "I'm interviewing for a Python backend developer position at a fintech startup",
        "max_tokens": 500
    }
    
    response = requests.post(f"{BASE_URL}/process", json=data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Result: {result['result'][:300]}...\n")
    else:
        print(f"Error: {response.text}\n")

def test_custom_task():
    """Test custom task"""
    print("🎨 Testing custom task...")
    data = {
        "task": "Generate 3 creative project ideas based on:",
        "input_text": "AI, web development, and automation",
        "max_tokens": 400
    }
    
    response = requests.post(f"{BASE_URL}/process", json=data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Result: {result['result']}\n")
    else:
        print(f"Error: {response.text}\n")

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 AI Task Agent - API Tests")
    print("=" * 60 + "\n")
    
    try:
        test_health()
        test_tasks()
        test_summarize()
        test_interview_prep()
        test_custom_task()
        
        print("=" * 60)
        print("✅ All tests completed!")
        print("=" * 60)
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API.")
        print("Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"❌ Error: {e}")
