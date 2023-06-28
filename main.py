serial.redirect_to_usb()

def on_forever():
    serial.write_value("x", input.acceleration(Dimension.X))
    basic.pause(100)
    serial.write_value("y", input.acceleration(Dimension.Y))
    basic.pause(100)
    serial.write_value("z", input.acceleration(Dimension.Z))
basic.forever(on_forever)
