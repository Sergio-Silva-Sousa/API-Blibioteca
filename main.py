from app import app
from config import config_tudo

config_tudo()

app.run(debug=True)