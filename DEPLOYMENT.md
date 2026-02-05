# Quick Deployment Guide 🚀

## Prerequisites

Before deploying, you need:
- OpenAI API key (get one at https://platform.openai.com/api-keys)
- Git installed
- Account on your chosen platform (Railway, Render, Fly.io, or AWS)

---

## Option 1: Railway (Recommended - Easiest)

### Why Railway?
- ✅ Automatic deployments from Git
- ✅ Free tier available
- ✅ Simple environment variable management
- ✅ Zero-config deployments

### Steps:

1. **Push to GitHub** (if not already):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/ai-task-agent.git
   git push -u origin main
   ```

2. **Deploy on Railway**:
   - Go to [railway.app](https://railway.app)
   - Click "Start New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway auto-detects configuration

3. **Set Environment Variables**:
   - In Railway dashboard, go to your service
   - Click "Variables" tab
   - Add: `OPENAI_API_KEY` = `your_key_here`

4. **Done!** Your API will be live at:
   ```
   https://your-app.railway.app
   ```

---

## Option 2: Render

### Why Render?
- ✅ Free tier with always-on option
- ✅ Auto-deploy from Git
- ✅ Built-in SSL certificates
- ✅ Easy scaling

### Steps:

1. **Push to GitHub** (same as above)

2. **Deploy on Render**:
   - Go to [render.com](https://render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repo
   - Render detects `render.yaml` automatically

3. **Configure**:
   - Name: `ai-task-agent`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. **Set Environment Variables**:
   - In dashboard, add `OPENAI_API_KEY`

5. **Deploy!** URL will be:
   ```
   https://ai-task-agent.onrender.com
   ```

---

## Option 3: Fly.io

### Why Fly.io?
- ✅ Global edge deployment
- ✅ Fast cold starts
- ✅ Free tier available
- ✅ Docker-based

### Steps:

1. **Install Fly CLI**:
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Login**:
   ```bash
   fly auth login
   ```

3. **Initialize and Deploy**:
   ```bash
   cd ai-task-agent
   fly launch
   ```
   - Select region
   - Confirm app name
   - Say "No" to Postgres
   - Say "Yes" to deploy now

4. **Set Secrets**:
   ```bash
   fly secrets set OPENAI_API_KEY=your_key_here
   ```

5. **Access your app**:
   ```
   https://your-app.fly.dev
   ```

---

## Option 4: AWS Lightsail

### Why AWS Lightsail?
- ✅ Simple AWS experience
- ✅ Predictable pricing ($5/month)
- ✅ Container service
- ✅ AWS infrastructure

### Steps:

1. **Build Docker Image**:
   ```bash
   docker build -t ai-task-agent .
   ```

2. **Push to AWS**:
   ```bash
   # Install AWS CLI first
   aws lightsail push-container-image \
     --service-name ai-task-agent \
     --label ai-task-agent \
     --image ai-task-agent:latest
   ```

3. **Create Container Service**:
   - Go to AWS Lightsail console
   - Click "Create container service"
   - Choose plan (Nano/Micro)
   - Deploy uploaded image

4. **Set Environment Variables**:
   - In service settings, add `OPENAI_API_KEY`

5. **Deploy and access**:
   ```
   https://your-service.lightsail.aws
   ```

---

## Option 5: Docker Anywhere

Deploy Docker container to any platform that supports containers:

### Build:
```bash
docker build -t ai-task-agent .
```

### Run locally:
```bash
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_key_here \
  ai-task-agent
```

### Push to Docker Hub:
```bash
docker tag ai-task-agent yourusername/ai-task-agent
docker push yourusername/ai-task-agent
```

Then deploy to: DigitalOcean App Platform, Google Cloud Run, Azure Container Apps, etc.

---

## Testing Your Deployment

Once deployed, test your API:

### 1. Check health:
```bash
curl https://your-app-url.com/health
```

### 2. Test with cURL:
```bash
curl -X POST "https://your-app-url.com/process" \
  -H "Content-Type: application/json" \
  -d '{
    "task": "summarize",
    "input_text": "Your text here",
    "max_tokens": 200
  }'
```

### 3. Visit API docs:
```
https://your-app-url.com/docs
```

---

## Cost Comparison

| Platform | Free Tier | Paid Plans | Best For |
|----------|-----------|------------|----------|
| **Railway** | $5 credit/month | From $5/month | Quick deploys |
| **Render** | 750 hrs/month | From $7/month | Always-on apps |
| **Fly.io** | 3 VMs free | From $1.94/month | Edge deployment |
| **AWS Lightsail** | None | From $5/month | AWS ecosystem |

**Note**: OpenAI API costs are separate and based on usage.

---

## Monitoring

After deployment, monitor your app:

1. **Check logs** on your platform dashboard
2. **Set up alerts** for downtime
3. **Monitor OpenAI usage** at platform.openai.com
4. **Use health endpoint**: `/health`

---

## Troubleshooting

### Common Issues:

**❌ 500 Error on /process**
- Check if `OPENAI_API_KEY` is set correctly
- Verify API key has credits
- Check logs for detailed error

**❌ App not starting**
- Verify Python version (3.11+)
- Check all dependencies installed
- Review deployment logs

**❌ Timeout errors**
- Increase `max_tokens` limit
- Check OpenAI API status
- Consider upgrading plan

---

## Security Best Practices

1. **Never commit** `.env` file
2. **Rotate API keys** regularly
3. **Add rate limiting** for production
4. **Enable CORS** only for trusted domains
5. **Use HTTPS** (automatic on most platforms)
6. **Monitor usage** to prevent abuse

---

## Next Steps

After deployment:
- ✅ Test all endpoints
- ✅ Share your API URL
- ✅ Add authentication (optional)
- ✅ Monitor usage and costs
- ✅ Scale as needed

---

## Support

- Railway: https://railway.app/help
- Render: https://render.com/docs
- Fly.io: https://fly.io/docs
- AWS: https://docs.aws.amazon.com/lightsail

Happy deploying! 🚀
