# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Action(Base):
    __tablename__ = 'action'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

    role = relationship('Role', secondary='action_role')


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(45))


class Supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    address = Column(String(45))
    legal_status = Column(String(45))
    turnover = Column(String(45))
    headcounts = Column(String(45))
    authorized = Column(TINYINT)
    num_SIREN = Column(String(45))


t_action_role = Table(
    'action_role', metadata,
    Column('id_action', ForeignKey('action.id'), primary_key=True, nullable=False, index=True),
    Column('id_role', ForeignKey('role.id'), primary_key=True, nullable=False, index=True)
)


class Request(Base):
    __tablename__ = 'request'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    id_supplier = Column(ForeignKey('supplier.id'), nullable=False, index=True)
    supp_status = Column(Enum('Not delivered', 'Delivering', 'Delivered'))
    order_nature = Column(String(45))
    order_amount = Column(String(45))
    order_ispaid = Column(TINYINT)
    opinion = Column(String(45))

    supplier = relationship('Supplier')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    lastname = Column(String(70), nullable=False)
    firstname = Column(String(70), nullable=False)
    personal_id = Column(String(45))
    password = Column(String(45), nullable=False)
    internal = Column(TINYINT, nullable=False)
    id_supplier = Column(ForeignKey('supplier.id'), index=True)
    id_role = Column(ForeignKey('role.id'), index=True)

    role = relationship('Role')
    supplier = relationship('Supplier')