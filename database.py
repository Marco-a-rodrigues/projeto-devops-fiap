from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://livraria_database_user:32IrCiXdJcsGPLNGERwUUpd5vpRECNzS@dpg-csptgo5ds78s73dc9j8g-a.oregon-postgres.render.com/livraria_database"

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


if __name__ == "__main__":
    try:
        db = SessionLocal()
        print("conexão feita")
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)
    finally:
        db.close()
