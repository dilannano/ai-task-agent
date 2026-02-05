#!/usr/bin/env python3
"""
AI Task Agent - Command Line Interface
A simple CLI to interact with your AI Task Agent API
"""

import requests
import json
import argparse
import sys
from typing import Optional

# Default API URL
DEFAULT_API_URL = "http://localhost:8000"

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    """Print colored header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{text}{Colors.ENDC}")

def print_success(text):
    """Print success message"""
    print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}", file=sys.stderr)

def print_info(text):
    """Print info message"""
    print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")

def check_health(api_url: str) -> bool:
    """Check if the API is healthy"""
    try:
        response = requests.get(f"{api_url}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("api_key_configured", False)
        return False
    except requests.exceptions.RequestException:
        return False

def list_tasks(api_url: str):
    """List available tasks"""
    try:
        response = requests.get(f"{api_url}/tasks", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print_header("📋 Available Task Types:")
            for task in data.get("available_tasks", []):
                print(f"  • {Colors.OKGREEN}{task}{Colors.ENDC}")
            print(f"\n{Colors.OKCYAN}💡 You can also use custom instructions!{Colors.ENDC}")
            return True
        else:
            print_error(f"Failed to fetch tasks: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print_error(f"Connection error: {e}")
        return False

def process_task(
    api_url: str,
    task: str,
    input_text: str,
    model: str = "gpt-3.5-turbo",
    max_tokens: int = 1000,
    temperature: float = 0.7,
    verbose: bool = False
):
    """Process a task with the AI agent"""
    
    # Check if reading from stdin
    if input_text == "-":
        print_info("Reading from stdin... (Press Ctrl+D when done)")
        input_text = sys.stdin.read()
    
    if not input_text.strip():
        print_error("Input text cannot be empty!")
        return False
    
    print_info(f"Processing task: {task}")
    
    payload = {
        "task": task,
        "input_text": input_text,
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    try:
        response = requests.post(
            f"{api_url}/process",
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            data = response.json()
            
            print_header("✨ Result:")
            print(f"\n{data['result']}\n")
            
            if verbose:
                print_info(f"Model: {data['model_used']}")
                print_info(f"Tokens: {data.get('tokens_used', 'N/A')}")
                print_info(f"Timestamp: {data['timestamp']}")
            
            return True
        else:
            error_data = response.json()
            print_error(f"API Error: {error_data.get('detail', 'Unknown error')}")
            return False
            
    except requests.exceptions.Timeout:
        print_error("Request timed out. Try reducing max_tokens or check your connection.")
        return False
    except requests.exceptions.RequestException as e:
        print_error(f"Connection error: {e}")
        print_info("Make sure the server is running: python main.py")
        return False
    except json.JSONDecodeError:
        print_error("Invalid response from server")
        return False

def interactive_mode(api_url: str):
    """Interactive mode for continuous task processing"""
    print_header("🤖 AI Task Agent - Interactive Mode")
    print(f"{Colors.OKCYAN}Type 'help' for commands, 'exit' to quit{Colors.ENDC}\n")
    
    while True:
        try:
            # Get task type
            task = input(f"{Colors.BOLD}Task type (or 'help'): {Colors.ENDC}").strip()
            
            if not task:
                continue
            
            if task.lower() in ['exit', 'quit', 'q']:
                print_success("Goodbye! 👋")
                break
            
            if task.lower() == 'help':
                print_header("📚 Available Commands:")
                print("  • help       - Show this help")
                print("  • list       - List available tasks")
                print("  • exit/quit  - Exit interactive mode")
                print("\n📝 Task Types:")
                list_tasks(api_url)
                continue
            
            if task.lower() == 'list':
                list_tasks(api_url)
                continue
            
            # Get input text
            print(f"{Colors.OKCYAN}Enter your text (or paste, then press Enter):{Colors.ENDC}")
            input_text = input().strip()
            
            if not input_text:
                print_error("Input text cannot be empty!")
                continue
            
            # Process the task
            process_task(api_url, task, input_text, verbose=True)
            print()
            
        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}Interrupted. Type 'exit' to quit.{Colors.ENDC}")
            continue
        except EOFError:
            print_success("\nGoodbye! 👋")
            break

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="🤖 AI Task Agent CLI - Process tasks with AI from the command line",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  %(prog)s -i
  
  # Summarize text
  %(prog)s summarize "Your long text here..."
  
  # Interview prep
  %(prog)s "interview prep" "Senior Python Developer at startup"
  
  # Custom task
  %(prog)s "Generate 5 blog ideas about" "AI and automation"
  
  # Read from stdin
  cat article.txt | %(prog)s summarize -
  
  # Use different model
  %(prog)s -m gpt-4 summarize "Your text here"
  
  # List available tasks
  %(prog)s --list
        """
    )
    
    parser.add_argument(
        'task',
        nargs='?',
        help='Task type (e.g., summarize, interview prep, analyze) or custom instruction'
    )
    parser.add_argument(
        'text',
        nargs='?',
        help='Input text to process (use "-" to read from stdin)'
    )
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Start interactive mode'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List available task types'
    )
    parser.add_argument(
        '-u', '--url',
        default=DEFAULT_API_URL,
        help=f'API URL (default: {DEFAULT_API_URL})'
    )
    parser.add_argument(
        '-m', '--model',
        default='gpt-3.5-turbo',
        help='Model to use (default: gpt-3.5-turbo)'
    )
    parser.add_argument(
        '-t', '--max-tokens',
        type=int,
        default=1000,
        help='Maximum tokens in response (default: 1000)'
    )
    parser.add_argument(
        '--temperature',
        type=float,
        default=0.7,
        help='Temperature for generation (default: 0.7)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed output'
    )
    
    args = parser.parse_args()
    
    # Check API health
    if not check_health(args.url):
        print_error("Cannot connect to API server!")
        print_info(f"Make sure the server is running at: {args.url}")
        print_info("Start server with: python main.py")
        sys.exit(1)
    
    if args.verbose:
        print_success(f"Connected to API at {args.url}")
    
    # Handle different modes
    if args.list:
        list_tasks(args.url)
        sys.exit(0)
    
    if args.interactive:
        interactive_mode(args.url)
        sys.exit(0)
    
    if not args.task:
        parser.print_help()
        print(f"\n{Colors.WARNING}💡 Tip: Use -i for interactive mode{Colors.ENDC}")
        sys.exit(1)
    
    if not args.text:
        print_error("Input text is required!")
        print_info("Usage: cli.py <task> <text>")
        print_info("Or use: cli.py -i for interactive mode")
        sys.exit(1)
    
    # Process the task
    success = process_task(
        args.url,
        args.task,
        args.text,
        args.model,
        args.max_tokens,
        args.temperature,
        args.verbose
    )
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
