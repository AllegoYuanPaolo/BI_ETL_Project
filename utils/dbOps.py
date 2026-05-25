from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def get_db_connection(db_name: str)-> Session:
    DATABASE_URL = f"mysql+pymysql://root:@localhost/{db_name}"
    engine = create_engine(DATABASE_URL)

    SessionLocal = sessionmaker(bind=engine)

    db_session: Session = SessionLocal()

    return db_session

        


from models import src_models 
from sqlalchemy import text

if __name__ == "__main__":
    db = get_db_connection("ordertracking")
    result = db.query(src_models.Order).all()
    for row in result:
        print(row.orderNumber, row.total_price)
    ... 