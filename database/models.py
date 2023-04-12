# External libraries
from datetime import date
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

# Own libraries
from database.engine import Base


class Editor(Base):

    __tablename__ = 'Editor'

    id_editor = Column(Integer, primary_key=True, autoincrement=True)
    # resena = relationship('Resena', back_populates='Editor')
    nombre = Column(String(40), nullable=False)
    apellido = Column(String(40), nullable=False)
    correo = Column(String(50), nullable=False, unique=True)
    fecha_nacimiento = Column(Date, nullable=False)
    hash_contrasena = Column(String(64), nullable=False)

    def __init__(self, nombre: str, apellido: str, correo: str,
                 fecha_nacimiento: date, hash_contrasena: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.hash_contrasena = hash_contrasena

    def __repr__(self) -> str:
        return f'{__class__}: {self.nombre} {self.apellido}, {self.correo}'

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'


class Producto(Base):

    __tablename__ = 'Producto'

    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    # resena = relationship('Resena', back_populates='Producto')
    nombre = Column(String(60), nullable=False)
    marca = Column(String(50), nullable=False)
    precio = Column(Float, nullable=False)
    sku = Column(String(50), nullable=False)

    def __init__(self, nombre: str, marca: str,
                 precio: float, sku: str) -> None:
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.sku = sku

    def __repr__(self) -> str:
        return f'{__class__}: {self.nombre} {self.marca}, {self.sku}'

    def __str__(self) -> str:
        return f'{self.nombre}, {self.marca}'


class Resena(Base):

    __tablename__ = 'Resena'

    id_resena = Column(Integer, primary_key=True, autoincrement=True)
    id_editor = Column(Integer, ForeignKey(Editor.id_editor),
                       nullable=False)
    # editor = relationship('Editor', back_populates='Resena')
    titulo = Column(String(60), nullable=False)
    contenido = Column(String(2000), nullable=False)
    id_producto = Column(Integer, ForeignKey(Producto.id_producto),
                         nullable=False)
    # resena = relationship('Producto', back_populates='Resena')

    def __init__(self, id_editor: int, titulo: str, contenido: str,
                 id_producto: int) -> None:
        self.id_editor = id_editor
        self.titulo = titulo
        self.contenido = contenido
        self.id_producto = id_producto

    def __repr__(self) -> str:
        return f'{__class__}: {self.titulo}, Editor: {self.id_editor}'

    def __str__(self) -> str:
        return f'{self.titulo}'


class Imagen(Base):

    __tablename__ = 'Imagen'

    id_imagen = Column(Integer, primary_key=True, autoincrement=True)
    imagen = Column(String(256), nullable=False)
    id_resena = Column(Integer, ForeignKey(Resena.id_resena),
                       nullable=False)

    def __init__(self, imagen: str, id_resena: int) -> None:
        self.imagen = imagen
        self.id_resena = id_resena

    def __repr__(self) -> str:
        return f'{__class__}: {self.imagen} Reseña: {self.id_resena}'

    def __str__(self) -> str:
        return f'{self.imagen}'
