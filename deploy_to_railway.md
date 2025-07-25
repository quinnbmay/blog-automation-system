# Railway Deployment Instructions

## Option 1: Using Railway Dashboard
1. Go to https://railway.app/
2. Open project "Blog Automation System" 
3. Click on the service "blog-automation-api"
4. Go to Settings > Deploy
5. Choose "GitHub Repo" and connect your GitHub account
6. Create a new repo and push the code from `/home/maymarketing/claude-code-project`

## Option 2: Using Railway CLI (requires installation)
```bash
# Install Railway CLI
curl -fsSL https://railway.app/install.sh | sh

# Login
railway login

# Link to existing project
cd /home/maymarketing/claude-code-project
railway link 903233c8-2ec5-4095-a3eb-9612c7074843

# Deploy
railway up
```

## Option 3: Keep using local deployment
The API is already running at: http://100.111.33.88:5680
This is accessible within your network.

## Files to Deploy
- simple_blog_api.py
- requirements.txt
- Dockerfile
- clients.json
- blog_automation_clients.json

## Environment Variables (already set in Railway)
- PORT=5680

## Railway URL (when deployed)
https://blog-automation-api-production.up.railway.app