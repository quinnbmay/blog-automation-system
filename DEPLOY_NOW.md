# Deploy to Railway - Quick Steps

Railway CLI is now installed! Follow these steps on your Mac:

## 1. Login to Railway
```bash
railway login
```

## 2. Navigate to project directory
```bash
cd /path/to/your/claude-code-project
# The files should be at: /home/maymarketing/claude-code-project on the server
```

## 3. Link to existing project
```bash
railway link
```
Choose: Blog Automation System

## 4. Deploy
```bash
railway up
```

## Files to copy from server to your Mac:
- simple_blog_api.py
- requirements.txt
- Dockerfile
- clients.json
- blog_automation_clients.json

## Current Status:
- ✅ Local API running at: http://100.111.33.88:5680
- ✅ All 18 clients tested and working
- ✅ Railway project created with domain: https://blog-automation-api-production.up.railway.app
- ⏳ Waiting for code deployment

## After deployment:
1. Update n8n workflow to use Railway URL instead of local URL
2. Test the workflow
3. Activate for Tuesday/Thursday 9AM EST schedule