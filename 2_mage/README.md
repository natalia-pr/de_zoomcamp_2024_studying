# Configure Mage
1. Matt's repositor with Mage
git clone https://github.com/mage-ai/mage-zoomcamp.git mage-zoomcamp
2. Rename dev.env to simply .env— this will ensure the file is not committed to Git by accident
cp dev.env .env
3. Build docker compose
docker compose build
4. Updating the last version of Mage
docker pull mageai/mageai:latest