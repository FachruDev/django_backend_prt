# Portfolio Website API Documentation

## Overview

This API provides access to all data from the portfolio website backend. It's built using Django REST Framework and provides both individual endpoints and a comprehensive endpoint that returns all data at once.

## Base URL

```
/api/
```

## Quick Start

### Get All Data at Once
```bash
GET /api/all-data/
```

This endpoint returns all data from all applications in a single response, perfect for initial page loads.

### Get API Overview
```bash
GET /api/
```

Returns a list of all available endpoints.

## Available Endpoints

### 📰 Articles
- `GET /api/articles/` - Get all published articles
- `GET /api/articles/{id}/` - Get specific article by ID
- `GET /api/article-categories/` - Get all article categories
- `GET /api/article-tags/` - Get all article tags

### ⚙️ Web Configuration
- `GET /api/web-settings/` - Get website settings (title, meta, logo, favicon)
- `GET /api/my-documents/` - Get CV/document files
- `GET /api/social-links/` - Get social media links

### 📄 Pages Sections
- `GET /api/pages/hero/` - Get hero section data
- `GET /api/pages/about/` - Get about section data
- `GET /api/pages/certificate/` - Get certificate section data
- `GET /api/pages/project/` - Get project section data
- `GET /api/pages/call-to-action/` - Get call to action section data
- `GET /api/pages/header-experience/` - Get header experience section data
- `GET /api/pages/skills/` - Get skills section data
- `GET /api/pages/article/` - Get article section data
- `GET /api/pages/contact/` - Get contact section data

### 📞 Contact
- `GET /api/contact/forms/` - Get all contact form submissions
- `GET /api/contact/information/` - Get contact information

### 💼 Portfolio
- `GET /api/portfolio/certificates/` - Get all certificates
- `GET /api/portfolio/project-categories/` - Get all project categories
- `GET /api/portfolio/projects/` - Get all projects
- `GET /api/portfolio/project-images/` - Get all project images
- `GET /api/portfolio/experiences/` - Get all work experiences
- `GET /api/portfolio/achievement-experiences/` - Get all achievement experiences
- `GET /api/portfolio/skills-categories/` - Get all skills categories
- `GET /api/portfolio/skills/` - Get all skills

## Response Format

### Success Response
```json
{
    "status": "success",
    "message": "Data retrieved successfully",
    "data": {
        // Your data here
    }
}
```

### Error Response
```json
{
    "status": "error",
    "message": "Error description"
}
```

## Usage Examples

### JavaScript (Fetch API)
```javascript
// Get all data
fetch('/api/all-data/')
  .then(response => response.json())
  .then(data => {
    console.log('All data:', data);
  })
  .catch(error => {
    console.error('Error:', error);
  });

// Get specific data
fetch('/api/articles/')
  .then(response => response.json())
  .then(articles => {
    console.log('Articles:', articles);
  });
```

### Axios
```javascript
import axios from 'axios';

// Get all data
const getAllData = async () => {
  try {
    const response = await axios.get('/api/all-data/');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

// Get portfolio data
const getPortfolioData = async () => {
  try {
    const [projects, skills, experiences] = await Promise.all([
      axios.get('/api/portfolio/projects/'),
      axios.get('/api/portfolio/skills/'),
      axios.get('/api/portfolio/experiences/')
    ]);
    return {
      projects: projects.data,
      skills: skills.data,
      experiences: experiences.data
    };
  } catch (error) {
    console.error('Error fetching portfolio data:', error);
  }
};
```

### React Hook
```javascript
import { useState, useEffect } from 'react';

const usePortfolioData = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch('/api/all-data/');
        const result = await response.json();
        setData(result.data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return { data, loading, error };
};
```

## Data Structure

### All Data Response Structure
```json
{
  "status": "success",
  "message": "All data retrieved successfully",
  "data": {
    "articles": {
      "articles": [...],
      "categories": [...],
      "tags": [...]
    },
    "webconfig": {
      "settings": {...},
      "documents": {...},
      "social_links": [...]
    },
    "pages": {
      "hero": {...},
      "about": {...},
      "certificate": {...},
      "project": {...},
      "call_to_action": {...},
      "header_experience": {...},
      "skills": {...},
      "article": {...},
      "contact": {...}
    },
    "contact": {
      "forms": [...],
      "information": {...}
    },
    "portfolio": {
      "certificates": [...],
      "project_categories": [...],
      "projects": [...],
      "project_images": [...],
      "experiences": [...],
      "achievement_experiences": [...],
      "skills_categories": [...],
      "skills": [...]
    }
  }
}
```

## Best Practices

1. **Use `/api/all-data/` for initial page load** - This gets all data in one request
2. **Use specific endpoints for updates** - Call individual endpoints when you need fresh data
3. **Implement caching** - Cache responses on the frontend for better performance
4. **Handle errors gracefully** - Always check for error responses
5. **Use loading states** - Show loading indicators while fetching data

## CORS Configuration

The API is configured to allow CORS requests from:
- `http://localhost:3000` (default)
- Any origins specified in `CORS_ALLOWED_ORIGINS` environment variable

## Authentication

Currently, all endpoints are public (AllowAny permission). For production, consider adding authentication if needed.

## Performance Considerations

1. The `/api/all-data/` endpoint may be slow if there's a lot of data
2. Consider implementing pagination for large datasets
3. Use database indexing for better query performance
4. Implement caching strategies (Redis, Memcached)
5. Consider using GraphQL for more flexible data fetching

## Security Considerations

1. All endpoints are currently public - add authentication if needed
2. Validate and sanitize all input data
3. Implement rate limiting for API endpoints
4. Use HTTPS in production
5. Consider implementing API versioning

## Future Enhancements

- [ ] Add POST/PUT/DELETE endpoints for CRUD operations
- [ ] Implement pagination for large datasets
- [ ] Add filtering and sorting capabilities
- [ ] Implement search functionality
- [ ] Add API versioning
- [ ] Implement rate limiting
- [ ] Add authentication and authorization
- [ ] Add API documentation using Swagger/OpenAPI

## Testing the API

You can test the API endpoints using:

1. **Browser** - Navigate to `http://localhost:8000/api/`
2. **Postman** - Import the endpoints and test them
3. **cURL** - Use command line tools
4. **Frontend Application** - Integrate with your React/Vue/Angular app

Example cURL commands:
```bash
# Get all data
curl http://localhost:8000/api/all-data/

# Get articles
curl http://localhost:8000/api/articles/

# Get portfolio projects
curl http://localhost:8000/api/portfolio/projects/
```

## Support

If you encounter any issues or have questions about the API, please check:
1. The Django server is running
2. The database is properly configured
3. All required environment variables are set
4. The API endpoints are accessible via the correct URLs 