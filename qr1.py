#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:47:21 2020

@author: nagln
"""

import qrcode
qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5
    )

data = "Hello I am a QRcode"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("1.png")