# Build the image
podman build -t a2a-server .

# Run the container
podman run -p 9999:9999 a2a-server