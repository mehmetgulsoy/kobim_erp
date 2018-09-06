from flask import render_template, url_for, flash, redirect
from app.malzeme import bp
from app.malzeme.form import CariForm, MalzemeForm, MalzemeAramaForm
from app.veri_model import Cari, Parca
from app import db


@bp.route('/')
def index():
    return render_template('base4.html')


@bp.route('/cari', methods=['GET', 'POST'])
def cari():
    form = CariForm()
    form.vergi_no(style="width: 200px;", class_="bar")
    if form.validate_on_submit():
        c = Cari()
        c.unvan = form.unvan.data
        c.il = form.il.data
        c.ilce = form.ilce.data
        c.para_brm = form.para_brm.data

        db.session.add(c)
        db.session.commit()
        if form.id.data != "":
            flash('Cari güncellendi.')
        else:
            flash('Yeni Cari Oluşturuldu.')

        return redirect(url_for('malzeme.cari'))
    return render_template('selam.html', form=form)


@bp.route('/parca_ara', methods=['GET', 'POST'])
def parca_ara():
    p = Parca.query.all()

    return render_template('parca_ara.html', form=None, parcalar=p)


@bp.route('/parca_ekle', methods=['GET', 'POST'])
def parca_ekle():
    form = MalzemeForm()

    if form.validate_on_submit():
        p = Parca()
        # p.id = form.id.data
        p.parca = form.parca.data
        p.aciklama = form.aciklama.data
        p.tur = form.tur.data
        p.sinif_kodu = form.sinif_kodu.data
        db.session.add(p)
        db.session.commit()
        flash('Yeni Parça Oluşturuldu.')
        return redirect(url_for('malzeme.parca_ekle'))
    elif form.is_submitted():
        flash(form.errors)
    return render_template('parca_ekle.html', form=form)


@bp.route('/parca_guncelle', methods=['GET'])
@bp.route('/parca_guncelle/<id>', methods=['GET', 'POST'])
def parca_guncelle(id=None):

    if id is None:
        arama_form = MalzemeAramaForm()
        return render_template('parca_ara.html', form=arama_form)

    p = Parca.query.filter_by(id=id).first_or_404()
    form = MalzemeForm()
    form.id = p.id
    form.parca = p.parca
    form.aciklama = p.aciklama

    if form.validate_on_submit():
        p = Parca()
        p.aciklama = form.aciklama.data
        p.tur = form.tur.data
        p.sinif_kodu = form.sinif_kodu.data
        db.session.add(p)
        db.session.commit()
        flash('Parça Güncellendi.')
        return redirect(url_for('malzeme.parca_ekle'))
    elif form.is_submitted():
        flash(form.errors)
    return render_template('parca_ekle.html', form=form)


