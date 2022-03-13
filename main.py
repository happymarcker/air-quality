def on_button_pressed_a():
    global Temperature
    Temperature = PlanetX_Basic.dht11_sensor(PlanetX_Basic.DigitalRJPin.J2,
        PlanetX_Basic.DHT11_state.DHT11_TEMPERATURE_C)
    basic.show_number(Temperature)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Humidite
    Humidite = PlanetX_Basic.dht11_sensor(PlanetX_Basic.DigitalRJPin.J2,
        PlanetX_Basic.DHT11_state.DHT11_HUMIDITY)
    basic.show_number(Humidite)
input.on_button_pressed(Button.B, on_button_pressed_b)

Humidite = 0
Temperature = 0
basic.show_icon(IconNames.HOUSE)
basic.pause(100)
basic.clear_screen()

def on_forever():
    global Temperature
    Temperature = PlanetX_Basic.dht11_sensor(PlanetX_Basic.DigitalRJPin.J2,
        PlanetX_Basic.DHT11_state.DHT11_TEMPERATURE_C)
    if Temperature >= 25:
        basic.show_icon(IconNames.SURPRISED)
    else:
        if Temperature <= 20:
            basic.show_icon(IconNames.SAD)
        else:
            for index in range(4):
                basic.show_icon(IconNames.HEART)
                basic.show_icon(IconNames.SMALL_HEART)
basic.forever(on_forever)
