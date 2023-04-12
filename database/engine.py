# External libraries
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///productos.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.engine import URL
# from sqlalchemy import text

# url_object = URL.create(
#     "mysql+pymysql",
#     username="root",
#     password="Simurdieracolacao5677656",  # plain (unescaped) text
#     host="localhost",
#     database="pruebas_cameras_review",
# )
# consulta = text('SElECT * FROM editores')
# engine = create_engine(url_object)
# conn = engine.connect()
# res = conn.execute(consulta)
# print(list(res.keys()))
# for row in res:
#     print(row)
