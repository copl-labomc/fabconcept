from simple_pid import PID


pid = PID(1, 0.1, 0.05, setpoint=1)

# Assume we have a system we want to control in controlled_system
controlled_system = 0
v = controlled_system.update(0)
pid.output_limits = (0, 1)    # Output value will be between 0 and 10

while True:
    # Compute new output from the PID according to the systems current value
    control = pid(v)

    # Feed the PID output to the system and get its current value
    v = controlled_system.update(control)
    print(pid(current_value))