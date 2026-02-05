# Railway Template for AI Task Agent

This template deploys an AI Task Agent built with FastAPI that can process various AI tasks using OpenAI's API.

## Features

- 🚀 FastAPI backend with auto-generated API docs
- 🤖 Multiple AI tasks: summarize, analyze, interview prep, and more
- 🖥️ Command-line interface (CLI) included
- 🎨 Beautiful web UI demo included
- 📝 Batch processing support

## Required Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key (get one at https://platform.openai.com/api-keys)

## After Deployment

1. Set your `OPENAI_API_KEY` in Railway's environment variables
2. Visit your app URL at `https://your-app.railway.app/docs`
3. Try the interactive API documentation
4. Use the CLI: `python cli.py -u https://your-app.railway.app -i`

## Endpoints

- `/` - Welcome page
- `/docs` - Interactive API documentation  
- `/health` - Health check
- `/tasks` - List available tasks
- `/process` - Process AI tasks

## Available Tasks

- **summarize** - Summarize long text
- **interview prep** - Generate interview tips
- **analyze** - Analyze and provide insights
- **translate** - Translate text
- **improve** - Improve writing
- **questions** - Generate questions
- **outline** - Create outlines
- **custom** - Any custom instruction

## Usage Example

```bash
curl -X POST "https://your-app.railway.app/process" \
  -H "Content-Type: application/json" \
  -d '{
    "task": "summarize",
    "input_text": "Your long text here...",
    "max_tokens": 500
  }'
```

## Cost

- Railway: Free tier available
- OpenAI API: Usage-based (~$0.002 per 1K tokens for GPT-3.5-Turbo)

## Documentation

See the full [README.md](https://github.com/dilannano/ai-task-agent) for complete documentation.
