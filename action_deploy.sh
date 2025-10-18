mkdir -p /www/code
cd /www/code
git clone https://github.com/codists/python-talk.git

mkdir -p /www/frontend/python_talk
cd /www/code/python-talk/frontend
npm install -y
npm run build
cp -r /www/code/python-talk/frontend/dist /www/frontend/python_talk/

cp -r /www/code/python-talk/deployment/common /www
cd /www/common/
docker compose -f docker-compose-common.yml up -d

mkdir -p /www/backend/python_talk
cp -r /www/code/python-talk/backend/ /www/backend/python_talk/
cd /www/backend/python_talk/backend
docker build -t python_talk:0.0.1 /www/backend/python_talk/backend
docker compose -f /www/backend/python_talk/backend/docker-compose.yml up -d
