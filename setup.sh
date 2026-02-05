#!/bin/bash

echo "🚀 Starting AI Task Agent Setup..."
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your OPENAI_API_KEY"
echo "2. Run: source venv/bin/activate"
echo "3. Run: python main.py"
echo "4. Visit: http://localhost:8000/docs"
echo ""
