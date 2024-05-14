import cmath
from math import pi

class Resistor:
    def __init__(self,resistance):
        self.resistance=resistance
    def impedance_of_resistor(self):
        return self.resistance
class Capacitor:
    def __init__(self,capacitance):
        self.capacitance=capacitance
    def impedance_of_capacitance(self,frequency):
        return 1/(1j*2*pi*frequency*self.capacitance)
class inductor:
    def __init__(self,inductance):
        self.inductance=inductance
    def impedanace_of_inductor(self,frequency):
        return 1j*2*pi*frequency*self.inductance
class Circuit:
    def __init__(self,resistance,inductance,capacitance):
        self.inductance=inductance
        self.capacitance=capacitance
        self.resistance=resistance
    def connection(self,series=True):
        if series is True:
            self.total_impedance=self.resistance+self.inductance+self.capacitance
        else:
            self.total_impedance=1/(1/self.resistance+1/self.capacitance+1/self.inductance)
        return self.total_impedance
    def voltage(self,current):
        self.voltage=current*self.total_impedance
        return self.voltage

def test_resistor_impedance():
    resistor = Resistor(1000)
    impedance_of_resistor = resistor.impedance_of_resistor()  # Assuming frequency of 1000 Hz
    return impedance_of_resistor

def test_series_connection():
    circuit = Circuit(1000, 1e-3, 1e-9)
    impedance = circuit.connection(series=True)
    impedance_of_resistor = test_resistor_impedance()
    expected_impedance = impedance_of_resistor + 1j * 2 * pi * 1000 * 1e-3 - 1j / (2 * pi * 1000 * 1e-6)
    return expected_impedance, impedance
  #assert abs(impedance - expected_impedance) < 1e-6, "Series impedance incorrect"


expected_impedance,Equivalent_impedance,= test_series_connection()
print("Impedance:", Equivalent_impedance)
print("Expected Impedance:", expected_impedance)
