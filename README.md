

# Build the image
docker build -t contributor-spotlight .

# Run the container
docker run -p 8080:80 contributor-spotlight

Cuisinsta Backend API 🚀This is the backend service for the Cuisinsta application, providing video reel data and service health status.📍 Base URLWhen running locally via Docker:http://localhost:5002🛠 Endpoints1. Health CheckCheck if the server is alive and kicking.URL: /healthMethod: GETResponse:JSON{
  "status": "online"
}
2. Get Reels FeedFetch a paginated list of video reels. Data is currently mocked (20 items total).URL: /reelsMethod: GETQuery Parameters:| Parameter | Type | Default | Description || :--- | :--- | :--- | :--- || page | int | 1 | The page number to fetch (Batch size is 5). |Success Response (200 OK):Returns an array of Reel objects.JSON[
  {
    "id": "vid_1",
    "username": "user_1",
    "likes": 100,
    "views": 1000,
    "shares": 10
  },
  ...
]
📦 Data Schema (Reel Object)FieldTypeDescriptionidstringUnique identifier for the video.usernamestringThe handle of the content creator.likesintegerTotal like count.viewsintegerTotal view count.sharesintegerTotal share count.💡 Frontend Integration NotesPagination Logic: The API returns 5 reels per page.To get the first batch: GET /reels?page=1To get the next batch: GET /reels?page=2End of Data: Since there are currently only 20 mock items, any request for page=5 or higher will return an empty list [].CORS: If your Vite/React app is running on a different port (e.g., 5173), ensure the backend has CORS enabled (I can help you add that middleware if you hit a "CORS error" in the browser console).
