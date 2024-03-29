# Stage 1: build dependencies and install requirements
FROM python:3.8-slim-buster AS builder

WORKDIR /build
COPY requirements.txt .

# update packages and install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    pip install --upgrade pip setuptools wheel && \
    pip wheel --wheel-dir=/wheels -r requirements.txt

# Stage 2: Create the final image
FROM python:3.8-slim-buster

WORKDIR /app

# copy built wheels from the previous stage
COPY --from=builder /wheels /wheels
COPY . .

# install application and clean up
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --no-index --find-links=/wheels -r requirements.txt && \
    apt-get purge -y gcc && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /wheels

EXPOSE 5000

CMD ["python3", "app.py"]
