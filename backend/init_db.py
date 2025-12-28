from sqlalchemy import create_engine
from models import Base

# Подключение к Docker-контейнеру
DATABASE_URL = "postgresql://user:password@localhost:5432/auto_db"

def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("🚀 Таблицы успешно созданы в Docker!")

if __name__ == "__main__":
    init_db()