
#         # This code allows you to install a orion-ld broker in a linux system
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#         # now the python code you can use to insert some value in the context broker according to the data model
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "MotionDeviceSystem"
subject = "dataModel.OPCUA"
controllers = [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:Controller'}, 'components': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:Component'}}], 'manufacturer': {'type': 'Property', 'value': 'Engineering Ingegneria Informatica'}, 'model': {'type': 'Property', 'value': 'Model'}, 'parameterSet': {'type': 'Property', 'value': {'cpuFanSpeed': 1600.0, 'cabinetFanSpeed': 2000.5, 'inputVoltage': 2500.0, 'startUpTime': '2020-10-19T07:36:06.713Z', 'temperature': 50.0, 'totalEnergyConsumption': 170.1, 'totalPowerOnTime': '', 'upsState': 'alive'}}, 'productCode': {'type': 'Property', 'value': 'MP695ENG004'}, 'serialNumber': {'type': 'Property', 'value': 'ENG-004'}, 'software': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:Software'}}], 'taskControls': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:TaskControl'}, 'componentName': {'type': 'Property', 'value': 'TaskControl'}, 'parameterSet': {'type': 'Property', 'value': {'taskProgramName': 'TaskProg', 'taskProgramLoaded': True, 'executionMode': 0}}}]}]
attribute = "controllers"
value = controllers
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

motionDevices = [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:MotionDevice'}, 'additionalComponents': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:AdditionalComponent'}}], 'axes': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:AxisX'}, 'motionProfile': {'type': 'Property', 'value': 'OTHER'}, 'parameterSet': {'type': 'Property', 'value': {'actualPosition': 1.0, 'actualSpeed': 2.5, 'actualAcceleration': 3.0}}}, {'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:AxisY'}, 'motionProfile': {'type': 'Property', 'value': 'LINEAR'}, 'parameterSet': {'type': 'Property', 'value': {'actualPosition': 1.5, 'actualSpeed': 2.0, 'actualAcceleration': 3.0}}}], 'manufacturer': {'type': 'Property', 'value': 'Engineering Ingegneria Informatica'}, 'model': {'type': 'Property', 'value': 'Model'}, 'motionDeviceCategory': {'type': 'Property', 'value': 'OTHER'}, 'powerTrains': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:PowerTrain'}, 'gears': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:Gear'}, 'gearRatio': {'type': 'Property', 'value': 0.5}, 'manufacturer': {'type': 'Property', 'value': 'Engineering Ingegneria Informatica'}, 'model': {'type': 'Property', 'value': 'Model'}, 'pitch': {'type': 'Property', 'value': 1.0}, 'productCode': {'type': 'Property', 'value': 'MP695ENG003'}, 'serialNumber': {'type': 'Property', 'value': 'ENG-003'}}], 'motors': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:Motor'}, 'manufacturer': {'type': 'Property', 'value': 'Engineering Ingegneria Informatica'}, 'model': {'type': 'Property', 'value': 'Model'}, 'parameterSet': {'type': 'Property', 'value': {'brakeReleased': True, 'effectiveLoadRate': 0, 'motorTemperature': 75}}, 'productCode': {'type': 'Property', 'value': 'MP695ENG002'}, 'serialNumber': {'type': 'Property', 'value': 'ENG-002'}}]}]}]
attribute = "motionDevices"
value = motionDevices
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

safetyStates = [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:SafetyState'}, 'emergencyStopFunctions': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:EmergencyStopFunction'}, 'active': {'type': 'Property', 'value': True}, 'name': {'type': 'Property', 'value': 'emergencyStop'}}], 'parameterSet': {'type': 'Property', 'value': {'emergencyStop': True, 'operationalMode': 'AUTOMATIC', 'protectiveStop': True}}, 'protectiveStopFunctions': [{'browseName': {'type': 'Property', 'value': 'uri:ngsi-ld:ProtectiveStopFunction'}, 'active': {'type': 'Property', 'value': True}, 'enabled': {'type': 'Property', 'value': True}, 'name': {'type': 'Property', 'value': 'protectiveStop'}}]}]
attribute = "safetyStates"
value = safetyStates
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
