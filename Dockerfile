FROM node:20-slim

# Install dependencies for downloading ADNL proxy
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Node.js dependencies
COPY package*.json ./
RUN npm install

# Copy application files (including the reverse-proxy configuration)
COPY . .

# Expose HTTP port (3000) and ADNL UDP port (if configured)
EXPOSE 3000
EXPOSE 12146/udp

# Set start script as entrypoint
CMD ["bash", "start.sh"]
