from A_serialToExcel import SerialToExcel

serialToExcel = SerialToExcel("COM6",9600)

#columnas = ["Nro Lectura","Valor"]

serialToExcel.setColumns([" ","Bits CH1","Volts CH1","Bits CH2","Volts CH2","Bits CH3","Volts CH3","Bits CH4","Volts CH4","Bits CH1"])
serialToExcel.setRecordsNumber(10)
serialToExcel.readPort()

#filedialog.asksaveasfilename

serialToExcel.writeFile("archivo2.xls")
