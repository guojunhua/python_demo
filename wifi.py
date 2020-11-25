from segno import helpers

qr = helpers.make_wifi(ssid="android", password="guo123456", security="WPA2")
qr.save("wifi.png", scale=20)
