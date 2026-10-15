# =========================================================
# BASE IMAGE
# =========================================================
# Our host computer does NOT need Python 3.12 installed.
# This image provides Python inside the Docker environment.
FROM python:3.12-slim


# =========================================================
# PYTHON SETTINGS
# =========================================================

# Don't create unnecessary .pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Immediately send Python output to Docker logs.
ENV PYTHONUNBUFFERED=1


# =========================================================
# WORKING DIRECTORY
# =========================================================

# Create/use /app as our working directory inside Docker.
WORKDIR /app


# =========================================================
# INSTALL DEPENDENCIES
# =========================================================

# Copy requirements first.
# Keeping this separate improves Docker layer caching.
COPY requirements.txt .

# Install Django + PostgreSQL driver inside the image.
RUN pip install --no-cache-dir -r requirements.txt


# =========================================================
# APPLICATION CODE
# =========================================================

# Copy our project files into /app.
COPY . .


# =========================================================
# DJANGO PORT
# =========================================================

# Document that Django listens on port 8000.
EXPOSE 8000


# =========================================================
# DEFAULT COMMAND
# =========================================================

# Start Django whenever this container starts.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]