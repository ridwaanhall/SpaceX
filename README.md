# SpaceX API 🚀

[![Django](https://img.shields.io/badge/Django-5.2.5-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)
[![API Status](https://img.shields.io/badge/API-Online-brightgreen.svg)](https://spacex-api.ridwaanhall.com)

A comprehensive RESTful API providing real-time SpaceX mission data, launch statistics, upcoming launches, and Dragon capsule tracking information.

## 🌐 Base URL

```txt
https://spacex-api.ridwaanhall.com
```

## ✨ Features

- **📊 Launch Statistics**: Get comprehensive SpaceX launch statistics including total launches, landings, and reflights
- **🚀 Upcoming Launches**: Access detailed information about upcoming SpaceX missions with real-time updates  
- **📚 Launch History**: Browse complete historical launch data with detailed mission information
- **🐉 Dragon Tracking**: Real-time GPS tracking and telemetry data for Dragon capsules
- **⚡ Fast & Reliable**: Built with Django REST Framework for optimal performance
- **📖 Well Documented**: Comprehensive API documentation with examples

## 🛠️ Quick Start

### Python Example

```python
import requests

# Base API URL
BASE_URL = "https://spacex-api.ridwaanhall.com"

def get_spacex_stats():
    """Get SpaceX launch statistics"""
    response = requests.get(f"{BASE_URL}/stats/")
    if response.status_code == 200:
        data = response.json()
        return data['data']
    return None

def get_upcoming_launches():
    """Get upcoming SpaceX launches"""
    response = requests.get(f"{BASE_URL}/upcoming/")
    if response.status_code == 200:
        data = response.json()
        return data['data']
    return None

def get_dragon_tracking():
    """Get real-time Dragon capsule tracking data"""
    response = requests.get(f"{BASE_URL}/dragon/")
    if response.status_code == 200:
        data = response.json()
        return data['data']
    return None

# Usage examples
stats = get_spacex_stats()
if stats:
    print(f"Total Launches: {stats['totalLaunches']}")
    print(f"Total Landings: {stats['totalLandings']}")
    print(f"Total Reflights: {stats['totalReflights']}")

upcoming = get_upcoming_launches()
if upcoming:
    print(f"Upcoming launches: {upcoming['upcoming_count']}")
    for launch in upcoming['launches'][:3]:  # Show first 3
        print(f"- {launch['title']} ({launch['launchDate']})")
```

### JavaScript/Node.js Example

```javascript
const axios = require('axios');

const BASE_URL = 'https://spacex-api.ridwaanhall.com';

// Get SpaceX statistics
async function getSpaceXStats() {
    try {
        const response = await axios.get(`${BASE_URL}/stats/`);
        return response.data.data;
    } catch (error) {
        console.error('Error fetching stats:', error.message);
        return null;
    }
}

// Get upcoming launches
async function getUpcomingLaunches() {
    try {
        const response = await axios.get(`${BASE_URL}/upcoming/`);
        return response.data.data;
    } catch (error) {
        console.error('Error fetching upcoming launches:', error.message);
        return null;
    }
}

// Usage
(async () => {
    const stats = await getSpaceXStats();
    if (stats) {
        console.log(`Total Launches: ${stats.totalLaunches}`);
        console.log(`Total Landings: ${stats.totalLandings}`);
    }
    
    const upcoming = await getUpcomingLaunches();
    if (upcoming) {
        console.log(`Upcoming launches: ${upcoming.upcoming_count}`);
    }
})();
```

## 📚 API Endpoints

### 1. Launch Statistics

**Endpoint:** `GET /stats/`

Get comprehensive SpaceX launch statistics.

**Response Example:**

```json
{
    "success": true,
    "message": "SpaceX statistics retrieved successfully",
    "data": {
        "id": 1,
        "documentId": "xyz123",
        "totalLaunches": 200,
        "totalLandings": 180,
        "totalReflights": 150
    }
}
```

### 2. Upcoming Launches

**Endpoint:** `GET /upcoming/`

Get detailed information about upcoming SpaceX launches.

**Response Example:**

```json
{
    "success": true,
    "message": "Upcoming launches retrieved successfully",
    "data": {
        "total_count": 10,
        "upcoming_count": 8,
        "starlink_count": 5,
        "launches": [
            {
                "id": 1,
                "title": "Starlink Mission",
                "subtitle": "Starlink Group 7-15",
                "launchDate": "2025-09-15",
                "launchTime": "10:30:00",
                "vehicle": "Falcon 9",
                "launchSite": "Kennedy Space Center",
                "missionStatus": "upcoming",
                "missionType": "starlink",
                "isLive": false
            }
        ]
    }
}
```

**Statistics Endpoint:** `GET /upcoming/stats/`

Get statistical breakdown of upcoming launches.

### 3. Launch History

**Endpoint:** `GET /launches/`

Get historical SpaceX launch data.

**Detail Endpoint:** `GET /launches/{link}/`

Get detailed information about a specific launch using the `link` field from the launches list.

**Response Example:**

```json
{
    "success": true,
    "message": "SpaceX launches data retrieved successfully",
    "data": {
        "total_launches": 200,
        "launches": [
            {
                "id": 1,
                "title": "Crew-11 Mission",
                "link": "crew11",
                "launchDate": "2025-08-15",
                "vehicle": "Falcon 9",
                "missionStatus": "success",
                "callToAction": "Watch Replay"
            }
        ]
    }
}
```

### 4. Dragon Tracking

**Endpoint:** `GET /dragon/`

Get real-time Dragon capsule GPS tracking and telemetry data.

**Response Example:**

```json
{
    "success": true,
    "message": "Dragon tracking data retrieved successfully",
    "data": {
        "glass.dragon.gps_time_f64": 1725379200.0,
        "glass.dragon.mission_time_f64": 86400.0,
        "glass.dgn_alt_geod_f64": 408000.0,
        "glass.dgn_speed_f64": 7800.0,
        "glass.predict_iss_r_lla_v3": [51.6441, -0.1275, 408000],
        "glass.predict_dgn_r_lla_v3": [51.6441, -0.1275, 408000]
    }
}
```

## 🔍 Health Checks

Monitor API service health with dedicated health check endpoints:

- **Stats Health:** `GET /stats/health/`
- **Upcoming Health:** `GET /upcoming/health/`
- **Launches Health:** `GET /launches/health/`

## 📋 Response Format

All endpoints return standardized JSON responses:

```json
{
    "success": boolean,
    "message": "Human readable message",
    "data": {} // Actual response data or null on error
}
```

## ⚡ Rate Limiting & Performance

- **No Authentication Required**: Public API with open access
- **Response Time**: Average response time < 500ms
- **Caching**: Responses are optimized for performance
- **Uptime**: 99.9% availability SLA

## 🔧 Error Handling

The API returns appropriate HTTP status codes:

- `200` - Success
- `400` - Bad Request (invalid parameters)
- `404` - Not Found (resource doesn't exist)
- `500` - Internal Server Error
- `503` - Service Unavailable (external API issues)

**Error Response Example:**

```json
{
    "success": false,
    "message": "Launch not found. Please check the launch identifier and try again.",
    "data": null
}
```

## 🚀 Use Cases

- **Space Enthusiasts**: Track upcoming launches and mission details
- **Developers**: Build space-themed applications and dashboards
- **Researchers**: Access historical launch data for analysis
- **Educational**: Learn about SpaceX missions and achievements
- **Real-time Tracking**: Monitor Dragon capsule missions in real-time

## 🤝 Contributing

This is an open-source project. Feel free to:

- Report issues or bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is released under the [CC0 1.0 Universal](LICENSE) license - completely free to use for any purpose.

## 🔗 Links

- **API Documentation**: [Interactive API Explorer](https://spacex-api.ridwaanhall.com)
- **GitHub Repository**: [Source Code](https://github.com/ridwaanhall/SpaceX)
- **Developer**: [Ridwan Hall](https://github.com/ridwaanhall)

## 🏷️ Keywords

SpaceX API, NASA, rocket launches, space missions, Dragon capsule, Falcon 9, Starlink, space data, REST API, real-time tracking, launch statistics, upcoming missions, space technology, satellite tracking, ISS missions, space exploration

---

**Built with ❤️ for the space community**

*Keep exploring the final frontier! 🌌*
