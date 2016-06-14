# -*- coding:utf-8 -*-
import shutil
import subprocess
import commands
import os
from common import Common
from book import Book
from topic import Topic
from magazine import Magazine
import time
import threading
from pyPdf import PdfFileReader,PdfFileWriter

def render_html(save_dir, filename,\
                page_filename="view.html", \
                css_filename="style.css", ):
    # cmd = "pdf2htmlEX \
    #         --split-pages 1 \
    #         --fit-width 860 \
    #         --page-filename {page_filename} \
    #         --embed-outline 0 \
    #         --embed-css 0 \
    #         --no-drm 1 \
    #         --css-filename {css_filename} \
    #         --dest-dir {save_dir} \
    #         {filename}".format(page_filename=page_filename,\
    #                             css_filename=css_filename,\
    #                             save_dir=save_dir,\
    #                             filename=filename)
    cmd = ["pdf2htmlEX", "--split-pages","1", "--fit-width","860",\
            "--page-filename", page_filename,\
            "--embed-outline","0", "--embed-css","0","--no-drm","1", \
            "--css-filename", css_filename,\
            "--dest-dir", save_dir, filename]
    subprocess.Popen(cmd)
    #return commands.getstatusoutput(cmd)

class Upload:

    def __init__(self, file_info, file_path):
        filename = "%s" % time.time()
        filepath = "file/%s/%s" % (file_info["category"], filename)
        file_info["path"] = os.path.join(filepath, filename+".pdf")
        save_dir = os.path.join(file_path["static_path"], filepath)
        if not os.path.isdir(save_dir):
            os.mkdir(save_dir)

        file_info["type"] = file_info["tmp_file"].split(".")[-1]
        file_info["realname"] = "%s.%s" %(filename, file_info["type"])
        file_info["realpath"] = os.path.join(filepath, file_info["realname"])

        if file_info["type"] != "pdf":
            self.convert2pdf(file_path["temp_path"], file_info["tmp_file"])
            shutil.move( file_info["tmp_file"], \
                                    os.path.join(save_dir, "%s.%s" \
                                            %(filename, file_info["type"])
                                            ))
            file_info["tmp_file"] = file_info["tmp_file"].replace(file_info["type"], "pdf")
        file_info["cover"] = "img/cover/%s.jpg" % filename
        filename += ".pdf"
        pdf_info = self.get_first_page(file_path["temp_path"], \
                                        file_info["tmp_file"])
        file_info["pages"] = pdf_info[1]
        if pdf_info[0] != "default_book.jpg":
            self.make_cover(os.path.join(file_path["static_path"], \
                                                file_info["cover"]), \
                                        os.path.join(file_path["temp_path"],\
                                                        pdf_info[0]))
        else:
            file_info["cover"] = "img/default_book.jpg"
        shutil.move(os.path.join(file_path["temp_path"], \
                                        file_info["tmp_file"]), \
                         os.path.join(save_dir, filename))
        status = render_html(save_dir, os.path.join(save_dir, filename))
        self.save(file_info)

    def save(self, file_info):
        globals()[file_info["category"].capitalize()]().save(file_info)

    def convert2pdf(self, outdir, filename):
        cmd = "libreoffice \
                --convert-to pdf \
                --outdir {outdir} \
                    {filename}".format(outdir=outdir, filename=filename)
        return commands.getstatusoutput(cmd)

    def get_first_page(self, temp_dir, filename):
        tmp_pdf = "%s.pdf" %time.time()
        pages = 999999
        try:
            with open(filename, "rb") as src, \
                    open(os.path.join(temp_dir, tmp_pdf), "wb") as tmp:
                pdf_file = PdfFileReader(src)
                pages = pdf_file.getNumPages()
                first = pdf_file.getPage(0)
                outer = PdfFileWriter()
                outer.addPage(first)
                outer.write(tmp)
        except:
            tmp_pdf = "default_book.jpg"
        return tmp_pdf, pages

    def make_cover(self, cover_name, filename):
        cmd = "convert \
                -density 150 \
                -quality 100 \
                    '{filename}' \
                    '{cover_name}'".format(filename=filename,\
                                            cover_name=cover_name)
        return commands.getstatusoutput(cmd)
