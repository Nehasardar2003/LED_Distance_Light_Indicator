# LED_Distance_Light_Indicator

This Arduino project uses an ultrasonic distance sensor (HC-SR04) to measure the distance of an object and indicates the distance using a series of LEDs. As the object moves closer to the sensor, more LEDs light up to show the distance range.

## Components Required

- Arduino Uno
- Ultrasonic Sensor HC-SR04
- 7 LEDs
- Resistors (220 ohm for each LED)
- Jumper Wires
- Breadboard

  ## Circuit Diagram

1. **HC-SR04 Connections:**
    - VCC to Arduino 5V
    - GND to Arduino GND
    - Trig to Arduino Pin 11
    - Echo to Arduino Pin 12

2. **LED Connections:**
    - LED1 to Arduino Pin 2
    - LED2 to Arduino Pin 3
    - LED3 to Arduino Pin 4
    - LED4 to Arduino Pin 5
    - LED5 to Arduino Pin 6
    - LED6 to Arduino Pin 7
    - LED7 to Arduino Pin 8

Each LED should have a resistor connected in series to limit the current.

## Code Explanation

The code initializes the pins for the ultrasonic sensor and the LEDs. In the loop function, it measures the distance using the ultrasonic sensor and lights up the LEDs according to the distance range.
