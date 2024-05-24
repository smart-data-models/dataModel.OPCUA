
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
#         # Version Warning! 
#         # This code is designed to work with the version 0.8 of pysmartdatamodels or later
#         # to work with earlier version you need to replace the import instruction for
#         # from pysmartdatamodels import pysmartdatamodels as sdm
#         
#         
import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "WoodworkingMachine"
subject = "dataModel.OPCUA"
Machines = [{'Identification': {'LocationPlant': 'Frankfurt', 'LocationGPS': '52.3235858255059, 9.804918108600956', 'CustomerCompanyName': 'Customer Company', 'ProductInstanceUri': 'some-company.com/5ff40f78-9210-494f-8206-c2c082f0609c', 'Manufacturer': 'Some Company', 'ManufacturerUri': '', 'Model': 'SawingMachine 9 Series', 'ProductCode': '', 'HardwareRevision': '', 'SoftwareRevision': '', 'DeviceClass': 'SawingMachine', 'SerialNumber': 'SM-9210', 'YearOfConstruction': 2022, 'MonthOfConstruction': 1, 'InitialOperationDate': '2022-01-01 10:00:00', 'AssetId': '', 'ComponentName': ''}, 'State': {'Machine': {'Overview': {'CurrentState': 'STANDBY', 'CurrentMode': 'AUTOMATIC'}, 'Flags': {'MachineOn': False, 'MachineInitialized': False, 'PowerPresent': False, 'AirPresent': False, 'DustChipSuction': False, 'Emergency': False, 'Safety': False, 'Calibrated': False, 'Remote': False, 'WorkpiecePresent': False, 'Moving': False, 'Error': False, 'Alarm': False, 'Warning': False, 'Hold': False, 'RecipeInRun': False, 'RecipeInSetup': False, 'RecipeInHold': False, 'ManualActivityRequired': False, 'LoadingEnabled': False, 'WaitUnload': False, 'WaitLoad': False, 'EnergySaving': False, 'ExternalEmergency': False, 'MaintenanceRequired': False, 'FeedRuns': False}, 'Values': {'AxisOverride': 0, 'SpindleOverride': 0, 'FeedSpeed': 0.0, 'ActualCycle': 0.0, 'AbsoluteMachineOffTime': 0, 'AbsoluteStandbyTime': 0, 'RelativeStandbyTime': 0, 'AbsoluteReadyTime': 0, 'RelativeReadyTime': 0, 'AbsoluteWorkingTime': 0, 'RelativeWorkingTime': 0, 'AbsoluteErrorTime': 0, 'RelativeErrorTime': 0, 'AbsoluteMachineOnTime': 0, 'RelativeMachineOnTime': 0, 'AbsoluteProductionTime': 0, 'RelativeProductionTime': 0, 'AbsoluteProductionWithoutWorkpieceTime': 0, 'RelativeProductionWithoutWorkpieceTime': 0, 'AbsoluteProductionWaitWorkpieceTime': 0, 'RelativeProductionWaitWorkpieceTime': 0, 'AbsoluteRunsGood': 0, 'RelativeRunsGood': 0, 'AbsoluteRunsAborted': 0, 'RelativeRunsAborted': 0, 'AbsoluteLength': 0, 'RelativeLength': 0, 'AbsolutePiecesIn': 0, 'RelativePiecesIn': 0, 'AbsolutePiecesOut': 0, 'RelativePiecesOut': 0}}}, 'Events': [{'EventCategory': 'OTHER', 'MessageId': 'A4711', 'MessageName': '', 'PathParts': ['Machine', 'FixedSide', 'Sizing', 'Milling1'], 'Group': '', 'LocalizedMessages': [], 'Arguments': []}], 'ManufacturerSpecific': {}}]
attribute = "Machines"
value = Machines
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
