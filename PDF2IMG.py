#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "kinoshitakenta"
__email__ = "ybs0306748@gmail.com"


from argparse import ArgumentParser
from configparser import ConfigParser
import os
from pathlib import Path, WindowsPath
import sys

from pdf2image import convert_from_path


def PDF2IMG(PDF_path: WindowsPath, img_format: str, dpi=500, userpw=None):
    pages = convert_from_path(PDF_path.as_posix(), dpi, userpw=userpw)
    PDF_without_suffix = PDF_path.stem

    for count, page in enumerate(pages, start=1):
        IMG_name = f"{PDF_without_suffix}_{count:03}.{img_format.lower()}"
        page.save(PDF_path.with_name(IMG_name), img_format)


def main(opt):
    PDF_path = Path(opt.PDF_path)

    cf = ConfigParser()
    cf.read(opt.config_ini)

    PASSWD = cf["permission"]["passwd"]
    img_format = cf["convert param"]["format"]
    dpi = cf["convert param"]["dpi"]

    password = PASSWD if PASSWD != "" else None

    PDF2IMG(PDF_path, img_format, dpi=dpi, userpw=password)


if __name__ == "__main__":
    work_path = Path(os.path.abspath(sys.argv[0]))
    os.chdir(work_path.parents[0])

    parser = ArgumentParser()
    parser.add_argument("PDF_path", type=str, help="source path of PDF")
    parser.add_argument("--config_ini", type=str,
                        help="read config path", default="config.ini")

    opt = parser.parse_args()

    main(opt)
