
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
dataModel = "MachineTool"
subject = "dataModel.OPCUA"
myMachine = [{'notification': {'messages': [{'alertType': {'errorCode': '334'}, 'notificationEventType': {'identifier': '1'}}], 'prognoses': [{'prognosisN': {'predictedTime': '09:59:01Z'}, 'nodeVersion': '2'}]}, 'production': {'activeProgram': {'jobNodeId': 1, 'jobIdentifier': 'JobIdentifier', 'state': 1}, 'productionPlan': [{'customerOrderIdentifier': 'CustomerOrderIdentifier', 'identifier': 'Identifier', 'orderIdentifier': 'OrderIdentifier', 'partsCompleted': 1, 'partSets': [{'partSetN': {'name': '', 'partsPlannedPerRun': 0, 'partsCompletedPerRun': 0, 'partsPerRun': [{'customerOrderIdentifier': 'CustomerOrderIdentifier', 'name': 'Name', 'identifier': 'Identifier', 'partQuality': 0, 'processIrregularity': 0, 'state': 0}], 'containsMixedParts': True}}], 'partsGood': 1, 'productionPrograms': {'name': 'Name', 'numberInList': 0, 'state': 0}, 'runsCompleted': 2, 'runsPlanned': 3, 'state': 0}], 'statistics': [{'partsProducedInLifetime': 1}]}, 'identification': {'softwareIdentification': {'machineSoftware': {'softwareRevision': '0.5-Beta', 'identifier': 'MachineSoftware', 'manufacturer': 'AManufacturer'}, 'hmi': {'softwareRevision': '1.5', 'identifier': 'HMI-DesktopX', 'manufacturer': 'BManufacturer'}}}, 'equipment': {'tools': [{'toolN': {'name': 'Name', 'identifier': 'Identifier', 'location': {'name': 'Name', 'placeNumber': 0}}, 'nodeVersion': 'NodeVersion'}]}, 'monitoring': {'monitoredElementN': {'name': 'MonitoredElement_0'}, 'machineTool': {'feedOverride': 0, 'powerOnDuration': 1, 'operationMode': 2, 'isWarmUp': False}, 'stacklight': [{'signalOn': True, 'signalColor': 0, 'signalMode': 0}]}}]
attribute = "myMachine"
value = myMachine
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
