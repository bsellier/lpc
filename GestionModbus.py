from pyModbusTCP.client import ModbusClient
# TCP auto connect on first modbus request
c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)

# TCP auto connect on modbus request, close after it : dans la ligne suivante
# c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=True)
