import serial
ser = serial.Serial(
         port='/dev/ttyS0',
         baudrate =62500 ,
         parity=serial.PARITY_NONE,
         stopbits=serial.STOPBITS_ONE,
         bytesize=serial.EIGHTBITS,
         timeout=1
)

def load(data2):
    counter = 1
    data = []
    id = 0
    parameterNum = 0
    parameterValue = 0
    checkSum = 0
    while 1:
        if counter<11 :
            x = ser.read()
            data.append(x)
            counter += 1
        else:
            counter=1
            # print(data)
#            myfile.write(str(id)+" "+str(parameterNum)+" "+str(parameterValue)$
            try:
                print(data)
                id=int(data[1])
                parameterNum=int(data[2]+data[3])
                parameterValue=int(data[4]+data[5]+data[6])
                checkSum=int(data[7]+data[8])
#                print(int(data[1])+int(data[2])+int(data[3])+int(data[4])+int($
#                print(checkSum)
                if int(data[1])+int(data[2])+int(data[3])+int(data[4])+int(data[5])+int(data[6]) is checkSum:
                    # print(id)
                    # print(parameterNum)
                    # print(parameterValue)
                    if parameterNum >=0 and parameterNum <=47:
                        if parameterNum is 0:
                            data2.append({"name":"CalParNum", "id":id,"parameterNum":parameterNum,"parameterValue":parameterValue})
                        elif parameterNum is 1:
                            data2.append ( {"name": "DsplFlagParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 2:

                            data2.append ({"name": "Rpm2ParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 3:

                            data2.append ({"name": "Fsp2ParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 4:

                            data2.append ( {"name": "Set2ParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 5:

                            data2.append({"name": "Code2ParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 6:

                            data2.append ({"name": "CodeParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 7:

                            data2.append ({"name": "HspParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 8:

                            data2.append ({"name": "LspParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 9:

                            data2.append({"name": "DsplFlagParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 10:

                            data2.append ({"name": "JogParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 11:

                            data2.append({"name": "AccParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 12:

                            data2.append({"name": "DecParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 13:

                            data2.append ({"name": "JogAccParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 14:

                            data2.append ({"name": "JogDecParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 15:

                            data2.append ({"name": "McuParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 16:

                            data2.append ({"name": "BrpParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 17:

                            data2.append ({"name": "BrtParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})

                        elif parameterNum is 18:

                            data2.append({"name": "DiaiParNUm", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 19:

                            data2.append ({"name": "IanParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 20:

                            data2.append({"name": "OanParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 21:

                            data2.append ({"name": "FedParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 22:

                            data2.append ({"name": "SetParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 23:

                            data2.append({"name": "FdvParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 24:

                            data2.append({"name": "VchParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 25:

                            data2.append({"name": "TdlParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 26:

                            data2.append ({"name": "InoParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 27:

                            data2.append({"name": "UfaParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 28:

                            data2.append ( {"name": "ShvParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 29:

                            data2.append({"name": "IvParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 30:

                            data2.append({"name": "FrsParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 31:

                            data2.append ({"name": "FdcParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 32:

                            data2.append ( {"name": "SstParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 33:

                            data2.append ( {"name": "OvrParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 34:

                            data2.append ( {"name": "SfParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 35:

                            data2.append ( {"name": "Rl1ParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 36:

                            data2.append ( {"name": "CslParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 37:

                            data2.append ( {"name": "CshParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 38:

                            data2.append ( {"name": "FpoParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 39:

                            data2.append ({"name": "FanParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 40:

                            data2.append ({"name": "FtParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 41:

                            data2.append({"name": "FbParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 42:

                            data2.append({"name": "RpmParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 43:

                            data2.append({"name": "ArsParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 44:

                            data2.append({"name": "OvpParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 45:

                            data2.append({"name": "BypParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        elif parameterNum is 46:

                            data2.append({"name": "EopParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})
                        else:

                            data2.append ({"name": "CalParNum", "id": id, "parameterNum": parameterNum,
                                            "parameterValue": parameterValue})


                        # print data2
                        if parameterNum ==47:
                            break
                            # myfile.write(json.dump({"id":id,"parameterNum":parameterNum,"parameterValue":parameterValue}))
            except:
                print("check sum is not equal to value")
            del data[:]
