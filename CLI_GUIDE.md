# 🖥️ CLI Usage Guide

## Quick Start

### 1. List Available Tasks
```bash
python cli.py --list
```

### 2. Interactive Mode (Easiest!)
```bash
python cli.py -i
```
Then just follow the prompts!

### 3. Direct Commands

#### Summarize Text
```bash
python cli.py summarize "Your long text here..."
```

#### Interview Preparation
```bash
python cli.py "interview prep" "Senior Python Developer at a tech startup"
```

#### Analyze Code
```bash
python cli.py analyze "def hello(): print('hi')"
```

#### Translate
```bash
python cli.py translate "Hello, how are you? (to Spanish)"
```

#### Custom Tasks
```bash
python cli.py "Generate 5 creative startup ideas about" "AI and education"
```

## Advanced Usage

### Read from File
```bash
cat article.txt | python cli.py summarize -
```

### Use Different Model
```bash
python cli.py -m gpt-4 summarize "Your text"
```

### Control Output Length
```bash
python cli.py -t 200 summarize "Your text"  # Max 200 tokens
```

### Verbose Output (show token usage)
```bash
python cli.py -v summarize "Your text"
```

### Use Remote API
```bash
python cli.py -u https://your-app.railway.app summarize "Your text"
```

## Practical Examples

### 1. Summarize a Blog Post
```bash
curl -s https://example.com/article | python cli.py summarize -
```

### 2. Get Interview Tips
```bash
python cli.py "interview prep" "Full-stack developer at fintech startup, React and Node.js"
```

### 3. Code Review
```bash
python cli.py analyze "$(cat mycode.py)"
```

### 4. Generate Ideas
```bash
python cli.py "Generate 10 blog post ideas about" "machine learning for beginners"
```

### 5. Improve Writing
```bash
python cli.py improve "I think that AI is good and useful for many things."
```

### 6. Generate Questions
```bash
python cli.py questions "Python programming fundamentals"
```

### 7. Create Outline
```bash
python cli.py outline "Building a full-stack web application with React and FastAPI"
```

## Tips & Tricks

### Create an Alias
Add to your `~/.zshrc` or `~/.bashrc`:
```bash
alias ai='python /path/to/ai-task-agent/cli.py'
```

Then use:
```bash
ai summarize "Your text"
ai -i  # Interactive mode
```

### Pipe from Commands
```bash
# Summarize git log
git log --oneline -20 | ai summarize -

# Analyze Python files
cat *.py | ai analyze -

# Get ideas from your notes
cat notes.txt | ai "Generate action items from" -
```

### Use in Scripts
```bash
#!/bin/bash
# auto-summarize.sh

for file in *.txt; do
    echo "Summarizing $file..."
    python cli.py summarize "$(cat $file)" > "$file.summary"
done
```

## All Options

```
-h, --help              Show help message
-i, --interactive       Start interactive mode
--list                  List available tasks
-u, --url URL          API URL (default: localhost:8000)
-m, --model MODEL      Model to use (gpt-3.5-turbo, gpt-4)
-t, --max-tokens NUM   Maximum tokens (default: 1000)
--temperature FLOAT    Creativity (0.0-1.0, default: 0.7)
-v, --verbose          Show detailed output
```

## Exit Codes

- `0` - Success
- `1` - Error (API down, invalid input, etc.)

## Examples by Use Case

### For Developers
```bash
# Code review
python cli.py analyze "$(cat app.py)"

# Generate documentation
python cli.py "Write API documentation for" "$(cat api.py)"

# Debug help
python cli.py "Explain this error" "$(cat error.log)"
```

### For Writers
```bash
# Improve text
python cli.py improve "$(cat draft.txt)"

# Generate ideas
python cli.py "Generate article ideas about" "climate change"

# Create outline
python cli.py outline "How to learn programming in 2026"
```

### For Students
```bash
# Summarize lecture notes
python cli.py summarize "$(cat notes.txt)"

# Generate study questions
python cli.py questions "$(cat chapter1.txt)"

# Interview prep
python cli.py "interview prep" "Software engineering internship"
```

### For Professionals
```bash
# Meeting notes summary
python cli.py summarize "$(cat meeting-notes.txt)"

# Email improvement
python cli.py improve "$(cat draft-email.txt)"

# Report outline
python cli.py outline "Q4 Sales Performance Report"
```

## Troubleshooting

### API Not Connected
```bash
# Check if server is running
curl http://localhost:8000/health

# Start server if needed
python main.py
```

### Timeout Errors
```bash
# Reduce max tokens
python cli.py -t 500 summarize "Your text"
```

### Rate Limits
```bash
# Add delays in scripts
python cli.py task1 "text1"
sleep 2
python cli.py task2 "text2"
```

---

**Pro Tip:** Use interactive mode (`python cli.py -i`) for exploratory work, and direct commands for automation and scripting!
