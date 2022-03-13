input.onButtonPressed(Button.A, function () {
    Temperature = PlanetX_Basic.dht11Sensor(PlanetX_Basic.DigitalRJPin.J2, PlanetX_Basic.DHT11_state.DHT11_temperature_C)
    basic.showNumber(Temperature)
})
input.onButtonPressed(Button.B, function () {
    Humidite = PlanetX_Basic.dht11Sensor(PlanetX_Basic.DigitalRJPin.J2, PlanetX_Basic.DHT11_state.DHT11_humidity)
    basic.showNumber(Humidite)
})
let Humidite = 0
let Temperature = 0
basic.showIcon(IconNames.House)
basic.pause(100)
basic.clearScreen()
basic.forever(function () {
    Temperature = PlanetX_Basic.dht11Sensor(PlanetX_Basic.DigitalRJPin.J2, PlanetX_Basic.DHT11_state.DHT11_temperature_C)
    if (Temperature >= 25) {
        basic.showIcon(IconNames.Surprised)
    } else {
        if (Temperature <= 20) {
            basic.showIcon(IconNames.Sad)
        } else {
            for (let index = 0; index < 4; index++) {
                basic.showIcon(IconNames.Heart)
                basic.showIcon(IconNames.SmallHeart)
            }
        }
    }
})
