from typing import Optional

from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Index, Integer, LargeBinary, PrimaryKeyConstraint, SmallInteger, String, TEXT, Table
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
import decimal

class Base(DeclarativeBase):
    pass


class AConfiguracion(Base):
    __tablename__ = 'AConfiguracion'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='AConfi_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    RUTASERVIDOR: Mapped[Optional[str]] = mapped_column(String(499, 'Modern_Spanish_CI_AS'))


class ADescargas(Base):
    __tablename__ = 'ADescargas'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='Descar_PKConsecutivo'),
        Index('Descar_FKFacEntNumComp', 'FACTURAENTRADA', 'NUMPARTECOM'),
        Index('Descar_FKNumParte', 'NUMPARTECOM'),
        Index('Descar_FKOrdFacEntParLin', 'NUMORDEN', 'FACTURAENTRADA', 'NUMPARTECOM', 'LINEAREQ', 'LINEACOMPONENTE', unique=True)
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMORDEN: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FACTURAENTRADA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    LINEAREQ: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTEPAR: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    NUMPARTECOM: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTDESC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    FECHADESC: Mapped[Optional[int]] = mapped_column(Integer)
    LINEACOMPONENTE: Mapped[Optional[int]] = mapped_column(Integer)


class ETipoMat(Base):
    __tablename__ = 'ETipoMat'
    __table_args__ = (
        PrimaryKeyConstraint('TIPO', name='ETipos_PKTipoMat'),
    )

    TIPO: Mapped[str] = mapped_column(String(4, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))


class GAAduanal(Base):
    __tablename__ = 'GAAduanal'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEAA', name='AgeAdu_PKClaveAA'),
    )

    CLAVEAA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    NOMBRE: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    DIRECCION: Mapped[Optional[str]] = mapped_column(String(1500, 'Modern_Spanish_CI_AS'))
    CODIGOPOSTAL: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CIUDAD: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESTADO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    TELEFONO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    FAX: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    EMAIL: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    RFC: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CURP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PUESTO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PATENTE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    EMPRESA: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    CONTACTO: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    RUTAARCHCER: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    RUTAARCHKEY: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    CLAVEACCESO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FORMAGENFIEL: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    RUTALEERARCHAAFIRMA: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    RUTADEPARCHIVO: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    CLAVEACCESOFIEL: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    USUARIOWEBSERVICEVU: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CLAVEACCESOWEBSERVICEVU: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    EMAILVU: Mapped[Optional[str]] = mapped_column(String(800, 'Modern_Spanish_CI_AS'))
    TIPOFIGURAVU: Mapped[Optional[str]] = mapped_column(String(29, 'Modern_Spanish_CI_AS'))
    RUTAARCHIVOSXML: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    RFCCONSULTA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    RUTAARCHCERDODA: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    RUTAARCHKEYDODA: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    USUARIOWEBSERVICEDODA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CLAVEACCESOWEBSERVICEDODA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CLAVEACCESOFIELDODA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    RUTAARCHIVOSXMLDODA: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))


class GAAduanalPersonal(Base):
    __tablename__ = 'GAAduanalPersonal'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEAA', 'LINEA', name='AgeAduP_PKClaveAALin'),
    )

    CLAVEAA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    NOMBRE: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    RFC: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CURP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PUESTO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PATENTE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    NOMBRES: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    APELLIDOPATERNO: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    APELLIDOMATERNO: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    EMAIL: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class GAccesos(Base):
    __tablename__ = 'GAccesos'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='GAC_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FECHAINICIAL: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAFINAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAINICIAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAFINAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORADEUSO: Mapped[Optional[int]] = mapped_column(Integer)
    MAQUINA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    IP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ESTADO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))


class GAccesosModulos(Base):
    __tablename__ = 'GAccesosModulos'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='GAccMod_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FECHAINICIAL: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAFINAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAINICIAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAFINAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORADEUSO: Mapped[Optional[int]] = mapped_column(Integer)
    MAQUINA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    IP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ESTADO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    MODULO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    INDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class GAduanaSec(Base):
    __tablename__ = 'GAduanaSec'
    __table_args__ = (
        PrimaryKeyConstraint('ADUANASECCION', name='AduSec_PKAduanaSec'),
    )

    ADUANASECCION: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    NOMBRE: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))


class GAgencyTariffCodes(Base):
    __tablename__ = 'GAgencyTariffCodes'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='PK_CONSECUTIVO'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    TARIFFFLAGCODE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    AGENCYCODE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    REQUIREDMAYBEREQUIRED: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PROGRAMCODE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TARIFFFLAGCODEDEFINITION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))


class GAnexo22App3(Base):
    __tablename__ = 'GAnexo22App3'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='GAN22_PKClaveAnexo22'),
    )

    CLAVE: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    METODOTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    TIPOFECHAPAGO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class GAphis(Base):
    __tablename__ = 'GAphis'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVOAPHIS', name='GAps_Consecutivo'),
    )

    CONSECUTIVOAPHIS: Mapped[int] = mapped_column(Integer, primary_key=True)
    PROGRAMCODE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PROCESSINGCODE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    APHISTYPE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    DISCLAIMER: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ELECTRONICIMAGE: Mapped[Optional[str]] = mapped_column(CHAR(3, 'Modern_Spanish_CI_AS'))
    CONFIDENTIAL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    GLOBALPRODUCTID: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    INTENDEDUSECODE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    INTENDEDUSEDESCRIPTION: Mapped[Optional[str]] = mapped_column(String(24, 'Modern_Spanish_CI_AS'))
    ITEMTYPE: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PRODUCTCODE: Mapped[Optional[str]] = mapped_column(String(24, 'Modern_Spanish_CI_AS'))
    PRODUCTCODE2: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    PRODUCTCODE3: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SCIENTIFICGENUSNAME: Mapped[Optional[str]] = mapped_column(String(24, 'Modern_Spanish_CI_AS'))
    SCIENTIFICSPECIESNAME: Mapped[Optional[str]] = mapped_column(String(24, 'Modern_Spanish_CI_AS'))
    SCIENTIFICSUBSPECIESNAME: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    COMMONNAMESPECIFIC: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    COMMONNAMEGENERAL: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    SIGNEDDOC: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    SIGNEDDOCDATE: Mapped[Optional[int]] = mapped_column(Integer)
    SIGNEDDOCID: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    INVOICENUMBER: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    QUANTITY1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    QUANTITY2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    QUANTITY3: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    INSPECTION: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    INSPECTIONDATE: Mapped[Optional[int]] = mapped_column(Integer)
    INSPECTIONLOCCODE: Mapped[Optional[int]] = mapped_column(Integer)
    INSPECTIONLOCATION: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CTRYPROD: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    CTRYSRC: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))


class GAphisContainers(Base):
    __tablename__ = 'GAphisContainers'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVOAPHIS', 'LINEAAPHIS', name='GACO_ConsecAphis_LinCont'),
    )

    CONSECUTIVOAPHIS: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAAPHIS: Mapped[int] = mapped_column(Integer, primary_key=True)
    CONTAINERNUMBER: Mapped[Optional[str]] = mapped_column(String(24, 'Modern_Spanish_CI_AS'))
    TYPE: Mapped[Optional[int]] = mapped_column(Integer)
    LENGTH: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))


class GAphisEntities(Base):
    __tablename__ = 'GAphisEntities'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVOAPHIS', 'LINEAENTITI', name='GAEN_ConsecAphisLinEn'),
    )

    CONSECUTIVOAPHIS: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAENTITI: Mapped[int] = mapped_column(Integer, primary_key=True)
    CONSIGNEEKEY: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LPCOAUTHPARTYKEY: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    GROWERKEY: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    BROKERKEY: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class GAphisItemsChr(Base):
    __tablename__ = 'GAphisItemsChr'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVOAPHIS', 'LINEAITEM', name='GAic_ConsecAphisLinea'),
    )

    CONSECUTIVOAPHIS: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAITEM: Mapped[int] = mapped_column(Integer, primary_key=True)
    ITEMID: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    NUMBERFROM: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    NUMBERTO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CATEGORYTYPE: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CATEGORYCODE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    COMMODITYQUA: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    COMMODITYCHARQUA: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    DESCRIPCTION: Mapped[Optional[str]] = mapped_column(String(59, 'Modern_Spanish_CI_AS'))


class GAphisLpcos(Base):
    __tablename__ = 'GAphisLpcos'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVOAPHIS', 'LINEALPCOS', name='GALP_ConsecAphisLinLp'),
    )

    CONSECUTIVOAPHIS: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEALPCOS: Mapped[int] = mapped_column(Integer, primary_key=True)
    ISSUER: Mapped[Optional[str]] = mapped_column(String(39, 'Modern_Spanish_CI_AS'))
    ISSUERLOCQUA: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    ISSUERLOC: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    ISSUERLOCDESC: Mapped[Optional[str]] = mapped_column(String(29, 'Modern_Spanish_CI_AS'))
    TXNTYPE: Mapped[Optional[int]] = mapped_column(Integer)
    TYPE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    NUMBER: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    DATEQUAL: Mapped[Optional[int]] = mapped_column(Integer)
    DATE: Mapped[Optional[int]] = mapped_column(Integer)
    QTY: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UOM: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))


class GAphisPItems(Base):
    __tablename__ = 'GAphisPItems'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVOAPHIS', 'LINEAPITEM', name='GAPI_ConsecLineaIt'),
    )

    CONSECUTIVOAPHIS: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAPITEM: Mapped[int] = mapped_column(Integer, primary_key=True)
    SOURCETYPECODE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    COUNTRYCODE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    GEOLOCATION: Mapped[Optional[str]] = mapped_column(String(24, 'Modern_Spanish_CI_AS'))
    PROCESSINGSTART: Mapped[Optional[int]] = mapped_column(Integer)
    PROCESSINGEND: Mapped[Optional[int]] = mapped_column(Integer)
    PROCESSINGTYPE: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    PROCESSINGDESC: Mapped[Optional[str]] = mapped_column(String(49, 'Modern_Spanish_CI_AS'))


class GAphisRoutings(Base):
    __tablename__ = 'GAphisRoutings'
    __table_args__ = (
        PrimaryKeyConstraint('APHISCONSEC', 'LINEAROUTING', name='GARO_ConsecAphis_LinRouting'),
    )

    APHISCONSEC: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAROUTING: Mapped[int] = mapped_column(Integer, primary_key=True)
    TYPE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    COUNTRY: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    NAME: Mapped[Optional[str]] = mapped_column(String(59, 'Modern_Spanish_CI_AS'))


class GArchivosConsecutivos(Base):
    __tablename__ = 'GArchivosConsecutivos'
    __table_args__ = (
        PrimaryKeyConstraint('ARCHIVO', name='PKARCHIVO'),
    )

    ARCHIVO: Mapped[str] = mapped_column(String(100, 'Modern_Spanish_CI_AS'), primary_key=True)
    CONSECUTIVO: Mapped[Optional[int]] = mapped_column(Integer)


class GArchivosDescargaSifra(Base):
    __tablename__ = 'GArchivosDescargaSifra'
    __table_args__ = (
        PrimaryKeyConstraint('ARCHIVO', name='GAR_PKArchivo'),
    )

    ARCHIVO: Mapped[str] = mapped_column(String(99, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPO: Mapped[Optional[str]] = mapped_column(CHAR(20, 'Modern_Spanish_CI_AS'))


class GArchivosSIAA(Base):
    __tablename__ = 'GArchivosSIAA'
    __table_args__ = (
        PrimaryKeyConstraint('ARCHIVO', name='gArcSiaa_PKArchivo'),
    )

    ARCHIVO: Mapped[str] = mapped_column(String(255, 'Modern_Spanish_CI_AS'), primary_key=True)
    MEDIDA: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    HORA: Mapped[Optional[int]] = mapped_column(Integer)
    NUMFACTURA: Mapped[Optional[str]] = mapped_column(String(21, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FOLDER_LLEGADA_FTP: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))


class GAvisosElectronicos(Base):
    __tablename__ = 'GAvisosElectronicos'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='GAvE_SysIDAE'),
        Index('GAvE_NumAviso', 'NUMERODEAVISO')
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMERODEAVISO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    ANIO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PATENTE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    ARCHIVOENVIADO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    ARCHIVORESPUESTA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FACTURA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    ACUSEVALIDACION: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FEA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    NUMCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


t_GBasedeDatos = Table(
    'GBasedeDatos', Base.metadata,
    Column('VERSION', String(19, 'Modern_Spanish_CI_AS'))
)


class GBitacora(Base):
    __tablename__ = 'GBitacora'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='GBit_PKSysID'),
        Index('Bit_AKFechaHoraSysID', 'FECHA', 'HORA', 'SYSID', unique=True)
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    REFERENCIA: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    PROCEDIMIENTO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    MOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    USUARIO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    HORA: Mapped[Optional[int]] = mapped_column(Integer)
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(29, 'Modern_Spanish_CI_AS'))


class GBotonLeyendas(Base):
    __tablename__ = 'GBotonLeyendas'
    __table_args__ = (
        PrimaryKeyConstraint('NUMBOTON', name='BOTLEY_PKNumBoton'),
    )

    NUMBOTON: Mapped[int] = mapped_column(TINYINT, primary_key=True)
    BOTONLEYENDA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    BOTONLEYENDA2: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class GBultos(Base):
    __tablename__ = 'GBultos'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='GenBul_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    PESOUNI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PLURALES: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PLURALIN: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    CLAVEACE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    CLAVEAAMEX: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))


class GCatErrores(Base):
    __tablename__ = 'GCatErrores'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='CatErr_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    CLASIFICACION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class GCatErroresClas(Base):
    __tablename__ = 'GCatErroresClas'
    __table_args__ = (
        PrimaryKeyConstraint('CLASIFICACION', name='ClaErr_PKClasificacion'),
    )

    CLASIFICACION: Mapped[str] = mapped_column(String(100, 'Modern_Spanish_CI_AS'), primary_key=True)
    NIVEL: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class GCertOrigen(Base):
    __tablename__ = 'GCertOrigen'
    __table_args__ = (
        PrimaryKeyConstraint('NUMERO', name='CerOrg_PKNumero'),
    )

    NUMERO: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    EXPORTADOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FECHAINICIO: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAFINAL: Mapped[Optional[int]] = mapped_column(Integer)
    PRODUCTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    IMPORTADOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    EMPRESA: Mapped[Optional[str]] = mapped_column(String(256, 'Modern_Spanish_CI_AS'))
    NOMBRE: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CARGO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FECHAGEN: Mapped[Optional[int]] = mapped_column(Integer)
    TELEFONO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    FAX: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TAXID1: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TAXID2: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TAXID3: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CORREOELECTRONICO: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    NUMEROEMBARQUE: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CLIENTEASIGNAR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    NUMERODEFACTURA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class GClavePed(Base):
    __tablename__ = 'GClavePed'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEPED', name='ClaPed_PKClavePed'),
    )

    CLAVEPED: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(250, 'Modern_Spanish_CI_AS'))


class GClavePedRegimen(Base):
    __tablename__ = 'GClavePedRegimen'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='ClaReg_PKConsecutivo'),
        Index('ClaReg_FKClaPRegTipo', 'REGIMENPED', 'CLAVEPED', 'TIPO'),
        Index('ClaReg_FKClavePed_Tipo', 'CLAVEPED', 'TIPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    CLAVEPED: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    REGIMENPED: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))


class GClientesPro(Base):
    __tablename__ = 'GClientesPro'
    __table_args__ = (
        PrimaryKeyConstraint('CLIENTE', name='CliPro_PKCliente'),
        Index('CliPro_FKPaisEstado', 'PAIS', 'ESTADO')
    )

    CLIENTE: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOEXTNAC: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NOMBRE: Mapped[Optional[str]] = mapped_column(String(256, 'Modern_Spanish_CI_AS'))
    RFC: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CALLES: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    NUMEXT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMINT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CODIGOPOSTAL: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    COLONIA: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    CIUDAD: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESTADO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TELEFONO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    NUMFAX: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    EMAIL: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CURP: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CLIENTE_O_PROV: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PROGRAMA: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    NUMEROPROGRAMA: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    PROSEC: Mapped[Optional[int]] = mapped_column(TINYINT)
    AUTORIZACIONPROSEC: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHAAUTSECON: Mapped[Optional[int]] = mapped_column(Integer)
    MANUFACTERID: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    TAXID: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    BROKER: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    BROKERIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    CLAVETRANSFER: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CLAVEWEB: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    TRASFORMASUBMAQ: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    AUTORIZACIONSECON: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PROPORCIONAPLICADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    VINCULACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ESEMPRESACERTIFICADA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    REGISTROEMPCERT: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    INFORMACIONEXTRA: Mapped[Optional[str]] = mapped_column(String(399, 'Modern_Spanish_CI_AS'))
    CONTACTO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMAUTDONACION: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NOMBRECORTO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ESPROVNACIONAL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MUNICIPIO: Mapped[Optional[str]] = mapped_column(String(150, 'Modern_Spanish_CI_AS'))
    CTPAT_SVI: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    RESPONSABLE: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    PUESTO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    HABILITADODESAHABILITADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMREGLTRIBUTARIO: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    REFERENCIA: Mapped[Optional[str]] = mapped_column(String(250, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SERVICIOSUBMAQ: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHASAUTSE: Mapped[Optional[int]] = mapped_column(Integer)
    NUMAUTSE: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))


class GCodigosFCC(Base):
    __tablename__ = 'GCodigosFCC'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEFCC', name='CodFCC_PKClaveFCC'),
    )

    CLAVEFCC: Mapped[str] = mapped_column(String(30, 'Modern_Spanish_CI_AS'), primary_key=True)
    CODIGOFCC: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    MARCA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CONDICIONIMP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MODELO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INSPECCION: Mapped[Optional[int]] = mapped_column(TINYINT)
    REQUERIMIENTO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class GCodigosFDA(Base):
    __tablename__ = 'GCodigosFDA'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEFDA', name='CodFDA_PKCodigo'),
    )

    CLAVEFDA: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    CODIGOPRO: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    REQUERIMIENTOS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    MANUFACTERID: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    STATUSALMACEN: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CODIGOAFI1: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CALIFAFI1: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    CODIGOAFI2: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CALIFAFI2: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    CODIGOAFI3: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CALIFAFI3: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    CODIGOAFI4: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CALIFAFI4: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    CODIGOAFI5: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CALIFAFI5: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    FDA01PRODCODE: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    FDA01COMODITYDESC: Mapped[Optional[str]] = mapped_column(String(57, 'Modern_Spanish_CI_AS'))
    FDA01BRANDNAME: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    FDA01DISCLAIMER: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FDA01PGMCODE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FDA01PROCCODE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FDA01INTNDUSECODE: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    FDA01INTNDUSEDESC: Mapped[Optional[str]] = mapped_column(String(22, 'Modern_Spanish_CI_AS'))
    FDA01TEMPQUAL: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FDA01TEMPTYPE: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FDA01TEMPDEGREES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    FDA01TEMPNEGATIVE: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FDA01TEMPLOCATION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FDA01QUANTITY1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(9, 2))
    FDA01QTYUOM1: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FDA01QUANTITY2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(9, 2))
    FDA01QTYUOM2: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FDA01QUANTITY3: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(9, 2))
    FDA01QTYUOM3: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FDA01LACFCONT1: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    FDA01LACFCONT2: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    FDA01LACFCONT3: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    FDA01CTRYPROD: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FDA01CTRYSOURCE: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FDA01CTRYGROWTH: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FDA01CTRYREFUSAL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FDA01CTRYSHIPPING: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FDA01MANUFKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01SHIPPERKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01UITCONSKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01FDAIMPKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01PNSUBMKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01CONSOLKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01PRODUCERKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01OWNERKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01DELIPARTYKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01GROWERKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01DEVINIIMPKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    FDA01PNTRANSMITTERKEY: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class GCodigosFDA04(Base):
    __tablename__ = 'GCodigosFDA04'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEFDA', 'LINEA', name='FDA04ClaveLinea'),
    )

    CLAVEFDA: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FDA04ELENAME: Mapped[Optional[str]] = mapped_column(String(51, 'Modern_Spanish_CI_AS'))
    FDA04ELEQTY: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 2))
    FDA04ELEQTYUOM: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FDA04ELEPCTG: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 4))


class GCodigosFDA23(Base):
    __tablename__ = 'GCodigosFDA23'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEFDA', 'LINEA', name='FDA23ClaveLinea'),
    )

    CLAVEFDA: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FDA23AOCCODE: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FDA23AOCQUAL: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))


class GCodigosFDA25(Base):
    __tablename__ = 'GCodigosFDA25'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEFDA', 'LINEA', name='FDA25ClaveLinea'),
    )

    CLAVEFDA: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FDA25LOTNUMBER: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    FDA25LOTPRODBD: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FDA25LOTPRODED: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))


t_GCodigosProductoCP = Table(
    'GCodigosProductoCP', Base.metadata,
    Column('SYSID', Integer),
    Column('CODIGO', String(50, 'Modern_Spanish_CI_AS')),
    Column('DESCRIPCION', String(5001, 'Modern_Spanish_CI_AS')),
    Column('PALABRASSIMILARES', String(5001, 'Modern_Spanish_CI_AS')),
    Column('MATPELIGROSO', String(10, 'Modern_Spanish_CI_AS')),
    Column('FECHAINICIOVIGENCIA', Integer),
    Column('FECHAFINVIGENCIA', Integer)
)


class GConCobranza(Base):
    __tablename__ = 'GConCobranza'
    __table_args__ = (
        PrimaryKeyConstraint('CONCEPTO', name='ConCob_PKConcepto'),
    )

    CONCEPTO: Mapped[str] = mapped_column(String(100, 'Modern_Spanish_CI_AS'), primary_key=True)


class GConceptos(Base):
    __tablename__ = 'GConceptos'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='Concep_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(120, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONINGLES: Mapped[Optional[str]] = mapped_column(String(120, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONDETALLADA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PRIORIDAD: Mapped[Optional[int]] = mapped_column(Integer)
    PRIORIDADAME: Mapped[Optional[int]] = mapped_column(Integer)
    PRIMERTOTAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    SEIMPRIME: Mapped[Optional[int]] = mapped_column(TINYINT)
    SECCION: Mapped[Optional[int]] = mapped_column(Integer)
    CLASIFICACION: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))


class GConceptosAAduanal(Base):
    __tablename__ = 'GConceptosAAduanal'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEAA', 'CONCEPTO', name='ConAA_PKClaveAAConcepto'),
        Index('ConAA_AKConcepto', 'CONCEPTO')
    )

    CLAVEAA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    CONCEPTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    IMPORTE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 2))
    PRIORIDAD: Mapped[Optional[int]] = mapped_column(Integer)


class GConceptosClasif(Base):
    __tablename__ = 'GConceptosClasif'
    __table_args__ = (
        PrimaryKeyConstraint('CLASIFICACION', name='ConCla_PKClasificacion'),
    )

    CLASIFICACION: Mapped[str] = mapped_column(String(30, 'Modern_Spanish_CI_AS'), primary_key=True)


class GConductor(Base):
    __tablename__ = 'GConductor'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVETRANS', 'LINEA', name='Conduc_PKTransLinea'),
        Index('Conduc_FKTranspCoduc', 'CLAVETRANS', 'CONDUCTOR')
    )

    CLAVETRANS: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    NUMLICENCIA: Mapped[Optional[str]] = mapped_column(String(29, 'Modern_Spanish_CI_AS'))
    IDLINEAEXPRESS: Mapped[Optional[str]] = mapped_column(String(17, 'Modern_Spanish_CI_AS'))
    IDENTIFICACIONACE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHANAC: Mapped[Optional[int]] = mapped_column(Integer)
    SEXO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PAISNACIMIENTO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    AUTTRANSMATPELIGROSO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESTADOMATPELIGROSO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    NOMBRE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    APELLIDOPATERNO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CLAVEID1: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    NUMEROID1: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ESTADOID1: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PAISID1: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CLAVEID2: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    NUMEROID2: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ESTADOID2: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PAISID2: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    NUMGAFETE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NUMGAFETEUNICO: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class GConfigReportes(Base):
    __tablename__ = 'GConfigReportes'
    __table_args__ = (
        PrimaryKeyConstraint('SISTEMA', 'MODULO', 'REPORTE', name='GConRep_PKSisModRep'),
    )

    SISTEMA: Mapped[str] = mapped_column(String(19, 'Modern_Spanish_CI_AS'), primary_key=True)
    MODULO: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    REPORTE: Mapped[str] = mapped_column(String(50, 'Modern_Spanish_CI_AS'), primary_key=True)
    IMPRIMIR: Mapped[Optional[int]] = mapped_column(TINYINT)
    VENTANALLAMAR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    TIPOFACTURA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    TIPOUM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    IMPRIMIRAGEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPRIMIRTRANSPOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPRIMIRIMPORTADOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPRIMIRAA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTCOPIAS: Mapped[Optional[int]] = mapped_column(Integer)
    GENPDF: Mapped[Optional[int]] = mapped_column(TINYINT)


class GConfigTablas(Base):
    __tablename__ = 'GConfigTablas'
    __table_args__ = (
        PrimaryKeyConstraint('TABLA', 'CAMPO', name='GConTab_PKTablaCampo'),
    )

    TABLA: Mapped[str] = mapped_column(String(100, 'Modern_Spanish_CI_AS'), primary_key=True)
    CAMPO: Mapped[str] = mapped_column(String(100, 'Modern_Spanish_CI_AS'), primary_key=True)
    VENTANA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class GContenedores(Base):
    __tablename__ = 'GContenedores'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='Conten_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))


class GControlDeCredito(Base):
    __tablename__ = 'GControlDeCredito'
    __table_args__ = (
        PrimaryKeyConstraint('FRACCION', name='GCONTR_PK_FraccionControlCredito'),
    )

    FRACCION: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    CARGA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    ABONO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))


class GConversiones(Base):
    __tablename__ = 'GConversiones'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEUNI1', 'CLAVEUNI2', name='GConve_FKUnidades12'),
        Index('GConve_FKClaveUni1', 'CLAVEUNI1'),
        Index('GConve_FKClaveUni2', 'CLAVEUNI2'),
        Index('GConve_FKUnidades21', 'CLAVEUNI2', 'CLAVEUNI1')
    )

    CLAVEUNI1: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVEUNI2: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    FACTORCONV: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))


class GDestinoAduanero(Base):
    __tablename__ = 'GDestinoAduanero'
    __table_args__ = (
        PrimaryKeyConstraint('ID', name='GDEADU_PKIDDestinoAduanero'),
    )

    ID: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVE: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    DESTINOADUANERO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))


class GDestruccion(Base):
    __tablename__ = 'GDestruccion'
    __table_args__ = (
        PrimaryKeyConstraint('OFICIO', name='PKOFICIO'),
        Index('AKFECHA', 'FECHADESTRUCCION')
    )

    OFICIO: Mapped[str] = mapped_column(String(30, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHADESTRUCCION: Mapped[Optional[int]] = mapped_column(Integer)


t_GDivisionPeligro = Table(
    'GDivisionPeligro', Base.metadata,
    Column('CLASEDEPELIGRO', String(4, 'Modern_Spanish_CI_AS')),
    Column('DESCRIPCION', String(499, 'Modern_Spanish_CI_AS')),
    Index('DivPel_PKClaseDiv', 'CLASEDEPELIGRO')
)


class GDocumentosDigital(Base):
    __tablename__ = 'GDocumentosDigital'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='DocDig_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    IDTIPODOCUMENTO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    NOMBREARCHIVO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FECHADIGITALIZACION: Mapped[Optional[int]] = mapped_column(Integer)
    INDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    MODULO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CLAVEAA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    RUTAENVIOXML: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    RUTARESPUESTAXML: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    RFCCONSULTA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CADENAORIGINALDOC: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    SELLODIGITALSOLICITANTE: Mapped[Optional[str]] = mapped_column(String(2499, 'Modern_Spanish_CI_AS'))
    SELLODIGITALVU: Mapped[Optional[str]] = mapped_column(String(1800, 'Modern_Spanish_CI_AS'))
    FOLIOSOLICITUD: Mapped[Optional[str]] = mapped_column(String(60, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))


class GDotInformation(Base):
    __tablename__ = 'GDotInformation'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEDOT', name='DOT01CLAVEDOT'),
    )

    CLAVEDOT: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    BOXNUMBER: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PGMCODE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    INTNDUSECODE: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    INTNDUSEDESC: Mapped[Optional[str]] = mapped_column(String(22, 'Modern_Spanish_CI_AS'))
    DISCLAIMER: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CATTYPECODE: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    CATCODE: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    BRANDNAME: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    MODEL: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    MANUFMONTH: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MANUFYEAR: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    MODELYEAR: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    DRIVESIDE: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    EMBASSYCO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PASSPORTCO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PASSPORTNO: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    SURETYCODE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    BONDSERIAL: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    BONDQUAL: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    BONDAMT: Mapped[Optional[int]] = mapped_column(Integer)
    FABMANUFKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    RETDISTKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CERTINDKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    OWNERKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    OEIKEY: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))


class GDotInformation08(Base):
    __tablename__ = 'GDotInformation08'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEDOT', 'LINEA', name='DOT08ClaveDotLinea'),
    )

    CLAVEDOT: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    IDQUAL: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    IDNUMBER: Mapped[Optional[str]] = mapped_column(String(17, 'Modern_Spanish_CI_AS'))


class GDotInformation14(Base):
    __tablename__ = 'GDotInformation14'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEDOT', 'LINEA', name='DOT14ClaveDotLinea'),
    )

    CLAVEDOT: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    TRANSTYPE: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    LPCOTYPE: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    LPCONUMBER: Mapped[Optional[str]] = mapped_column(String(33, 'Modern_Spanish_CI_AS'))
    LPCODTQUAL: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    LPCODT: Mapped[Optional[int]] = mapped_column(Integer)
    LPCOQTY: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(21, 4))


class GEmails(Base):
    __tablename__ = 'GEmails'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='Email_PKSysID'),
        Index('AKEMAILSYSID', 'EMAIL', 'SYSID', unique=True),
        Index('Email_AKEmail', 'EMAIL', unique=True)
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    EMAIL: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NOMBRE: Mapped[Optional[str]] = mapped_column(String(199, 'Modern_Spanish_CI_AS'))
    EMPRESA: Mapped[Optional[str]] = mapped_column(String(199, 'Modern_Spanish_CI_AS'))
    TELEFONOS: Mapped[Optional[str]] = mapped_column(String(199, 'Modern_Spanish_CI_AS'))
    CATEGORIA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class GEmpresa(Base):
    __tablename__ = 'GEmpresa'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='DatEmp_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NOMBRE: Mapped[Optional[str]] = mapped_column(String(256, 'Modern_Spanish_CI_AS'))
    RFC: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CALLES: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CALLESIND: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    NUMEXT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMEXTIND: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CODIGOPOSTAL: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CODIGOPOSTALIND: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    COLONIA: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    COLONIAIND: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    CIUDAD: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CIUDADIND: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESTADO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESTADOIND: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    TELEFONO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    TELEFONOIND: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    NUMFAX: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    NUMFAXIND: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    EMAIL: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    EMAILIND: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    ACTPREPONDERANTE: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    PROGRAMA: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    NUMEROPROGRAMA: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    PROSEC: Mapped[Optional[int]] = mapped_column(TINYINT)
    AUTORIZACIONPROSEC: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SECTOR1: Mapped[Optional[str]] = mapped_column(String(150, 'Modern_Spanish_CI_AS'))
    SECTOR2: Mapped[Optional[str]] = mapped_column(String(150, 'Modern_Spanish_CI_AS'))
    SECTOR3: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    MANUFACTERID: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    BROKER: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    RESPONSABLE: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    RFCRESPONSABLE: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    RESPPATERNO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    RESPMATERNO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    RESPNOMBRE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PUESTO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    LOGO: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    ACTETIQUETAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    CLAVEFTP: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ACTFRACCIONES: Mapped[Optional[int]] = mapped_column(TINYINT)
    RUTASIFRA: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    BUFETEINTERNACIONAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOVERSION: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ESEMPRESACERTIFICADA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    REGISTROEMPCERT: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    TIENELINEAEXPRESS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOFORMATOPED: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CODIGOANTERIOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACTIVACAAT: Mapped[Optional[int]] = mapped_column(TINYINT)
    INTERFASETRANS: Mapped[Optional[int]] = mapped_column(TINYINT)
    COSTOSAMERICANOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    SCAFSOLOLECTURA: Mapped[Optional[int]] = mapped_column(TINYINT)
    ESEMPRESASERVICIO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    SUSTPARTES: Mapped[Optional[int]] = mapped_column(TINYINT)
    NOMBRECLIENTE: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    ACTFACMEXAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARTEREFERENCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    SQLLENGUAJE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    MODOSUBMAQUILA: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    FECHAINICIALEMPCERT: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAFINALEMPCERT: Mapped[Optional[int]] = mapped_column(Integer)
    MODOOPERACIONSALDO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CURP: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    RUTAARCHCER: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    RUTAARCHKEY: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    CLAVEACCESOFIEL: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    USUARIOWEBSERVICEVU: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CLAVEACCESOWEBSERVICEVU: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    EMAILVU: Mapped[Optional[str]] = mapped_column(String(800, 'Modern_Spanish_CI_AS'))
    NOMBREBDINTER: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    TIPOFIGURAVU: Mapped[Optional[str]] = mapped_column(String(29, 'Modern_Spanish_CI_AS'))
    RUTAVUCENTRAL: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    RUTAARCHIVOSXML: Mapped[Optional[str]] = mapped_column(String(1499, 'Modern_Spanish_CI_AS'))
    RFCCONSULTA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    TOMACONFIGURACIONVU: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    VUUNIDADESMEDIDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    RFCVALIDACIONVU: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CTPAT_SVI: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FECHACERTIFICACIONANEXO31: Mapped[Optional[int]] = mapped_column(Integer)
    NUMEROCERTIFICACIONANEXO31: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODALIDADANEXO31: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPOEMPRESAANEXO31: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    EMPRESANEEC: Mapped[Optional[int]] = mapped_column(Integer)
    RUTAARCHIVOCERCFDI: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    RUTAARCHIVOKEYCFDI: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    FECHAVENCCERCFDI: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAVENCKEYCFDI: Mapped[Optional[int]] = mapped_column(Integer)
    CONTRASEÐACFDI: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    RUTAGUARDARXML: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    RUTAAPPCFDI: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    RUTAAPPPAC: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    RUTAARCHIVOCANCELACION: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    CONTRASEÐACANCELACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    NUMDEEXPORTADORCONFIABLE: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMINTERIOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMINTIND: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    MUNICIPIO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MUNICIPIOIND: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PAISIND: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    FECHARENOVACIONCERTIFICACIONA31: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAFINALCERTIFICACIONA31: Mapped[Optional[int]] = mapped_column(Integer)
    EMPRESAOEA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALLESIND2: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    COLONIAIND2: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    CODIGOPOSTALIND2: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CIUDADIND2: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    TELEFONOIND2: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    MUNICIPIOIND2: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMEXTIND2: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ESTADOIND2: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    NUMFAXIND2: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PAISIND2: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    EMAILIND2: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    ADUANAPREVALIDADOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CLAVEPREVALIDADOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PATENTEPREVALIDADOR: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONPREVALIDADOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FOLDERENTRADAAELECTRONICO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    FOLDERSALIDAAELECTRONICO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    MASCARAENVIARAELECTRONICO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    MASCARARESPAELECTRONICO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    EXTENSIONRESPUESTAAELECTRONICO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INICIOCONTADORAELECTRONICO: Mapped[Optional[int]] = mapped_column(Integer)
    FINALCONTADORAELECTRONICO: Mapped[Optional[int]] = mapped_column(Integer)
    SIGUIENTECONTADORAELECTRONICO: Mapped[Optional[int]] = mapped_column(Integer)


class GEncAnexo(Base):
    __tablename__ = 'GEncAnexo'
    __table_args__ = (
        PrimaryKeyConstraint('MODULO', name='EAnexo_PKModulo'),
    )

    MODULO: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    TITULO: Mapped[Optional[str]] = mapped_column(String(256, 'Modern_Spanish_CI_AS'))


class GEncFacturas(Base):
    __tablename__ = 'GEncFacturas'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='ApoFac_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FACTURA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    MANIFIESTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    MARCAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    MODULO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class GEquivPartidas(Base):
    __tablename__ = 'GEquivPartidas'
    __table_args__ = (
        PrimaryKeyConstraint('ID', 'CAMPOORIG', 'CAMPOEXT', name='GEPar_PKId_Orig_Ext'),
        Index('GEPar_FK_IDCampoOrg', 'ID', 'CAMPOORIG')
    )

    ID: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    CAMPOORIG: Mapped[str] = mapped_column(String(100, 'Modern_Spanish_CI_AS'), primary_key=True)
    CAMPOEXT: Mapped[str] = mapped_column(String(100, 'Modern_Spanish_CI_AS'), primary_key=True)


class GEquivalenteEnc(Base):
    __tablename__ = 'GEquivalenteEnc'
    __table_args__ = (
        PrimaryKeyConstraint('IDENTIFICADOR', name='GEQ_PK_Id'),
    )

    IDENTIFICADOR: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))


class GErroresFac(Base):
    __tablename__ = 'GErroresFac'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'MODULO', 'LINEA', name='ErrFac_PKConsecModLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    MODULO: Mapped[str] = mapped_column(String(50, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 0))


class GEstados(Base):
    __tablename__ = 'GEstados'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEM3', 'DESCRIPCION', name='GenEst_PKClaveM3Desc'),
    )

    CLAVEM3: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[str] = mapped_column(String(50, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVE_MEX: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CLAVE_AME: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))


class GExpedienteElecEnc(Base):
    __tablename__ = 'GExpedienteElecEnc'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='PKConsecutivoExpediente'),
        Index('FKConsecutivoFactor', 'CONSECUTIVO', 'FACTOR')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    MOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    TIPOFACTURA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))


class GExpedienteElecPartidas(Base):
    __tablename__ = 'GExpedienteElecPartidas'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVOEXT', 'CONSECUTIVOINT', name='PKLlaveporConsecutivoExterno'),
    )

    CONSECUTIVOEXT: Mapped[int] = mapped_column(Integer, primary_key=True)
    CONSECUTIVOINT: Mapped[int] = mapped_column(Integer, primary_key=True)
    RUTA: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    TIPODOCUMENTO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class GFacProforma(Base):
    __tablename__ = 'GFacProforma'
    __table_args__ = (
        PrimaryKeyConstraint('NUMEROPROFORMA', name='FacPro_PorNumProforma'),
    )

    NUMEROPROFORMA: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMERODUNS: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORTOTALME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORTOTALMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    PROVEEDORNAC: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    REMITIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CLAVECLIENTE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))


class GFiltros(Base):
    __tablename__ = 'GFiltros'
    __table_args__ = (
        PrimaryKeyConstraint('FILTRO', name='Gfiltro_PKFiltro'),
    )

    FILTRO: Mapped[str] = mapped_column(String(200, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class GFirmas(Base):
    __tablename__ = 'GFirmas'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEFIRMA', name='GFirm_PKClaveFirma'),
    )

    CLAVEFIRMA: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    FIRMA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHFOTO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))


class GFormaPago(Base):
    __tablename__ = 'GFormaPago'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='ForPag_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class GFracAme(Base):
    __tablename__ = 'GFracAme'
    __table_args__ = (
        PrimaryKeyConstraint('FRACCION', name='FraAme_PKFraccion'),
    )

    FRACCION: Mapped[str] = mapped_column(String(16, 'Modern_Spanish_CI_AS'), primary_key=True)
    PREFIJO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ADV: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    UNIDAD: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    TIPOADV: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ADVCOSTOFIJO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))


class GFracEUACan(Base):
    __tablename__ = 'GFracEUACan'
    __table_args__ = (
        PrimaryKeyConstraint('FRACCION', 'CLAVEM3', name='FraEUC_PKFraccionPais'),
    )

    FRACCION: Mapped[str] = mapped_column(String(13, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVEM3: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    ADV: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    UNIDAD: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))


class GFracROctava(Base):
    __tablename__ = 'GFracROctava'
    __table_args__ = (
        PrimaryKeyConstraint('PERMISO', 'LINEA', 'FRACCION', name='FraOct_PKPermFracLin'),
        Index('FraOct_FKPermLin', 'PERMISO', 'LINEA', unique=True)
    )

    PERMISO: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    CANTIDADCUPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORCUPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))


class GFraccionesHistorico(Base):
    __tablename__ = 'GFraccionesHistorico'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='sFracHis_PKConsecutivo'),
        Index('sFracHis_AKFracPaiTiSeFe', 'FRACCIONHISTORICA', 'PAIS', 'TIPOFRACCION', 'SECTOR', 'FECHAPUBLICACION', unique=True)
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCIONHISTORICA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    UMCLAVE: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TASAIMNUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TASAEXNUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    FECHAPUBLICACION: Mapped[Optional[int]] = mapped_column(Integer)
    ESIMMEX: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TEMPORALIDADNORMAL: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TEMPORALIDADSERVICIOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TEMPORALIDADCERTIFICADA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    PORLOG: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    FECHATERMINO: Mapped[Optional[int]] = mapped_column(Integer)


class GINPC(Base):
    __tablename__ = 'GINPC'
    __table_args__ = (
        PrimaryKeyConstraint('ANIO', 'MES', name='GeINPC_PKAnioMes'),
    )

    ANIO: Mapped[str] = mapped_column(String(4, 'Modern_Spanish_CI_AS'), primary_key=True)
    MES: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    VALOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))


class GIdentificadores(Base):
    __tablename__ = 'GIdentificadores'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='Identi_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    NIVEL: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    COMPLEMENTO: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))


t_GIdentificadoresPartidas = Table(
    'GIdentificadoresPartidas', Base.metadata,
    Column('CONSECUTIVOFACTURA', Integer),
    Column('LINEAPARTIDA', Integer),
    Column('ID', String(2, 'Modern_Spanish_CI_AS')),
    Column('MODULO', String(20, 'Modern_Spanish_CI_AS')),
    Column('COMPLEMENTO1', String(50, 'Modern_Spanish_CI_AS')),
    Column('COMPLEMENTO2', CHAR(51, 'Modern_Spanish_CI_AS')),
    Column('COMPLEMENTO3', String(50, 'Modern_Spanish_CI_AS')),
    Index('PK_MODULO_CONSFAC_LINEA_ID', 'CONSECUTIVOFACTURA', 'LINEAPARTIDA', 'ID', 'MODULO', unique=True)
)


t_GIncoterm = Table(
    'GIncoterm', Base.metadata,
    Column('INCOTERM', String(5, 'Modern_Spanish_CI_AS')),
    Column('DESCESPANOL', String(256, 'Modern_Spanish_CI_AS')),
    Column('DESCINGLES', String(256, 'Modern_Spanish_CI_AS')),
    Index('Incote_PKIncoterm', 'INCOTERM')
)


class GLeyendas(Base):
    __tablename__ = 'GLeyendas'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVELEY', name='GenLey_PKClaveLey'),
    )

    CLAVELEY: Mapped[int] = mapped_column(Integer, primary_key=True)
    DESCLEYENDA: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))


class GManifCoductor(Base):
    __tablename__ = 'GManifCoductor'
    __table_args__ = (
        PrimaryKeyConstraint('MANIFIESTO', 'CONDUCTOR', name='ManCon_PKManifConductor'),
    )

    MANIFIESTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    CONDUCTOR: Mapped[str] = mapped_column(String(80, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    DIRECCION1: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    DIRECCION2: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CIUDAD: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESTADO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CODIGOPOSTAL: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class GManifestacionAnexo(Base):
    __tablename__ = 'GManifestacionAnexo'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='MVAnex_PorConsecutivoLin'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    TIPOANEXO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    NUMERO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    DOCANEXADO: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))


class GManifestacionConcepto(Base):
    __tablename__ = 'GManifestacionConcepto'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='MVCone_PorConsecutivoLin'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    TIPOANEXO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    NUMERO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    MCIAOPROV: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FACODOC: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    IMPORTE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    MONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CONCEPTOCARGO: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))


class GManifestacionValor(Base):
    __tablename__ = 'GManifestacionValor'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='ManVal_PKConsecutivo'),
        Index('ManVal_NumeroManVal', 'NUMEROMANVAL', unique=True)
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMEROMANVAL: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PERIODICIDAD: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SEMESTRE: Mapped[Optional[int]] = mapped_column(TINYINT)
    ANIO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    TIPOPEDIMENTO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CLAVEAA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PATENTE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    NOMBRES: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    APELLIDOPATERNO: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    APELLIDOMATERNO: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    CANTMETODOSUTIL: Mapped[Optional[int]] = mapped_column(Integer)
    METVALPORMCIAPRO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    VALORTRANSACCIËN: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALTRAMCIASIDENTICAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALTRAMCIASSIMILARES: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALPREUNIVENTA: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALRECONSTRUIDO: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALDETART78: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALDECLARACIONVALORPROV: Mapped[Optional[int]] = mapped_column(Integer)
    PRESENTAANEXOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMHOJASANEX: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    PRECIOPAGADOMETVALTRANS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PRECIOPREFAC: Mapped[Optional[int]] = mapped_column(TINYINT)
    PRECIOOTROSDOC: Mapped[Optional[int]] = mapped_column(TINYINT)
    CONCEPSENALART66: Mapped[Optional[int]] = mapped_column(TINYINT)
    CONCEPART66DESGLOSAODOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    ANEXORELART66: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PREPAGADOMCIASART65: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ANEXORELART65: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    BASEGRAVNOCOMPRAVENTA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    EXISTECIRCDISTART67Y71: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ANEXOVALADUANA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    VALDETPROVISIONAL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ANEXOCONSTAVALMCIA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    RFCREPLEGAL: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    REPRESANTANTELEGAL: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    FACTURASELECCIONADA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OPCIONFACTURA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    IMPORTADORAUSAR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))


class GManifiesto(Base):
    __tablename__ = 'GManifiesto'
    __table_args__ = (
        PrimaryKeyConstraint('MANIFIESTO', name='GenMan_PKManifiesto'),
    )

    MANIFIESTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    NOMNUMDESCIMPO: Mapped[Optional[str]] = mapped_column(String(60, 'Modern_Spanish_CI_AS'))
    NOMPERSACARGO: Mapped[Optional[str]] = mapped_column(String(60, 'Modern_Spanish_CI_AS'))
    CONSIGNADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    PTOEXTSAL: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    LOCALIZAPTOEXTSAL: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PTODESTINO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    LOCALIZAPTODESTINO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PTOENTRADA: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    LOCALIZAPTOENTRADA: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    FECHAENTRADA: Mapped[Optional[int]] = mapped_column(Integer)
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORTOTAL: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(2500, 'Modern_Spanish_CI_AS'))
    CLAVEBROKER: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLAVETRANS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FACTURAPAG: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    HORAENTRADA: Mapped[Optional[int]] = mapped_column(Integer)
    MATERIALPELIGROSO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CLAVETRANSPORTE: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONESTATUS: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    TIPOMANIFIESTO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class GMetValor(Base):
    __tablename__ = 'GMetValor'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='MetVal_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))


class GModTransporte(Base):
    __tablename__ = 'GModTransporte'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEMOD', name='ModTra_PKClaveMod'),
    )

    CLAVEMOD: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    MODOTRANS: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))


class GNivelesSeguridad(Base):
    __tablename__ = 'GNivelesSeguridad'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='GNiv_PKSysID'),
        Index('GNiv_AKClave', 'CLAVE', 'SISTEMA', unique=True)
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    CLAVE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ACCAMBIOREGIMEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACCOMPRASMEXICANAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACREMISIONESENTRADA: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACFACTURASSALIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACFACTURASREPARACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACFACTURAIMPOTEMPORAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACFACTURAIMPODEFINITIVA: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACREMISIONSALIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACFACTINTEGRACIONCTM: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACREMRECIBOCTM: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACREMENVIOCTM: Mapped[Optional[int]] = mapped_column(TINYINT)
    PERMITECAMBIARCLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    PERMITEDESSEG: Mapped[Optional[int]] = mapped_column(TINYINT)
    PERMITEDESCOSTOFIJO: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESTRINGIRMODCOSTOFIJO: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESTRINGEDESHABILITARDESCPARTE: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAREXCANTPESODESVSFAC: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTSERIEVSCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    PERMITEACTREVCLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESHABILITAUMPARTIDAIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESTRINGEMODVU: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESTRINGEMODEDOCOPEADEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESTRINGEMODFIRMACERFIEL: Mapped[Optional[int]] = mapped_column(TINYINT)
    REPOPEPORNIVEL: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACFACTURASMODULOCTM: Mapped[Optional[int]] = mapped_column(TINYINT)
    AUTACTUALIZAREXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    PERMITIRMODIFICARPEDIMENTOSPREVIOSALAFECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    SOLICITARPERMISOADMINAGREGARPED: Mapped[Optional[int]] = mapped_column(Integer)
    MODIFICARFECHASDEPEDIMENTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    ESTATUSPED: Mapped[Optional[int]] = mapped_column(TINYINT)


class GNivelesSeguridadTablas(Base):
    __tablename__ = 'GNivelesSeguridadTablas'
    __table_args__ = (
        PrimaryKeyConstraint('SYSIDNIVEL', 'TABLA', name='GNivTab_PkNivelTabla'),
        Index('GNivTab_AKSysIDTabla', 'SYSIDNIVEL', 'TABLA')
    )

    SYSIDNIVEL: Mapped[int] = mapped_column(Integer, primary_key=True)
    TABLA: Mapped[str] = mapped_column(String(49, 'Modern_Spanish_CI_AS'), primary_key=True)
    INSERTAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    EDITAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    BORRAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PROIMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))


class GPaisReglaOct(Base):
    __tablename__ = 'GPaisReglaOct'
    __table_args__ = (
        PrimaryKeyConstraint('PERMISO', 'LINEA', 'FRACCION', 'CLAVEM3', name='PaiOct_PKPermiFraccLinPais'),
        Index('PaiOct_FKPermiLinPais', 'PERMISO', 'LINEA', 'CLAVEM3')
    )

    PERMISO: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVEM3: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)


class GPaises(Base):
    __tablename__ = 'GPaises'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEM3', name='GenPai_PKClaveM3'),
        Index('AKPAIS_AME', 'PAIS_AME', unique=True)
    )

    CLAVEM3: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAIS_MEX: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAIS_AME: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESC_E: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    DESC_I: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class GPaisesGrupoSifra(Base):
    __tablename__ = 'GPaisesGrupoSifra'
    __table_args__ = (
        PrimaryKeyConstraint('GRUPO', 'PAIS', name='PaiG_PKGrupoPais'),
    )

    GRUPO: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAIS: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)


class GParAnexo(Base):
    __tablename__ = 'GParAnexo'
    __table_args__ = (
        PrimaryKeyConstraint('MODULO', 'LINEA', name='PAnexo_FKModuloLinea'),
    )

    MODULO: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    TITULO: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))


class GParFacturas(Base):
    __tablename__ = 'GParFacturas'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='MatPar_PKConsecLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMPERMISO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAGRENGLON: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCIMPO: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIENECO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    ORDENCOMPRAVENTA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONPARTE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    VALORAGREGADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPOVA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    VALEMPAQUEUS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))


class GPartidasCO(Base):
    __tablename__ = 'GPartidasCO'
    __table_args__ = (
        PrimaryKeyConstraint('NUMERO', 'NUMPARTE', name='ParCer_FKNumCOParte'),
    )

    NUMERO: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CLASIFARANCEL: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    CRITERIOPREFERENCIAL: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ESPRODUCTOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ENCASONO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    COSTONETO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class GPeriodoAnexo31(Base):
    __tablename__ = 'GPeriodoAnexo31'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='GPEA31_PKPeriodoAnexo31'),
    )

    CLAVE: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    PERIODO: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))


class GPermisoReglaOct(Base):
    __tablename__ = 'GPermisoReglaOct'
    __table_args__ = (
        PrimaryKeyConstraint('PERMISO', name='RegOct_PKPermiso'),
    )

    PERMISO: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHAINICIO: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAFINAL: Mapped[Optional[int]] = mapped_column(Integer)
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))


class GPrecintos(Base):
    __tablename__ = 'GPrecintos'
    __table_args__ = (
        PrimaryKeyConstraint('PRECINTO', name='Precin_PKPrecinto'),
    )

    PRECINTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)


class GPrevalidadores(Base):
    __tablename__ = 'GPrevalidadores'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='PK_ClavePrevAElec'),
    )

    CLAVE: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    ADUANAPREVALIDADOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PATENTEPREVALIDADOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONPREVALIDADOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class GProcesos(Base):
    __tablename__ = 'GProcesos'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='GProces_PKConsecutivo'),
        Index('GProces_FKSistemaIDPro', 'SISTEMA', 'IDPROCESO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    IDPROCESO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))


class GPuertoEnt(Base):
    __tablename__ = 'GPuertoEnt'
    __table_args__ = (
        PrimaryKeyConstraint('PUERTO', 'LOCALIZACION', name='PueEnt_PKPuertoLoc'),
    )

    PUERTO: Mapped[str] = mapped_column(String(6, 'Modern_Spanish_CI_AS'), primary_key=True)
    LOCALIZACION: Mapped[str] = mapped_column(String(4, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    DESCLOCALIZACION: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))


class GRecintos(Base):
    __tablename__ = 'GRecintos'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', 'ADUANA', name='PKRECINTO'),
    )

    CLAVE: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    ADUANA: Mapped[str] = mapped_column(String(100, 'Modern_Spanish_CI_AS'), primary_key=True)
    RECINTOFISCALIZADO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))


class GRegimenPed(Base):
    __tablename__ = 'GRegimenPed'
    __table_args__ = (
        PrimaryKeyConstraint('REGIMENPED', name='GenCPed1_PKRegimenPed'),
    )

    REGIMENPED: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class GRelFacFacturas(Base):
    __tablename__ = 'GRelFacFacturas'
    __table_args__ = (
        PrimaryKeyConstraint('FOLIO', 'LINEA', name='RelFac_PKFolioLinea'),
    )

    FOLIO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SISTEMA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    MODULO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class GRelacionFacturas(Base):
    __tablename__ = 'GRelacionFacturas'
    __table_args__ = (
        PrimaryKeyConstraint('FOLIO', name='RelFac_PKFolio'),
    )

    FOLIO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FECHAEXP: Mapped[Optional[int]] = mapped_column(Integer)
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CONTENEDORESTIPO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DATOSVEHICULO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMERONIU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CANTGUIASEMBARQUE: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    OBSERVACIONESVU: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NUMEROCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    TIPOIANOIA: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    ESFERROCARRIL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ADENDAVU: Mapped[Optional[str]] = mapped_column(String(204, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    IMPORTADOREXPORTADOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ESAGRANEL: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESTINOORIGENCOVE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


t_GRutasGenerales = Table(
    'GRutasGenerales', Base.metadata,
    Column('NOMBRERUTA', String(50, 'Modern_Spanish_CI_AS')),
    Column('RUTA', String(1500, 'Modern_Spanish_CI_AS'))
)


class GSIAA(Base):
    __tablename__ = 'GSIAA'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='gVer_PKSysID'),
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    SIFRA: Mapped[Optional[int]] = mapped_column(TINYINT)
    WINSAAI: Mapped[Optional[int]] = mapped_column(TINYINT)
    REMESAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    WINVAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHAINFORMACIONSIAA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOACTUALIZACION: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    HTTPSERVER: Mapped[Optional[str]] = mapped_column(String(199, 'Modern_Spanish_CI_AS'))
    MANUALFOLDER: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    NOAJUSTE: Mapped[Optional[int]] = mapped_column(Integer)
    SCAII: Mapped[Optional[int]] = mapped_column(TINYINT)
    SCAF: Mapped[Optional[int]] = mapped_column(TINYINT)
    SCON: Mapped[Optional[int]] = mapped_column(TINYINT)
    GERENCIALES: Mapped[Optional[int]] = mapped_column(TINYINT)
    UTILERIAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    SISET: Mapped[Optional[int]] = mapped_column(TINYINT)
    ALMACEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHAINFORMACIONSIFRA: Mapped[Optional[int]] = mapped_column(Integer)
    ANEXO31: Mapped[Optional[int]] = mapped_column(TINYINT)


t_GSQLFile = Table(
    'GSQLFile', Base.metadata,
    Column('C1', String(499, 'Modern_Spanish_CI_AS')),
    Column('C2', String(499, 'Modern_Spanish_CI_AS')),
    Column('C3', String(499, 'Modern_Spanish_CI_AS')),
    Column('C4', String(499, 'Modern_Spanish_CI_AS')),
    Column('C5', String(499, 'Modern_Spanish_CI_AS')),
    Column('C6', String(499, 'Modern_Spanish_CI_AS')),
    Column('C7', String(499, 'Modern_Spanish_CI_AS')),
    Column('C8', String(499, 'Modern_Spanish_CI_AS')),
    Column('C9', String(499, 'Modern_Spanish_CI_AS')),
    Column('C10', String(499, 'Modern_Spanish_CI_AS')),
    Column('C11', String(499, 'Modern_Spanish_CI_AS')),
    Column('C12', String(499, 'Modern_Spanish_CI_AS')),
    Column('C13', String(499, 'Modern_Spanish_CI_AS')),
    Column('C14', String(499, 'Modern_Spanish_CI_AS')),
    Column('C15', String(499, 'Modern_Spanish_CI_AS')),
    Column('C16', String(499, 'Modern_Spanish_CI_AS')),
    Column('C17', String(499, 'Modern_Spanish_CI_AS')),
    Column('C18', String(499, 'Modern_Spanish_CI_AS')),
    Column('C19', String(499, 'Modern_Spanish_CI_AS')),
    Column('C20', String(499, 'Modern_Spanish_CI_AS')),
    Column('C21', String(499, 'Modern_Spanish_CI_AS')),
    Column('C22', String(499, 'Modern_Spanish_CI_AS')),
    Column('C23', String(499, 'Modern_Spanish_CI_AS')),
    Column('C24', String(499, 'Modern_Spanish_CI_AS')),
    Column('C25', String(499, 'Modern_Spanish_CI_AS')),
    Column('C26', String(499, 'Modern_Spanish_CI_AS')),
    Column('C27', String(499, 'Modern_Spanish_CI_AS')),
    Column('C28', String(499, 'Modern_Spanish_CI_AS')),
    Column('C29', String(499, 'Modern_Spanish_CI_AS')),
    Column('C30', String(499, 'Modern_Spanish_CI_AS')),
    Column('C31', String(499, 'Modern_Spanish_CI_AS')),
    Column('C32', String(499, 'Modern_Spanish_CI_AS')),
    Column('C33', String(499, 'Modern_Spanish_CI_AS')),
    Column('C34', String(499, 'Modern_Spanish_CI_AS')),
    Column('C35', String(499, 'Modern_Spanish_CI_AS')),
    Column('C36', String(499, 'Modern_Spanish_CI_AS')),
    Column('C37', String(1499, 'Modern_Spanish_CI_AS')),
    Column('C38', String(499, 'Modern_Spanish_CI_AS')),
    Column('C39', String(499, 'Modern_Spanish_CI_AS')),
    Column('C40', String(499, 'Modern_Spanish_CI_AS')),
    Column('C41', String(1499, 'Modern_Spanish_CI_AS')),
    Column('C42', String(499, 'Modern_Spanish_CI_AS')),
    Column('C43', String(499, 'Modern_Spanish_CI_AS')),
    Column('C44', String(499, 'Modern_Spanish_CI_AS')),
    Column('C45', String(499, 'Modern_Spanish_CI_AS')),
    Column('C46', String(499, 'Modern_Spanish_CI_AS')),
    Column('C47', String(499, 'Modern_Spanish_CI_AS')),
    Column('C48', String(499, 'Modern_Spanish_CI_AS')),
    Column('C49', String(499, 'Modern_Spanish_CI_AS')),
    Column('C50', String(499, 'Modern_Spanish_CI_AS')),
    Column('C51', String(499, 'Modern_Spanish_CI_AS')),
    Column('C52', String(499, 'Modern_Spanish_CI_AS')),
    Column('C53', String(499, 'Modern_Spanish_CI_AS')),
    Column('C54', String(499, 'Modern_Spanish_CI_AS')),
    Column('C55', String(499, 'Modern_Spanish_CI_AS')),
    Column('C56', String(499, 'Modern_Spanish_CI_AS')),
    Column('C57', String(499, 'Modern_Spanish_CI_AS')),
    Column('C58', String(499, 'Modern_Spanish_CI_AS')),
    Column('C59', String(499, 'Modern_Spanish_CI_AS')),
    Column('C60', String(499, 'Modern_Spanish_CI_AS')),
    Column('C61', String(499, 'Modern_Spanish_CI_AS')),
    Column('C62', String(499, 'Modern_Spanish_CI_AS')),
    Column('C63', String(499, 'Modern_Spanish_CI_AS')),
    Column('C64', String(499, 'Modern_Spanish_CI_AS')),
    Column('C65', String(499, 'Modern_Spanish_CI_AS')),
    Column('C66', String(499, 'Modern_Spanish_CI_AS')),
    Column('C67', String(499, 'Modern_Spanish_CI_AS')),
    Column('C68', String(499, 'Modern_Spanish_CI_AS')),
    Column('C69', String(499, 'Modern_Spanish_CI_AS')),
    Column('C70', String(499, 'Modern_Spanish_CI_AS'))
)


t_GSQLFile2 = Table(
    'GSQLFile2', Base.metadata,
    Column('C1', String(499, 'Modern_Spanish_CI_AS')),
    Column('C2', String(499, 'Modern_Spanish_CI_AS')),
    Column('C3', String(499, 'Modern_Spanish_CI_AS')),
    Column('C4', String(499, 'Modern_Spanish_CI_AS')),
    Column('C5', String(499, 'Modern_Spanish_CI_AS')),
    Column('C6', String(499, 'Modern_Spanish_CI_AS')),
    Column('C7', String(499, 'Modern_Spanish_CI_AS')),
    Column('C8', String(499, 'Modern_Spanish_CI_AS')),
    Column('C9', String(499, 'Modern_Spanish_CI_AS')),
    Column('C10', String(499, 'Modern_Spanish_CI_AS')),
    Column('C11', String(499, 'Modern_Spanish_CI_AS')),
    Column('C12', String(499, 'Modern_Spanish_CI_AS')),
    Column('C13', String(499, 'Modern_Spanish_CI_AS')),
    Column('C14', String(499, 'Modern_Spanish_CI_AS')),
    Column('C15', String(499, 'Modern_Spanish_CI_AS')),
    Column('C16', String(499, 'Modern_Spanish_CI_AS')),
    Column('C17', String(499, 'Modern_Spanish_CI_AS')),
    Column('C18', String(499, 'Modern_Spanish_CI_AS')),
    Column('C19', String(499, 'Modern_Spanish_CI_AS')),
    Column('C20', String(499, 'Modern_Spanish_CI_AS')),
    Column('C21', String(499, 'Modern_Spanish_CI_AS')),
    Column('C22', String(499, 'Modern_Spanish_CI_AS')),
    Column('C23', String(499, 'Modern_Spanish_CI_AS')),
    Column('C24', String(499, 'Modern_Spanish_CI_AS')),
    Column('C25', String(499, 'Modern_Spanish_CI_AS')),
    Column('C26', String(499, 'Modern_Spanish_CI_AS')),
    Column('C27', String(499, 'Modern_Spanish_CI_AS')),
    Column('C28', String(499, 'Modern_Spanish_CI_AS')),
    Column('C29', String(499, 'Modern_Spanish_CI_AS')),
    Column('C30', String(499, 'Modern_Spanish_CI_AS'))
)


t_GSQLFile3 = Table(
    'GSQLFile3', Base.metadata,
    Column('C1', String(499, 'Modern_Spanish_CI_AS')),
    Column('C2', String(499, 'Modern_Spanish_CI_AS')),
    Column('C3', String(499, 'Modern_Spanish_CI_AS')),
    Column('C4', String(499, 'Modern_Spanish_CI_AS')),
    Column('C5', String(499, 'Modern_Spanish_CI_AS')),
    Column('C6', String(499, 'Modern_Spanish_CI_AS')),
    Column('C7', String(499, 'Modern_Spanish_CI_AS'))
)


class GSectores(Base):
    __tablename__ = 'GSectores'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='Sector_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(150, 'Modern_Spanish_CI_AS'))
    AUTORIZADO: Mapped[Optional[int]] = mapped_column(TINYINT)


class GSisManifiesto(Base):
    __tablename__ = 'GSisManifiesto'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SisMan_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PREFIJO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOMAN: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    NOMNUMDESCIMPO: Mapped[Optional[str]] = mapped_column(String(60, 'Modern_Spanish_CI_AS'))
    NOMPERSACARGO: Mapped[Optional[str]] = mapped_column(String(60, 'Modern_Spanish_CI_AS'))
    CONSIGNADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    PTOEXTSAL: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    LOCALIZAPTOEXTSAL: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PTODESTINO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    LOCALIZAPTODESTINO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PTOENTRADA: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    LOCALIZAPTOENTRADA: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    CLAVEBROKER: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLAVETRANS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FACTURAPAG: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ESCODERCODBARRASSCAC: Mapped[Optional[int]] = mapped_column(TINYINT)


class GSisMultiples(Base):
    __tablename__ = 'GSisMultiples'
    __table_args__ = (
        PrimaryKeyConstraint('IDENTIFICADOR', name='SisMul_PKIdentificador'),
    )

    IDENTIFICADOR: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    PREFIJO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TIPOMOV: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PROVEEDOREXPORTADOR: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOPORVENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    VENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))


class GSubEmpresa(Base):
    __tablename__ = 'GSubEmpresa'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVESUB', name='GenSub_PKClaveSub'),
    )

    CLAVESUB: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(256, 'Modern_Spanish_CI_AS'))
    BROKER: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))


class GTipoCambio(Base):
    __tablename__ = 'GTipoCambio'
    __table_args__ = (
        PrimaryKeyConstraint('FECHA', name='GenTC_PKFecha_Asc'),
        Index('GenTC_AKFecha_Desc', 'FECHA')
    )

    FECHA: Mapped[int] = mapped_column(Integer, primary_key=True)
    VALOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))


class GTipoCambioMM(Base):
    __tablename__ = 'GTipoCambioMM'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEMONEDA', 'ANIO', name='TCMMon_PKClaveMonAnio'),
    )

    CLAVEMONEDA: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    ANIO: Mapped[str] = mapped_column(String(4, 'Modern_Spanish_CI_AS'), primary_key=True)
    ENERO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    FEBRERO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    MARZO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    ABRIL: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    MAYO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    JUNIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    JULIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    AGOSTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    SEPTIEMBRE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    OCTUBRE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    NOVIEMBRE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    DICIEMBRE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))


class GTipoDoc(Base):
    __tablename__ = 'GTipoDoc'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVETD', name='TPDOC_PKClave'),
    )

    CLAVETD: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class GTipoDocDigital(Base):
    __tablename__ = 'GTipoDocDigital'
    __table_args__ = (
        PrimaryKeyConstraint('IDTIPODOCUMENTO', name='TDogDig_PKIDTipoDoc'),
    )

    IDTIPODOCUMENTO: Mapped[str] = mapped_column(String(9, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPODOCUMENTO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))


class GTipoMultiMoneda(Base):
    __tablename__ = 'GTipoMultiMoneda'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', 'FECHAPUBLICACION', name='TipoMM_PKClaveFecha'),
    )

    CLAVE: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHAPUBLICACION: Mapped[int] = mapped_column(Integer, primary_key=True)
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FACTORCONV: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))


class GTipoTrailer(Base):
    __tablename__ = 'GTipoTrailer'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVETRAILER', name='TipTra_PKClaveTrailer'),
    )

    CLAVETRAILER: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class GTipoTransportes(Base):
    __tablename__ = 'GTipoTransportes'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVETRANSPORTE', name='TipTran_PKClaveTrans'),
    )

    CLAVETRANSPORTE: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class GTiposMoneda(Base):
    __tablename__ = 'GTiposMoneda'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='TIPMON_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    MONEDA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    DESCPAIS: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class GTrailers(Base):
    __tablename__ = 'GTrailers'
    __table_args__ = (
        PrimaryKeyConstraint('NUMTRAILER', name='Traila_PKNumTrailer'),
    )

    NUMTRAILER: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMTRAILERACE: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOTRAILER: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CODENTIDADIIT: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NUMEROPLACAS: Mapped[Optional[str]] = mapped_column(String(17, 'Modern_Spanish_CI_AS'))
    ESTADO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CLAVECONTENEDOR: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class GTransportes(Base):
    __tablename__ = 'GTransportes'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVETRANSPORTE', name='GTrans_PKClaveTransp'),
    )

    CLAVETRANSPORTE: Mapped[str] = mapped_column(String(14, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVETRANSACE: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    CLAVETRANS: Mapped[Optional[str]] = mapped_column(String(23, 'Modern_Spanish_CI_AS'))
    NUMIDENTIFICATRANS: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    TIPOTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CODENTIDADIIT: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NUMTRANSPONDEDOR: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    NUMERODOT: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    NUMEROPLACAS: Mapped[Optional[str]] = mapped_column(String(17, 'Modern_Spanish_CI_AS'))
    CIUDAD: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESTADO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(49, 'Modern_Spanish_CI_AS'))
    NOMEMPASEGURADORA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    NUMEROASEGURANZA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    MONTOASEGURANZA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 2))
    FECHAASEGURANZA: Mapped[Optional[int]] = mapped_column(Integer)
    NUMEROCAJA: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    MARCA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ANIO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    SERIE: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    NUMMOTOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    PERMISOSCT: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    COLOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CLAVECONTENEDOR: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class GTransportista(Base):
    __tablename__ = 'GTransportista'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVETRANS', name='GenTra_PKClaveTrans'),
    )

    CLAVETRANS: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    NOMBRE: Mapped[Optional[str]] = mapped_column(String(256, 'Modern_Spanish_CI_AS'))
    NOMBRECORTO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    RESPONSABLE: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    RFC: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CALLES: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CODIGOPOSTAL: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CIUDAD: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESTADO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CODCARGADOR: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CODIGOCAAT: Mapped[Optional[str]] = mapped_column(String(49, 'Modern_Spanish_CI_AS'))
    CODIGOTRANS: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    TIPOINTERFASETRANS: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SERVIDOR_FTP: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    USUARIO_FTP: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    CLAVEACCESSO_FTP: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    DIRECTORIO_FTP: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    FILLERCODE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))


class GUMAduana(Base):
    __tablename__ = 'GUMAduana'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='GenUMA_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    UNIDADSCAII: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))


class GUMAme(Base):
    __tablename__ = 'GUMAme'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='UMAAme_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))


class GUMOMA(Base):
    __tablename__ = 'GUMOMA'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEUM', name='UMOMA_PKClaveUM'),
    )

    CLAVEUM: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))


class GUniMed(Base):
    __tablename__ = 'GUniMed'
    __table_args__ = (
        PrimaryKeyConstraint('UNIDAD', name='GenUni_PKUnidad'),
    )

    UNIDAD: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FACTORCONV: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    UNIDAD_MEX: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    UNIDAD_AME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLAVE_ADUANA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEACE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))


class GUniMedACE(Base):
    __tablename__ = 'GUniMedACE'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEACE', name='UMACE_PKClaveACE'),
    )

    CLAVEACE: Mapped[str] = mapped_column(String(4, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(49, 'Modern_Spanish_CI_AS'))


class GUniMedida(Base):
    __tablename__ = 'GUniMedida'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVEUNI', name='UniMed_PKUnidad'),
    )

    CLAVEUNI: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONINGLES: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CLAVE_AMEX: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVE_AAMER: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CLAVEACE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    CLAVEOMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))

class PedimentosAmericanos(Base):
    __tablename__ = 'PedimentosAmericanos'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='PKClavePedAme'),
    )

    CLAVE: Mapped[int] = mapped_column(Integer, primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(249, 'Modern_Spanish_CI_AS'))
    TIPOOPERACION: Mapped[Optional[int]] = mapped_column(Integer)


class QAssetTag(Base):
    __tablename__ = 'QAssetTag'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAIMPO', 'TIPOFACTURA', 'ASSETNUMBER', name='AssetT_PKConsecLinAsset'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAIMPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    ASSETNUMBER: Mapped[str] = mapped_column(String(25, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOFACTURA: Mapped[str] = mapped_column(String(6, 'Modern_Spanish_CI_AS'), primary_key=True)
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FOTOPARTE: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))


class QClaAct(Base):
    __tablename__ = 'QClaAct'
    __table_args__ = (
        PrimaryKeyConstraint('CLASE', name='EqiCla_PKClase'),
    )

    CLASE: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    TIPOMAQEQUIPO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FRACCION: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    FRACCIONEXPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACEXPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    TASADEPRECIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    FRACCIONAME: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    CLAVESUB: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    REVFISICA: Mapped[Optional[int]] = mapped_column(TINYINT)
    FDA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ECCN: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    HABILITADESHABILITACLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONEXENTAIVA: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))


class QClasePermiso(Base):
    __tablename__ = 'QClasePermiso'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'CLASE', name='ClaPer_PKConsecClase'),
        Index('ClaPer_AKClaseFecha', 'CLASE', 'FECHA')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    CLASE: Mapped[str] = mapped_column(String(9, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMOFICIO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    LINEA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    PAGINARENGLON: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)


class QConfiguracion(Base):
    __tablename__ = 'QConfiguracion'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='QConfi_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    TIPODEFONDOS: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ACTIMPLEMENTACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    ALTAUSUARIOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESPALDO: Mapped[Optional[int]] = mapped_column(TINYINT)
    FOLDER_LLEGADA: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    ACTIVAR_BUSQUEDA: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    INTERVALO_BUSQUEDA: Mapped[Optional[int]] = mapped_column(Integer)
    FTP_SERVER: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FTP_USERNAME: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FTP_PASSWORD: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FTP_DIRECTORY: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    TIPOACTUALIZACION: Mapped[Optional[str]] = mapped_column(CHAR(20, 'Modern_Spanish_CI_AS'))
    DIRECCTORIOMANUALSIFRA: Mapped[Optional[str]] = mapped_column(String(199, 'Modern_Spanish_CI_AS'))
    DIRECCIONHTTP: Mapped[Optional[str]] = mapped_column(CHAR(200, 'Modern_Spanish_CI_AS'))
    FTP_FOLDER_LLEGADA: Mapped[Optional[str]] = mapped_column(String(1999, 'Modern_Spanish_CI_AS'))
    FECHAACTUALIZACION: Mapped[Optional[int]] = mapped_column(Integer)
    RUTASERVIDOR: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))


class QEqeMaq(Base):
    __tablename__ = 'QEqeMaq'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAEXPO', name='EqiPex_PKConsecLinea'),
        Index('EqiPex_AKConsLinTipoAs', 'CONSECUTIVO', 'LINEAEXPO', 'TIPOFACTURAASSET'),
        Index('EqiPex_FKFacImpLinImp', 'FACTURAIMPO', 'LINEAIMPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAEXPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    LINEAIMPO: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOMOVIMPO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    CANTEXPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOCAPTURA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIODLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUCOMDLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOACTUALDLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTODEPRECME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUCOMPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOACTUALMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTODEPRECMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOCOMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORACTUALIZADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOCOMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORACTUALIZADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    DESCBULTOS: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    FRACCIONEXPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TASAEX: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ADVEXPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    TIPOFRAC: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    ADVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    MARCA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    LLEVASERIE: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCARGA: Mapped[Optional[int]] = mapped_column(TINYINT)
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    RECTIFICACION: Mapped[Optional[int]] = mapped_column(SmallInteger)
    CANT_SERIES: Mapped[Optional[int]] = mapped_column(Integer)
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CERTORIGEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SUBPARTIDA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    INCUYESUBPARTIDAS: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    LLEVACODFDA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CLAVEFDA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PROCEDENCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TASADEPRECIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    FRACCIONREFERENCIA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONEEXTRA: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    TIPOBUSQUEDA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ESSUBPARTIDA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CONTIENESUBP: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ADVALORMELINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    ADVALORMNLINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PERMISOSPED: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    LINEAPED: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFCC: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    TIPOFACTURAASSET: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    CANTEXPOUMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEUMA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    VALOREXPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    METVALORVALORDETERMINADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    METVALORMOTIVODEUSO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    LOTE: Mapped[Optional[str]] = mapped_column(String(254, 'Modern_Spanish_CI_AS'))
    NUMENTRADA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CONTENEDORREGLA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOAPHIS: Mapped[Optional[int]] = mapped_column(Integer)


class QEqeMaqRep(Base):
    __tablename__ = 'QEqeMaqRep'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAEXPO', name='RepPex_PKConsecLinea'),
        Index('RepPex_AKConsLinTipoAs', 'CONSECUTIVO', 'LINEAEXPO', 'TIPOFACTURAASSET'),
        Index('RepPex_FKFacImpLinImp', 'FACTURAIMPO', 'LINEAIMPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAEXPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    LINEAIMPO: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOMOVIMPO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    CANTEXPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOCAPTURA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIODLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUCOMDLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOACTUALDLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTODEPRECME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUCOMPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOACTUALMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTODEPRECMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOCOMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORACTUALIZADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOCOMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORACTUALIZADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    DESCBULTOS: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    FRACCIONEXPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TASAEX: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ADVEXPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    TIPOFRAC: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    ADVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    MARCA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    LLEVASERIE: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCARGA: Mapped[Optional[int]] = mapped_column(TINYINT)
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    RECTIFICACION: Mapped[Optional[int]] = mapped_column(SmallInteger)
    CANT_SERIES: Mapped[Optional[int]] = mapped_column(Integer)
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CERTORIGEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SUBPARTIDA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    INCUYESUBPARTIDAS: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    LLEVACODFDA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CLAVEFDA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PROCEDENCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TASADEPRECIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPOBUSQUEDA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ESSUBPARTIDA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CONTIENESUBP: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CANTRETORNADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORRETORNADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORRETORNADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ADVALORMELINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    ADVALORMNLINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PERMISOSPED: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    LINEAPED: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFCC: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    TIPOFACTURAASSET: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONEEXTRA: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    CANTEXPOUMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEUMA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    VALOREXPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    LOTE: Mapped[Optional[str]] = mapped_column(String(254, 'Modern_Spanish_CI_AS'))
    NUMENTRADA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class QEqiDef(Base):
    __tablename__ = 'QEqiDef'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAIMPODEF', name='EqiPdf_PKConsecLinea'),
        Index('EqiPdf_AKConsLinTipoAs', 'CONSECUTIVO', 'LINEAIMPODEF', 'TIPOFACTURAASSET'),
        Index('SQL_FK_CLASE_IMPDEF', 'CLASE')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAIMPODEF: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTIMPODEF: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEXPOTEMP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEXISTENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOCAPTURA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIODLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOSUBPDLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOSUBPPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORSUBPMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORSUBPME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMPERMISO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAGRENGLON: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    DESCBULTOS: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    FRACCION: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TASAIM: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    ADVIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    ADVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    MARCA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    LLEVASERIE: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTRETORNADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTRETORNADATEMP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORRETORNADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORRETORNADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    RECTIFICACION: Mapped[Optional[int]] = mapped_column(SmallInteger)
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESSUBPARTIDA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CONTIENESUBP: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    SUBPARTIDA: Mapped[Optional[int]] = mapped_column(Integer)
    ESREPARACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CERTORIGEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ASSETNUMBER: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    EQI_MENSAJE: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    EQUIPOPROPIO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NUMREFERENCIA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CANT_SERIESDEF: Mapped[Optional[int]] = mapped_column(Integer)
    FOTOACTIVOFIJO: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    CLAVETIPOIV32: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMEROIV32: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    BODEGA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    REQUISITOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    PERMISOROCTAVA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FRACCIONROCTAVA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MONTOIGI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    LINEARO: Mapped[Optional[int]] = mapped_column(Integer)
    ADVALORMELINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ADVALORMNLINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PERMISOSPED: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    LINEAPED: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOFACTURAASSET: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONEEXTRA: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CANTIMPOUMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEUMA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESMCIAMILITAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    METVALORVALORDETERMINADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    METVALORMOTIVODEUSO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    LOTE: Mapped[Optional[str]] = mapped_column(String(254, 'Modern_Spanish_CI_AS'))
    NUMENTRADA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CONTENEDORPARTESII: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPOMAT: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))


class QEqiMaq(Base):
    __tablename__ = 'QEqiMaq'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAIMPO', name='EqiPim_PKConsecLinea'),
        Index('EqiPim_AKConsLinTipoAs', 'CONSECUTIVO', 'LINEAIMPO', 'TIPOFACTURAASSET'),
        Index('SQL_FK_CLASE', 'CLASE')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAIMPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHADEPRECIACION: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEXPOTEMP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEXISTENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOCAPTURA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIODLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOSUBPDLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOSUBPPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORSUBPMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORSUBPME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    NUMPERMISO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAGRENGLON: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    DESCBULTOS: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCION: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ADVIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    TASAIM: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    ADVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    MARCA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    LLEVASERIE: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTRETORNADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTRETORNADATEMP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORRETORNADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORDEPRECIADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORRETORNADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORDEPRECIADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    RECTIFICACION: Mapped[Optional[int]] = mapped_column(SmallInteger)
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESSUBPARTIDA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CONTIENESUBP: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    SUBPARTIDA: Mapped[Optional[int]] = mapped_column(Integer)
    ESREPARACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CERTORIGEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ASSETNUMBER: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    NUMREFERENCIA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CANT_SERIES: Mapped[Optional[int]] = mapped_column(Integer)
    FOTOACTIVOFIJO: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    CLAVETIPOIV32: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMEROIV32: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    FECHAFACIMPORET: Mapped[Optional[int]] = mapped_column(Integer)
    FACTURAIMPORET: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONEEXTRA: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    BODEGA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    REQUISITOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    PERMISOROCTAVA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FRACCIONROCTAVA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MONTOIGI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    LINEARO: Mapped[Optional[int]] = mapped_column(Integer)
    ADVALORMELINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ADVALORMNLINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PERMISOSPED: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    LINEAPED: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOFACTURAASSET: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CANTIMPOUMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEUMA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESMCIAMILITAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    LOTE: Mapped[Optional[str]] = mapped_column(String(254, 'Modern_Spanish_CI_AS'))
    VALORIVAMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAMNUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAMEUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    METVALORVALORDETERMINADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    METVALORMOTIVODEUSO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMENTRADA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    OMITITENANEXO31: Mapped[Optional[int]] = mapped_column(TINYINT)
    CONTENEDORPARTESII: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPOMAT: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))


class QEqiMaqRep(Base):
    __tablename__ = 'QEqiMaqRep'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAIMPO', name='RepPim_PKConsecLinea'),
        Index('RepPim_AKConsLinTipoAs', 'CONSECUTIVO', 'LINEAIMPO', 'TIPOFACTURAASSET'),
        Index('RepPim_FKFacExpLinExp', 'FACTURAEXPO', 'LINEAEXPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAIMPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    LINEAEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOMOVIMPO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FECHADEPRECIACION: Mapped[Optional[int]] = mapped_column(Integer)
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOCAPTURA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIODLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOSUBPDLLS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOSUBPPESOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORSUBPMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORSUBPME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMPERMISO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAGRENGLON: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(900, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    DESCBULTOS: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCION: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ADVIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    TASAIM: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    ADVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    MARCA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    LLEVASERIE: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTRETORNADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORRETORNADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORDEPRECIADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORRETORNADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORDEPRECIADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    RECTIFICACION: Mapped[Optional[int]] = mapped_column(SmallInteger)
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESSUBPARTIDA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CONTIENESUBP: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    SUBPARTIDA: Mapped[Optional[int]] = mapped_column(Integer)
    ESREPARACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CERTORIGEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ASSETNUMBER: Mapped[Optional[str]] = mapped_column(String(25, 'Modern_Spanish_CI_AS'))
    NUMREFERENCIA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CANT_SERIES: Mapped[Optional[int]] = mapped_column(Integer)
    FOTOACTIVOFIJO: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    CLAVETIPOIV32: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMEROIV32: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    DESCARGA: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONALTERNA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    BODEGA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    PERMISOROCTAVA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FRACCIONROCTAVA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MONTOIGI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPOBUSQUEDA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ADVALORMELINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ADVALORMNLINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PERMISOSPED: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    LINEAPED: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOFACTURAASSET: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONEEXTRA: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CANTIMPOUMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEUMA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESMCIAMILITAR: Mapped[Optional[int]] = mapped_column(TINYINT)


class QFacExp(Base):
    __tablename__ = 'QFacExp'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='EqiFex_PKConsecutivo'),
        Index('EqiFex_FKFacProforma', 'NUMEROPROFORMA'),
        Index('EqiFex_FKFacturaExpo', 'FACTURAEXPO', unique=True),
        Index('EqiFex_FKManFacExp', 'MANIFIESTO', 'FACTURAEXPO'),
        Index('EqiFex_FKPedExp_Reme', 'PEDIMENTOEXPO', 'REMESA'),
        Index('EqiFex_FKPedimento', 'PEDIMENTOEXPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PED_PENDIENTE_ASIGNAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEDIMENTOEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    CAMBIOREGIMEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    DEFINITIVA: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOPORVENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    VENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    MANIFIESTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    VALOREXPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORACTUALIZADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORACTUALIZADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CANTEXPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTAAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTECOMPLE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    BILLNUMBER: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    COMPLEMENTO1: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    IDENTIFICADOR2: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    COMPLEMENTO2: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    OBSERVACIONES: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOFACTURA: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    CLAVETIPOIV18: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMEROIV18: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    ESCAMBIOREGIMEN: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CUALTIPOCAMBIO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    GENERAID: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ACTVALOR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 0))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 9))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMEROPROFORMA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OFICIO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    NUMEROGUIA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMEMBARQUE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    RECIBIDOPOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FECHAENTREGA: Mapped[Optional[int]] = mapped_column(Integer)
    ENTREGADO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PEDIMENTOR1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOMOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    FACTURAALTERNA: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    COMENTARIOSESTATUS: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TOTALINCREMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMFACTURABROKER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHAFACBROKER: Mapped[Optional[int]] = mapped_column(Integer)
    IDRELDOC: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFIRMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    GENPARTIDAS: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    COMOFUEPROCESADA: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    PROVEEDOREXPORTADOR: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIOMM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    VALOREXPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    OBSERVACIONESVU: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NUMEROCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    CONTENEDORESTIPO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DATOSVEHICULO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMERONIU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CANTGUIASEMBARQUE: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    ADENDAVU: Mapped[Optional[str]] = mapped_column(String(204, 'Modern_Spanish_CI_AS'))
    ESFERROCARRIL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESTINOORIGENCOVE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FECHAEMISION: Mapped[Optional[int]] = mapped_column(Integer)
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MODOCONTINGENCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    RAZONEXPORTACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TERMINOSPAGO: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    MANIOBRAS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    RECINTO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    SEMAFOROEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    OPCIONIV18: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPODEGUIAAIDENTIFICAR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CFDIUUID: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CFDIPATHPDF: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CFDIPATHXML: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CLAVEDOT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SUBDIVISION: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FUNGIRCOMOCO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ENAJENACIONBIENES: Mapped[Optional[int]] = mapped_column(TINYINT)
    APENDICE17: Mapped[Optional[int]] = mapped_column(TINYINT)


class QFacExpCobranza(Base):
    __tablename__ = 'QFacExpCobranza'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='CobExpQ_PKConsecutivoLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CONCEPTO: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    COBRADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHACOBRANZA: Mapped[Optional[int]] = mapped_column(Integer)
    VALOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    DEPTOCOBRANZA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FACTCOBRADOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NOMBRECOBRADOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class QFacExpRep(Base):
    __tablename__ = 'QFacExpRep'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='FexRep_PKConsecutivo'),
        Index('FexRep_FKFacProforma', 'NUMEROPROFORMA'),
        Index('FexRep_FKFacturaExpo', 'FACTURAEXPO', unique=True),
        Index('FexRep_FKManFacExp', 'MANIFIESTO', 'FACTURAEXPO'),
        Index('FexRep_FKPedExp_Reme', 'PEDIMENTOEXPO', 'REMESA'),
        Index('FexRep_FKPedimento', 'PEDIMENTOEXPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PED_PENDIENTE_ASIGNAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEDIMENTOEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    CAMBIOREGIMEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    DEFINITIVA: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOPORVENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    VENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    MANIFIESTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    VALOREXPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORACTUALIZADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORACTUALIZADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CANTEXPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTAAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTECOMPLE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    BILLNUMBER: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    COMPLEMENTO1: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    IDENTIFICADOR2: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    COMPLEMENTO2: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    OBSERVACIONES: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOFACTURA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLAVETIPOIV18: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMEROIV18: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    ESCAMBIOREGIMEN: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CUALTIPOCAMBIO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    GENERAID: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ACTVALOR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 0))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMEROPROFORMA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OFICIO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    NUMEROGUIA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMEMBARQUE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    RECIBIDOPOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FECHAENTREGA: Mapped[Optional[int]] = mapped_column(Integer)
    ENTREGADO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PEDIMENTOR1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOMOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    FACTURAALTERNA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FORMADESCARGA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    COMENTARIOSESTATUS: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TOTALINCREMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMFACTURABROKER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHAFACBROKER: Mapped[Optional[int]] = mapped_column(Integer)
    IDRELDOC: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFIRMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    COMOFUEPROCESADA: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    PROVEEDOREXPORTADOR: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIOMM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    VALOREXPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    OBSERVACIONESVU: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NUMEROCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    CONTENEDORESTIPO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DATOSVEHICULO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMERONIU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CANTGUIASEMBARQUE: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    ADENDAVU: Mapped[Optional[str]] = mapped_column(String(204, 'Modern_Spanish_CI_AS'))
    ESFERROCARRIL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESTINOORIGENCOVE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MODOCONTINGENCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    RAZONEXPORTACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TERMINOSPAGO: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    MANIOBRAS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    RECINTO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    SEMAFOROEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    OPCIONIV18: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPODEGUIAAIDENTIFICAR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CFDIUUID: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CFDIPATHPDF: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CFDIPATHXML: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CLAVEDOT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))


class QFacImp(Base):
    __tablename__ = 'QFacImp'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='EqiFim_PKConsecutivo'),
        Index('EqiFim_FKFacturaImpo', 'FACTURAIMPO', unique=True),
        Index('EqiFim_FKPedImp_Remes', 'PEDIMENTOIMPO', 'REMESA'),
        Index('EqiFim_FKPedimento', 'PEDIMENTOIMPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PED_PENDIENTE_ASIGNAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEDIMENTOIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOCAMBIOMM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CANTIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    CANTRETORNADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    SUJECION: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    OBSERVACIONES: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    CLAVETIPOIV18: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMEROIV18: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CUALTIPOCAMBIO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FECHAEMISION: Mapped[Optional[int]] = mapped_column(Integer)
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 0))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    PEDIMENTOR1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SELLOVALOR2500: Mapped[Optional[int]] = mapped_column(TINYINT)
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TOTALINCREMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FACTURAALTERNA: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    TIPOMOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    COMENTARIOSESTATUS: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IDRELDOC: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFIRMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    COMOFUEPROCESADA: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    OBSERVACIONESVU: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NUMEROCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    CONTENEDORESTIPO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DATOSVEHICULO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMERONIU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CANTGUIASEMBARQUE: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    ADENDAVU: Mapped[Optional[str]] = mapped_column(String(204, 'Modern_Spanish_CI_AS'))
    ESFERROCARRIL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESTINOORIGENCOVE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    PUERTOENTRADA: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    FUEREVISADAMCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    MODOCONTINGENCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    RECINTO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    SEMAFOROIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FACTORIVA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    VALORIVAMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPODEGUIAAIDENTIFICAR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CLAVEDOT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SUBDIVISION: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FUNGIRCOMOCO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    APENDICE17: Mapped[Optional[int]] = mapped_column(TINYINT)
    APLICAPARTESII: Mapped[Optional[int]] = mapped_column(TINYINT)


class QFacImpCobranza(Base):
    __tablename__ = 'QFacImpCobranza'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='QCobImT_PKConsecLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CONCEPTO: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    COBRADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHACOBRANZA: Mapped[Optional[int]] = mapped_column(Integer)
    VALOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    DEPTOCOBRANZA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FACTCOBRADOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NOMBRECOBRADOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class QFacImpDef(Base):
    __tablename__ = 'QFacImpDef'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='EqiFID_PKConsecutivo'),
        Index('EqiFID_FKFacImpoDef', 'FACTURAIMPODEF', unique=True),
        Index('EqiFID_FKPedID_Remes', 'PEDIMENTOIMPODEF', 'REMESA'),
        Index('EqiFID_FKPedimento', 'PEDIMENTOIMPODEF')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PED_PENDIENTE_ASIGNAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEDIMENTOIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FACTURAIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOCAMBIOMM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    PROVIMPODEFCR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FACTORIVA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 4))
    CANTIMPODEF: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    CANTRETORNADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    SUJECION: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    OBSERVACIONES: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    CLAVETIPOIV18: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMEROIV18: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CUALTIPOCAMBIO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FECHAEMISION: Mapped[Optional[int]] = mapped_column(Integer)
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 0))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    PEDIMENTOR1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SELLOVALOR2500: Mapped[Optional[int]] = mapped_column(TINYINT)
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TOTALINCREMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FACTURAALTERNA: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    TIPOMOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    COMENTARIOSESTATUS: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IDRELDOC: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFIRMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    COMOFUEPROCESADA: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    OBSERVACIONESVU: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NUMEROCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    CONTENEDORESTIPO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DATOSVEHICULO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMERONIU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CANTGUIASEMBARQUE: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    ADENDAVU: Mapped[Optional[str]] = mapped_column(String(204, 'Modern_Spanish_CI_AS'))
    ESFERROCARRIL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESTINOORIGENCOVE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    PUERTOENTRADA: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    FUEREVISADAMCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    MODOCONTINGENCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    RECINTO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    SEMAFOROIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPODEGUIAAIDENTIFICAR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CLAVEDOT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SUBDIVISION: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FUNGIRCOMOCO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    APENDICE17: Mapped[Optional[int]] = mapped_column(TINYINT)
    APLICAPARTESII: Mapped[Optional[int]] = mapped_column(TINYINT)


class QFacImpRep(Base):
    __tablename__ = 'QFacImpRep'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='FimRep_PKConsecutivo'),
        Index('FimRep_FKFacturaImpo', 'FACTURAIMPO', unique=True),
        Index('FimRep_FKPedImp_Remes', 'PEDIMENTOIMPO', 'REMESA'),
        Index('FimRep_FKPedimento', 'PEDIMENTOIMPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PED_PENDIENTE_ASIGNAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEDIMENTOIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOCAMBIOMM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CANTIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    CANTRETORNADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    SUJECION: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    OBSERVACIONES: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    CLAVETIPOIV18: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMEROIV18: Mapped[Optional[str]] = mapped_column(String(35, 'Modern_Spanish_CI_AS'))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CUALTIPOCAMBIO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FECHAEMISION: Mapped[Optional[int]] = mapped_column(Integer)
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 0))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    PEDIMENTOR1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SELLOVALOR2500: Mapped[Optional[int]] = mapped_column(TINYINT)
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TOTALINCREMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FACTURAALTERNA: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    TIPOMOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    COMENTARIOSESTATUS: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IDRELDOC: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFIRMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    ESCAMBIOREGIMEN: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    COMOFUEPROCESADA: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    OBSERVACIONESVU: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NUMEROCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    CONTENEDORESTIPO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DATOSVEHICULO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMERONIU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CANTGUIASEMBARQUE: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    ADENDAVU: Mapped[Optional[str]] = mapped_column(String(204, 'Modern_Spanish_CI_AS'))
    ESFERROCARRIL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESTINOORIGENCOVE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PUERTOENTRADA: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    FUEREVISADAMCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    MODOCONTINGENCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    RECINTO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    SEMAFOROIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPODEGUIAAIDENTIFICAR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CLAVEDOT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))


class QInfDepre(Base):
    __tablename__ = 'QInfDepre'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='QIDp_ConsecIDP'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    SUPUESTO: Mapped[Optional[str]] = mapped_column(String(800, 'Modern_Spanish_CI_AS'))
    PORCENTAJE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))


class QLocalizacion(Base):
    __tablename__ = 'QLocalizacion'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='EqiLoc_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))


t_QLocalizacionExt = Table(
    'QLocalizacionExt', Base.metadata,
    Column('CLAVE', String(6, 'Modern_Spanish_CI_AS')),
    Column('DEPARTAMENTO', String(1001, 'Modern_Spanish_CI_AS')),
    Column('RESPONSABLE', String(1001, 'Modern_Spanish_CI_AS')),
    Column('OBSERVACIONES', String(1001, 'Modern_Spanish_CI_AS'))
)


class QNiveles(Base):
    __tablename__ = 'QNiveles'
    __table_args__ = (
        PrimaryKeyConstraint('NIVEL', name='QNivel_PKNivel'),
        Index('QNivel_FKTipoNivel', 'TIPO')
    )

    NIVEL: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPO: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    MENUARCHIVO: Mapped[Optional[int]] = mapped_column(TINYINT)
    CONFIGIMPRESORA: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESPSCAF: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPLEMENTACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    MENUCONFIGURACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    DATOSEMPRESA: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBPARAMETROS: Mapped[Optional[int]] = mapped_column(TINYINT)
    GENERALES: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPOTEMPORAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPODEFINITIVA: Mapped[Optional[int]] = mapped_column(TINYINT)
    EXPORTACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    MENUCATALOGOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBGENERALES: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBEMPRESA: Mapped[Optional[int]] = mapped_column(TINYINT)
    LOCALIZACIONES: Mapped[Optional[int]] = mapped_column(TINYINT)
    UNIDADESADUANA: Mapped[Optional[int]] = mapped_column(TINYINT)
    UNIDADESMEDIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOSCAMBIO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOSMONEDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOSDOCUMENTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    PUERTOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISES: Mapped[Optional[int]] = mapped_column(TINYINT)
    BULTOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    IDENTIFICADORES: Mapped[Optional[int]] = mapped_column(TINYINT)
    INCOTERMS: Mapped[Optional[int]] = mapped_column(TINYINT)
    LEYENDASFIJAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBFRACCIONES: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACIMPOEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    AMERICANAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    SECTORES: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBACTIVOFIJO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOSAF: Mapped[Optional[int]] = mapped_column(TINYINT)
    CLASESAF: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBPEDIMENTOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    CATPEDIMENTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    REGIMENES: Mapped[Optional[int]] = mapped_column(TINYINT)
    CLAVESPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    CLIENTESPRO: Mapped[Optional[int]] = mapped_column(TINYINT)
    AADUANALES: Mapped[Optional[int]] = mapped_column(TINYINT)
    TRANSPORTISTA: Mapped[Optional[int]] = mapped_column(TINYINT)
    MENUPERMISO: Mapped[Optional[int]] = mapped_column(TINYINT)
    PERSECON: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBREPSECON: Mapped[Optional[int]] = mapped_column(TINYINT)
    BOTONCLASES: Mapped[Optional[int]] = mapped_column(TINYINT)
    BOTONPERMISO: Mapped[Optional[int]] = mapped_column(TINYINT)
    PERACTFIJO: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBREPACTFIJO: Mapped[Optional[int]] = mapped_column(TINYINT)
    BOTONCLASESAF: Mapped[Optional[int]] = mapped_column(TINYINT)
    BOTONPERMISOAF: Mapped[Optional[int]] = mapped_column(TINYINT)
    MENUIMPORTACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBTEMPORAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    CATIMPOTEMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    BITACTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    BITDESACTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBREPIMPOTEMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    BITBUSQUEDAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    BITCONSPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    BITRANGOCLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    BITRANGOPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    BITVALORDIS: Mapped[Optional[int]] = mapped_column(TINYINT)
    BITSAFEH: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBDEFINITIVA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CATIMPODEF: Mapped[Optional[int]] = mapped_column(TINYINT)
    BIDACTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    BIDDESACTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBREPIMPODEF: Mapped[Optional[int]] = mapped_column(TINYINT)
    BIDBUSQUEDAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    BIDCONSPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    BIDRANGOCLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    BIDRANGOPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    CATCREGIMEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    BCRACTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    BCRDESCTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    TRANSELECIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    BIASIGPEDPEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    BIASIGPEDRECT: Mapped[Optional[int]] = mapped_column(TINYINT)
    MENUEXPORTACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBEXPOTEMPORAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    BETACTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    BETDESACTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBEXPODEFINITIVO: Mapped[Optional[int]] = mapped_column(TINYINT)
    BEDACTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    BEDDESACTUALIZAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    MANIFIESTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TRANSELECEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    BEASIGPEDPEN: Mapped[Optional[int]] = mapped_column(TINYINT)
    BEASIGPEDRECT: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBREPEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    BEBUSQUEDAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    BECONSPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    BERANGOCLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    BERANGOPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    MENUDIVERSOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBREPORTES: Mapped[Optional[int]] = mapped_column(TINYINT)
    REPMOVTEM: Mapped[Optional[int]] = mapped_column(TINYINT)
    REPMOVDEF: Mapped[Optional[int]] = mapped_column(TINYINT)
    HOJACALCULO: Mapped[Optional[int]] = mapped_column(TINYINT)
    MANIFESTACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    REPANUAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    SUBCATALOGOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    REPCLASESAF: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCLASESAF: Mapped[Optional[int]] = mapped_column(TINYINT)
    REPPEDIMENTOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    REPFRACCIONES: Mapped[Optional[int]] = mapped_column(TINYINT)
    REPCLIENTES: Mapped[Optional[int]] = mapped_column(TINYINT)
    MENUSEGURIDAD: Mapped[Optional[int]] = mapped_column(TINYINT)
    NIVELES: Mapped[Optional[int]] = mapped_column(TINYINT)
    USUARIOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    INSCATALOGOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    EDITCATALOGOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    BORRARCATALOGOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    INSPERMISOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    EDITPERMISOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    BORRARPERMISOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    INSIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    EDITIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    BORRARIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    INSEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    EDITEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    BORRAREXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    INSSEG: Mapped[Optional[int]] = mapped_column(TINYINT)
    EDITSEG: Mapped[Optional[int]] = mapped_column(TINYINT)
    BORRARSEG: Mapped[Optional[int]] = mapped_column(TINYINT)


class QPartes(Base):
    __tablename__ = 'QPartes'
    __table_args__ = (
        PrimaryKeyConstraint('NUMPARTE', name='QParte_PKNumParte'),
    )

    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTECOM: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESOUNITARIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FRACCION: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FECHAMODIFICA: Mapped[Optional[int]] = mapped_column(Integer)
    FOTOPARTE: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    FECHAMODIFICA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    FRACCIONAME: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    HABILITADADESHABILITADA: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHACREACIONPARTE: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFDA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CLAVEFCC: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    LICENSECODE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    ECCN: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    EXPORTCODE: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    SIMBOLOEXCLIC: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class QPedimentos(Base):
    __tablename__ = 'QPedimentos'
    __table_args__ = (
        PrimaryKeyConstraint('PEDIMENTO', name='EqiPed_PKPedimento'),
    )

    PEDIMENTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CLAVEPED: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    REGIMEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FECHA_INICIO: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_FIN: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_PAGO: Mapped[Optional[int]] = mapped_column(Integer)
    ACUSEELECTRONICO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FACTOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 4))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PEDRECTIFICA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SERECTIFICO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    OBSRECTIFICA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    INDIVIDUALCONS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    DTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 4))
    VALORIVA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PEDIMENTODESCARGO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PREVALIDACION: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    MONTOTIGIE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SERECTIFICO2: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PEDRECTIFICA2: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHA_REC_1: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_REC_2: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_CIERRE: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_REVISION: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_AUTORIZACION: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_RECIBIDO: Mapped[Optional[int]] = mapped_column(Integer)
    ERRORES: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PERSONAREV: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    REPRESANTANTEAA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CLAVEDESTORIGEN: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANAS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CLAVETRANSPORTACION: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FACTORINCREMENTABLE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    FEA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    FECHA_PAGO_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    FECHA_ENTRADARECINTO: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_EXTRACCIONRECINTO: Mapped[Optional[int]] = mapped_column(Integer)
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    FORMAPAGODTA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FORMAPAGOPREVAL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FORMAPAGOIGI: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FORMAPAGOIVA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    RECARGOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    IVADEPREV: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CUOTASCOMPENS: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    MULTAS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    IDENTIFICADORES: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CNT: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IEPS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    OPCIONDESTINO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    TIPOPEDIMENTOTRANSPORTEE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOPEDIMENTOTRANSPORTEA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOPEDIMENTOTRANSPORTES: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PEDIMENTO18: Mapped[Optional[str]] = mapped_column(String(18, 'Modern_Spanish_CI_AS'))
    IEPS2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    DTA2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 4))
    IVA2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IGI2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PREVALIDACION2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CNT2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IEPS2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DTA2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IVA2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IGI2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PREVALIDACION2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CNT2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IDPEDVIEJONUEVO: Mapped[Optional[int]] = mapped_column(Integer)


class QPedimentosAA(Base):
    __tablename__ = 'QPedimentosAA'
    __table_args__ = (
        PrimaryKeyConstraint('PEDIMENTO', 'CLAVEAA', name='PedEAA_PKPedAAduanal'),
    )

    PEDIMENTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVEAA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    FACTURA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FECHAFAC: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAREC: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAENT: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAVENC: Mapped[Optional[int]] = mapped_column(Integer)
    SECCION: Mapped[Optional[int]] = mapped_column(Integer)


class QPedimentosConcep(Base):
    __tablename__ = 'QPedimentosConcep'
    __table_args__ = (
        PrimaryKeyConstraint('PEDIMENTO', 'CLAVEAA', 'CONCEPTO', name='PedECon_PKPedAAConcepto'),
    )

    PEDIMENTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVEAA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    CONCEPTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    IMPORTE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 2))
    TIPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))


class QPermiso(Base):
    __tablename__ = 'QPermiso'
    __table_args__ = (
        PrimaryKeyConstraint('NUMSOLICITUD', 'FECHA_ENTREGA', name='Permiso_PKSoli_FechaE'),
        Index('Permiso_AKNumSolicitud', 'NUMSOLICITUD'),
        Index('Permiso_FKPermiso', 'PERMISO')
    )

    NUMSOLICITUD: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHA_ENTREGA: Mapped[int] = mapped_column(Integer, primary_key=True)
    PERMISO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHA_INICIO: Mapped[Optional[int]] = mapped_column(Integer)


class QPermisoClase(Base):
    __tablename__ = 'QPermisoClase'
    __table_args__ = (
        PrimaryKeyConstraint('NUMSOLICITUD', 'FECHA_ENTREGA', 'LINEA', 'CLASE', name='PerCla_PKSolFecLinCl'),
        Index('PerCla_FKClase', 'CLASE'),
        Index('PerCla_FKClase_Fecha', 'CLASE', 'FECHA_ENTREGA'),
        Index('PerCla_FKSolic_Clase', 'NUMSOLICITUD', 'CLASE', unique=True)
    )

    NUMSOLICITUD: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHA_ENTREGA: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    CLASE: Mapped[str] = mapped_column(String(9, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAGINARENGLON: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))


class QPermisoPR(Base):
    __tablename__ = 'QPermisoPR'
    __table_args__ = (
        PrimaryKeyConstraint('NUMSOLICITUD', 'FECHA_ENTREGA', 'LINEA', name='perPR_PKSoliFechLin'),
    )

    NUMSOLICITUD: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHA_ENTREGA: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    PAGINARENGLON: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))


class QPermisoSECON(Base):
    __tablename__ = 'QPermisoSECON'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='EqiSic_PKConsecutivo'),
        Index('EqiSic_FKOficioPerm', 'NUMOFICIO', 'PERMISO', unique=True),
        Index('EqiSic_FKPermiso', 'PERMISO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMOFICIO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PERMISO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)


t_QRepMovimientos = Table(
    'QRepMovimientos', Base.metadata,
    Column('FACTURAIMPO', String(15, 'Modern_Spanish_CI_AS')),
    Column('FECHA', Integer),
    Column('PEDIMENTO', String(15, 'Modern_Spanish_CI_AS')),
    Column('LINEAIMPO', SmallInteger),
    Column('DESCRIPCIONE', String(1000, 'Modern_Spanish_CI_AS')),
    Column('CANTIDADIMPO', DECIMAL(19, 8)),
    Column('UNIMED', String(5, 'Modern_Spanish_CI_AS')),
    Column('VALORIMPOMN', DECIMAL(23, 8)),
    Column('CANTRETORNADA', DECIMAL(19, 8)),
    Column('VALORRETORNADO', DECIMAL(23, 8)),
    Column('CANTSALDO', DECIMAL(19, 8)),
    Column('MARCA', String(50, 'Modern_Spanish_CI_AS')),
    Column('MODELO', String(50, 'Modern_Spanish_CI_AS')),
    Column('SERIE', String(50, 'Modern_Spanish_CI_AS')),
    Index('EqiRMov_AKFecha', 'FECHA'),
    Index('EqiRMov_PKFacIm_LinIm', 'FACTURAIMPO', 'LINEAIMPO')
)


class QSeriesDef(Base):
    __tablename__ = 'QSeriesDef'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAIMPODEF', 'RENGLON', name='SerDef_PKConsec_Lin_Ren'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAIMPODEF: Mapped[int] = mapped_column(Integer, primary_key=True)
    RENGLON: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SERIEEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    SERIEIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELOIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SUBMODELOIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    PARTEIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMIDIMPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))


class QSeriesExpo(Base):
    __tablename__ = 'QSeriesExpo'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAEXPO', 'RENGLON', name='SerExpo_PKConsec_Lin_Ren'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAEXPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    RENGLON: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SERIEEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELOEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SUBMODELOEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MARCA: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARTEEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    LINEASERIEIMPO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMIDEXPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))


class QSeriesExpoRep(Base):
    __tablename__ = 'QSeriesExpoRep'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAEXPO', 'RENGLON', name='SerExR_PKConsec_Lin_Ren'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAEXPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    RENGLON: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SERIEEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELOEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SUBMODELOEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MARCA: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARTEEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SERIEIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    LINEASERIEIMPO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMIDEXPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))


class QSeriesImpo(Base):
    __tablename__ = 'QSeriesImpo'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAIMPO', 'RENGLON', name='SerImp_PKConsec_Lin_Ren'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAIMPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    RENGLON: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SERIEEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    SERIEIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELOIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SUBMODELOIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    PARTEIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMIDIMPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))


class QSeriesImpoRep(Base):
    __tablename__ = 'QSeriesImpoRep'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAIMPO', 'RENGLON', name='SerImR_PKConsec_Lin_Ren'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAIMPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    RENGLON: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SERIEEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    SERIEIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELOIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SUBMODELOIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    PARTEIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MARCA: Mapped[Optional[int]] = mapped_column(TINYINT)
    LINEASERIEEXPOREP: Mapped[Optional[int]] = mapped_column(Integer)
    NUMIDIMPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))


class QSisCMex(Base):
    __tablename__ = 'QSisCMex'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SisMex_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PREFIJOCM: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOCM: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FRACCIONIMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPORDENCOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    PACKINGORDENCOMPRA: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRLOTE: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRNUMENTRADA: Mapped[Optional[int]] = mapped_column(Integer)


class QSisDef(Base):
    __tablename__ = 'QSisDef'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SisDef_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PREFIJOIMPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FIRMAFAME: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    GENERARASSETTAG: Mapped[Optional[int]] = mapped_column(TINYINT)
    CODIGOBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONIMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPORDENCOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CONTROLREMESA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    REMESAINICIO: Mapped[Optional[int]] = mapped_column(SmallInteger)
    REMESAFINAL: Mapped[Optional[int]] = mapped_column(SmallInteger)
    CANTLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    NUMPARTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ACTUALIZARPARTEPARTIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    PACKINGORDENCOMPRA: Mapped[Optional[int]] = mapped_column(Integer)
    SOLICITARCONTRASENAADMINISTRADOR: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRLOTE: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRNUMENTRADA: Mapped[Optional[int]] = mapped_column(Integer)


class QSisExpo(Base):
    __tablename__ = 'QSisExpo'
    __table_args__ = (
        PrimaryKeyConstraint('TIPOFACTURA', 'ESCAMBIOREGIMEN', name='SisExp_PKTipoFactura'),
    )

    TIPOFACTURA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    ESCAMBIOREGIMEN: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    PREFIJOEXPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOEXPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CODIGOBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTPNCODBAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DTACEROCODBAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    CBARRASVALOR: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FRACCIONEXP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    COSTOUNITMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    OCULTAREMPAQUEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    FIRMAFAME: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FRACCIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    FDAINFORMACIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    CODIGOSCAC: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPORDENCOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    MOSTRARVALACT: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEPSPORCLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEPSPORFRACCION: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEPSPORDESCRIPCION: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEPSPORFRACCALTERNA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VENTQUEUEACT: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALFACTTC: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    COLCANTPORPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ENVIADOPORVENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    PROVEEDOREXPORTADOR: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    CANTLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SOLICITARPSWDACTUAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    SOLICITARPSWDDESACTUAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    PACKINGORDENVENTA: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRPO: Mapped[Optional[int]] = mapped_column(Integer)
    PACKINGPEDCLAVE: Mapped[Optional[int]] = mapped_column(Integer)
    GENERAFACTURAIMD: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    GENERAFACTURAIMDENBASEA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SOLICITARCONTRASENAADMINISTRADOR: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRLOTE: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRNUMENTRADA: Mapped[Optional[int]] = mapped_column(Integer)


class QSisExpoRep(Base):
    __tablename__ = 'QSisExpoRep'
    __table_args__ = (
        PrimaryKeyConstraint('TIPOFACTURA', name='SExRep_PKTipoFactura'),
    )

    TIPOFACTURA: Mapped[str] = mapped_column(String(6, 'Modern_Spanish_CI_AS'), primary_key=True)
    PREFIJOEXPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOEXPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CODIGOBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTPNCODBAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DTACEROCODBAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    CBARRASVALOR: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FRACCIONEXP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    FIRMAFAME: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FRACCIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    CODIGOSCAC: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPORDENCOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    MOSTRARVALACT: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEPSPORCLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEPSPORFRACCION: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEPSPORDESCRIPCION: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VENTQUEUEACT: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALFACTTC: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ENVIADOPORVENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    PROVEEDOREXPORTADOR: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    CANTLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SOLICITARPSWDACTUAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    SOLICITARPSWDDESACTUAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    PACKINGORDENVENTA: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRPO: Mapped[Optional[int]] = mapped_column(Integer)
    FDAINFORMACIONAME: Mapped[Optional[int]] = mapped_column(Integer)
    PACKINGPEDCLAVE: Mapped[Optional[int]] = mapped_column(Integer)
    SOLICITARCONTRASENAADMINISTRADOR: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRLOTE: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRNUMENTRADA: Mapped[Optional[int]] = mapped_column(Integer)


class QSisGen(Base):
    __tablename__ = 'QSisGen'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SisGen_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    DTA: Mapped[Optional[int]] = mapped_column(Integer)
    DTAEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PATHARCH: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    PATHARCHTRANSMISION: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    PATHRESPUESTA: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    PATHARCHPED: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHARCHPEDCONSM: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHGENIMPOTEMP: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHGENEXPO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    APLICAPERMAT: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACTSEGURIDAD: Mapped[Optional[int]] = mapped_column(TINYINT)
    CONTROLDES: Mapped[Optional[int]] = mapped_column(TINYINT)
    DIADESACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    FECHADES: Mapped[Optional[int]] = mapped_column(Integer)
    UBIPLANTA: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    DATOSHISTORICOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOVENRO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CANTVENRO: Mapped[Optional[int]] = mapped_column(Integer)
    OMITIRIMPOSUBPCODBARRAS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MUESTRAARCHCODBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALVALBASETCPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALVALBASETCPEDEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    FACTORIVA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 4))
    FILTROCANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    FIRMAPACKING: Mapped[Optional[int]] = mapped_column(TINYINT)
    ESCONDAAMEXPACKING: Mapped[Optional[int]] = mapped_column(TINYINT)
    ADVERTENCIATM: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALCDEPRECIACION: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    VALMANIFUSADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALIDADECENCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    MOSTRARADVERTENCIARO: Mapped[Optional[int]] = mapped_column(TINYINT)
    USARTRANSPAMEDOCAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTVSCANTSERIES: Mapped[Optional[int]] = mapped_column(TINYINT)
    COVEFECHAEMISION: Mapped[Optional[int]] = mapped_column(TINYINT)
    INTERFACEAACONSOLIDADA: Mapped[Optional[int]] = mapped_column(TINYINT)
    INTERFACEAATCFPFF: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    INCLUIROBSCOVEOBSIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    AGREGARINCREIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    REPDESCARGOLINEAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    IDENTIFICADORNODOSERIECOVE: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACTPDFREPORTES: Mapped[Optional[int]] = mapped_column(TINYINT)
    PATHARCHPDFIMPO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHARCHPDFEXPO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    MENSAJESVURFC: Mapped[Optional[int]] = mapped_column(Integer)
    MOSTRARPACKINGLISTINGLES: Mapped[Optional[int]] = mapped_column(Integer)
    ENVIARSUBPARTIDASCOVE: Mapped[Optional[int]] = mapped_column(Integer)
    RESTRINGEPAISIMPO: Mapped[Optional[int]] = mapped_column(Integer)
    RESTRINGEPAISEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARFECHAPAGOPEDDEUNDIAANTERIOR: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARTITULOSALTERNATIVOSIMPRESIONFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    USARTCDELAFECHAPAGOPEDIMPOENDESCARGA: Mapped[Optional[int]] = mapped_column(Integer)
    USARVUDE128O256: Mapped[Optional[int]] = mapped_column(Integer)
    AGREGARNUMEROEMBARQUE: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARUMDEEXISTENCIAENTRANSMISIONVU: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARCODIGODEBROKERDECLIENTEENMAINX30: Mapped[Optional[int]] = mapped_column(Integer)
    HOJACALCULOSEPARARINCREMENTABLESANEXO3: Mapped[Optional[int]] = mapped_column(Integer)
    HOJACALCULODESGLOSEFACTURAANEXO3: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARNOMBREGENERICOMAINX30: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARTCRESPECTOATIPOPED: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARSOLOPARTESNAFTAENCO: Mapped[Optional[int]] = mapped_column(Integer)
    CAMBIARPESOSPORCOSTOUNITARIO: Mapped[Optional[int]] = mapped_column(Integer)
    BLOQUEODEEDICIONDEFACTURAS: Mapped[Optional[int]] = mapped_column(Integer)
    CALCULARCOSTOUNITARIOENBASEAVALORTOTALSCAF: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPRESIONFACTURAALTERNA: Mapped[Optional[int]] = mapped_column(TINYINT)
    TRANSMITIRFACALTERNA: Mapped[Optional[int]] = mapped_column(TINYINT)


class QSisImpo(Base):
    __tablename__ = 'QSisImpo'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SisImp_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PREFIJOIMPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FIRMAFAME: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    CODIGOBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONIMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPORDENCOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    GENERARASSETTAG: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CONTROLREMESA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    REMESAINICIO: Mapped[Optional[int]] = mapped_column(SmallInteger)
    REMESAFINAL: Mapped[Optional[int]] = mapped_column(SmallInteger)
    PERPAGRENGLON: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    NUMPARTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ACTUALIZARPARTEPARTIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    PACKINGORDENCOMPRA: Mapped[Optional[int]] = mapped_column(Integer)
    SOLICITARCONTRASENAADMINISTRADOR: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRLOTE: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRNUMENTRADA: Mapped[Optional[int]] = mapped_column(Integer)


class QSisImpoRep(Base):
    __tablename__ = 'QSisImpoRep'
    __table_args__ = (
        PrimaryKeyConstraint('TIPOFACTURA', name='SImRep_PKTipoFactura'),
    )

    TIPOFACTURA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    CONSECUTIVO: Mapped[Optional[int]] = mapped_column(Integer)
    PREFIJOIMPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FIRMAFAME: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    CODIGOBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONIMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPORDENCOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    GENERARASSETTAG: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOMN: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    TIPOME: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CONTROLREMESA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    REMESAINICIO: Mapped[Optional[int]] = mapped_column(SmallInteger)
    REMESAFINAL: Mapped[Optional[int]] = mapped_column(SmallInteger)
    PERPAGRENGLON: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VENTQUEUEACT: Mapped[Optional[int]] = mapped_column(TINYINT)
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    NUMPARTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PACKINGORDENCOMPRA: Mapped[Optional[int]] = mapped_column(Integer)
    SOLICITARCONTRASENAADMINISTRADOR: Mapped[Optional[int]] = mapped_column(Integer)


class QTipoActFijo(Base):
    __tablename__ = 'QTipoActFijo'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='TipAct_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(256, 'Modern_Spanish_CI_AS'))


class QTiposFactura(Base):
    __tablename__ = 'QTiposFactura'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='QTFACT_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    OBSERVACION: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))


class SAceesos(Base):
    __tablename__ = 'SAceesos'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SAC_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FECHAENTRADA: Mapped[Optional[int]] = mapped_column(Integer)
    FECHASALIDA: Mapped[Optional[int]] = mapped_column(Integer)
    HORAENTRADA: Mapped[Optional[int]] = mapped_column(Integer)
    HORASALIDA: Mapped[Optional[int]] = mapped_column(Integer)
    NOMBRECOMPUTADORA: Mapped[Optional[str]] = mapped_column(CHAR(200, 'Modern_Spanish_CI_AS'))
    DIRECCIONIP: Mapped[Optional[str]] = mapped_column(CHAR(30, 'Modern_Spanish_CI_AS'))


class SBOMVer(Base):
    __tablename__ = 'SBOMVer'
    __table_args__ = (
        PrimaryKeyConstraint('NUMPARTE', 'VERSION', name='BOMVer_PKNumParteVer'),
    )

    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    VERSION: Mapped[int] = mapped_column(Integer, primary_key=True)
    FECHAMODIFICA: Mapped[Optional[int]] = mapped_column(Integer)


class SBackFlashPL(Base):
    __tablename__ = 'SBackFlashPL'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SBaF'),
        Index('SBaF_PackingNP', 'PACKINGLIST', 'NUMPARTE')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PACKINGLIST: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))


class SCTM(Base):
    __tablename__ = 'SCTM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SCTM_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FOLIO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FECHAINICIO: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAEXPEDICION: Mapped[Optional[int]] = mapped_column(Integer)
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))


class SClasePermiso(Base):
    __tablename__ = 'SClasePermiso'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'CLASE', name='ClaSEC_PKConsecClase'),
        Index('ClaSEC_AKClaseFecha', 'CLASE', 'FECHA')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    CLASE: Mapped[str] = mapped_column(String(9, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMOFICIO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    LINEA: Mapped[Optional[int]] = mapped_column(Integer)
    PAGINARENGLON: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))


class SClases(Base):
    __tablename__ = 'SClases'
    __table_args__ = (
        PrimaryKeyConstraint('CLASE', name='ClaMat_PKClase'),
    )

    CLASE: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    TIPOMAT: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    UMEXISTENCIA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FRACCION: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCIONAME: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    MATERIALPPAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    CLAVESUB: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    REVFISICA: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONEXENTAIVA: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANAUSA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class SComprasMexID(Base):
    __tablename__ = 'SComprasMexID'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='ComFid_PKConsecutivo'),
        Index('ComFid_FKFactCMID', 'FACCMIMPODEF', unique=True),
        Index('ComFid_FKPedIDRemesa', 'PEDIMENTOIMPODEF', 'REMESA'),
        Index('ComFid_FKPedimento', 'PEDIMENTOIMPODEF')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PED_PENDIENTE_ASIGNAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEDIMENTOIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOR1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOK1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FACCMIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOCAMBIOMM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    PROVDECR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESTATUSREC: Mapped[Optional[int]] = mapped_column(TINYINT)
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FACTORIVA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 4))
    INCREMENTOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FLETES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOFACTURA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CUALTIPOCAMBIO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FECHAEMISION: Mapped[Optional[int]] = mapped_column(Integer)
    SELLOVALOR2500: Mapped[Optional[int]] = mapped_column(TINYINT)
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    TOTALINCREMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    ESAGRANEL: Mapped[Optional[int]] = mapped_column(TINYINT)
    FACTORPESO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    FACTURAALTERNA: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    TIPOMOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    DESTINO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    GENERARSALDOS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    COMENTARIOSESTATUS: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESDUENOMCIA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IDRELDOC: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFIRMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    COMOFUEPROCESADA: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    FUEREVISADAMCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    OBSERVACIONESVU: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    ORIGENUBICACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    DESTINOUBICACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    ITINERARIOTRANPORTE: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NUMEROCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    CONTENEDORESTIPO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DATOSVEHICULO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMERONIU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CANTGUIASEMBARQUE: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    ADENDAVU: Mapped[Optional[str]] = mapped_column(String(204, 'Modern_Spanish_CI_AS'))
    ESFERROCARRIL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESTINOORIGENCOVE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    PUERTOENTRADA: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    MODOCONTINGENCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    RECINTO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    SEMAFOROIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPODEGUIAAIDENTIFICAR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    CLAVEDOT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SUBDIVISION: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FUNGECOMOCO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    APENDICE17: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMOV: Mapped[Optional[str]] = mapped_column(String(31, 'Modern_Spanish_CI_AS'))
    IDFERRORCARRIL: Mapped[Optional[str]] = mapped_column(String(31, 'Modern_Spanish_CI_AS'))


class SConfigFTP(Base):
    __tablename__ = 'SConfigFTP'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SCoFTP_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    SERVIDOR_FTP: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    USUARIO_FTP: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CLAVEACCESSO_FTP: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    DIRECTORIO_FTP: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    FOLDER_LLEGADA_FTP: Mapped[Optional[str]] = mapped_column(String(1999, 'Modern_Spanish_CI_AS'))
    FOLDER_HISTORICO_LOCAL: Mapped[Optional[str]] = mapped_column(String(1999, 'Modern_Spanish_CI_AS'))
    PUERTO: Mapped[Optional[int]] = mapped_column(Integer)
    FTPTRANSBINARIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFACTURA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CONSOLIDAFACTURA: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))


class SConfiguracion(Base):
    __tablename__ = 'SConfiguracion'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='Config_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    TIPODEFONDOS: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ACTIMPLEMENTACION: Mapped[Optional[int]] = mapped_column(TINYINT)
    ALTAUSUARIOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESPALDO: Mapped[Optional[int]] = mapped_column(TINYINT)
    FOLDER_LLEGADA: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    ACTIVAR_BUSQUEDA: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    INTERVALO_BUSQUEDA: Mapped[Optional[int]] = mapped_column(Integer)
    FTP_SERVER: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FTP_USERNAME: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FTP_PASSWORD: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FTP_DIRECTORY: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    TIPOACTUALIZACION: Mapped[Optional[str]] = mapped_column(CHAR(20, 'Modern_Spanish_CI_AS'))
    DIRECCTORIOMANUALSIFRA: Mapped[Optional[str]] = mapped_column(String(199, 'Modern_Spanish_CI_AS'))
    DIRECCIONHTTP: Mapped[Optional[str]] = mapped_column(CHAR(200, 'Modern_Spanish_CI_AS'))
    FTP_FOLDER_LLEGADA: Mapped[Optional[str]] = mapped_column(String(1999, 'Modern_Spanish_CI_AS'))
    FECHAACTUALIZACION: Mapped[Optional[int]] = mapped_column(Integer)
    RUTASERVIDOR: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))


class SDescargaCTM(Base):
    __tablename__ = 'SDescargaCTM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='DesRec_PKConsecutivo'),
        Index('DesRec_FKFactRecParte', 'FACTRECIBO', 'NUMPARTE'),
        Index('DesRec_FKREPaLin', 'FACTRECIBO', 'FACTENVIO', 'NUMPARTE', 'LINEA', unique=True),
        Index('FKFACENVPARTE', 'FACTENVIO', 'NUMPARTE')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTRECIBO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FACTENVIO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTDESC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FECHAENT: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTEEXPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    LINEA: Mapped[Optional[int]] = mapped_column(Integer)


class SDescargaD(Base):
    __tablename__ = 'SDescargaD'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='DesDef_PKConsecutivo'),
        Index('DesDef_FKClase', 'CLASE'),
        Index('DesDef_FKEIPaPiTiSeOrRefLin', 'FACTEXPO', 'FACTIMPODEF', 'NUMPARTE', 'PAISMERCANCIA', 'TIPOFRACCION', 'SECTOR', 'PARTEORIGINAL', 'FACREFERENCIA', 'LINEAEXPO'),
        Index('DesDef_FKFacImpClase', 'FACTIMPODEF', 'CLASE'),
        Index('DesDef_FKFacImpParte', 'FACTIMPODEF', 'NUMPARTE'),
        Index('DesDef_FKFactExpo', 'FACTEXPO'),
        Index('DesDef_FKFactImpo', 'FACTIMPODEF'),
        Index('DesDef_FKFactReferencia', 'FACREFERENCIA'),
        Index('DesDef_FKFecha', 'FECHADESC'),
        Index('DesDef_FKImpParPaiTipSec', 'FACTIMPODEF', 'NUMPARTE', 'PAISMERCANCIA', 'TIPOFRACCION', 'SECTOR'),
        Index('DesDef_FKOrdVentaParte', 'ORDENVENTA', 'NUMPARTE'),
        Index('DesDef_FKParte', 'NUMPARTE'),
        Index('DesDef_FKPedExpo', 'PEDIMENTOEXPO'),
        Index('DesDef_FKPedImpoFecha', 'PEDIMENTOIMPODEF', 'FECHADESC')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTEXPO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FACREFERENCIA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FACTIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTDESC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PAISMERCANCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FECHADESC: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    ADVALOREMIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    NUMPARTEEXPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    LINEAEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    PARTEORIGINAL: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    TIPODESC: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    MONTOIGI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    TIENECERT: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ORDENVENTA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ACTUALREPARACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    TIPOMATEXPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    CONSECPARCIAL: Mapped[Optional[int]] = mapped_column(Integer)
    LINEAEXPOREF: Mapped[Optional[int]] = mapped_column(Integer)
    APARTADOCTM: Mapped[Optional[str]] = mapped_column(CHAR(3, 'Modern_Spanish_CI_AS'))
    PORUTILERIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCARGASM: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))


class SDescargaM(Base):
    __tablename__ = 'SDescargaM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='DesMan_PKConsecutivo'),
        Index('DesMan_FKConsExpoLinea', 'CONSECUTIVOEXPO', 'LINEA'),
        Index('DesMan_FKExImPrPiTiSe', 'CONSECUTIVOEXPO', 'FACTURA', 'NUMPARTE', 'PAIS', 'TIPOFRACCION', 'SECTOR')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    CONSECUTIVOEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEA: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTEMP: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FACTURADEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PROCEDENCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FACTURA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TIPODESPERDICIO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ORDENVENTA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    TOMARSALDOBASEALPT: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))


class SDescargaMerDes(Base):
    __tablename__ = 'SDescargaMerDes'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='DesMeDe_PKConsecutivo'),
        Index('DesMeDe_FKFacSCProTipParLin', 'FACTEXPOSCRAP', 'FACTURAEXPO', 'PROCEDENCIA', 'TIPO', 'NUMPARTE', 'NUMPARTEPAREXPO', 'LINEAEXPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    PEDIMENTOEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTEPAREXPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    FACTEXPOSCRAP: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOEXPOSCRAP: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTDESC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    FECHADESC: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTEEXPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    LINEAEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    PROCEDENCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class SDescargaR(Base):
    __tablename__ = 'SDescargaR'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVOEXPO', 'LINEA', name='DesRep_PKConsecLinea'),
    )

    CONSECUTIVOEXPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    NUMPARTEMP: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROCEDENCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CANTEQUIVALENTE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMEQUIVALENTE: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    LINEAEXPO: Mapped[Optional[int]] = mapped_column(Integer)


class SDescargaS(Base):
    __tablename__ = 'SDescargaS'
    __table_args__ = (
        PrimaryKeyConstraint('FACTEXPO', 'FACTURAEXPO', 'NUMPARTE', 'TIPO', name='DesScr_PKOrigExpoParteTipo'),
    )

    FACTEXPO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    FACTURAEXPO: Mapped[str] = mapped_column(String(19, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPO: Mapped[str] = mapped_column(String(1, 'Modern_Spanish_CI_AS'), primary_key=True)
    CANTDESC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))


class SDescargaSM(Base):
    __tablename__ = 'SDescargaSM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='DesEnt_PKConsecutivo'),
        Index('DesEnt_FKEIPaLin', 'REMISIONENTRADA', 'REMISIONSALIDA', 'NUMPARTE', 'LINEA', unique=True),
        Index('DesEnt_FKRemEntradaParte', 'REMISIONENTRADA', 'NUMPARTE'),
        Index('FKREMSALPARTE', 'REMISIONSALIDA', 'NUMPARTE')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    REMISIONENTRADA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMISIONSALIDA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTDESC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FECHAENT: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTEEXPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    LINEA: Mapped[Optional[int]] = mapped_column(Integer)


class SDescargaT(Base):
    __tablename__ = 'SDescargaT'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='DesTem_PKConsecutivo'),
        Index('DesTem_FKClase', 'CLASE'),
        Index('DesTem_FKEIPaPiTiSeOrRefLin', 'FACTEXPO', 'FACTIMPO', 'NUMPARTE', 'PAISMERCANCIA', 'TIPOFRACCION', 'SECTOR', 'PARTEORIGINAL', 'FACREFERENCIA', 'LINEAEXPO'),
        Index('DesTem_FKFacImpClase', 'FACTIMPO', 'CLASE'),
        Index('DesTem_FKFacImpParte', 'FACTIMPO', 'NUMPARTE'),
        Index('DesTem_FKFactExpo', 'FACTEXPO'),
        Index('DesTem_FKFactImpo', 'FACTIMPO'),
        Index('DesTem_FKFactReferencia', 'FACREFERENCIA'),
        Index('DesTem_FKFecha', 'FECHADESC'),
        Index('DesTem_FKImpParPaiTipSec', 'FACTIMPO', 'NUMPARTE', 'PAISMERCANCIA', 'TIPOFRACCION', 'SECTOR'),
        Index('DesTem_FKOrdVentaParte', 'ORDENVENTA', 'NUMPARTE'),
        Index('DesTem_FKParte', 'NUMPARTE'),
        Index('DesTem_FKPedExpo', 'PEDIMENTOEXPO'),
        Index('DesTem_FKPedImpoFecha', 'PEDIMENTOIMPO', 'FECHADESC')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTEXPO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FACREFERENCIA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FACTIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTDESC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PAISMERCANCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FECHADESC: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOFRACCION: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    ADVALOREMIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMPARTEEXPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    LINEAEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    PARTEORIGINAL: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    TIPODESC: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    MONTOIGI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    TIENECERT: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ORDENVENTA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ACTUALREPARACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    TIPOMATEXPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    CONSECPARCIAL: Mapped[Optional[int]] = mapped_column(Integer)
    LINEAEXPOREF: Mapped[Optional[int]] = mapped_column(Integer)
    APARTADOCTM: Mapped[Optional[str]] = mapped_column(CHAR(3, 'Modern_Spanish_CI_AS'))
    PORUTILERIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCARGASM: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    CANTIDADRETORNADASM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))


class SFacEntradaSM(Base):
    __tablename__ = 'SFacEntradaSM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='EntMaq_PKConsecutivo'),
        Index('EntMaq_FKFacturaRemision', 'FACTURAREMISION', unique=True)
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAREMISION: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAENTRADA: Mapped[Optional[int]] = mapped_column(Integer)
    ENVIADOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    VALORENTMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORENTME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SEM: Mapped[Optional[int]] = mapped_column(Integer)


class SFacEnviaCTM(Base):
    __tablename__ = 'SFacEnviaCTM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='FacEnv_PKConsecutivo'),
        Index('FacEnv_FKFacturaEnvio', 'FACTURAENVIO', unique=True)
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAENVIO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAENVIO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMVEHICULO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ENVIADOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))


class SFacExp(Base):
    __tablename__ = 'SFacExp'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='MatFex_PKConsecutivo'),
        Index('MatFex_FKFacProforma', 'NUMEROPROFORMA'),
        Index('MatFex_FKFacturaExpo', 'FACTURAEXPO', unique=True),
        Index('MatFex_FKManFacExp', 'MANIFIESTO', 'FACTURAEXPO'),
        Index('MatFex_FKPedExpRem', 'PEDIMENTOEXPO', 'REMESA'),
        Index('MatFex_FKPedimento', 'PEDIMENTOEXPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PED_PENDIENTE_ASIGNAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEDIMENTOEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOR1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOK1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    MANIFIESTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESTATUSREC: Mapped[Optional[int]] = mapped_column(TINYINT)
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    VALOREXPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMPMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORAGREMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAEXPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORVMEXMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALEMPAQUENACMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALOREXPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMPME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORAGREME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAEXPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORVMEXME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALEMPAQUENACME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FACTORIVA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 4))
    CANTEXPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTAAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTECOMPLE: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    COMPLEMENTO1: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    IDENTIFICADOR2: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    COMPLEMENTO2: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOFACTURA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    GENERAID: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ACTVALOR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    BILLNUMBER: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    APLICADESCMANUAL: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    DESTINOMCIA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FECHAPAGO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMRECIBOPAGO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    VALORIMPUESTOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPODESPERDICIO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ESCAMBIOREGIMEN: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CUALTIPOCAMBIO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TOTALINCREMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ESTATUSREP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    DESCARGASUST: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCARGACLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCARGADEF: Mapped[Optional[int]] = mapped_column(TINYINT)
    ESAGRANEL: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMEROPROFORMA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMEROGUIA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NUMEMBARQUE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    RECIBIDOPOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FECHAENTREGA: Mapped[Optional[int]] = mapped_column(Integer)
    ENTREGADO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ENVIADOPORVENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    NUMREFERENCIA: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    OFICIO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOMOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    FACTURAALTERNA: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    COMENTARIOSESTATUS: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    SEMAFORO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    NUMPROYECTO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOSCRAP: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NUMFACTURABROKER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHAFACBROKER: Mapped[Optional[int]] = mapped_column(Integer)
    IDRELDOC: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFIRMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    GENDESCPARTIDAS: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    COMOFUEPROCESADA: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    FACTURAEXPOREF: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PROVEEDOREXPORTADOR: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIOMM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    VALOREXPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORAGREMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAEXPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALEMPAQUENACMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORVMEXMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    OBSERVACIONESVU: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    ORIGENUBICACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    DESTINOUBICACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    ITINERARIOTRANPORTE: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    SETRATAPROCESOCTM: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NUMEROCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    CONTENEDORESTIPO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DATOSVEHICULO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMERONIU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CANTGUIASEMBARQUE: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    ADENDAVU: Mapped[Optional[str]] = mapped_column(String(204, 'Modern_Spanish_CI_AS'))
    ESFERROCARRIL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESTINOORIGENCOVE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FECHAEMISION: Mapped[Optional[int]] = mapped_column(Integer)
    MODOCONTINGENCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    RAZONEXPORTACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TERMINOSPAGO: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    MANIOBRAS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    RECINTO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    SEMAFOROEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    OPCIONIV18: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPODEGUIAAIDENTIFICAR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    CFDIUUID: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CFDIPATHPDF: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CFDIPATHXML: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CLAVEDOT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SUBDIVISION: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FUNGECOMOCO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ENAJENACIONBIENES: Mapped[Optional[int]] = mapped_column(TINYINT)
    APENDICE17: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMOV: Mapped[Optional[str]] = mapped_column(String(31, 'Modern_Spanish_CI_AS'))
    IDFERRORCARRIL: Mapped[Optional[str]] = mapped_column(String(31, 'Modern_Spanish_CI_AS'))


class SFacExpCobranza(Base):
    __tablename__ = 'SFacExpCobranza'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='CobExp_PKConsecutivoLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CONCEPTO: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    COBRADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHACOBRANZA: Mapped[Optional[int]] = mapped_column(Integer)
    VALOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    DEPTOCOBRANZA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FACTCOBRADOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NOMBRECOBRADOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class SFacImp(Base):
    __tablename__ = 'SFacImp'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='MatFim_PKConsecutivo'),
        Index('MatFim_FKFacturaImpo', 'FACTURAIMPO', unique=True),
        Index('MatFim_FKPedImpoRem', 'PEDIMENTOIMPO', 'REMESA'),
        Index('MatFim_FKPedimento', 'PEDIMENTOIMPO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PED_PENDIENTE_ASIGNAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEDIMENTOIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOR1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOCAMBIOMM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESTATUSREC: Mapped[Optional[int]] = mapped_column(TINYINT)
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CANTIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CUALTIPOCAMBIO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FECHAEMISION: Mapped[Optional[int]] = mapped_column(Integer)
    SELLOVALOR2500: Mapped[Optional[int]] = mapped_column(TINYINT)
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TOTALINCREMME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    ESAGRANEL: Mapped[Optional[int]] = mapped_column(TINYINT)
    FACTORPESO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    FACTURAALTERNA: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    TIPOMOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(34, 'Modern_Spanish_CI_AS'))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    NUMTRAILER: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    DESTINO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    GENERARSALDOS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    COMENTARIOSESTATUS: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESDUENOMCIA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IDRELDOC: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFIRMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    COMOFUEPROCESADA: Mapped[Optional[str]] = mapped_column(String(300, 'Modern_Spanish_CI_AS'))
    FUEREVISADAMCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMOPERACIONVU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    OBSERVACIONESVU: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    ORIGENUBICACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    DESTINOUBICACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    ITINERARIOTRANPORTE: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    NUMEROCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(99, 'Modern_Spanish_CI_AS'))
    CONTENEDORESTIPO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DATOSVEHICULO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    NUMERONIU: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CANTGUIASEMBARQUE: Mapped[Optional[str]] = mapped_column(String(12, 'Modern_Spanish_CI_AS'))
    ADENDAVU: Mapped[Optional[str]] = mapped_column(String(204, 'Modern_Spanish_CI_AS'))
    ESFERROCARRIL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESTINOORIGENCOVE: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    PUERTOENTRADA: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    MODOCONTINGENCIA: Mapped[Optional[int]] = mapped_column(TINYINT)
    RECINTO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PEDIMENTOK1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FACTORIVA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    VALORIVAMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SEMAFOROIMPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPODEGUIAAIDENTIFICAR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CLAVEDOT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    SUBDIVISION: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FUNGECOMOCO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    APENDICE17: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMOV: Mapped[Optional[str]] = mapped_column(String(31, 'Modern_Spanish_CI_AS'))
    IDFERRORCARRIL: Mapped[Optional[str]] = mapped_column(String(31, 'Modern_Spanish_CI_AS'))


class SFacImpCobranza(Base):
    __tablename__ = 'SFacImpCobranza'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='CobImpT_PKConsecutivoLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CONCEPTO: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    COBRADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHACOBRANZA: Mapped[Optional[int]] = mapped_column(Integer)
    VALOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    DEPTOCOBRANZA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FACTCOBRADOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    NOMBRECOBRADOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class SFacOrdenVenta(Base):
    __tablename__ = 'SFacOrdenVenta'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='FacOrd_PKConsecLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ORDENVENTA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    COLORES: Mapped[Optional[str]] = mapped_column(String(49, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    COLORCUADRITO: Mapped[Optional[str]] = mapped_column(CHAR(1, 'Modern_Spanish_CI_AS'))


class SFacReciboCTM(Base):
    __tablename__ = 'SFacReciboCTM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='FacRec_PKConsecutivo'),
        Index('FacRec_FKFacturaEnvio', 'FACTURARECIBO', unique=True)
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURARECIBO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHARECIBO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMVEHICULO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ENVIADOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))


class SFacRep(Base):
    __tablename__ = 'SFacRep'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAIMPO', name='FacRep_PKFacturaImpo'),
        Index('FacRep_FKAAduanal', 'AADUANAL'),
        Index('FacRep_FKEnviado', 'ENVIADOA'),
        Index('FacRep_FKEstatus', 'ESTATUS'),
        Index('FacRep_FKFechaFact', 'FECHAFACTURA'),
        Index('FacRep_FKIncoterm', 'INCOTERM'),
        Index('FacRep_FKModTrans', 'MODTRANS'),
        Index('FacRep_FKPedImpoRem', 'PEDIMENTOIMPO', 'REMESA'),
        Index('FacRep_FKPedimento', 'PEDIMENTOIMPO'),
        Index('FacRep_FKProveedor', 'PROVEEDOR'),
        Index('FacRep_FKSubEmpresa', 'SUBEMPRESA'),
        Index('FacRep_FKTipoDoc', 'TIPODOC'),
        Index('FacRep_FKTransCond', 'TRANSPORTISTA', 'CONDUCTOR'),
        Index('FacRep_FKTransportista', 'TRANSPORTISTA'),
        Index('FacRep_FKVendido', 'VENDIDOA')
    )

    FACTURAIMPO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    PED_PENDIENTE_ASIGNAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PEDIMENTOIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PEDIMENTOR1: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[int]] = mapped_column(SmallInteger)
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOCAMBIOMM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPODOC: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESTATUSREC: Mapped[Optional[int]] = mapped_column(TINYINT)
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CANTIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRASPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PRECINTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 0))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    MODTRANS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CUALTIPOCAMBIO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    IDRELDOC: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEFIRMA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SEMAFOROEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class SFacSalidaSM(Base):
    __tablename__ = 'SFacSalidaSM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SalMaq_PKConsecutivo'),
        Index('SalMaq_FKFacturaSalida', 'FACTURASALIDA', unique=True)
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURASALIDA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAENVIO: Mapped[Optional[int]] = mapped_column(Integer)
    ENVIADOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    VALORSALMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORSALME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    USUARIOACT: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    USUARIOCAP: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FECHACAPTURA: Mapped[Optional[int]] = mapped_column(Integer)
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SEM: Mapped[Optional[int]] = mapped_column(Integer)


class SFracAmeFact(Base):
    __tablename__ = 'SFracAmeFact'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='FraFac_PKConsecutivo'),
        Index('FraFac_AKConsExpoLineaTV', 'CONSECUTIVOEXPO', 'LINEA', 'TIPOVALOR'),
        Index('FraFac_FKConsExpoLineas', 'CONSECUTIVOEXPO', 'LINEA', 'LINEAPARTE')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    CONSECUTIVOEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    LINEA: Mapped[Optional[int]] = mapped_column(Integer)
    LINEAPARTE: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    FRACCIONAME: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    TASA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPOVALOR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOADVALOREM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PREFIJO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    AR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    OH: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))


class SFracAmeParte(Base):
    __tablename__ = 'SFracAmeParte'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='FraPar_PKConsecutivo'),
        Index('FKPARTEFRACPAIS', 'NUMPARTE', 'FRACCIONAME', 'PAIS'),
        Index('FKPARTEFRACTIPO', 'NUMPARTE', 'FRACCIONAME', 'TIPOVALOR'),
        Index('FraPar_FKParte', 'NUMPARTE'),
        Index('FraPar_FKParteConsec', 'NUMPARTE', 'CONSECUTIVO', unique=True)
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    FRACCIONAME: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    VALOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPOVALOR: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PREFIJO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANASIFRA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    AR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    OH: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))


t_SFraccionesAnterioresN = Table(
    'SFraccionesAnterioresN', Base.metadata,
    Column('SysID', Integer),
    Column('FraccionActual', String(50, 'Modern_Spanish_CI_AS')),
    Column('FraccionAnterior', String(50, 'Modern_Spanish_CI_AS'))
)


t_SIdentificadoresPedimento = Table(
    'SIdentificadoresPedimento', Base.metadata,
    Column('PEDIMENTO', String(19, 'Modern_Spanish_CI_AS')),
    Column('CLAVEID', String(2, 'Modern_Spanish_CI_AS')),
    Column('COMPLEMENTO1', String(5000, 'Modern_Spanish_CI_AS')),
    Column('COMPLEMENTO2', String(5000, 'Modern_Spanish_CI_AS')),
    Column('COMPLEMENTO3', String(5000, 'Modern_Spanish_CI_AS')),
    Index('SIdP_PedID', 'PEDIMENTO', 'CLAVEID', unique=True)
)


class SImplosion(Base):
    __tablename__ = 'SImplosion'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='ImpFac_PKConsecutivo'),
        Index('ImpFac_FolioImplosion', 'FOLIOIMPLOSION', unique=True)
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FOLIOIMPLOSION: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAIMPOSION: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOCAMBIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CANTIMPLO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANT_PARTIDAS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FECHAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    HORAACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOPESO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOFRACIMPO: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROCEDENCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class SLocalizacion(Base):
    __tablename__ = 'SLocalizacion'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='SLOCMP_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))


class SMatBOM(Base):
    __tablename__ = 'SMatBOM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='MatBOM_PKConsecutivo'),
        Index('MatBOM_FKNumParteConsec', 'NUMPARTE', 'CONSECUTIVO', unique=True),
        Index('MatBOM_FKNumParteParteBOM', 'NUMPARTE', 'NUMPARTEBOM'),
        Index('MatBOM_FKParteBOM', 'NUMPARTEBOM')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    NUMPARTEBOM: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROCEDENCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CANTMP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTDESP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTMERMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEQUIVALENTE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMEQUIVALENTE: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTDESPEQUI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTMERMAEQUI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCDESPAPARTADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    PORCENTAJEMP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    PORCENTAJEDESP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    PORCENTAJEMERMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TIPODESPMERMA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class SMatBOMClase(Base):
    __tablename__ = 'SMatBOMClase'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='BomCla_PKConsecutivo'),
        Index('BomCla_FKClase', 'CLASE')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    PORCENTAJE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))


class SMermaDesp(Base):
    __tablename__ = 'SMermaDesp'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAEXPO', 'NUMPARTE', 'TIPO', 'PROCEDENCIA', 'NUMPARTEPAREXPO', name='MerDes_PKExpoParteTipo'),
    )

    FACTURAEXPO: Mapped[str] = mapped_column(String(19, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPO: Mapped[str] = mapped_column(String(1, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTEPAREXPO: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    PROCEDENCIA: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHAEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    PEDIMENTOEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTIDADUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))


class SModificaciones(Base):
    __tablename__ = 'SModificaciones'
    __table_args__ = (
        PrimaryKeyConstraint('LINEA', name='ModDiv_PKLinea'),
        Index('ModDiv_FKCampoRef1', 'CAMPOREF1'),
        Index('ModDiv_FKFechaHora', 'FECHA', 'HORA'),
        Index('ModDiv_FKLogin', 'LOGIN'),
        Index('ModDiv_FKMovR2TablaR1', 'MOVIMIENTO', 'CAMPOREF2', 'TABLA', 'CAMPOREF1'),
        Index('ModDiv_FKMovimiento', 'MOVIMIENTO'),
        Index('ModDiv_FKReferencia2', 'CAMPOREF2'),
        Index('ModDiv_FKTabla', 'TABLA')
    )

    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    MOVIMIENTO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    TABLA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CAMPOREF1: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    CAMPOREF2: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    HORA: Mapped[Optional[int]] = mapped_column(Integer)
    LOGIN: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CLAVE_ACCESO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))


class SPackingList(Base):
    __tablename__ = 'SPackingList'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='XXX_PKConsecutivo'),
        Index('XXX_NumPackingList', 'NUMPACKINGLIST')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMPACKINGLIST: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    EXPORTADOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    EXPORTADOA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    ENVIADOPOR: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    FACTURAREFERENCIA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))


class SParPruSuf(Base):
    __tablename__ = 'SParPruSuf'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAEXPO', 'LINEAEXPO', 'LINEA', name='ParPru_PKFacParLinea'),
    )

    FACTURAEXPO: Mapped[str] = mapped_column(String(19, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAEXPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    ADVALOREM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))

class SParteCliente(Base):
    __tablename__ = 'SParteCliente'
    __table_args__ = (
        PrimaryKeyConstraint('NUMPARTE', 'CLIENTE', name='ParCli_PKParteCliente'),
    )

    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLIENTE: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))


class SPartePais(Base):
    __tablename__ = 'SPartePais'
    __table_args__ = (
        PrimaryKeyConstraint('NUMPARTE', 'FRACCION', 'PAIS', 'TIPOFRACCION', 'SECTOR', name='ParPai_PKPaFrPaTiSec'),
        Index('ParPai_FKNumParte', 'NUMPARTE'),
        Index('ParPai_FKParPaiTipSec', 'NUMPARTE', 'PAIS', 'TIPOFRACCION', 'SECTOR')
    )

    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    FRACCION: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAIS: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOFRACCION: Mapped[str] = mapped_column(String(7, 'Modern_Spanish_CI_AS'), primary_key=True)
    SECTOR: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAISDEFAULT: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISDEFAULTEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAIM: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TASAEX: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIENECERT: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHAFINALCO: Mapped[Optional[int]] = mapped_column(Integer)
    TASAIMNUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TASAEXNUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))

class SPartesSustitutos(Base):
    __tablename__ = 'SPartesSustitutos'
    __table_args__ = (
        PrimaryKeyConstraint('NUMPARTE', 'NUMPARTESUSTITUTO', name='SPaSu_NumParte_NPS'),
    )

    NUMPARTE: Mapped[str] = mapped_column(String(99, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTESUSTITUTO: Mapped[str] = mapped_column(String(99, 'Modern_Spanish_CI_AS'), primary_key=True)
    FACTORCONVERSION: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 6))
    UNIDADMEDIDA1: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    UNIDADMEDIDA2: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))


class SPartidasCM(Base):
    __tablename__ = 'SPartidasCM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEACMIMPDEF', name='ParCom_PKConsecLineaCM'),
        Index('ParCom_FKNumParte', 'NUMPARTE'),
        Index('ParCom_FKParPaiTipSecCons', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACCIMPO', 'SECTOR', 'CONSECUTIVO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEACMIMPDEF: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACCMIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTALTERNA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMEDALTERNA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(4999, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONI: Mapped[Optional[str]] = mapped_column(String(4999, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    DESCBULTOS: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCIMPO: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    ADVIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ADVIMPONUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TIENECO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    ADVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    INFOADICIONESP: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    INFOADICIONING: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    MONTOIGI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    NUMEROGUIA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CANTIMPOAUXILIAR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMEDAUXILIAR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUAUXILIARME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOAUXILIARME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CLIENTEFACTURAR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONROCTAVA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PERMISOROCTAVA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    BODEGA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    REQUISITOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    LINEARO: Mapped[Optional[int]] = mapped_column(Integer)
    ADVALORMELINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ADVALORMNLINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PERMISOSPED: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    LINEAPED: Mapped[Optional[int]] = mapped_column(Integer)
    CAMPOCOMODIN: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    ESMCIAMILITAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONPARTE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CANTIMPOUMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEUMA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    NUMPARTECOM: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    NOCAJAS: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    VALIDACIONZERO: Mapped[Optional[int]] = mapped_column(Integer)
    VALIDACIONUNO: Mapped[Optional[int]] = mapped_column(Integer)
    METVALORVALORDETERMINADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    METVALORMOTIVODEUSO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CLIENTEASIGNADO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMERODEENTRADA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    LOTE: Mapped[Optional[str]] = mapped_column(String(254, 'Modern_Spanish_CI_AS'))


class SPartidasEntradaSM(Base):
    __tablename__ = 'SPartidasEntradaSM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAREMISION', name='EntPSM_PKConsecLinea'),
        Index('EntPSM_FKFacLineaSalida', 'FACTURASALIDA', 'LINEASALIDA')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAREMISION: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAREMISION: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FACTURASALIDA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    LINEASALIDA: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTENTRADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORENTMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORENTME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPODENUMPARTE: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPODEORDEN: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CONCEPTODELAPARTIDA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FRACCIONDELAPRENDA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class SPartidasEnviaCTM(Base):
    __tablename__ = 'SPartidasEnviaCTM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAENVIO', name='ParEnv_PKConsecLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAENVIO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTENVIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    MARCA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SERIES: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    VALORAGREMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORAGREME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORAGREMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALEMPAQUENACMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALEMPAQUENACME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALEMPAQUENACMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    ORDENVENTA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))


class SPartidasExpo(Base):
    __tablename__ = 'SPartidasExpo'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='MatPex_PKConsecLinea'),
        Index('MatPex_FKFacLineParte', 'FACTURAEXPO', 'LINEA', 'NUMPARTE'),
        Index('MatPex_FKFacPenParte', 'FACTURASCRAP', 'NUMPARTE'),
        Index('MatPex_FKFactParte', 'FACTURAEXPO', 'NUMPARTE')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTEXPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PAISDESTINO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    DESCBULTOS: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCRIPCIONPARTE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONCLASE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOVENTAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORTOTALME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMPTEMPME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORAGREME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMPDEFME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAEXPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOVENTAMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORTOTALMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMPTEMPMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORAGREMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMPDEFMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAEXPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CANTBULCONT: Mapped[Optional[int]] = mapped_column(SmallInteger)
    DESCCONTENEDOR: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CANTEXISTENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMEDEXISTENCIA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    INFOADICIONESP: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    INFOADICIONING: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    FRACCIONEXPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ADVALOREMEXPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACEXPO: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    VERSIONBILL: Mapped[Optional[int]] = mapped_column(Integer)
    FRACCIONTLCAN: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    ADVTLCAN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    VALORTLCAN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORNOORIGINARIOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORORIGINARIOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    MONTOIGIME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    MONTOEXCENTOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIENECO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FACTURASCRAP: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    CONSECUTIVODES: Mapped[Optional[int]] = mapped_column(Integer)
    COSTOUNICOMERCIAL: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORTOTALCOMERCIAL: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PROCSCRAP: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    VALORAGREMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    PAISOPCIONAL: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    VALEMPAQUENACMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALEMPAQUENACME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALEMPAQUENACMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALEMPAQUEUSME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ADVALORMELINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    ADVALORMNLINEAPED: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PERMISOSPED: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    LINEAPED: Mapped[Optional[int]] = mapped_column(Integer)
    REVISARDESP: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    CANTEXPOUMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEUMA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    VALORTOTALMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMPTEMPMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMPDEFMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAEXPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    APARTADOCTM: Mapped[Optional[str]] = mapped_column(CHAR(3, 'Modern_Spanish_CI_AS'))
    NUMPARTECOM: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    VERSIONBOM: Mapped[Optional[int]] = mapped_column(Integer)
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    METVALORVALORDETERMINADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    METVALORMOTIVODEUSO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    VALIDACIONZERO: Mapped[Optional[int]] = mapped_column(Integer)
    VALIDACIONUNO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMERODEGUIA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CLIENTEASIGNADO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    NUMERODEENTRADA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    LOCALIZACION: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    TOMARCOMOPT: Mapped[Optional[int]] = mapped_column(Integer)
    FRACAMESELEXTRA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    LOTE: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    PALLET2: Mapped[Optional[int]] = mapped_column(SmallInteger)


t_SPartidasImpo = Table(
    'SPartidasImpo', Base.metadata,
    Column('CONSECUTIVO', Integer, nullable=False),
    Column('FACTURAIMPO', String(15, 'Modern_Spanish_CI_AS')),
    Column('LINEAIMPO', Integer, nullable=False),
    Column('FECHAFACTURA', Integer),
    Column('NUMPARTE', String(70, 'Modern_Spanish_CI_AS')),
    Column('CLASE', String(8, 'Modern_Spanish_CI_AS')),
    Column('CANTIMPO', DECIMAL(19, 8)),
    Column('UNIMED', String(5, 'Modern_Spanish_CI_AS')),
    Column('CANTALTERNA', DECIMAL(19, 8)),
    Column('UNIMEDALTERNA', String(5, 'Modern_Spanish_CI_AS')),
    Column('COSTOUNITARIOME', DECIMAL(23, 8)),
    Column('COSTOUNITARIOMN', DECIMAL(23, 8)),
    Column('COSTOUNITARIOMC', DECIMAL(23, 8)),
    Column('VALORIMPOMN', DECIMAL(23, 8)),
    Column('VALORIMPOME', DECIMAL(23, 8)),
    Column('VALORIMPOMC', DECIMAL(23, 8)),
    Column('VALORIVAMN', DECIMAL(23, 8)),
    Column('VALORIVAME', DECIMAL(23, 8)),
    Column('NUMPERMISO', String(20, 'Modern_Spanish_CI_AS')),
    Column('PAGRENGLON', String(10, 'Modern_Spanish_CI_AS')),
    Column('PAISORIGEN', String(3, 'Modern_Spanish_CI_AS')),
    Column('PESONETO', DECIMAL(19, 8)),
    Column('PESONETOKGS', DECIMAL(19, 8)),
    Column('PESONETOLBS', DECIMAL(19, 8)),
    Column('PESOBRUTO', DECIMAL(19, 8)),
    Column('PESOBRUTOKGS', DECIMAL(19, 8)),
    Column('PESOBRUTOLBS', DECIMAL(19, 8)),
    Column('CLAVEBULTOS', String(5, 'Modern_Spanish_CI_AS')),
    Column('CANTBULTOS', Integer),
    Column('DESCBULTOS', String(40, 'Modern_Spanish_CI_AS')),
    Column('FRACCIONIMPO', String(10, 'Modern_Spanish_CI_AS')),
    Column('TIPOFRACCIMPO', String(7, 'Modern_Spanish_CI_AS')),
    Column('ADVIMPO', String(10, 'Modern_Spanish_CI_AS')),
    Column('ADVIMPONUM', DECIMAL(7, 2)),
    Column('TIENECO', String(1, 'Modern_Spanish_CI_AS')),
    Column('NOCERTIFICADO', String(10, 'Modern_Spanish_CI_AS')),
    Column('SECTOR', String(8, 'Modern_Spanish_CI_AS')),
    Column('FRACCIONAMERICANA', String(16, 'Modern_Spanish_CI_AS')),
    Column('ADVAME', DECIMAL(5, 2)),
    Column('ORDENCOMPRA', String(50, 'Modern_Spanish_CI_AS')),
    Column('INFOADICIONESP', String(1000, 'Modern_Spanish_CI_AS')),
    Column('INFOADICIONING', String(1000, 'Modern_Spanish_CI_AS')),
    Column('MONTOIGI', DECIMAL(19, 8)),
    Column('PAGOIMPUESTO', String(1, 'Modern_Spanish_CI_AS')),
    Column('FORMAPAGO', String(2, 'Modern_Spanish_CI_AS')),
    Column('NUMEROGUIA', String(20, 'Modern_Spanish_CI_AS')),
    Column('PROVEEDOR', String(30, 'Modern_Spanish_CI_AS')),
    Column('CANTIMPOAUXILIAR', DECIMAL(19, 8)),
    Column('UNIMEDAUXILIAR', String(5, 'Modern_Spanish_CI_AS')),
    Column('COSTOUAUXILIARME', DECIMAL(23, 8)),
    Column('VALORIMPOAUXILIARME', DECIMAL(23, 8)),
    Column('VALORADUANASMN', DECIMAL(23, 8)),
    Column('VALORADUANASME', DECIMAL(23, 8)),
    Column('CLIENTEFACTURAR', String(8, 'Modern_Spanish_CI_AS')),
    Column('FRACCIONROCTAVA', String(10, 'Modern_Spanish_CI_AS')),
    Column('PERMISOROCTAVA', String(20, 'Modern_Spanish_CI_AS')),
    Column('BODEGA', String(30, 'Modern_Spanish_CI_AS')),
    Column('REQUISITOR', String(100, 'Modern_Spanish_CI_AS')),
    Column('LINEARO', Integer),
    Column('ADVALORMELINEAPED', DECIMAL(19, 8)),
    Column('ADVALORMNLINEAPED', DECIMAL(19, 8)),
    Column('PERMISOSPED', String(500, 'Modern_Spanish_CI_AS')),
    Column('LINEAPED', Integer),
    Column('CAMPOCOMODIN', String(100, 'Modern_Spanish_CI_AS')),
    Column('ESMCIAMILITAR', TINYINT),
    Column('METVALOR', String(2, 'Modern_Spanish_CI_AS')),
    Column('DESCRIPCIONPARTE', String(500, 'Modern_Spanish_CI_AS')),
    Column('CANTIMPOUMA', DECIMAL(19, 8)),
    Column('CLAVEUMA', String(2, 'Modern_Spanish_CI_AS')),
    Column('NUMPARTECOM', String(70, 'Modern_Spanish_CI_AS')),
    Column('NOCAJAS', String(30, 'Modern_Spanish_CI_AS')),
    Column('VALIDACIONZERO', Integer),
    Column('VALIDACIONUNO', Integer),
    Column('METVALORACIONVALORDETERMINADO', DECIMAL(29, 8)),
    Column('METVALORACIONMOTIVODEUSO', String(500, 'Modern_Spanish_CI_AS')),
    Column('CLIENTEASIGNADO', String(50, 'Modern_Spanish_CI_AS')),
    Column('NUMERODEENTRADA', String(50, 'Modern_Spanish_CI_AS')),
    Column('LOCALIZACION', String(200, 'Modern_Spanish_CI_AS')),
    Column('LOTE', String(254, 'Modern_Spanish_CI_AS')),
    Column('FORMAPAGOTIGI', String(9, 'Modern_Spanish_CI_AS')),
    Index('MatPim_FKNumParte', 'NUMPARTE'),
    Index('MatPim_FKParPaiTipSecCons', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACCIMPO', 'SECTOR', 'CONSECUTIVO')
)


class SPartidasImposion(Base):
    __tablename__ = 'SPartidasImposion'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAIMPO', name='MatImp_PKConsecLinea'),
        Index('MatImp_FKNumParte', 'NUMPARTE'),
        Index('MatImp_FKParPaiTipSecCons', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACCIMPO', 'SECTOR', 'CONSECUTIVO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAIMPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTALTERNA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMEDALTERNA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMPERMISO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PAGRENGLON: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOKGS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOLBS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    DESCBULTOS: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCIMPO: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    ADVIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ADVIMPONUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TIENECO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    ADVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INFOADICIONESP: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    INFOADICIONING: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    MONTOIGI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    NUMEROGUIA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CANTIMPOAUXILIAR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMEDAUXILIAR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUAUXILIARME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOAUXILIARME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CLIENTEFACTURAR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONROCTAVA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PERMISOROCTAVA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    BODEGA: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    REQUISITOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))


class SPartidasPackingList(Base):
    __tablename__ = 'SPartidasPackingList'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEA', name='XXXP_PKConsecutivoLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMPACKINGLIST: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))


class SPartidasReciboCTM(Base):
    __tablename__ = 'SPartidasReciboCTM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEARECIBO', name='ParRec_PKConsecLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEARECIBO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTENVIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    MARCA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SERIES: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    OPCION: Mapped[Optional[str]] = mapped_column(CHAR(3, 'Modern_Spanish_CI_AS'))
    FACTURASALIDA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class SPartidasRep(Base):
    __tablename__ = 'SPartidasRep'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAIMPO', 'LINEAIMPO', name='ParRep_PKFactLinea'),
        Index('ParRep_FKClase', 'CLASE'),
        Index('ParRep_FKClaveBultos', 'CLAVEBULTOS'),
        Index('ParRep_FKFacturaImpo', 'FACTURAIMPO'),
        Index('ParRep_FKFraccAme', 'FRACCIONAMERICANA'),
        Index('ParRep_FKNumParte', 'NUMPARTE'),
        Index('ParRep_FKNumParteFact', 'NUMPARTE', 'FACTURAIMPO'),
        Index('ParRep_FKParPaiTipSec', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACCIMPO', 'SECTOR'),
        Index('ParRep_FKUnidadMed', 'UNIMED')
    )

    FACTURAIMPO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEAIMPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTIMPO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTALTERNA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMEDALTERNA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOUNITARIOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMPERMISO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PAGRENGLON: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAISORIGEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    DESCBULTOS: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIPOFRACCIMPO: Mapped[Optional[str]] = mapped_column(String(7, 'Modern_Spanish_CI_AS'))
    ADVIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    TIENECO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    ADVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(5, 2))
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    INFOADICIONESP: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    INFOADICIONING: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))


class SPartidasSalidaSM(Base):
    __tablename__ = 'SPartidasSalidaSM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEASALIDA', name='SalPSM_PKConsecLinea'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEASALIDA: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURASALIDA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTSALIDA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIDADMEDIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    COSTOUNITARIOMC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORSALMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORSALME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    TIPODENUMPARTE: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TIPODEORDEN: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CONCEPTODELAPARTIDA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FRACCIONDELAPARTIDA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class SPedimentos(Base):
    __tablename__ = 'SPedimentos'
    __table_args__ = (
        PrimaryKeyConstraint('PEDIMENTO', name='PedMat_PKPedimento'),
    )

    PEDIMENTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CLAVEPED: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    REGIMEN: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FECHA_INICIO: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_FIN: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_PAGO: Mapped[Optional[int]] = mapped_column(Integer)
    ACUSEELECTRONICO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FACTOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 4))
    ADUANA_CRUCE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PEDRECTIFICA: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SERECTIFICO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    OBSRECTIFICA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    INDIVIDUALCONS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    DTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 4))
    VALORIVA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PEDIMENTODESCARGO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PREVALIDACION: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 4))
    MONTOTIGIE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 4))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    ESMIXTO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SERECTIFICO2: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PEDRECTIFICA2: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHA_REC_1: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_REC_2: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_CIERRE: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_REVISION: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_AUTORIZACION: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_RECIBIDO: Mapped[Optional[int]] = mapped_column(Integer)
    ERRORES: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PERSONAREV: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    REPRESANTANTEAA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    CLAVEDESTORIGEN: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANAS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    CLAVETRANSPORTACION: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    PEDIMENTOCOMPLEMENTARIO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TOTALINCREMMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FACTORINCREMENTABLE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FEA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    FECHA_PAGO_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    FECHA_ENTRADARECINTO: Mapped[Optional[int]] = mapped_column(Integer)
    FECHA_EXTRACCIONRECINTO: Mapped[Optional[int]] = mapped_column(Integer)
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALSEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    SEGUROS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    EMBALAJES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    OTROSINCREMENTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    FORMAPAGODTA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FORMAPAGOPREVAL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FORMAPAGOIGI: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FORMAPAGOIVA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    RECARGOS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    IVADEPREV: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CUOTASCOMPENS: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    MULTAS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    IDENTIFICADORES: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    CNT: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 4))
    CLIENTEASIGNADO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SEDESISTIO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PEDDESISTIDO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    IEPS: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    OPCIONDESTINO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    TIPOPEDIMENTOTRANSPORTEE: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOPEDIMENTOTRANSPORTEA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TIPOPEDIMENTOTRANSPORTES: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PEDIMENTO18: Mapped[Optional[str]] = mapped_column(String(18, 'Modern_Spanish_CI_AS'))
    SUBDIVISION: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    IEPS2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(29, 8))
    DTA2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 4))
    IVA2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IGI2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PREVALIDACION2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CNT2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IEPS2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    DTA2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IVA2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IGI2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PREVALIDACION2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CNT2FP: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    IDPEDVIEJONUEVO: Mapped[Optional[int]] = mapped_column(Integer)


class SPedimentosAA(Base):
    __tablename__ = 'SPedimentosAA'
    __table_args__ = (
        PrimaryKeyConstraint('PEDIMENTO', 'CLAVEAA', name='PedMAA_PKPedAAduanal'),
    )

    PEDIMENTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVEAA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    FACTURA: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FECHAFAC: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAREC: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAENT: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAVENC: Mapped[Optional[int]] = mapped_column(Integer)
    SECCION: Mapped[Optional[int]] = mapped_column(Integer)


class SPedimentosConcep(Base):
    __tablename__ = 'SPedimentosConcep'
    __table_args__ = (
        PrimaryKeyConstraint('PEDIMENTO', 'CLAVEAA', 'CONCEPTO', name='PedMCon_PKPedAAConcepto'),
    )

    PEDIMENTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVEAA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    CONCEPTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    IMPORTE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 2))
    TIPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))


class SPedimentosEDocument(Base):
    __tablename__ = 'SPedimentosEDocument'
    __table_args__ = (
        PrimaryKeyConstraint('PEDIMENTO', 'CONSECUTIVO', name='SPedED_PKPedimentoConsecutivo'),
    )

    PEDIMENTO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    EDOCUMENT: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    RUTA_XML: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    OPERACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))


class SPermisoSECON(Base):
    __tablename__ = 'SPermisoSECON'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='MatSic_PKConsecutivo'),
        Index('MatSic_FKOficioPerm', 'NUMOFICIO', 'PERMISO', unique=True),
        Index('MatSic_FKPermiso', 'PERMISO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMOFICIO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PERMISO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    FECHAVIGENCIA: Mapped[Optional[int]] = mapped_column(Integer)
    PROGRAMA: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))


class SRegulaciones(Base):
    __tablename__ = 'SRegulaciones'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='SReg_PKSYSID'),
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    IMPORTACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    EXPORTACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PERMISO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ACUERDO: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CONDICION: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    FUNDAMENTO: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    DOF: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FORMATONOM: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    INSTRUCCIONES: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    CRITERIO: Mapped[Optional[str]] = mapped_column(String(254, 'Modern_Spanish_CI_AS'))
    COMPLEMENTO: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    CRITERIOESPECIAL: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))


class SSaldoCTM(Base):
    __tablename__ = 'SSaldoCTM'
    __table_args__ = (
        PrimaryKeyConstraint('FACTENVIO', 'NUMPARTE', name='SalEnv_PKFactParte'),
    )

    FACTENVIO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHAENVIO: Mapped[Optional[int]] = mapped_column(Integer)
    CANTENVIO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEXITENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMEXITENCIA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTPARTIDA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMPARTIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VENCIMIENTO: Mapped[Optional[int]] = mapped_column(Integer)


class SSaldoDef(Base):
    __tablename__ = 'SSaldoDef'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAIMPO', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACIMPO', 'SECTOR', name='ConPdf_PKFaParPaiTiSe'),
        Index('ConPdf_FKClase', 'CLASE'),
        Index('ConPdf_FKClaseFecha', 'CLASE', 'FECHAFACTURA'),
        Index('ConPdf_FKFacImpParte', 'FACTURAIMPO', 'NUMPARTE'),
        Index('ConPdf_FKFechaFact', 'FECHAFACTURA'),
        Index('ConPdf_FKNumParte', 'NUMPARTE'),
        Index('ConPdf_FKParteFecha', 'NUMPARTE', 'FECHAFACTURA'),
        Index('ConPdf_FKPedImpClase', 'PEDIMENTOIMPODEF', 'CLASE'),
        Index('ConPdf_FKPedImpParte', 'PEDIMENTOIMPODEF', 'NUMPARTE')
    )

    FACTURAIMPO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAISORIGEN: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOFRACIMPO: Mapped[str] = mapped_column(String(7, 'Modern_Spanish_CI_AS'), primary_key=True)
    SECTOR: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOSALDO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PEDIMENTOIMPODEF: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    ESNAFTA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    CANTIDADCLASE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMEDCLASE: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTUSADADESP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEXITENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTGENDESP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMEXITENCIA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTPARTIDA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMPARTIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    DESCBULTO: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    SUBVALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    SUBVALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    IVAIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMSOLICITUD: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PAGRENGLON: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ADVIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    CANTALTERNA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMALTERNA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    MONTOIGI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    MONTOIGIUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CANTAUXILIAR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMAUXILIAR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORAUXILIARIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(150, 'Modern_Spanish_CI_AS'))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ESREPARACION: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    FECHAVENC_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    NUMPARTECOM: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))


class SSaldoRep(Base):
    __tablename__ = 'SSaldoRep'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAIMPO', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACIMPO', 'SECTOR', name='ConRep_FKFaParPaiTiSe'),
        Index('ConRep_FKClase', 'CLASE'),
        Index('ConRep_FKClaseFecha', 'CLASE', 'FECHAFACTURA'),
        Index('ConRep_FKFacImpParte', 'FACTURAIMPO', 'NUMPARTE'),
        Index('ConRep_FKFechaFact', 'FECHAFACTURA'),
        Index('ConRep_FKFechaVenc', 'FECHAVENC'),
        Index('ConRep_FKParteFecha', 'NUMPARTE', 'FECHAFACTURA'),
        Index('ConRep_FKPedImpClase', 'PEDIMENTOIMPO', 'CLASE'),
        Index('ConRep_FKPedImpParte', 'PEDIMENTOIMPO', 'NUMPARTE')
    )

    FACTURAIMPO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAISORIGEN: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOFRACIMPO: Mapped[str] = mapped_column(String(7, 'Modern_Spanish_CI_AS'), primary_key=True)
    SECTOR: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    PEDIMENTOIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    ESNAFTA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    CANTIDADCLASE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMEDCLASE: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEXITENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMEXITENCIA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTPARTIDA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMPARTIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    DESCBULTO: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMSOLICITUD: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PAGRENGLON: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ADVALOREMIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    CANTALTERNA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMALTERNA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FECHAVENC: Mapped[Optional[int]] = mapped_column(Integer)


class SSaldoSalidaSM(Base):
    __tablename__ = 'SSaldoSalidaSM'
    __table_args__ = (
        PrimaryKeyConstraint('REMISIONSALIDA', 'NUMPARTE', name='SalSal_PKRemSalidaParte'),
    )

    REMISIONSALIDA: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHASALIDA: Mapped[Optional[int]] = mapped_column(Integer)
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    CANTUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEXITENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMEXITENCIA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTPARTIDA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMPARTIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))


class SSaldoTem(Base):
    __tablename__ = 'SSaldoTem'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAIMPO', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACIMPO', 'SECTOR', name='ConPim_PKFaParPaiTiSe'),
        Index('ConPim_FKClase', 'CLASE'),
        Index('ConPim_FKClaseFecha', 'CLASE', 'FECHAFACTURA'),
        Index('ConPim_FKFacImpParte', 'FACTURAIMPO', 'NUMPARTE'),
        Index('ConPim_FKFechaFact', 'FECHAFACTURA'),
        Index('ConPim_FKFechaVenc', 'FECHAVENC'),
        Index('ConPim_FKNumParte', 'NUMPARTE'),
        Index('ConPim_FKParteFecha', 'NUMPARTE', 'FECHAFACTURA'),
        Index('ConPim_FKPedImpClase', 'PEDIMENTOIMPO', 'CLASE'),
        Index('ConPim_FKPedImpParte', 'PEDIMENTOIMPO', 'NUMPARTE')
    )

    FACTURAIMPO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAISORIGEN: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOFRACIMPO: Mapped[str] = mapped_column(String(7, 'Modern_Spanish_CI_AS'), primary_key=True)
    SECTOR: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    PEDIMENTOIMPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONE: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    ESNAFTA: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    NOCERTIFICADO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    CANTIDADCLASE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMEDCLASE: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PESONETO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOBRUTOUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTUSADADESP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEXITENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTGENDESP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMEXITENCIA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTPARTIDA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMPARTIDA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    DESCBULTO: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    VALORIMPOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORUSADOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    NUMSOLICITUD: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    VALORIVAMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAMNUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORIVAMEUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PAGRENGLON: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    ADVALOREMIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCIONAMERICANA: Mapped[Optional[str]] = mapped_column(String(16, 'Modern_Spanish_CI_AS'))
    CANTALTERNA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMALTERNA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    FECHAVENC: Mapped[Optional[int]] = mapped_column(Integer)
    MONTOIGI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    MONTOIGIUSADO: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CANTAUXILIAR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMAUXILIAR: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    VALORAUXILIARIMPOME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ORDENCOMPRA: Mapped[Optional[str]] = mapped_column(String(150, 'Modern_Spanish_CI_AS'))
    VALORADUANASMN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORADUANASME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    ESREPARACION: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    SALDOSIMPLOSION: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FECHAFACTURA_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    FECHAVENC_ISO: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    NUMPARTECOM: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))


class SSaldosBultos(Base):
    __tablename__ = 'SSaldosBultos'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAIMPO', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACIMPO', 'SECTOR', 'PROCEDENCIA', 'CLAVEBULTOS', name='BulSal_PKFaPaPsTiSeProBu'),
        Index('BulSal_FKFaClPstiSePro', 'FACTURAIMPO', 'CLASE', 'PAISORIGEN', 'TIPOFRACIMPO', 'SECTOR', 'PROCEDENCIA')
    )

    FACTURAIMPO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAISORIGEN: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOFRACIMPO: Mapped[str] = mapped_column(String(7, 'Modern_Spanish_CI_AS'), primary_key=True)
    SECTOR: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    PROCEDENCIA: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLAVEBULTOS: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    CANTBULTOS: Mapped[Optional[int]] = mapped_column(Integer)
    DESCBULTO: Mapped[Optional[str]] = mapped_column(String(40, 'Modern_Spanish_CI_AS'))


class SSaldosDetallado(Base):
    __tablename__ = 'SSaldosDetallado'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAIMPO', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACIMPO', 'SECTOR', 'CAMPOCOMODIN', 'PROCEDENCIA', name='SalDet_PKFaPaPsTiSeCCPro'),
    )

    FACTURAIMPO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAISORIGEN: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOFRACIMPO: Mapped[str] = mapped_column(String(7, 'Modern_Spanish_CI_AS'), primary_key=True)
    SECTOR: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    CAMPOCOMODIN: Mapped[str] = mapped_column(String(100, 'Modern_Spanish_CI_AS'), primary_key=True)
    PROCEDENCIA: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    CANTEXISTENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTUSADA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))


class SSaldosReglaOctava(Base):
    __tablename__ = 'SSaldosReglaOctava'
    __table_args__ = (
        PrimaryKeyConstraint('FACTURAIMPO', 'NUMPARTE', 'PAISORIGEN', 'TIPOFRACIMPO', 'SECTOR', 'PERMISOROCTAVA', 'PROCEDENCIA', 'SISTEMA', 'LINEA', name='ROctSal_PKFaParPaiTiSeROProSisLin'),
        Index('ROctSal_FKPermisoRO', 'PERMISOROCTAVA')
    )

    FACTURAIMPO: Mapped[str] = mapped_column(String(15, 'Modern_Spanish_CI_AS'), primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAISORIGEN: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    TIPOFRACIMPO: Mapped[str] = mapped_column(String(7, 'Modern_Spanish_CI_AS'), primary_key=True)
    SECTOR: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    PERMISOROCTAVA: Mapped[str] = mapped_column(String(20, 'Modern_Spanish_CI_AS'), primary_key=True)
    LINEA: Mapped[int] = mapped_column(Integer, primary_key=True)
    PROCEDENCIA: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    SISTEMA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    CANTEXITENCIA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CLASE: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONIMPO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCIONROCTAVA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    VALORME: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))


class SSeriesExpo(Base):
    __tablename__ = 'SSeriesExpo'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', 'LINEAEXPO', 'RENGLON', name='SerExpo_PKConsec_Lin_RenSCAII'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAEXPO: Mapped[int] = mapped_column(Integer, primary_key=True)
    RENGLON: Mapped[int] = mapped_column(Integer, primary_key=True)
    FACTURAEXPO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    SERIEEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MODELOEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    SUBMODELOEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    MARCA: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMIDEXPO: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    MARCAEXPO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))


class SSisCMex(Base):
    __tablename__ = 'SSisCMex'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SSICM_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PREFIJOCM: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOCM: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PORPARTECLASEMEX: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PORPARTECLASEAME: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FRACCIONIMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    FIRMAFAME: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    IMPORDENCOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    UMAUXILIARMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMALTERNAMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PACKINGORDENCOMPRA: Mapped[Optional[int]] = mapped_column(Integer)
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    INCLUIRLINEADELPO: Mapped[Optional[int]] = mapped_column(Integer)
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    AGREGARVAENPRODTERMINADOS: Mapped[Optional[int]] = mapped_column(Integer)
    OCULTARFECHAHORA: Mapped[Optional[int]] = mapped_column(TINYINT)


class SSisDef(Base):
    __tablename__ = 'SSisDef'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SSIDef_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PREFIJOIMPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PORPARTECLASEMEX: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PORPARTECLASEAME: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FIRMAFAME: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    CODIGOBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONIMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMAUXILIARMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPORDENCOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CANTLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    UMALTERNAMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESTRINGEIMPOPT: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARTECOMPLEMENTARIAMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PACKINGPEDCLAVE: Mapped[Optional[int]] = mapped_column(TINYINT)
    PORORDENPOROCPACK: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ACTUALIZARPARTEPARTIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PARTECOMPLEMEXPARTIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    PACKINGORDENCOMPRA: Mapped[Optional[int]] = mapped_column(Integer)
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SOLICITARCONTRASENAADMINISTRADOR: Mapped[Optional[int]] = mapped_column(Integer)
    INCLUIRLINEADELPO: Mapped[Optional[int]] = mapped_column(Integer)
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    AGREGARVAENPRODTERMINADOS: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRLOTE: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRNUMENTRADA: Mapped[Optional[int]] = mapped_column(Integer)
    OCULTARFECHAHORA: Mapped[Optional[int]] = mapped_column(TINYINT)


class SSisExpo(Base):
    __tablename__ = 'SSisExpo'
    __table_args__ = (
        PrimaryKeyConstraint('TIPOFACTURA', 'ESCAMBIOREGIMEN', name='SSExpo_PKTipoFacturaEsCR'),
    )

    TIPOFACTURA: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    ESCAMBIOREGIMEN: Mapped[str] = mapped_column(String(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    PORPARTECLASEMEX: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PORPARTECLASEAME: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PREFIJOEXPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOEXPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    MONEDA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONEXP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    COSTOUNITMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    ORDENCOMPMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    CONSFACMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    OCULTAREMPAQUEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    OCULTAREMPAQUEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    COSTOUNITMPMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    CODIGOBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARTECOMPLEMENTARIAMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALORDLLSMEXPESOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTPNCODBAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DTACEROCODBAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    NUMPARTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    FIRMAFAME: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FRACCIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    ORDENCOMPAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    FDAINFORMACIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISOPCAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    MUESTRAFREE: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCMEXDES: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEXDES: Mapped[Optional[int]] = mapped_column(TINYINT)
    COLVALORDES: Mapped[Optional[int]] = mapped_column(TINYINT)
    COLPESODES: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCARGACLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCARGASUST: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCARGADEF: Mapped[Optional[int]] = mapped_column(TINYINT)
    VENTQUEUEACT: Mapped[Optional[int]] = mapped_column(TINYINT)
    CODIGOSCAC: Mapped[Optional[int]] = mapped_column(TINYINT)
    FORMADESPERDICIO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    CALVALORBASECOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALVABASECAPT: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALPESOBASEDESCARGA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALEMPAQUEBASECAPT: Mapped[Optional[int]] = mapped_column(TINYINT)
    OCULTCANTCONS: Mapped[Optional[int]] = mapped_column(TINYINT)
    PREFIJOFRACCMULT: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTAMEPAISPARTE: Mapped[Optional[int]] = mapped_column(TINYINT)
    BASECOSTOMPOTOTAL: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    UMEQUIVALENTEMEX2: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEAME2: Mapped[Optional[int]] = mapped_column(TINYINT)
    TOTALEQUIVMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TOTALEQUIVAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    INFOADICIONAL: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    RESTRINGEEXPOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALVATOTAGREMP: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    ACTIVAADVPEDRTV1: Mapped[Optional[int]] = mapped_column(TINYINT)
    ASIGNAFRACC9801: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALOREXCFRACC9801: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    SCRAPSOLONODUTY: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCEXTRAAMEPARTES: Mapped[Optional[int]] = mapped_column(TINYINT)
    INCAMBIOREGDESC: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCNOCONTEMCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PESONETODESDIFFAC: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    ENVIADOPORVENDIDOPOR: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    OCULTACOLVA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALCCOSTOSAMEBASEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PROVEEDOREXPORTADOR: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARTECOMPLEMEXPARTIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALIDACANTPARCANDES: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    COSTOSAMEPAIS: Mapped[Optional[str]] = mapped_column(CHAR(20, 'Modern_Spanish_CI_AS'))
    INCLUIRFRACAMEBIL: Mapped[Optional[int]] = mapped_column(TINYINT)
    SOLICITARPSWDACTUAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    SOLICITARPSWDDESACTUAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    BUSCARSALDOSRECIENTES: Mapped[Optional[int]] = mapped_column(TINYINT)
    PACKINGORDENVENTA: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRORDENVENTA: Mapped[Optional[int]] = mapped_column(Integer)
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    MPF: Mapped[Optional[int]] = mapped_column(Integer)
    VALORMPF: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    COLCANTPORPESO: Mapped[Optional[int]] = mapped_column(Integer)
    PACKINGPEDCLAVE: Mapped[Optional[int]] = mapped_column(Integer)
    GENERAFACTURAIMD: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    GENERAFACTURAIMDENBASEA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SOLICITARCONTRASENAADMINISTRADOR: Mapped[Optional[int]] = mapped_column(Integer)
    INCLUIRLINEADELPO: Mapped[Optional[int]] = mapped_column(Integer)
    VALORPACKING1DLLS: Mapped[Optional[int]] = mapped_column(TINYINT)
    TOMARVALORMEXENFACAME: Mapped[Optional[int]] = mapped_column(Integer)
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    CALAMEBASEMEXMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALAMEBASEMEXVA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALAMEBASEMEXEMPAQUE: Mapped[Optional[int]] = mapped_column(TINYINT)
    USARVAENFACTURAAMERICANA: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACTIVARFECHACORTESALDOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHACORTESALDOS: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRLOTE: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRNUMENTRADA: Mapped[Optional[int]] = mapped_column(Integer)
    RESPALDARDESCARGAENDESCARGAM: Mapped[Optional[int]] = mapped_column(TINYINT)
    OCULTARFECHAHORA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALCULARVALORESAMERICANOSENBASEAPARTIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALIDARESTATUSPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESCAPAIS: Mapped[Optional[int]] = mapped_column(TINYINT)


class SSisGen(Base):
    __tablename__ = 'SSisGen'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SSGen_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    DTA: Mapped[Optional[int]] = mapped_column(Integer)
    DTAEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    SUBEMPRESA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PATHARCH: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHARCHTRANSMISION: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHTRANSEXPO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHRESPUESTA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHARCHPED: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHARCHPEDCONSM: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHGENIMPOTEMP: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHGENEXPO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    ACTSEGURIDAD: Mapped[Optional[int]] = mapped_column(TINYINT)
    CONTROLDES: Mapped[Optional[int]] = mapped_column(TINYINT)
    DIADESACTUAL: Mapped[Optional[int]] = mapped_column(Integer)
    DIAVENCIMIENTO: Mapped[Optional[int]] = mapped_column(Integer)
    MENSAJEVENC: Mapped[Optional[int]] = mapped_column(TINYINT)
    FECHADES: Mapped[Optional[int]] = mapped_column(Integer)
    FACTORIVA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 4))
    VALIDASIFRA: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALVALBASETCPED: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALVALBASETCPEDEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    FILTROCANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    MUESTRAARCHCODBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    DATOSHIST: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOVENRO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CANTVENRO: Mapped[Optional[int]] = mapped_column(Integer)
    COSTOPLANTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    FIRMAPACKING: Mapped[Optional[int]] = mapped_column(TINYINT)
    ESCONDAAMEXPACKING: Mapped[Optional[int]] = mapped_column(TINYINT)
    ADVERTENCIATM: Mapped[Optional[int]] = mapped_column(TINYINT)
    COSTOIMPOFIJO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TOMARSALDOSVENC: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALPARTEEXISTE: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALMANIFUSADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TEMPORALFECHAPAGO: Mapped[Optional[int]] = mapped_column(TINYINT)
    ASIGNADIASANTDESC: Mapped[Optional[int]] = mapped_column(TINYINT)
    DIASANTDESC: Mapped[Optional[int]] = mapped_column(Integer)
    DESHABILITARDESCPARTE: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESHABILITARDESCPARTEING: Mapped[Optional[int]] = mapped_column(TINYINT)
    ASIGNAFRACAMEPARTE: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALIDADECENCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    MOSTRARADVERTENCIARO: Mapped[Optional[int]] = mapped_column(TINYINT)
    USARTRANSPAMEDOCAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALCDUTYPACKING: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARAMMULTIPLES: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCNIVELPAIS: Mapped[Optional[int]] = mapped_column(TINYINT)
    COVEFECHAEMISION: Mapped[Optional[int]] = mapped_column(TINYINT)
    VALORDLLSTCFACTURAEXPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    INTERFACEAACONSOLIDADA: Mapped[Optional[int]] = mapped_column(TINYINT)
    INTERFACEAATCFPFF: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    INCLUIROBSCOVEOBSIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    AGREGARINCREIMPO: Mapped[Optional[int]] = mapped_column(TINYINT)
    COMPONENTEBOM: Mapped[Optional[int]] = mapped_column(TINYINT)
    LIMITESUBENSAMBLE: Mapped[Optional[int]] = mapped_column(Integer)
    ACTPDFREPORTES: Mapped[Optional[int]] = mapped_column(TINYINT)
    PATHARCHPDFIMPO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHARCHPDFEXPO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    NOIMPRIMIRCONS: Mapped[Optional[int]] = mapped_column(TINYINT)
    MOSTRARADVERTENCIAROVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARTESYPEDIMENTOSPORCLIENTE: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    MENSAJESVURFC: Mapped[Optional[int]] = mapped_column(Integer)
    MOSTRARPACKINGLISTINGLES: Mapped[Optional[int]] = mapped_column(Integer)
    OMITIREMPAQUEENCODIGOBARRAS: Mapped[Optional[int]] = mapped_column(Integer)
    RESTRINGEPAISIMPO: Mapped[Optional[int]] = mapped_column(Integer)
    RESTRINGPAISEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    BLOQUEOALDESACTIVARNUMERODEPARTE: Mapped[Optional[int]] = mapped_column(Integer)
    GENINFORMEANEXO31: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    UTILIZARFECHAPAGOPEDDEUNDIAANTERIOR: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARTITULOSALTERNATIVOSIMPRESIONFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZAREQUIVALENCIASDEUMPORNUMERODEPARTE: Mapped[Optional[int]] = mapped_column(Integer)
    USARFACTORCONVERSIONPORNUMERODEPARTE: Mapped[Optional[int]] = mapped_column(Integer)
    USARTCDELAFECHAPAGOPEDIMPOENDESCARGA: Mapped[Optional[int]] = mapped_column(Integer)
    USARVUDE128O256: Mapped[Optional[int]] = mapped_column(Integer)
    SOLICITARCONTRASENAADMINISTRADOR: Mapped[Optional[int]] = mapped_column(Integer)
    AGREGARNUMEROEMBARQUE: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARUMDEEXISTENCIAENTRANSMISIONVU: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARCODIGODEBROKERDECLIENTEENMAINX30: Mapped[Optional[int]] = mapped_column(Integer)
    HOJACALCULOSEPARARINCREMENTABLESANEXO3: Mapped[Optional[int]] = mapped_column(Integer)
    HOJACALCULODESGLOSEFACTURAANEXO3: Mapped[Optional[int]] = mapped_column(Integer)
    USARVALORAGREGADOENFACTURAAMERICANA: Mapped[Optional[int]] = mapped_column(Integer)
    OCULTARINFORMACIONFRACCION: Mapped[Optional[int]] = mapped_column(Integer)
    VALORAGREGADOENFACTURAMEXICANA: Mapped[Optional[int]] = mapped_column(Integer)
    RESALTARSALDOSTEMPCONCOLOR: Mapped[Optional[int]] = mapped_column(Integer)
    VALIDARSECTORPROSECR8: Mapped[Optional[int]] = mapped_column(Integer)
    AGREGARSUBTOTALINTERFAZAA: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARNOMBREGENERICOMAINX30: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARTCRESPECTOATIPOPED: Mapped[Optional[int]] = mapped_column(Integer)
    TOMARDECIMALESCOMPLETOS: Mapped[Optional[int]] = mapped_column(Integer)
    INCLUIRREMESAENINTERFAZAAWINSAAI: Mapped[Optional[int]] = mapped_column(Integer)
    CAMBIARPESOSPORCOSTOUNITARIO: Mapped[Optional[int]] = mapped_column(Integer)
    UTILIZARSOLOPARTESNAFTAENCO: Mapped[Optional[int]] = mapped_column(Integer)
    BLOQUEODEEDICIONDEFACTURAS: Mapped[Optional[int]] = mapped_column(Integer)
    REASIGNAFRACCIONCLASE: Mapped[Optional[int]] = mapped_column(TINYINT)
    CALCULARCOSTOUNITARIOENBASEAVALORTOTAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARAMETROAUXILIAR: Mapped[Optional[int]] = mapped_column(TINYINT)
    USARCONTROLDEFECHASDEVERSION: Mapped[Optional[int]] = mapped_column(TINYINT)
    DESACTIVACIONDEMODULOS: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPRIMIRFACTURAALTERNA: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACTIVAREXPEDIENTEELECTRONICO: Mapped[Optional[int]] = mapped_column(TINYINT)
    INFORMACIONAMERICANASUBTOTAL: Mapped[Optional[int]] = mapped_column(TINYINT)
    ACTIVARCATALOGOFRACCIONESAMERICANASSIFRA: Mapped[Optional[int]] = mapped_column(TINYINT)
    MOSTRARPROGRAMAIMMEXPROSEC: Mapped[Optional[int]] = mapped_column(TINYINT)
    COSTOUNITARIOPOREMPAQUEFAC: Mapped[Optional[int]] = mapped_column(TINYINT)
    TRANSMITIRFACALTERNA: Mapped[Optional[int]] = mapped_column(TINYINT)


class SSisImpo(Base):
    __tablename__ = 'SSisImpo'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SSImp_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PREFIJOIMPO: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    PREFIJOCR: Mapped[Optional[str]] = mapped_column(String(9, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOIMPO: Mapped[Optional[str]] = mapped_column(String(6, 'Modern_Spanish_CI_AS'))
    CONSECUTIVOCR: Mapped[Optional[int]] = mapped_column(Integer)
    PORPARTECLASEMEX: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PORPARTECLASEAME: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    PEDIMENTO: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROVEEDOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    VENDIDOCONSIGNADO: Mapped[Optional[str]] = mapped_column(String(13, 'Modern_Spanish_CI_AS'))
    VENDIDOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ENVIADOTRANSFERIDO: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ENVIADOA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    AADUANAL: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    INCOTERM: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    FLETE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(17, 6))
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    NUMPARTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    NUMPARTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    FIRMAFMEX: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    FIRMAFAME: Mapped[Optional[str]] = mapped_column(String(350, 'Modern_Spanish_CI_AS'))
    CODIGOBARRAS: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONIMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    TASAFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOFRACCMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMAUXILIARMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PERPAGRENGLON: Mapped[Optional[int]] = mapped_column(TINYINT)
    FRACCIONAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAISORIGENAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEAME: Mapped[Optional[int]] = mapped_column(TINYINT)
    IMPORDENCOMP: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESPESO: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCANT: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESVALOR: Mapped[Optional[int]] = mapped_column(TINYINT)
    DECIMALESCOSTO: Mapped[Optional[int]] = mapped_column(TINYINT)
    TIPOMONEDA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    CLAVEMONEDA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CANTLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORLIMITEPAR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMALTERNAMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    RESTRINGEIMPOPT: Mapped[Optional[int]] = mapped_column(TINYINT)
    CONTROLREMESA: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    REMESAINICIO: Mapped[Optional[int]] = mapped_column(SmallInteger)
    REMESAFINAL: Mapped[Optional[int]] = mapped_column(SmallInteger)
    LEYENDAFACAME: Mapped[Optional[str]] = mapped_column(String(400, 'Modern_Spanish_CI_AS'))
    CALCIGIBASECAPT: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEMEX2: Mapped[Optional[int]] = mapped_column(TINYINT)
    UMEQUIVALENTEAME2: Mapped[Optional[int]] = mapped_column(TINYINT)
    PARTECOMPLEMENTARIAMEX: Mapped[Optional[int]] = mapped_column(TINYINT)
    PAGOIMPUESTO: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    FORMAPAGO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    METVALOR: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    AADUANALAME: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CONDUCTOR: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TRANSPORTE: Mapped[Optional[str]] = mapped_column(String(15, 'Modern_Spanish_CI_AS'))
    NUMTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PACKINGPEDCLAVE: Mapped[Optional[int]] = mapped_column(TINYINT)
    PORORDENPOROCPACK: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    ACTUALIZARPARTEPARTIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    OBSERVACIONE: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    OBSERVACIONI: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    CLAVEBULTOS: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PARTECOMPLEMEXPARTIDA: Mapped[Optional[int]] = mapped_column(TINYINT)
    CANTLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PESOLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    VALORLIMITEMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(23, 8))
    VALORLIMITEPARMIN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    PACKINGORDENCOMPRA: Mapped[Optional[int]] = mapped_column(Integer)
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    SOLICITARCONTRASENAADMINISTRADOR: Mapped[Optional[int]] = mapped_column(Integer)
    INCLUIRLINEADELPO: Mapped[Optional[int]] = mapped_column(Integer)
    LINEAPERSONAAA: Mapped[Optional[int]] = mapped_column(Integer)
    AGREGARVAENPRODTERMINADOS: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRLOTE: Mapped[Optional[int]] = mapped_column(Integer)
    IMPRIMIRNUMENTRADA: Mapped[Optional[int]] = mapped_column(Integer)
    OCULTARFECHAHORA: Mapped[Optional[int]] = mapped_column(TINYINT)


class STipoMat(Base):
    __tablename__ = 'STipoMat'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='TipMat_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(256, 'Modern_Spanish_CI_AS'))
    TIPOMAT: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))


class STiposFactura(Base):
    __tablename__ = 'STiposFactura'
    __table_args__ = (
        PrimaryKeyConstraint('CLAVE', name='GTFACT_PKClave'),
    )

    CLAVE: Mapped[str] = mapped_column(String(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(CHAR(50, 'Modern_Spanish_CI_AS'))
    OBSERVACION: Mapped[Optional[str]] = mapped_column(CHAR(500, 'Modern_Spanish_CI_AS'))


class SVerBOM(Base):
    __tablename__ = 'SVerBOM'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='VerBOM_PKConsecutivo'),
        Index('FKNUMPARTECONSECUTIVO', 'NUMPARTE', 'CONSECUTIVO', unique=True),
        Index('FKNUMPARTEVERCOMP', 'NUMPARTE', 'VERSION', 'NUMPARTEBOM'),
        Index('VerBOM_FKNumParteVer', 'NUMPARTE', 'VERSION')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    VERSION: Mapped[Optional[int]] = mapped_column(Integer)
    NUMPARTE: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    NUMPARTEBOM: Mapped[Optional[str]] = mapped_column(String(70, 'Modern_Spanish_CI_AS'))
    CANTIDAD: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UNIMED: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    PROCEDENCIA: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    CANTMP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTDESP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTMERMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTEQUIVALENTE: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    UMEQUIVALENTE: Mapped[Optional[str]] = mapped_column(String(5, 'Modern_Spanish_CI_AS'))
    CANTDESPEQUI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    CANTMERMAEQUI: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(19, 8))
    DESCDESPAPARTADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    PORCENTAJEMP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    PORCENTAJEDESP: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    PORCENTAJEMERMA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TIPODESPMERMA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class SVerBOMEnc(Base):
    __tablename__ = 'SVerBOMEnc'
    __table_args__ = (
        PrimaryKeyConstraint('NUMPARTE', 'VERSION', name='VEncBOM_PKNumParteVer'),
    )

    VERSION: Mapped[int] = mapped_column(Integer, primary_key=True)
    NUMPARTE: Mapped[str] = mapped_column(String(70, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    IDENTIFICADOR: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    FECHAFINAL: Mapped[Optional[int]] = mapped_column(Integer)


class GDODA(Base):
    __tablename__ = 'gDODA'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='PKSQLDODAID'),
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    NOINTEGRACION: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    FECHADODA: Mapped[Optional[int]] = mapped_column(Integer)
    HORADODA: Mapped[Optional[int]] = mapped_column(Integer)
    ADUANADESPACHO: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    ADUANASECCIONES: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    PATENTE: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    PEIDMENTOS: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    CAAT: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    IDENTIFICACIONTRANSPORTE: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    FAST_ID: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    TIPOOPERACION: Mapped[Optional[str]] = mapped_column(String(1, 'Modern_Spanish_CI_AS'))
    SELECCIONADO: Mapped[Optional[int]] = mapped_column(TINYINT)
    USUARIOSELECCIONO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ULTIMOUSUARIO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    RESPONSABLE: Mapped[Optional[str]] = mapped_column(String(14, 'Modern_Spanish_CI_AS'))
    TRANSPORTISTA: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    REMESAS: Mapped[Optional[str]] = mapped_column(String(80, 'Modern_Spanish_CI_AS'))
    TIPOPEDIMENTO: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    CADENAORIGINAL: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    NUMEROSERIE: Mapped[Optional[str]] = mapped_column(CHAR(21, 'Modern_Spanish_CI_AS'))
    FIRMAELECTRONICA: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    NOTRANSACCION: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    ESTATUS: Mapped[Optional[str]] = mapped_column(String(30, 'Modern_Spanish_CI_AS'))
    LINQSATQR: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    SAT_CERTIFICADO: Mapped[Optional[str]] = mapped_column(CHAR(2001, 'Modern_Spanish_CI_AS'))
    SAT_SELLODIGITAL: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    PATHXMLDODAENVIO: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    PATHXMLDODARESPUESTA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))
    SAT_CADENAORIGINAL: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    DESPACHOADUANERO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMEROGAFETEUNICO: Mapped[Optional[str]] = mapped_column(String(250, 'Modern_Spanish_CI_AS'))


class GDodaContenedores(Base):
    __tablename__ = 'gDoda_Contenedores'
    __table_args__ = (
        PrimaryKeyConstraint('DODASYSID', 'LINEACONTENEDOR', name='PKSQLDDCT_ID_LN'),
    )

    DODASYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEACONTENEDOR: Mapped[int] = mapped_column(Integer, primary_key=True)
    VALORCONTENEDOR: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    PRECINTOS: Mapped[Optional[str]] = mapped_column(String(254, 'Modern_Spanish_CI_AS'))


class GDodaContenedoresCandados(Base):
    __tablename__ = 'gDoda_Contenedores_Candados'
    __table_args__ = (
        PrimaryKeyConstraint('DODASYSID', 'LINEACONTENEDOR', 'LINEACANDADO', name='PKSQLDCCAN_ID_LN_LN'),
    )

    DODASYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEACONTENEDOR: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEACANDADO: Mapped[int] = mapped_column(Integer, primary_key=True)
    VALORCANDADO: Mapped[Optional[str]] = mapped_column(String(21, 'Modern_Spanish_CI_AS'))


class GDodaPedimentoAmericano(Base):
    __tablename__ = 'gDoda_PedimentoAmericano'
    __table_args__ = (
        PrimaryKeyConstraint('DODASYSID', 'LINEAPEDAME', name='PKSQLDDPA_ID_LIN'),
    )

    DODASYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAPEDAME: Mapped[int] = mapped_column(Integer, primary_key=True)
    TIPOPEDIMENTOAMERICANO: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    VALORPEDIMENTOAMERICANO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))


class GDodaPedimentos(Base):
    __tablename__ = 'gDoda_Pedimentos'
    __table_args__ = (
        PrimaryKeyConstraint('DODASYSID', 'LINEAPEDIMENTO', name='PKSQLDDPED_ID_LN'),
    )

    DODASYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    LINEAPEDIMENTO: Mapped[int] = mapped_column(Integer, primary_key=True)
    PATENTEAUTORIZACION: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    DOCUMENTO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    REMESA: Mapped[Optional[str]] = mapped_column(String(11, 'Modern_Spanish_CI_AS'))
    COVE: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    UMC: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    IMPORTEEFECTIODOLARES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 2))
    IMPORTEDIFERENCIADOLARES: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(15, 2))
    DTA_NIU: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    ARTICULO7: Mapped[Optional[int]] = mapped_column(TINYINT)
    SYSIDPEDIMENTO: Mapped[Optional[int]] = mapped_column(Integer)
    LINEAFACTURA: Mapped[Optional[int]] = mapped_column(Integer)
    LINEAPARTEII: Mapped[Optional[int]] = mapped_column(Integer)
    TIPOPEDIMENTO: Mapped[Optional[str]] = mapped_column(String(20, 'Modern_Spanish_CI_AS'))
    VALIDACIONEMPAQUEZERO: Mapped[Optional[int]] = mapped_column(TINYINT)


class GMSSQLFile(Base):
    __tablename__ = 'gMSSQLFile'
    __table_args__ = (
        PrimaryKeyConstraint('DS_FIELD2', name='PK__gMSSQLFi__477FB1692AD800AB'),
    )

    DS_FIELD2: Mapped[str] = mapped_column(String(250, 'Modern_Spanish_CI_AS'), primary_key=True)
    DS_FIELD1: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD3: Mapped[Optional[str]] = mapped_column(String(250, 'Modern_Spanish_CI_AS'))
    DS_FIELD4: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD5: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD6: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD7: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD8: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD9: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD10: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD11: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD12: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD13: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD14: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD15: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD16: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD17: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD18: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD19: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD20: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD21: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD22: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD23: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD24: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD25: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD26: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD27: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD28: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD29: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD30: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD31: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD32: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD33: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD34: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD35: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD36: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD37: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD38: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD39: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))
    DS_FIELD40: Mapped[Optional[str]] = mapped_column(String(255, 'Modern_Spanish_CI_AS'))


class SAladi2(Base):
    __tablename__ = 'sAladi2'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='sAla_PKSysID'),
        Index('sAla_AKFraccAcuePaisSysID', 'FRACCION', 'ACUERDO', 'PAIS', 'SYSID', unique=True)
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ACUERDO: Mapped[Optional[str]] = mapped_column(String(49, 'Modern_Spanish_CI_AS'))
    PAIS: Mapped[Optional[str]] = mapped_column(String(3, 'Modern_Spanish_CI_AS'))
    TASATXT: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    TIPOTASA: Mapped[Optional[int]] = mapped_column(Integer)
    DOF: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    NOTAS: Mapped[Optional[str]] = mapped_column(String(499, 'Modern_Spanish_CI_AS'))
    OBSERVACIONES: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    TASANUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TASACALCULADA: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))


class SArchivosDescargados(Base):
    __tablename__ = 'sArchivosDescargados'
    __table_args__ = (
        PrimaryKeyConstraint('ARCHIVO', name='sArcDes_PKArchivo'),
    )

    ARCHIVO: Mapped[str] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    HORA: Mapped[Optional[int]] = mapped_column(Integer)


class SArchivosProcesados(Base):
    __tablename__ = 'sArchivosProcesados'
    __table_args__ = (
        PrimaryKeyConstraint('ARCHIVO', name='sArcPro_PKArchivo'),
    )

    ARCHIVO: Mapped[str] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'), primary_key=True)
    FECHA: Mapped[Optional[int]] = mapped_column(Integer)
    HORA: Mapped[Optional[int]] = mapped_column(Integer)


class SFracciones(Base):
    __tablename__ = 'sFracciones'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='sFracc_PKSysID'),
        Index('sFracc_AKFraccionSysID', 'FRACCION', 'SYSID', unique=True)
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCIONPUNTO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    UMCLAVE: Mapped[Optional[str]] = mapped_column(String(2, 'Modern_Spanish_CI_AS'))
    UMABREVIACION: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    ADVIMPOTXT: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ADVIMPONUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TIPOTASAADVIMPO: Mapped[Optional[int]] = mapped_column(Integer)
    ADVEXPOTXT: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ADVEXPONUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TIPOTASAADVEXPO: Mapped[Optional[int]] = mapped_column(Integer)
    TASAIVAFRANJA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TASAIVAINTERIOR: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TASAISAN: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    ARANCELMIXTO: Mapped[Optional[str]] = mapped_column(CHAR(1, 'Modern_Spanish_CI_AS'))
    TASAMIXTA: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(11, 6))
    DOF: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    NOTAS: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    HISTORICO: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))
    ARANCELESPECIFICO: Mapped[Optional[str]] = mapped_column(CHAR(1, 'Modern_Spanish_CI_AS'))
    TIPOVEHICULO: Mapped[Optional[str]] = mapped_column(CHAR(1, 'Modern_Spanish_CI_AS'))
    APLICAISAN: Mapped[Optional[str]] = mapped_column(CHAR(1, 'Modern_Spanish_CI_AS'))
    APLICAIEPS: Mapped[Optional[str]] = mapped_column(CHAR(1, 'Modern_Spanish_CI_AS'))
    NIVEL: Mapped[Optional[int]] = mapped_column(Integer)


class SFraccionesAnteriores(Base):
    __tablename__ = 'sFraccionesAnteriores'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='sFracAnt_PKSysID'),
        Index('sFracAnt_AKFracActFracAnt', 'FRACCIONACTUAL', 'FRACCIONANTERIOR', unique=True)
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCIONACTUAL: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    FRACCIONANTERIOR: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))


class SFraccionesCortas(Base):
    __tablename__ = 'sFraccionesCortas'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='FraCor_PKConsecutivo'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    DECRIPCIONCORTA: Mapped[Optional[str]] = mapped_column(String(100, 'Modern_Spanish_CI_AS'))
    DESCRIPCIONLARGA: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))


class SFraccionesResumidas(Base):
    __tablename__ = 'sFraccionesResumidas'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='FRR_PKLinea'),
        Index('FRR_AKFraccionSinPunto', 'FRACCION_SIN_PUNTO')
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION_SIN_PUNTO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    FRACCION_CON_PUNTO: Mapped[Optional[str]] = mapped_column(String(10, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))


class SFraccionesUSA(Base):
    __tablename__ = 'sFracciones_USA'
    __table_args__ = (
        PrimaryKeyConstraint('CONSECUTIVO', name='SFR_PKID'),
    )

    CONSECUTIVO: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION_SIN_PUNTO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FRACCION_CON_PUNTO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    FRACCION_MOSTRAR: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ESPECIFICO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    NIVEL: Mapped[Optional[int]] = mapped_column(Integer)
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    UNIDADCANTIDAD: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    TARIFA1: Mapped[Optional[str]] = mapped_column(String(250, 'Modern_Spanish_CI_AS'))
    TLC: Mapped[Optional[str]] = mapped_column(String(5000, 'Modern_Spanish_CI_AS'))
    TARIFA2: Mapped[Optional[str]] = mapped_column(String(250, 'Modern_Spanish_CI_AS'))
    NOTAS: Mapped[Optional[str]] = mapped_column(String(7998, 'Modern_Spanish_CI_AS'))


class SHistoricoReit(Base):
    __tablename__ = 'sHistoricoReit'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='sReitH_PKSysID'),
        Index('sReitH_AKFraccionSysID', 'FRACCION', 'SYSID', unique=True)
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ARTICULO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FUNDAMENTO: Mapped[Optional[str]] = mapped_column(String(1500, 'Modern_Spanish_CI_AS'))
    ACUERDO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    DOF: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    DOF2: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    DOF3: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    PERMISO: Mapped[Optional[str]] = mapped_column(CHAR(2, 'Modern_Spanish_CI_AS'))
    DOCUMENTO: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    TEMPORALIDAD: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TEMPORALIDADSERVICIOS: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TEMPORALIDADEMPRESACERTIFICADA: Mapped[Optional[int]] = mapped_column(SmallInteger)


class SProsec(Base):
    __tablename__ = 'sProsec'
    __table_args__ = (
        PrimaryKeyConstraint('FRACCION', 'ARTICULO', 'SECTOR', name='sProc_PKFraccionArtSector'),
        Index('sProc_AKSysID', 'SYSID', unique=True)
    )

    FRACCION: Mapped[str] = mapped_column(String(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    ARTICULO: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    SECTOR: Mapped[str] = mapped_column(String(6, 'Modern_Spanish_CI_AS'), primary_key=True)
    SYSID: Mapped[Optional[int]] = mapped_column(Integer)
    TASATXT: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    TASANUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    TIPOTASA: Mapped[Optional[int]] = mapped_column(Integer)
    DOF: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    OBSERVACION: Mapped[Optional[str]] = mapped_column(TEXT(2147483647, 'Modern_Spanish_CI_AS'))


class SRCG2(Base):
    __tablename__ = 'sRCG2'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='SRCG_SYSID'),
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    ANEXO: Mapped[Optional[str]] = mapped_column(String(19, 'Modern_Spanish_CI_AS'))
    SECTOR: Mapped[Optional[str]] = mapped_column(String(7999, 'Modern_Spanish_CI_AS'))
    REGIMEN: Mapped[Optional[str]] = mapped_column(String(1999, 'Modern_Spanish_CI_AS'))
    CONDICION: Mapped[Optional[str]] = mapped_column(String(7999, 'Modern_Spanish_CI_AS'))
    ADUANAS: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    DOF: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    ARCHIVOCRITERIO: Mapped[Optional[str]] = mapped_column(String(999, 'Modern_Spanish_CI_AS'))
    TIPO: Mapped[Optional[str]] = mapped_column(String(4, 'Modern_Spanish_CI_AS'))
    IMPO: Mapped[Optional[int]] = mapped_column(Integer)
    EXPO: Mapped[Optional[int]] = mapped_column(Integer)
    WEB_DOCUMENTO_ID: Mapped[Optional[int]] = mapped_column(Integer)


class SREIT(Base):
    __tablename__ = 'sREIT'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='sReit_PKSysID'),
        Index('sReit_AKFraccionSysID', 'FRACCION', 'SYSID', unique=True)
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    ARTICULO: Mapped[Optional[str]] = mapped_column(String(50, 'Modern_Spanish_CI_AS'))
    FUNDAMENTO: Mapped[Optional[str]] = mapped_column(String(1500, 'Modern_Spanish_CI_AS'))
    ACUERDO: Mapped[Optional[str]] = mapped_column(String(500, 'Modern_Spanish_CI_AS'))
    PERMISO: Mapped[Optional[str]] = mapped_column(CHAR(2, 'Modern_Spanish_CI_AS'))
    DOF: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    DOCUMENTO: Mapped[Optional[str]] = mapped_column(String(200, 'Modern_Spanish_CI_AS'))
    TEMPORALIDAD: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TEMPORALIDADSERVICIO: Mapped[Optional[int]] = mapped_column(SmallInteger)
    TEMPORALIDADCERTIFICADA: Mapped[Optional[int]] = mapped_column(SmallInteger)


class SRequisitoPrevio(Base):
    __tablename__ = 'sRequisitoPrevio'
    __table_args__ = (
        PrimaryKeyConstraint('SYSID', name='sReqPre_PKSysID'),
        Index('sReqPre_AKFraccionSysID', 'FRACCION', 'SYSID', unique=True)
    )

    SYSID: Mapped[int] = mapped_column(Integer, primary_key=True)
    FRACCION: Mapped[Optional[str]] = mapped_column(String(8, 'Modern_Spanish_CI_AS'))
    DESCRIPCION: Mapped[Optional[str]] = mapped_column(String(1999, 'Modern_Spanish_CI_AS'))
    OBSERVACION: Mapped[Optional[str]] = mapped_column(String(1999, 'Modern_Spanish_CI_AS'))
    DOF: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    VIGENCIA: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    PERMISO: Mapped[Optional[str]] = mapped_column(CHAR(2, 'Modern_Spanish_CI_AS'))
    NUMEROACUERDO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMEROCRITERIO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMEROFORMATO: Mapped[Optional[int]] = mapped_column(Integer)
    NUMEROINSTRUCCIONES: Mapped[Optional[int]] = mapped_column(Integer)
    HISTORICO: Mapped[Optional[str]] = mapped_column(String(2000, 'Modern_Spanish_CI_AS'))
    NOTA: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))


class STLCS(Base):
    __tablename__ = 'sTLCS'
    __table_args__ = (
        PrimaryKeyConstraint('FRACCION', 'PAIS', name='sTlc_PKFraccionPais'),
        Index('sTlc_AKSysID', 'SYSID', unique=True)
    )

    FRACCION: Mapped[str] = mapped_column(String(10, 'Modern_Spanish_CI_AS'), primary_key=True)
    PAIS: Mapped[str] = mapped_column(String(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    SYSID: Mapped[Optional[int]] = mapped_column(Integer)
    ORDEN: Mapped[Optional[int]] = mapped_column(Integer)
    TASATXT: Mapped[Optional[str]] = mapped_column(String(44, 'Modern_Spanish_CI_AS'))
    TIPOTASA: Mapped[Optional[int]] = mapped_column(Integer)
    TASA1NUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    FACTOR1: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 8))
    TASA2NUM: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 2))
    FACTOR2: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(13, 8))
    DOF: Mapped[Optional[str]] = mapped_column(CHAR(8, 'Modern_Spanish_CI_AS'))
    NOTAS: Mapped[Optional[str]] = mapped_column(String(1000, 'Modern_Spanish_CI_AS'))


t_sysdiagrams = Table(
    'sysdiagrams', Base.metadata,
    Column('name', Date, nullable=False),
    Column('principal_id', Integer, nullable=False),
    Column('diagram_id', Integer, nullable=False),
    Column('version', Integer),
    Column('definition', LargeBinary)
)
