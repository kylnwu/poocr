import unittest

from poocr.api.ocr import *
from poocr.api.ocr2excel import *


class TestTencent(unittest.TestCase):

    def test_vin_ocr(self):
        r = VatInvoiceOCR(img_path=r'C:\Users\Lenovo\Desktop\temp\增值税发票-test.jpg')
        print(r)

    def test_idcard_ocr(self):
        res = IDCardOCR(
            img_path=r'C:\Users\Lenovo\Desktop\temp\正面.jpg')
        print(res)

    def test_VatInvoiceOCR2Excel(self):
        VatInvoiceOCR2Excel(intput_path=r'C:\Users\Lenovo\Desktop\temp\Snipaste_2023-04-09_22-23-48.png',
                            output_excel=r'./VatInvoiceOCR2Excel.xlsx',
                            configPath=r'./poocr-config.toml')
    def test_TrainTicketOCR2Excel(self):
        TrainTicketOCR2Excel(input_path='', output_excel='',configPath='fdasf')