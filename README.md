

# Build the image
docker build -t contributor-spotlight .

# Run the container
docker run -p 8080:80 contributor-spotlight
