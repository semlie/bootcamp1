# Build Docker image
Write-Host "Building Docker image..."
docker build -t python-api .

# Check if the build was successful
if ($LastExitCode -eq 0) {
    Write-Host "Docker build completed successfully."

    # Run Docker container
    Write-Host "Running Docker container..."
    docker run --env-file .env -p 5000:5000 python-api
} else {
    Write-Host "Docker build failed. Exiting..."
}