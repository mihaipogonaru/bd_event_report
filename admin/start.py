from app.app import app
from app.config import ServerConfig

if __name__ == "__main__":
    app.run(host=ServerConfig.host, port=ServerConfig.port, threaded=ServerConfig.threaded)
