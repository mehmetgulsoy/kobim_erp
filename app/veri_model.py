import uuid
from sqlalchemy import Boolean, CHAR, Column, Date, DateTime, Enum, Float, Integer, SmallInteger, Table, Text, Time, \
    text
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy.dialects.postgresql.ranges import TSRANGE
from sqlalchemy.ext.declarative import declarative_base

from app import db

Base = declarative_base()
metadata = Base.metadata

e_parca_turu = Enum('', 'MİP İMALAT', 'MİP SATIN ALMA', 'YSN İMALAT', 'YSN SATIN ALMA', 'ANA ÇİZELGE', 'SAHTE', 'FASON', name='e_parca_turu')

class Ambar(db.Model):
    __tablename__ = 'ambar'
    __table_args__ = {'extend_existing': True}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    ambar = db.Column(Text)
    tanim = db.Column(Text)
    net_bayrak = db.Column(Boolean)
    ols_trh = db.Column(DateTime)
    sil_trh = db.Column(DateTime)
    gnc_trh = db.Column(DateTime, server_default=text("now()"))


class AmbarDetay(db.Model):
    __tablename__ = 'ambar_detay'
    __table_args__ = {'extend_existing': True}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    ambar_id = db.Column(UUID)
    parca = db.Column(UUID)
    eldeki = db.Column(Float(53))
    net_bayrak = db.Column(Boolean)
    lokasyon = db.Column(Text)
    ols_trh = db.Column(DateTime)
    sil_trh = db.Column(DateTime)
    gnc_trh = db.Column(DateTime, server_default=text("now()"))

class AmbarGeçmişi(db.Model):
    # __tablename__ = 'ambar_gecmi\u015fi'
    __tablename__ = 'ambar_gecmişi'
    __table_args__ = {'extend_existing': True}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    emir_id = db.Column(UUID)
    emir_turu = db.Column(Enum('TAHMİN', 'SİPARİŞ', 'ÇİZELGE', 'PLANLI', 'İMALAT', 'İSTEM', 'ALIM', 'SERVIS',
                               name='e_emir_turu'))
    parca_id = db.Column(UUID)
    kullanici = db.Column(UUID)
    tur = db.Column(Enum('GİRİŞ', 'ÇIKIŞ', 'SEVK', 'TRANSFER ÇIKIŞ', 'TRANSFER GİRİŞ', 'AYARLAMA', 'DEVRESEL SAYIM',
                         name='e_hareket_turu'))
    hrk_mkt = db.Column(Float)
    myt = db.Column(Float)
    eldeki = db.Column(Float(53))
    isl_trh = db.Column(DateTime, server_default=text("now()"))
    jdata = db.Column(JSONB(astext_type=Text()))


class Cari(db.Model):
    __tablename__ = 'cari'
    __table_args__ = {'extend_existing': True}

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    unvan = db.Column(Text)
    durum = db.Column(CHAR(1))
    firma_turu = db.Column(CHAR(1))
    telefon = db.Column(Text)
    fax = db.Column(Text)
    adres = db.Column(Text)
    ilce = db.Column(Text)
    il = db.Column(Text)
    ulke = db.Column(Text)
    para_brm = db.Column(Enum('TL', 'EURO', 'DOLAR', name='e_para_brm'))
    vergi_no = db.Column(Text)
    muhayyer_sevk = db.Column(UUID)
    muhasebe_kodu = db.Column(Text)
    ols_trh = db.Column(DateTime)
    sil_trh = db.Column(DateTime)
    gnc_trh = db.Column(DateTime, server_default=text("now()"))


class Emir(db.Model):
    __tablename__ = 'emir'
    __table_args__ = {'extend_existing': True}

    id= db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    emir_turu= db.Column(Enum('TAHMİN', 'SİPARİŞ', 'ÇİZELGE', 'PLANLI', 'İMALAT', 'İSTEM', 'ALIM', 'SERVIS', name='e_emir_turu'))
    emir= db.Column(Text)
    parca_id= db.Column(Integer)
    durum = db.Column(Enum('PLANLI', 'ONAYLI', 'AÇIK', 'TAMAMLANMIŞ', 'KAPATILMIŞ', 'İPTAL', name='e_emir_statu'))
    maliyet =db.Column(Float)
    orj_mkt =db.Column(Float)
    mkt= db.Column(Float)
    bakiye= db.Column(Float)
    orj_tslm_trh= db.Column(Date)
    teslim_trh = db.Column(Date)
    ols_trh= db.Column(DateTime)
    sil_trh= db.Column(DateTime)
    gnc_trh= db.Column(DateTime, server_default=text("now()"))


class Ihtiyac(db.Model):
    __tablename__ = 'ihtiyac'
    __table_args__ = {'extend_existing': True}

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    emir_id = db.Column(UUID(as_uuid=True))
    parca_id = db.Column(UUID(as_uuid=True))
    durum = db.Column(Enum('PLANLI', 'ONAYLI', 'AÇIK', 'TAMAMLANMIŞ', 'KAPATILMIŞ', 'İPTAL', name='e_emir_statu'))
    orj_mkt = db.Column(Float)
    mkt = db.Column(Float)
    bakiye = db.Column(Float)
    cikis_brm_mkt = db.Column(Float)
    cikis_mkt = db.Column(Float)
    teslim_trh = db.Column(Date)
    ols_trh = db.Column(DateTime)
    sil_trh = db.Column(DateTime)
    gnc_trh = db.Column(DateTime, server_default=text("now()"))
    
    
class Parca(db.Model):
    __tablename__ = 'parca'
    __table_args__ = {'extend_existing': True}

    id = db.Column(UUID(as_uuid=True), primary_key=True, default= uuid.uuid4())
    parca = db.Column(Text, nullable=False)
    aciklama = db.Column(Text, nullable=False)
    tur = db.Column(e_parca_turu)
    sinif_kodu = db.Column(Enum('A', 'B', 'C', name='e_stok_kodu'))
    planlayici = db.Column(UUID(as_uuid=True))
    satinalan = db.Column(UUID(as_uuid=True))
    uretim_atolyesi = db.Column(UUID(as_uuid=True))
    urun_grubu = db.Column(Text)
    adk = db.Column(SmallInteger)
    ua_ob = db.Column(Enum('ADET', 'KG', 'TON', 'LT', 'MT', 'M2', 'M3', name='e_olcu_birim'))
    statu = db.Column(Enum('PASİF', 'AKTİF', name='e_parca_statu'))
    gecerlilik_trh = db.Column(TSRANGE)
    agirlik = db.Column(Float(53))
    agirlik_brm = db.Column(Enum('ADET', 'KG', 'TON', 'LT', 'MT', 'M2', 'M3', name='e_olcu_birim'))
    revizyon = db.Column(Text)
    cizim_no = db.Column(Text)
    resim_yolu = db.Column(Text)
    birincil_ambar = db.Column(UUID(as_uuid=True))
    verim = db.Column(SmallInteger)
    ysn = db.Column(Float)
    ysm = db.Column(Float)
    emniyet_stok = db.Column(Float)
    min_mkt = db.Column(Float)
    mak_mkt = db.Column(Float)
    coklu_mkt = db.Column(Float)
    temin_suresi = db.Column(Integer)
    kts = db.Column(Integer)
    muhasebe_hesap = db.Column(Text)
    maliyet = db.Column(Float)
    maliyet_tur = db.Column(CHAR(1))
    fiyat = db.Column(Float)
    malzeme_myt = db.Column(Float)
    ua_malzeme_myt = db.Column(Float)
    sure = db.Column(Time)
    ua_sure = db.Column(Time)
    direk_iscilik_gider = db.Column(Float)
    genel_uretim_giderleri = db.Column(Float)
    ua_direk_iscilik_gider = db.Column(Float)
    ua_genel_uretim_giderleri = db.Column(Float)
    maliyet_gunu = db.Column(DateTime)
    lot_takib = db.Column(Boolean)
    seri_takip = db.Column(Boolean)
    raf_omru = db.Column(Integer)
    rota_degisim_no = db.Column(Integer)
    rota_degisim_trh = db.Column(DateTime)
    muhayyer_tedarikci = db.Column(UUID(as_uuid=True))
    ols_trh = db.Column(DateTime)
    sil_trh = db.Column(DateTime)
    gnc_trh = db.Column(DateTime, server_default=text("now()"))

    

t_parca_alim = Table(
    'parca_alim', metadata,
    Column('id', UUID),
    Column('parca_id', UUID),
    Column('cari_id', UUID),
    Column('fiyat', Float(53)),
    Column('ols_trh', DateTime),
    Column('sil_trh', DateTime),
    Column('gnc_trh', DateTime, server_default=text("now()"))
)


t_sevk_adres = Table(
    'sevk_adres', metadata,
    Column('id', UUID),
    Column('cari_id', UUID),
    Column('adres_id', Text),
    Column('fax', Text),
    Column('adres', Text),
    Column('ilce', Text),
    Column('il', Text),
    Column('ulke', Text),
    Column('ols_trh', DateTime),
    Column('sil_trh', DateTime),
    Column('gnc_trh', DateTime, server_default=text("now()"))
)


t_siparis_detay = Table(
    'siparis_detay', metadata,
    Column('id', UUID, nullable=False),
    Column('emir_turu', Enum('TAHMİN', 'SİPARİŞ', 'ÇİZELGE', 'PLANLI', 'İMALAT', 'İSTEM', 'ALIM', 'SERVIS', name='e_emir_turu')),
    Column('emir', Text),
    Column('parca_id', Integer),
    Column('durum', Enum('PLANLI', 'ONAYLI', 'AÇIK', 'TAMAMLANMIŞ', 'KAPATILMIŞ', 'İPTAL', name='e_emir_statu')),
    Column('maliyet', Float),
    Column('orj_mkt', Float),
    Column('mkt', Float),
    Column('bakiye', Float),
    Column('orj_tslm_trh', Date),
    Column('teslim_trh', Date),
    Column('ols_trh', DateTime),
    Column('sil_trh', DateTime),
    Column('gnc_trh', DateTime, server_default=text("now()")),
    Column('cari_id', UUID),
    Column('sip_veren_id', UUID),
    Column('mus_sip', Text),
    Column('sevk_adres_id', UUID),
    Column('temsilci_id', UUID),
    Column('odeme', Integer),
    Column('katagori', Text)
)


t_urun_agac = Table(
    'urun_agac', metadata,
    Column('id', UUID),
    Column('ana_parca', UUID),
    Column('bilesen_parca', UUID),
    Column('brm_mkt', Float),
    Column('gecerlilik', TSRANGE),
    Column('ambar', UUID),
    Column('ols_trh', DateTime),
    Column('sil_trh', DateTime),
    Column('gnc_trh', DateTime, server_default=text("now()"))
)
