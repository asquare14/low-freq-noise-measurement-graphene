import injecti_2400
import applyv_2400
import srs760

def start_noise_measurements():
    print("Enter the value of voltage that you want to apply : \n")
    voltage = input()
    print("Enter compliance current : \n")
    compliance_current = input()
    print("Enter the value of current you want to inject : \n")
    current = input()
    print("Enter compliance voltage : \n")
    compliance_voltage = input()
    print("Enter span for SRS760. Here is the span table: \n")
    f = open("span.txt","r")
    print(f)
    f.close()
    span = input()
    print("Enter start frequency of span: \n")
    start_frequency_of_span = input()

    voltage = float(voltage)
    compliance_current = float(compliance_current)
    current = float(current)
    compliance_voltage = float(compliance_voltage)
    start_frequency_of_span = float(start_frequency_of_span)

    applyv_2400.applyv(voltage,compliance_current)
    injecti_2400.inject_i(current,compliance_voltage)
    srs760.start_srs()
    srs760.set_frequency(span,start_frequency_of_span)
    injecti_2400.shutdown_i()
    applyv_2400.shutdown_v()
    srs760.daq()
