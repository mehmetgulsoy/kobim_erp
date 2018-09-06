from flask_wtf import FlaskForm
from sqlalchemy import Enum
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, HiddenField, SelectField , \
    IntegerField, TextField, FormField, DateTimeField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.veri_model import Cari, Parca


class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code')
    area_code    = IntegerField('Area Code/Exchange')
    number       = TextField('Number')


class CariForm(FlaskForm):
    id = HiddenField('id')
    unvan = StringField('Ünvan', validators=[DataRequired()], description='Firma Ünvanı')
    # durum = db.Column(CHAR(1))
    # firma_turu = db.Column(CHAR(1))
    telefon = StringField('Telefon', validators=[DataRequired()])
    fax = StringField('Fax', validators=[DataRequired()])
    adres = StringField('Adres', validators=[DataRequired()])
    ilce = StringField('İlce', validators=[DataRequired()], default='İSTAMBUL')
    il = StringField('İl', validators=[DataRequired()])
    ulke = StringField('Ülke', validators=[DataRequired()])
    para_brm = SelectField('Para Birimi', choices=[(g, g)for g in Cari.para_brm.property.columns[0].type.enums])
    vergi_no = StringField('Vergi No', validators=[DataRequired()])
    # muhayyer_sevk = db.Column(UUID)
    # muhasebe_kodu = db.Column(Text)
    # ols_trh = DateTimeField('Oluşturma tarihi')
    # sil_trh = db.Column(DateTime)
    # gnc_trh = db.Column(DateTime, server_default=text("now()"))
    submit = SubmitField('kayfet')


class MalzemeAramaForm(FlaskForm):
    arama = StringField('', validators=[DataRequired()])
    submit = SubmitField('ARA')


class MalzemeForm(FlaskForm):
    id = HiddenField('id')
    parca = StringField('Parça Kodu', validators=[DataRequired()])
    aciklama = TextAreaField(u'Açıklama', validators=[DataRequired()])
    tur = SelectField('Tür', choices=[(g, g)for g in Parca.tur.property.columns[0].type.enums])
    sinif_kodu = SelectField('Sınıf Kodu', choices=[(g, g)for g in Parca.sinif_kodu.property.columns[0].type.enums])
    # planlayici = Column(UUID)
    # satinalan = Column(UUID)
    # uretim_atolyesi = Column(UUID)
    urun_grubu = StringField('Ürün Grubu')
    adk = IntegerField('Alt Düzey Kodu')
    ua_ob = SelectField('Ölçü Birimi', choices=[(g,g) for g in Parca.ua_ob.property.columns[0].type.enums])
    statu = SelectField('Durum', choices=[(g, g) for g in Parca.statu.property.columns[0].type.enums], default='AKTİF')
    # gecerlilik_trh = Column(TSRANGE)
    agirlik = FloatField("Ağirlık", default=0)
    agirlik_brm = SelectField('Ağirlık Birimi', choices=[(g, g) for g in Parca.agirlik_brm.property.columns[0].type.enums])
    revizyon = StringField('Revizyon No')
    cizim_no = StringField('Çizim No')
    resim_yolu = StringField('Çizim Dosyayı')
    # birincil_ambar = Column(UUID)
    """
    verim = Column(SmallInteger)
    ysn = Column(Float)
    ysm = Column(Float)
    emniyet_stok = Column(Float)
    min_mkt = Column(Float)
    mak_mkt = Column(Float)
    coklu_mkt = Column(Float)
    temin_suresi = Column(Integer)
    kts = Column(Integer)
    muhasebe_hesap = Column(Text)
    maliyet = Column(Float)
    maliyet_tur = Column(CHAR(1))
    fiyat = Column(Float)
    malzeme_myt = Column(Float)
    ua_malzeme_myt = Column(Float)
    sure = Column(Time)
    ua_sure = Column(Time)
    direk_iscilik_gider = Column(Float)
    genel_uretim_giderleri = Column(Float)
    ua_direk_iscilik_gider = Column(Float)
    ua_genel_uretim_giderleri = Column(Float)
    maliyet_gunu = Column(DateTime)
    lot_takib = Column(Boolean)
    seri_takip = Column(Boolean)
    raf_omru = Column(Integer)
    rota_degisim_no = Column(Integer)
    rota_degisim_trh = Column(DateTime)
    muhayyer_tedarikci = Column(UUID)
"""
    submit = SubmitField('Kaydet')
