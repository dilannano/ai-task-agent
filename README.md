# AI Task Agent 🤖

A cloud-hosted AI agent that processes various tasks using LLM (Large Language Model) APIs. Built with FastAPI and designed for easy deployment on multiple cloud platforms.

## Features

- 🚀 **Fast API** - Built with FastAPI for high performance
- 🧠 **LLM-Powered** - Uses OpenAI API (or compatible alternatives)
- 📝 **Multiple Tasks** - Summarize, analyze, interview prep, translate, and more
- 🔄 **Batch Processing** - Process multiple tasks at once
- 🌐 **Cloud-Ready** - Deploy on Railway, Render, Fly.io, or AWS
- 📚 **Auto Documentation** - Interactive API docs at `/docs`
- ✅ **Health Checks** - Built-in health monitoring

## Quick Start

### Local Development

1. **Clone or navigate to the project:**
   ```bash
   cd ai-task-agent
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

5. **Run the application:**
   ```bash
   python main.py
   # or
   uvicorn main:app --reload
   ```

6. **Visit the API:**
   - API: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## API Endpoints

### `GET /`
Welcome page with API information

### `GET /health`
Health check endpoint

### `GET /tasks`
List all available task templates

### `POST /process`
Process a single task

**Request Body:**
```json
{
  "task": "summarize",
  "input_text": "Your text here...",
  "model": "gpt-3.5-turbo",
  "max_tokens": 1000,
  "temperature": 0.7
}
```

**Response:**
```json
{
  "task": "summarize",
  "result": "Summary of your text...",
  "timestamp": "2026-02-05T10:30:00",
  "model_used": "gpt-3.5-turbo",
  "tokens_used": 150
}
```

### `POST /batch`
Process multiple tasks in batch

## Available Tasks

- **summarize** - Summarize text
- **interview prep** - Generate interview preparation tips
- **analyze** - Analyze and provide insights
- **translate** - Translate text
- **improve** - Improve and enhance text
- **questions** - Generate questions
- **outline** - Create outlines

You can also use **custom tasks** by providing your own instructions!

## Example Usage

### Using cURL

```bash
curl -X POST "http://localhost:8000/process" \
  -H "Content-Type: application/json" \
  -d '{
    "task": "summarize",
    "input_text": "Long article text here...",
    "max_tokens": 500
  }'
```

### Using Python

```python
import requests

response = requests.post(
    "http://localhost:8000/process",
    json={
        "task": "interview prep",
        "input_text": "I'm interviewing for a senior software engineer position at a tech startup",
        "max_tokens": 800
    }
)

print(response.json()["result"])
```

### Using JavaScript

```javascript
fetch('http://localhost:8000/process', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    task: 'summarize',
    input_text: 'Your text here...',
    max_tokens: 500
  })
})
.then(res => res.json())
.then(data => console.log(data.result));
```

## Deployment

### Railway

1. Install Railway CLI:
   ```bash
   npm i -g @railway/cli
   ```

2. Login and deploy:
   ```bash
   railway login
   railway init
   railway up
   ```

3. Set environment variable:
   ```bash
   railway variables set OPENAI_API_KEY=your_key_here
   ```

4. Your app will be live at: `https://your-app.railway.app`

### Render

1. Create a new Web Service on [Render](https://render.com)
2. Connect your GitHub repository
3. Render will auto-detect the `render.yaml` configuration
4. Add environment variable `OPENAI_API_KEY` in the dashboard
5. Deploy!

### Fly.io

1. Install Fly CLI:
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. Login and launch:
   ```bash
   fly auth login
   fly launch
   ```

3. Set secrets:
   ```bash
   fly secrets set OPENAI_API_KEY=your_key_here
   ```

4. Deploy:
   ```bash
   fly deploy
   ```

### AWS Lightsail

1. Create a container service in AWS Lightsail
2. Push your Docker image:
   ```bash
   docker build -t ai-task-agent .
   docker tag ai-task-agent:latest your-registry/ai-task-agent:latest
   docker push your-registry/ai-task-agent:latest
   ```
3. Configure environment variables in Lightsail console
4. Deploy the container

## Docker

Build and run locally:

```bash
docker build -t ai-task-agent .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key_here ai-task-agent
```

## Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `PORT` - Port to run on (default: 8000)
- `HOST` - Host to bind to (default: 0.0.0.0)

## Alternative LLM Providers

You can use OpenAI-compatible APIs (like Azure OpenAI, LocalAI, etc.) by modifying the `openai.api_base` in `main.py`.

## Tech Stack

- **Python 3.11+**
- **FastAPI** - Modern web framework
- **OpenAI API** - LLM provider
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Docker** - Containerization

## Project Structure

```
ai-task-agent/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── railway.toml        # Railway deployment config
├── render.yaml         # Render deployment config
├── fly.toml           # Fly.io deployment config
├── .env.example       # Environment variables template
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Security Notes

- Never commit `.env` file or API keys
- Use environment variables for sensitive data
- Enable rate limiting for production
- Consider adding authentication for public APIs

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use this project for learning or production!

## Support

For issues or questions:
1. Check the `/docs` endpoint for API documentation
2. Review the logs for error messages
3. Ensure your OpenAI API key is valid and has credits

---

Built with ❤️ using FastAPI and OpenAI
