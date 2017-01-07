# -*- coding: utf-8 -*-

from reportlab.lib.enums import TA_RIGHT,TA_LEFT,TA_CENTER
from reportlab.lib.pagesizes import A5

import arabic_reshaper

from bidi.algorithm import get_display
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import mm,cm,inch


defaultPageSize=A5

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()


pageinfo = "platypus example"


pdfmetrics.registerFont(TTFont('Arabic-2', 'trado.ttf'))
pdfmetrics.registerFont(TTFont('Arabic-3', 'pashtuab.ttf'))
style = ParagraphStyle(name='Normal', fontName='Arabic-3', fontSize=12, leading=12. * 1.2, rightIndent=10)
style.alignment = TA_RIGHT



def myFirstPage(canvas, doc):
     canvas.saveState()
     canvas.setFont('Arabic-3',10)
     # canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
     # canvas.drawString(PAGE_WIDTH, 1*mm, "First Page / %s" % pageinfo)

     arabic_text = get_display(arabic_reshaper.reshape(u'طبقا لمقتضيات الظهير الشريف'))
     canvas.drawCentredString(PAGE_WIDTH-320, PAGE_HEIGHT-15, arabic_text)

     arabic_text = get_display(arabic_reshaper.reshape(u'الصادر في 03 اكتوبر 2002'))
     canvas.drawCentredString(PAGE_WIDTH-320, PAGE_HEIGHT-30, arabic_text)

     arabic_text = get_display(arabic_reshaper.reshape(u'المملكة المغربية'))
     canvas.drawRightString(PAGE_WIDTH-70, PAGE_HEIGHT-15, arabic_text)

     arabic_text = get_display(arabic_reshaper.reshape(u'وزارة الداخلية                                                                                               '))
     canvas.drawRightString(PAGE_WIDTH-70, PAGE_HEIGHT-30, arabic_text)



     arabic_text = get_display(arabic_reshaper.reshape(u'عمالة او اقليم:'))
     canvas.drawRightString(PAGE_WIDTH-30, PAGE_HEIGHT-60, "field 1 " + arabic_text)

     arabic_text = get_display(arabic_reshaper.reshape(u'جماعة:'))
     canvas.drawRightString(PAGE_WIDTH-30, PAGE_HEIGHT-75, "field 2 " + arabic_text)

     arabic_text = get_display(arabic_reshaper.reshape(u'مكتب الحالة المدنية:'))
     canvas.drawRightString(PAGE_WIDTH-30, PAGE_HEIGHT-90, "field 3 " + arabic_text)

     arabic_text = get_display(arabic_reshaper.reshape(u'رسم رقم:'))
     canvas.drawRightString(PAGE_WIDTH-30, PAGE_HEIGHT-105, "field 4 " + arabic_text)

     arabic_text = get_display(arabic_reshaper.reshape(u'لسنة:'))
     canvas.drawRightString(PAGE_WIDTH-30, PAGE_HEIGHT-120, "field 5 " + arabic_text)
     arabic_text = get_display(arabic_reshaper.reshape(u'هجرية'))
     canvas.drawRightString(PAGE_WIDTH-130, PAGE_HEIGHT-120, arabic_text)

     arabic_text = get_display(arabic_reshaper.reshape(u'        '))
     canvas.drawRightString(PAGE_WIDTH-30, PAGE_HEIGHT-135, "field 6 " + arabic_text)
     arabic_text = get_display(arabic_reshaper.reshape(u'ميلادية'))
     canvas.drawRightString(PAGE_WIDTH-130, PAGE_HEIGHT-135, arabic_text)


     canvas.setFont('Arabic-2',36)

     arabic_text = get_display(arabic_reshaper.reshape(u'نسخة موجزة من رسم الولادة'))
     canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-165, arabic_text)


     canvas.setFont('Arabic-3',10)

     arabic_text = get_display(arabic_reshaper.reshape(u'الاسم الشخصي:'))
     canvas.drawRightString(PAGE_WIDTH-30, PAGE_HEIGHT-190, "field 7 " + arabic_text)
     canvas.drawString(PAGE_WIDTH-380, PAGE_HEIGHT-190, "Prénom:  " + "field 7 bis")

     arabic_text = get_display(arabic_reshaper.reshape(u'الاسم العائلي:'))
     canvas.drawRightString(PAGE_WIDTH-30, PAGE_HEIGHT-210, "field 8 " + arabic_text)
     canvas.drawString(PAGE_WIDTH-380, PAGE_HEIGHT-210, "Nom: " + "field 8 bis")

     canvas.restoreState()



def myLaterPages(canvas, doc):
     canvas.saveState()
     canvas.setFont('Times-Roman',9)
     canvas.drawString(mm, 0.75 * mm, "Page %d %s" % (doc.page, pageinfo))
     canvas.restoreState()



doc = SimpleDocTemplate("phello.pdf",pagesize=A5,rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5,showBoundary=0)

Story =  [] #[Spacer(0,0)]








p = Paragraph("", style)
Story.append(p)

# pdfmetrics.registerFont(TTFont('Arabic-5', 'DejaVuSans.ttf'))
# style = ParagraphStyle(name='Normal', fontName='Arabic-5', fontSize=12, leading=12. * 1.2)
# style.alignment = TA_RIGHT
# p = Paragraph(Title, style)
# Story.append(p)
# Story.append(Spacer(0,0*mm))

doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)


