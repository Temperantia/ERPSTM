# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Action(Base):
    __tablename__ = 'action'

    idaction = Column(Integer, primary_key=True)
    nom = Column(String(45))

    rôle = relationship('Rôle', secondary='action_has_rôle')


class Fournisseur(Base):
    __tablename__ = 'fournisseur'

    idfournisseur = Column(Integer, primary_key=True)
    nom_raison_sociale = Column('nom/raison sociale', String(45))
    adresse = Column(String(45))
    forme = Column(String(45))
    Chiffre_d_affaire = Column("Chiffre d'affaire", Integer)
    effectif = Column(Integer)
    autorisation = Column(TINYINT)
    Status = Column(String(45))


class Request(Base):
    __tablename__ = 'request'

    idrequest = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    fournisseur_idfournisseur = Column(ForeignKey('fournisseur.idfournisseur'), nullable=False, index=True)

    fournisseur = relationship('Fournisseur')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nom = Column(String(70))
    prenom = Column(String(70))
    interne = Column(TINYINT)
    usercol = Column(VARCHAR(45))
    fournisseur_idfournisseur1 = Column(ForeignKey('fournisseur.idfournisseur'), nullable=False, index=True)

    fournisseur = relationship('Fournisseur')


class Rôle(Base):
    __tablename__ = 'rôle'
    __table_args__ = (
        Index('fk_rôle_user1_idx', 'user_id', 'user_idfournisseur'),
    )

    idrôle = Column(Integer, primary_key=True, unique=True)
    nom = Column(String(45))
    user_id = Column(ForeignKey('user.id'), nullable=False)
    user_idfournisseur = Column(Integer, nullable=False)

    user = relationship('User')


t_action_has_rôle = Table(
    'action_has_rôle', metadata,
    Column('action_idaction', ForeignKey('action.idaction'), primary_key=True, nullable=False, index=True),
    Column('rôle_idrôle', ForeignKey('rôle.idrôle'), primary_key=True, nullable=False, index=True)
)