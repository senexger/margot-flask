#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import sys
import slate3k as slate
# from datetime import datetime, timedelta

# from matriculation import Matriculation

# pdf parser
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

# TODO Verdammt. ldaptools ist python2
# sys.path.append('/net/local64') # Damit ldaptools gefunden wird
# import ldaptools

# DEBUG=True

# def margot(file_path, file_name):
# 	print("Das Spiel kann beginnen")
#
# 	file_name = file_path + '/' + file_name
# 	print(file_name)
# 	with open(file_name, 'rb') as f:
# 		doc = slate.PDF(f)
# 		doc
#
# 	return 1



def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        print(text)
        return text

if __name__ == '__main__':
    print(extract_text_from_pdf('w9.pdf'))

#
#if __name__ == "__main__":
#    # get pdf from parameter
#
#	# run pdfparser here
#
#    # CourseOfStudy = pdf.course
#    # name = pdf.name
#    # mat_nr = pdf.matNr
#    # date = pdf.expiration_t
#
#    print("hello World")
#    print('Number of arguments:', len(sys.argv), 'arguments.')
#    print('Argument List:', str(sys.argv))

# checke ob studiengang erlaubt ist
# from: https://www-pool.math.tu-berlin.de/wheel/wiki/index.php/Accountrichtlinien
# for c in CourseOfStudy:
# 	if c in ['Mathematik', 'Wirtschaftsmathematik', 'Technomathematik', 'Scientific Computing', 'Naturwissenschaften in der Informationstechnik', 'Physik'] :
# 		course_check = True
# 	else :
# 		course_check = False

# Wenn Studiengang erlaubt, checke Datum
# # VALIDATE DATA
# success = 1
# # course of study check
# if course_check:
# 	success = 2
# elif course_check == False :
# 	success = -1
# # Update check
# elif datetime.now() > datetime(date[0],date[1],date[2]):
# 	success = -2

# """NUTZERNAME AUS LDAP HOLEN mittels Matrikelnummer
# from: https://www-pool.math.tu-berlin.de/wheel/wiki/index.php/Ldaptools"""
# DEBUG: ldapsearch -Y GSSAPI -H ldap://ldap1-pool.math.tu-berlin.de -LLL -b "ou=People,dc=pool,dc=math,dc=tu-berlin,dc=de" '(uid=wtester)'

# if success > 0:
# 	print('ldap time')
# 	now = datetime.now()
# 	attributes = ldaptools.ldapsearch(ou='People',
# 		search_filter='(&(unixPoolBarcode=%s)(objectClass=unixPoolAccount)(unixPoolLV=stud))' %mat_nr,
# 		attr=['uid', 'cn'])
# 	for stud in attributes:
# 		for userUID in stud['uid']:
# 			# check UID
# Wenn Studiengang erlaubt, checke Datum
# # VALIDATE DATA
# success = 1
# # course of study check
# if course_check:
# 	success = 2
# elif course_check == False :
# 	success = -1
# # Update check
# elif datetime.now() > datetime(date[0],date[1],date[2]):
# 	success = -2

# 			# for more details: print(temp_acc)
#
# 			# extend account for one year
# 			temp_acc.krbPrincipalExpiration = datetime.now() + timedelta(days=365)
#
# 			# commit changes to ldap
# 			temp_acc.commit()
#
# 	for stud in attributes:
# 		for userCN in stud['cn']:
# 			print('cn: ' + userCN)

# #testdata:
# userCN = "Schn Tgai Spock"
# userUID = "Spock"

# #write kind and modular mail
#
# greeting = "Guten Tag " + userCN + ",\n"
# reasonSuccess = "ich habe deinen Account um ein Jahr verlängert. Dein Benutzername ist weiterhin " + userUID + ".\n\n"
# reasonSuccessMint = "ich habe deinen Account um ein Jahr verlängert. Dein Benutzername ist weiterhin " + userUID + ".\n\n"
# reasonWrongStudy = "ich darf deinen Account leider nicht verlängern, da dein Studiengang " + ", ".join(str(x) for x in CourseOfStudy) + " nicht mehr der Fakultät IV angehört. Bei weiteren Fragen wende dich bitte an die netten Kollegen an der Anmeldung im MA241.\n\n"
# reasonWrongDate = "ich darf deinen Account leider nicht verlängern, da deine Studienbescheinigung nicht mehr aktuell ist. Bei weiteren Fragen wende dich bitte an die netten Kollegen an der Anmeldung im MA241.\n\n"
# ending = "Liebe Grüße\nMargot"

# if success == -1:
# 	reason = reasonWrongStudy
# elif success == -2:
# 	reason = reasonWrongDate
# elif success == 2:
# 	reason = reasonWrongDate
# else:
# 	reason = reasonSuccess

# text = greeting + reason + ending

# #TODO send mail
# print(text)

# from net/....../erfassung.sh
#/usr/sbin/sendmail -i -f $SENDER $ERRRECEIP < $MAIL
#[ $? -eq 0 ] && writelog "ERROR mail sent"
