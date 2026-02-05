from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import openai
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="AI Task Agent",
    description="An intelligent agent that processes various tasks using LLM",
    version="1.0.0"
)

# CORS middleware for public access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class TaskRequest(BaseModel):
    task: str = Field(..., description="The task to perform (e.g., 'summarize', 'interview prep', 'analyze')")
    input_text: str = Field(..., description="The input text or context for the task")
    model: Optional[str] = Field(default="gpt-3.5-turbo", description="The LLM model to use")
    max_tokens: Optional[int] = Field(default=1000, description="Maximum tokens in response")
    temperature: Optional[float] = Field(default=0.7, description="Temperature for response generation")

class TaskResponse(BaseModel):
    model_config = {"protected_namespaces": ()}
    
    task: str
    result: str
    timestamp: str
    model_used: str
    tokens_used: Optional[int] = None

# Task templates for common operations
TASK_TEMPLATES = {
    "summarize": "Please provide a concise and clear summary of the following text:\n\n{input_text}",
    "interview prep": "Generate comprehensive interview preparation tips based on the following context:\n\n{input_text}",
    "analyze": "Analyze the following text and provide key insights:\n\n{input_text}",
    "translate": "Translate the following text:\n\n{input_text}",
    "improve": "Improve and enhance the following text:\n\n{input_text}",
    "questions": "Generate thoughtful questions based on the following:\n\n{input_text}",
    "outline": "Create a detailed outline for the following:\n\n{input_text}",
}

@app.get("/")
async def root():
    """Welcome endpoint with API information"""
    return {
        "message": "Welcome to AI Task Agent API",
        "version": "1.0.0",
        "endpoints": {
            "/process": "POST - Process a task with AI",
            "/tasks": "GET - List available task templates",
            "/health": "GET - Health check"
        },
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "api_key_configured": bool(os.getenv("OPENAI_API_KEY"))
    }

@app.get("/tasks")
async def list_tasks():
    """List available task templates"""
    return {
        "available_tasks": list(TASK_TEMPLATES.keys()),
        "custom_task_supported": True,
        "description": "Use predefined task names or provide custom instructions"
    }

@app.post("/process", response_model=TaskResponse)
async def process_task(request: TaskRequest):
    """
    Process a task using LLM
    
    - **task**: Type of task (use /tasks endpoint to see options) or custom instruction
    - **input_text**: The text/content to process
    - **model**: OpenAI model to use (default: gpt-3.5-turbo)
    - **max_tokens**: Maximum response length
    - **temperature**: Creativity level (0-1)
    """
    
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=500,
            detail="OpenAI API key not configured. Set OPENAI_API_KEY environment variable."
        )
    
    try:
        # Construct the prompt
        task_lower = request.task.lower()
        if task_lower in TASK_TEMPLATES:
            prompt = TASK_TEMPLATES[task_lower].format(input_text=request.input_text)
        else:
            # Custom task
            prompt = f"{request.task}\n\n{request.input_text}"
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model=request.model,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that performs various tasks accurately and efficiently."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
        
        result = response.choices[0].message.content
        tokens_used = response.usage.total_tokens if hasattr(response, 'usage') else None
        
        return TaskResponse(
            task=request.task,
            result=result,
            timestamp=datetime.now().isoformat(),
            model_used=request.model,
            tokens_used=tokens_used
        )
        
    except openai.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing task: {str(e)}")

@app.post("/batch")
async def batch_process(requests: list[TaskRequest]):
    """Process multiple tasks in batch"""
    results = []
    for req in requests:
        try:
            result = await process_task(req)
            results.append({"success": True, "data": result})
        except HTTPException as e:
            results.append({"success": False, "error": e.detail})
    
    return {
        "total": len(requests),
        "successful": sum(1 for r in results if r["success"]),
        "results": results
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
