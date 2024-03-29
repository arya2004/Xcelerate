
# Xcelerate

Xcelerate is an end-to-end machine learning project that predicts student exam performance using a Decision Tree model. It achieves a Best R-squared of 0.9994590956793753 with Decision Tree Regressor.

## Links

- Docker Hub: [Xcelerate Docker Image](https://hub.docker.com/repository/docker/zieglernattacatalyst/xcelerate/general)
- GitHub Repository: [Xcelerate GitHub](https://github.com/arya2004/xcelerate)

## Getting Started

### Docker Build

To build the Docker image for Xcelerate, run the following command in your terminal:

```bash
docker build -t xcelerate .
```

### Docker Run with Port Mapping

To run the Xcelerate app using Docker with port mapping to port 5000, use the following command:

```bash
docker run -p 5000:5000 xcelerate
```

The application will then be accessible at `http://localhost:5000`.

## Usage

1. Access the Xcelerate app through your browser at `http://localhost:5000`.
2. Follow the instructions on the web interface to input student data and predict exam performance.
3. View the prediction results on the web interface.

## Contributors

- [arya2004](https://github.com/arya2004)

