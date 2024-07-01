from dotenv import load_dotenv
import os

load_dotenv()

#user = os.environ["USER"]
#password = os.environ["PASSWORD"]
#host = os.environ["HOST"]
#database = os.environ["DATABASE"]
#server = os.environ["SERVER"]
#user = os.getenv("USER", "postgres")  # Cambiar a tu usuario de PostgreSQL si es diferente
#host = os.getenv("HOST", "localhost")  # Puedes usar 'localhost' si la base de datos está en tu máquina local
#database = os.getenv("DATABASE", "prueb-BSD")  # Nombre de tu base de datos
#server = "postgresql"
DATABASE_CONNECTION_URI = 'postgresql://post:23s@localhost:5432/prueba_bsd'
#print(DATABASE_CONNECTION_URI)