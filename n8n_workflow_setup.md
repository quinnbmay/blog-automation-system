# n8n Workflow Setup Instructions

## Access n8n
1. Open your browser and go to: http://100.111.33.88:8080
2. Login with your n8n credentials

## Create/Update Workflow

### 1. Schedule Trigger
- Add a "Schedule Trigger" node
- Set to: Every Tuesday and Thursday at 9:00 AM EST
- Cron expression: `0 9 * * 2,4`
- Timezone: America/New_York

### 2. HTTP Request Node (Get Clients)
- Method: GET
- URL: `http://100.111.33.88:5680/clients`
- Add to workflow after Schedule Trigger

### 3. Loop Over Items
- Add "Loop Over Items" node
- Connect to HTTP Request output
- This will process each client

### 4. HTTP Request Node (Get Blog Post)
- Inside the loop, add HTTP Request node
- Method: POST  
- URL: `http://100.111.33.88:5680/generate-blog`
- Body Type: JSON
- Body:
```json
{
  "client_name": "{{ $json.client_name }}",
  "business_description": "{{ $json.business_description }}",
  "services": {{ $json.services }},
  "content_preferences": {{ $json.content_preferences }},
  "additional_context": "{{ $json.additional_context }}"
}
```

### 5. Save/Send Blog Post
Add your preferred action:
- Email the blog post
- Save to Google Docs
- Post to WordPress
- Save to database

## Testing
1. Click "Execute Workflow" to test with all clients
2. Check execution logs for any errors
3. Verify blog posts are generated correctly

## Activation
Once tested, click "Active" toggle to enable the schedule

## Alternative API Endpoints
- Local: http://100.111.33.88:5680
- Railway (when deployed): https://blog-automation-api-production.up.railway.app

Note: Currently using local API. Update URL when Railway deployment is complete.