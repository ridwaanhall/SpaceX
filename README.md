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
        "total_count": 3,
        "upcoming_count": 3,
        "starlink_count": 2,
        "launches": [
            {
                "id": 2983,
                "documentId": "mtbreuw8mnwdog1e9xtrfehj",
                "correlationId": "55FDEC963805DE594B61B2C1692CADC2C1DFB844D6AC10C5BFED33C842087B2E",
                "endDate": null,
                "endTime": null,
                "title": "Starlink Mission",
                "subtitle": null,
                "quickDetail": null,
                "link": "sl-17-9",
                "youtubeVideoId": null,
                "streamingVideoType": null,
                "callToAction": "WATCH",
                "missionStatus": "upcoming",
                "vehicle": "Falcon 9",
                "returnSite": "Droneship",
                "launchSite": "SLC-4E, California",
                "isOngoing": false,
                "launchDate": "2025-09-06",
                "launchTime": "08:42:00",
                "missionType": "starlink",
                "directToCell": false,
                "isLive": false,
                "returnDateTime": null,
                "showLaunchTimeInsteadOfWindow": "false",
                "imageDesktop": {
                    "id": 4585,
                    "name": "mission_launches_3575_Desktop.jpg",
                    "alternativeText": "mission_launches_3575_Desktop.jpg",
                    "caption": "mission_launches_3575_Desktop.jpg",
                    "width": 2600,
                    "height": 1200,
                    "formats": {
                        "large": {
                            "ext": ".jpg",
                            "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/large_mission_launches_3575_Desktop_f4868ac3c6.jpg",
                            "hash": "large_mission_launches_3575_Desktop_f4868ac3c6",
                            "mime": "image/jpeg",
                            "name": "large_mission_launches_3575_Desktop.jpg",
                            "path": null,
                            "size": 24.77,
                            "width": 1000,
                            "height": 462
                        },
                        "small": {},
                        "medium": {},
                        "thumbnail": {}
                    },
                    "hash": "mission_launches_3575_Desktop_f4868ac3c6",
                    "ext": ".jpg",
                    "mime": "image/jpeg",
                    "size": 106.29,
                    "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/mission_launches_3575_Desktop_f4868ac3c6.jpg",
                    "previewUrl": null,
                    "provider": "strapi-provider-upload-azure-storage",
                    "provider_metadata": null,
                    "folderPath": "/28/68",
                    "createdAt": "2023-03-10T17:00:44.360000Z",
                    "updatedAt": "2023-03-10T17:00:44.360000Z",
                    "documentId": "ib1s9us9lugbdvfp24g54n9n",
                    "locale": null,
                    "publishedAt": "2024-10-21T16:04:39.469000Z"
                },
                "imageMobile": {
                    "id": 4591,
                    "name": "mission_launches_3560_Mobile.jpg",
                    "alternativeText": "mission_launches_3560_Mobile.jpg",
                    "caption": "mission_launches_3560_Mobile.jpg",
                    "width": 840,
                    "height": 1200,
                    "formats": {
                        "large": {
                            "ext": ".jpg",
                            "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/large_mission_launches_3560_Mobile_ff370a3659.jpg",
                            "hash": "large_mission_launches_3560_Mobile_ff370a3659",
                            "mime": "image/jpeg",
                            "name": "large_mission_launches_3560_Mobile.jpg",
                            "path": null,
                            "size": 42.52,
                            "width": 700,
                            "height": 1000
                        },
                        "small": {},
                        "medium": {},
                        "thumbnail": {}
                    },
                    "hash": "mission_launches_3560_Mobile_ff370a3659",
                    "ext": ".jpg",
                    "mime": "image/jpeg",
                    "size": 56.27,
                    "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/mission_launches_3560_Mobile_ff370a3659.jpg",
                    "previewUrl": null,
                    "provider": "strapi-provider-upload-azure-storage",
                    "provider_metadata": null,
                    "folderPath": "/28/68",
                    "createdAt": "2023-03-10T17:00:43.438000Z",
                    "updatedAt": "2023-03-10T17:00:43.438000Z",
                    "documentId": "ctx1qg31ucankugrow3txlsq",
                    "locale": null,
                    "publishedAt": "2024-10-21T16:04:39.469000Z"
                },
                "ongoingMissionImageDesktop": null,
                "ongoingMissionImageMobile": null,
                "videoDesktop": null,
                "videoMobile": null
            },
        ]
    }
}
```

**Statistics Endpoint:** `GET /upcoming/stats/`

Get statistical breakdown of upcoming launches.

### 3. Launch History

**Endpoint:** `GET /launches/`

Get historical SpaceX launch data.

**Response Example:**

```json
{
    "success": true,
    "message": "SpaceX launches data retrieved successfully",
    "data": {
        "total_launches": 567,
        "launches": [
            {
                "id": 2973,
                "documentId": "ep28dxp7vzgj0lq0uw1qwqre",
                "correlationId": "FB7BAB9EDF08F024AABF3501518399E82AB590666207A8B0AB7963B181ECF4B8",
                "endDate": null,
                "endTime": null,
                "title": "Starship's Tenth Flight Test",
                "subtitle": null,
                "quickDetail": null,
                "link": "starship-flight-10",
                "youtubeVideoId": null,
                "streamingVideoType": null,
                "callToAction": "WATCH",
                "missionStatus": "final",
                "vehicle": "Starship",
                "returnSite": "Expended",
                "launchSite": "Starbase, Texas",
                "isOngoing": false,
                "launchDate": "2025-08-26",
                "launchTime": "18:30:00",
                "missionType": "starship",
                "directToCell": false,
                "isLive": false,
                "returnDateTime": null,
                "showLaunchTimeInsteadOfWindow": "false",
                "imageDesktop": {
                    "id": 6184,
                    "name": "Flight_10_Website_Desktop_3.jpg",
                    "alternativeText": null,
                    "caption": null,
                    "width": 2600,
                    "height": 1200,
                    "formats": {
                        "large": {
                            "ext": ".jpg",
                            "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/large_Flight_10_Website_Desktop_3_2d3ade143a.jpg",
                            "hash": "large_Flight_10_Website_Desktop_3_2d3ade143a",
                            "mime": "image/jpeg",
                            "name": "large_Flight_10_Website_Desktop_3.jpg",
                            "path": null,
                            "size": 40.95,
                            "width": 1000,
                            "height": 462,
                            "sizeInBytes": 40954
                        },
                        "small": {},
                        "medium": {},
                        "thumbnail": {}
                    },
                    "hash": "Flight_10_Website_Desktop_3_2d3ade143a",
                    "ext": ".jpg",
                    "mime": "image/jpeg",
                    "size": 279.09,
                    "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/Flight_10_Website_Desktop_3_2d3ade143a.jpg",
                    "previewUrl": null,
                    "provider": "strapi-provider-upload-azure-storage",
                    "provider_metadata": null,
                    "folderPath": "/105/672",
                    "createdAt": "2025-08-27T02:12:22.062Z",
                    "updatedAt": "2025-08-27T02:12:22.062Z",
                    "documentId": "rqu4ebpg3vj3sg1r50ibt2cl",
                    "locale": null,
                    "publishedAt": "2025-08-27T02:12:22.063Z"
                },
                "imageMobile": {
                    "id": 6183,
                    "name": "Flight_10_Website_Mobile_3.jpg",
                    "alternativeText": null,
                    "caption": null,
                    "width": 840,
                    "height": 1200,
                    "formats": {
                        "large": {
                            "ext": ".jpg",
                            "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/large_Flight_10_Website_Mobile_3_39310629e9.jpg",
                            "hash": "large_Flight_10_Website_Mobile_3_39310629e9",
                            "mime": "image/jpeg",
                            "name": "large_Flight_10_Website_Mobile_3.jpg",
                            "path": null,
                            "size": 57.59,
                            "width": 700,
                            "height": 1000,
                            "sizeInBytes": 57590
                        },
                        "small": {},
                        "medium": {},
                        "thumbnail": {}
                    },
                    "hash": "Flight_10_Website_Mobile_3_39310629e9",
                    "ext": ".jpg",
                    "mime": "image/jpeg",
                    "size": 85.63,
                    "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/Flight_10_Website_Mobile_3_39310629e9.jpg",
                    "previewUrl": null,
                    "provider": "strapi-provider-upload-azure-storage",
                    "provider_metadata": null,
                    "folderPath": "/105/672",
                    "createdAt": "2025-08-27T02:12:21.344Z",
                    "updatedAt": "2025-08-27T02:12:21.344Z",
                    "documentId": "ojxw2eqzc2snfquuzxqwkm92",
                    "locale": null,
                    "publishedAt": "2025-08-27T02:12:21.345Z"
                },
                "ongoingMissionImageDesktop": null,
                "ongoingMissionImageMobile": null,
                "videoDesktop": null,
                "videoMobile": null
            },
        ]
    }
}
```

**Detail Endpoint:** `GET /launches/{link}/`

Get detailed information about a specific launch using the `link` field from the launches list.

**Response Example:**

```json
{
    "success": true,
    "message": "Launch details retrieved successfully",
    "data": {
        "id": 3276,
        "documentId": "eupgnxxhyxvkrxweakt6i5dd",
        "correlationId": "FB7BAB9EDF08F024AABF3501518399E82AB590666207A8B0AB7963B181ECF4B8",
        "missionId": "starship-flight-10",
        "title": "Starship's Tenth Flight Test",
        "subtitle": null,
        "callToAction": "WATCH",
        "quickDetail": null,
        "endDate": null,
        "youtubeVideoId": null,
        "streamingVideoType": null,
        "missionStatus": "final",
        "followDragonEnabled": false,
        "returnFromIssEnabled": false,
        "toTheIssEnabled": false,
        "toTheIssTense": null,
        "imageDesktop": {
            "id": 6184,
            "name": "Flight_10_Website_Desktop_3.jpg",
            "alternativeText": null,
            "caption": null,
            "width": 2600,
            "height": 1200,
            "formats": {
                "large": {
                    "ext": ".jpg",
                    "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/large_Flight_10_Website_Desktop_3_2d3ade143a.jpg",
                    "hash": "large_Flight_10_Website_Desktop_3_2d3ade143a",
                    "mime": "image/jpeg",
                    "name": "large_Flight_10_Website_Desktop_3.jpg",
                    "path": null,
                    "size": 40.95,
                    "width": 1000,
                    "height": 462,
                    "sizeInBytes": 40954
                },
                "small": {},
                "medium": {},
                "thumbnail": {}
            },
            "hash": "Flight_10_Website_Desktop_3_2d3ade143a",
            "ext": ".jpg",
            "mime": "image/jpeg",
            "size": 279.09,
            "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/Flight_10_Website_Desktop_3_2d3ade143a.jpg",
            "previewUrl": null,
            "provider": "strapi-provider-upload-azure-storage",
            "provider_metadata": null,
            "folderPath": "/105/672",
            "createdAt": "2025-08-27T02:12:22.062000Z",
            "updatedAt": "2025-08-27T02:12:22.062000Z",
            "documentId": "rqu4ebpg3vj3sg1r50ibt2cl",
            "locale": null,
            "publishedAt": "2025-08-27T02:12:22.063000Z"
        },
        "imageMobile": {
            "id": 6183,
            "name": "Flight_10_Website_Mobile_3.jpg",
            "alternativeText": null,
            "caption": null,
            "width": 840,
            "height": 1200,
            "formats": {
                "large": {},
                "small": {},
                "medium": {},
                "thumbnail": {}
            },
            "hash": "Flight_10_Website_Mobile_3_39310629e9",
            "ext": ".jpg",
            "mime": "image/jpeg",
            "size": 85.63,
            "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/Flight_10_Website_Mobile_3_39310629e9.jpg",
            "previewUrl": null,
            "provider": "strapi-provider-upload-azure-storage",
            "provider_metadata": null,
            "folderPath": "/105/672",
            "createdAt": "2025-08-27T02:12:21.344000Z",
            "updatedAt": "2025-08-27T02:12:21.344000Z",
            "documentId": "ojxw2eqzc2snfquuzxqwkm92",
            "locale": null,
            "publishedAt": "2025-08-27T02:12:21.345000Z"
        },
        "videoDesktop": null,
        "videoMobile": null,
        "infographicDesktop": {
            "id": 5730,
            "name": "SPACEX_STARSHIP_INFOGRAPHIC_032425_DESKTOP.jpg",
            "alternativeText": null,
            "caption": null,
            "width": 7223,
            "height": 3773,
            "formats": {},
            "hash": "SPACEX_STARSHIP_INFOGRAPHIC_032425_DESKTOP_769fc7b3bc",
            "ext": ".jpg",
            "mime": "image/jpeg",
            "size": 400.59,
            "url": "https://sxcontent9668.azureedge.us/cms-assets/assets/SPACEX_STARSHIP_INFOGRAPHIC_032425_DESKTOP_769fc7b3bc.jpg",
            "previewUrl": null,
            "provider": "strapi-provider-upload-azure-storage",
            "provider_metadata": null,
            "folderPath": "/6/205",
            "createdAt": "2025-05-20T16:28:06.572000Z",
            "updatedAt": "2025-05-20T16:28:06.572000Z",
            "documentId": "l3oxa8iyv3glg88mczgssfl3",
            "locale": null,
            "publishedAt": "2025-05-20T16:28:06.573000Z"
        },
        "infographicMobile": {},
        "preLaunchTimeline": {
            "id": 220,
            "name": "Starship's Tenth Flight Test",
            "title": "Countdown",
            "disclaimer": "All Times Approximate",
            "timeHeader": "Hr/Min/Sec",
            "descriptionHeader": "Event",
            "createdAt": "2024-05-21T16:17:21.287000Z",
            "updatedAt": "2025-08-19T15:13:18.653000Z",
            "publishedAt": "2025-08-19T15:13:18.703000Z",
            "documentId": "y7e6yzzsrjec5lx1kdjadjaq",
            "locale": null,
            "timelineEntries": [
                {
                    "id": 16532,
                    "time": "01:15:00",
                    "description": "SpaceX Flight Director conducts poll and verifies GO for propellant load"
                },
                {
                    "id": 16540,
                    "time": "00:00:30",
                    "description": "SpaceX flight director verifies GO for launch"
                },
                {
                    "id": 16541,
                    "time": "00:00:10",
                    "description": "Flame deflector activation"
                },
                {
                    "id": 16542,
                    "time": "00:00:03",
                    "description": "Raptor ignition sequence begins"
                },
                {
                    "id": 16543,
                    "time": "00:00:00",
                    "description": "Excitement guaranteed"
                }
            ]
        },
        "postLaunchTimeline": {
            "id": 1226,
            "title": "FLIGHT TEST TIMELINE",
            "disclaimer": "All Times Approximate",
            "timeHeader": "Hr/Min/Sec",
            "descriptionHeader": "Event",
            "timelineEntries": [
                {
                    "id": 17127,
                    "time": "00:00:02",
                    "description": "Liftoff"
                },
                {
                    "id": 17143,
                    "time": "01:06:14",
                    "description": "Landing flip"
                },
                {
                    "id": 17144,
                    "time": "01:06:20",
                    "description": "Landing burn start"
                },
                {
                    "id": 17145,
                    "time": "01:06:30",
                    "description": "An exciting landing!"
                }
            ]
        },
        "astronauts": [],
        "webcasts": [
            {
                "id": 1165,
                "videoId": "1960178606212063307",
                "streamingVideoType": "x.com",
                "title": null,
                "date": null,
                "isFeatured": null,
                "imageDesktop": null,
                "imageMobile": null
            }
        ],
        "paragraphs": [
            {
                "id": 8299,
                "content": "Starship’s tenth flight test lifted off on August 26, 2025, at 6:30 p.m. CT from Starbase, Texas, taking a significant step forward in developing the world’s first fully reusable launch vehicle. Every major objective was met, providing critical data to inform designs of the next generation Starship and Super Heavy."
            },
        ],
        "carousel": null
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
        "glass_dragon_gps_time_f64": 1440189106.249846,
        "glass_dragon_mission_time_f64": 135950.4,
        "glass_dgn_alt_geod_f64": 419647.907141,
        "glass_dgn_speed_f64": 7361.691727,
        "glass_predict_iss_r_lla_v3": [
            -0.272181,
            -2.229614,
            419645.197324
        ],
        "glass_predict_iss_r_ecef_v3": [
            -4009197.181579,
            -5178418.714829,
            -1816399.15774
        ],
        "glass_predict_dgn_r_lla_v3": [
            -0.272182,
            -2.229614,
            419646.528906
        ],
        "glass_predict_dgn_r_ecef_v3": [
            -4009194.023878,
            -5178420.860653,
            -1816404.957743
        ],
        "glass_prop_iss_r_ecef_v3": [
            [
                -4020829,
                -5174524,
                -1801706
            ],
        ],
        "glass_prop_dgn_r_ecef_v3": [
            [
                -4020825,
                -5174526,
                -1801711
            ],
        ]
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
    "success": true, // true or false
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

Built with ❤️ for the space community

## Keep exploring the final frontier! 🌌
