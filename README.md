

# Build the image
docker build -t contributor-spotlight .

# Run the container
docker run -p 8080:80 contributor-spotlight

# Cuisinsta Backend API 🚀

This is a fast, containerized FastAPI backend providing a mock reels feed for the Cuisinsta frontend application.

---

## 📍 Connection Details
- **Base URL:** `http://localhost:5002`
- **Container Port:** `5002`
- **Environment:** Docker (Python 3.11-bullseye)

---

## 🛠 Endpoints

### 1. Health Check
Verify the service is running.

* **URL:** `/health`
* **Method:** `GET`
* **Response:**
    ```json
    {
      "status": "online"
    }
    ```

### 2. Get Reels Feed (Mock Data)
Fetches a list of 5 reels per page. Total available mock items: 20.

* **URL:** `/reels`
* **Method:** `GET`
* **Query Parameters:**

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `page` | `int` | `1` | The page number to fetch (Batch size is 5). |

* **Response (200 OK):**
    ```json
    [
      {
        "id": "vid_1",
        "username": "user_1",
        "likes": 100,
        "views": 1000,
        "shares": 10
      }
    ]
    ```

---

## 📦 Data Schema (Reel Object)

| Field | Type | Description |
| :--- | :--- | :--- |
| **id** | `string` | Unique identifier for the video. |
| **username** | `string` | Creator's display handle. |
| **likes** | `integer` | Total likes count. |
| **views** | `integer` | Total views count. |
| **shares** | `integer` | Total shares count. |

---

## ⚠️ Developer Notes for Frontend
1. **CORS:** If you encounter a "Cross-Origin" error, ensure the backend has CORS Middleware enabled for your frontend's port.
2. **Pagination:** Requests for `page=5` or higher will return an empty array `[]` as the mock data limit is 20.
3. **Images/Videos:** The `id` field is currently a placeholder. No actual media URLs are served in this mock version.
