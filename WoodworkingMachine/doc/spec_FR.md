<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : WoodworkingMachine  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.OPCUA/blob/master/WoodworkingMachine/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **WoodworkingMachine est une machine qui est destinée à transformer le bois.**  
version : 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `Machines[array]`: . Liste de toutes les machines à bois gérées dans une usine. Chaque objet <Machine> représente une instance d'une machine. Dans le cas le plus simple, il n'y a qu'une seule machine.  - `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit s'agir de WoodworkingMachine.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `Machines`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapté de l'OPC UA original https://opcfoundation.org/developer-tools/specifications-opc-ua-information-models/opc-ua-for-woodworking pour travailler avec NGSI et répondre aux exigences minimales des Smart Data Models.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WoodworkingMachine:    
  description: 'WoodworkingMachine is a machine that is intended to process wood.'    
  properties:    
    Machines:    
      description: '. List of all woodworking machines managed in a plant. Each <Machine> Object represents an instance of a machine. In the simplest case, there is only one machine.'    
      items:    
        - properties:    
            Events:    
              description: 'Property. Model:''https://schema.org/StructuredValue''. The Events Object provides events.'    
              items:    
                - properties:    
                    Arguments:    
                      items: {}    
                      type: array    
                    EventCategory:    
                      enum:    
                        - OTHER    
                        - DIAGNOSTIC    
                        - INFORMATION    
                        - WARNING    
                        - ALARM    
                        - ERROR    
                      type: string    
                    Group:    
                      type: string    
                    LocalizedMessages:    
                      items: {}    
                      type: array    
                    MessageId:    
                      type: string    
                    MessageName:    
                      type: string    
                    PathParts:    
                      items: {}    
                      type: array    
                  type: object    
              type: array    
            Identification:    
              description: 'Property. Model:''https://schema.org/StructuredValue''. The Identification Object provides identification information of the woodworking machine.'    
              properties:    
                AssetId:    
                  type: string    
                ComponentName:    
                  type: string    
                CustomerCompanyName:    
                  type: string    
                DeviceClass:    
                  enum:    
                    - SawingMachine    
                    - ProfilingMachine    
                    - EdgebandingMachine    
                    - BoringMachine    
                    - SandingMachine    
                    - MachiningCenter    
                    - Press    
                    - HandlingMachine    
                  type: string    
                HardwareRevision:    
                  type: string    
                InitialOperationDate:    
                  type: string    
                Location:    
                  description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
                  oneOf: &woodworkingmachine_-_properties_-_location_-_oneof    
                    - description: 'Geoproperty. Geojson reference to the item. Point'    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            type: number    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - Point    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: 'GeoJSON Point'    
                      type: object    
                    - description: 'Geoproperty. Geojson reference to the item. LineString'    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              type: number    
                            minItems: 2    
                            type: array    
                          minItems: 2    
                          type: array    
                        type:    
                          enum:    
                            - LineString    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: 'GeoJSON LineString'    
                      type: object    
                    - description: 'Geoproperty. Geojson reference to the item. Polygon'    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              items:    
                                type: number    
                              minItems: 2    
                              type: array    
                            minItems: 4    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - Polygon    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: 'GeoJSON Polygon'    
                      type: object    
                    - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              type: number    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPoint    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: 'GeoJSON MultiPoint'    
                      type: object    
                    - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              items:    
                                type: number    
                              minItems: 2    
                              type: array    
                            minItems: 2    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiLineString    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: 'GeoJSON MultiLineString'    
                      type: object    
                    - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
                      properties:    
                        bbox:    
                          items:    
                            type: number    
                          minItems: 4    
                          type: array    
                        coordinates:    
                          items:    
                            items:    
                              items:    
                                items:    
                                  type: number    
                                minItems: 2    
                                type: array    
                              minItems: 4    
                              type: array    
                            type: array    
                          type: array    
                        type:    
                          enum:    
                            - MultiPolygon    
                          type: string    
                      required:    
                        - type    
                        - coordinates    
                      title: 'GeoJSON MultiPolygon'    
                      type: object    
                LocationGPS:    
                  type: string    
                LocationPlant:    
                  type: string    
                Manufacturer:    
                  type: string    
                ManufacturerUri:    
                  type: string    
                Model:    
                  type: string    
                MonthOfConstruction:    
                  type: integer    
                ProductCode:    
                  type: string    
                ProductInstanceUri:    
                  type: string    
                SerialNumber:    
                  type: string    
                SoftwareRevision:    
                  type: string    
                YearOfConstruction:    
                  type: integer    
              type: object    
            ManufacturerSpecific:    
              description: 'Property. Model:''https://schema.org/StructuredValue''. The ManufacturerSpecific Object provides manufacturer specific functionality.'    
              properties: {}    
              type: object    
            State:    
              description: 'Property. Model:''https://schema.org/StructuredValue''. The State Object provide information about the states of the machine.'    
              properties:    
                Machine:    
                  properties:    
                    Flags:    
                      properties:    
                        AirPresent:    
                          type: boolean    
                        Alarm:    
                          type: boolean    
                        Calibrated:    
                          type: boolean    
                        DustChipSuction:    
                          type: boolean    
                        Emergency:    
                          type: boolean    
                        EnergySaving:    
                          type: boolean    
                        Error:    
                          type: boolean    
                        ExternalEmergency:    
                          type: boolean    
                        FeedRuns:    
                          type: boolean    
                        Hold:    
                          type: boolean    
                        LoadingEnabled:    
                          type: boolean    
                        MachineInitialized:    
                          type: boolean    
                        MachineOn:    
                          type: boolean    
                        MaintenanceRequired:    
                          type: boolean    
                        ManualActivityRequired:    
                          type: boolean    
                        Moving:    
                          type: boolean    
                        PowerPresent:    
                          type: boolean    
                        RecipeInHold:    
                          type: boolean    
                        RecipeInRun:    
                          type: boolean    
                        RecipeInSetup:    
                          type: boolean    
                        Remote:    
                          type: boolean    
                        Safety:    
                          type: boolean    
                        WaitLoad:    
                          type: boolean    
                        WaitUnload:    
                          type: boolean    
                        Warning:    
                          type: boolean    
                        WorkpiecePresent:    
                          type: boolean    
                      type: object    
                    Overview:    
                      properties:    
                        CurrentMode:    
                          enum:    
                            - OTHER    
                            - AUTOMATIC    
                            - SEMIAUTOMATIC    
                            - MANUAL    
                            - SETUP    
                            - SLEEP    
                          type: string    
                        CurrentState:    
                          enum:    
                            - OFFLINE    
                            - STANDBY    
                            - READY    
                            - WORKING    
                            - ERROR    
                          type: string    
                      type: object    
                    Values:    
                      properties:    
                        AbsoluteErrorTime:    
                          type: integer    
                        AbsoluteLength:    
                          type: integer    
                        AbsoluteMachineOffTime:    
                          type: integer    
                        AbsoluteMachineOnTime:    
                          type: integer    
                        AbsolutePiecesIn:    
                          type: integer    
                        AbsolutePiecesOut:    
                          type: integer    
                        AbsoluteProductionTime:    
                          type: integer    
                        AbsoluteProductionWaitWorkpieceTime:    
                          type: integer    
                        AbsoluteProductionWithoutWorkpieceTime:    
                          type: integer    
                        AbsoluteReadyTime:    
                          type: integer    
                        AbsoluteRunsAborted:    
                          type: integer    
                        AbsoluteRunsGood:    
                          type: integer    
                        AbsoluteStandbyTime:    
                          type: integer    
                        AbsoluteWorkingTime:    
                          type: integer    
                        ActualCycle:    
                          type: number    
                        AxisOverride:    
                          type: integer    
                        FeedSpeed:    
                          type: number    
                        RelativeErrorTime:    
                          type: integer    
                        RelativeLength:    
                          type: integer    
                        RelativeMachineOnTime:    
                          type: integer    
                        RelativePiecesIn:    
                          type: integer    
                        RelativePiecesOut:    
                          type: integer    
                        RelativeProductionTime:    
                          type: integer    
                        RelativeProductionWaitWorkpieceTime:    
                          type: integer    
                        RelativeProductionWithoutWorkpieceTime:    
                          type: integer    
                        RelativeReadyTime:    
                          type: integer    
                        RelativeRunsAborted:    
                          type: integer    
                        RelativeRunsGood:    
                          type: integer    
                        RelativeStandbyTime:    
                          type: integer    
                        RelativeWorkingTime:    
                          type: integer    
                        SpindleOverride:    
                          type: integer    
                      type: object    
                  type: object    
              type: object    
          type: object    
      type: array    
      x-ngsi:    
        type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &woodworkingmachine_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *woodworkingmachine_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *woodworkingmachine_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be WoodworkingMachine'    
      enum:    
        - WoodworkingMachine    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - Machines    
  type: object    
  x-derived-from: https://opcfoundation.org/developer-tools/specifications-opc-ua-information-models/opc-ua-for-woodworking    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OPCUA/blob/master/WoodworkingMachine/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WoodworkingMachine/WoodworkingMachine/schema.json    
  x-model-tags: WoodworkingMachine    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Exemple de valeurs-clés NGSI-v2 de WoodworkingMachine  
Voici un exemple d'une WoodworkingMachine au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "WwMachine",  
  "type": "WoodWorkingMachine",  
  "Machines": [  
    {  
      "Identification": {  
        "LocationPlant": "Frankfurt",  
        "LocationGPS": "52.3235858255059, 9.804918108600956",  
        "CustomerCompanyName": "Customer Company",  
        "ProductInstanceUri": "some-company.com/5ff40f78-9210-494f-8206-c2c082f0609c",  
        "Manufacturer": "Some Company",  
        "ManufacturerUri": "",  
        "Model": "SawingMachine 9 Series",  
        "ProductCode": "",  
        "HardwareRevision": "",  
        "SoftwareRevision": "",  
        "DeviceClass": "SawingMachine",  
        "SerialNumber": "SM-9210",  
        "YearOfConstruction": 2022,  
        "MonthOfConstruction": 1,  
        "InitialOperationDate": "2022-01-01 10:00:00",  
        "AssetId": "",  
        "ComponentName": ""  
      },  
      "State": {  
        "Machine": {  
          "Overview": {  
            "CurrentState": "STANDBY",  
            "CurrentMode": "AUTOMATIC"  
          },  
          "Flags": {  
            "MachineOn": false,  
            "MachineInitialized": false,  
            "PowerPresent": false,  
            "AirPresent": false,  
            "DustChipSuction": false,  
            "Emergency": false,  
            "Safety": false,  
            "Calibrated": false,  
            "Remote": false,  
            "WorkpiecePresent": false,  
            "Moving": false,  
            "Error": false,  
            "Alarm": false,  
            "Warning": false,  
            "Hold": false,  
            "RecipeInRun": false,  
            "RecipeInSetup": false,  
            "RecipeInHold": false,  
            "ManualActivityRequired": false,  
            "LoadingEnabled": false,  
            "WaitUnload": false,  
            "WaitLoad": false,  
            "EnergySaving": false,  
            "ExternalEmergency": false,  
            "MaintenanceRequired": false,  
            "FeedRuns": false  
          },  
          "Values": {  
            "AxisOverride": 0,  
            "SpindleOverride": 0,  
            "FeedSpeed": 0.0,  
            "ActualCycle": 0.0,  
            "AbsoluteMachineOffTime": 0,  
            "AbsoluteStandbyTime": 0,  
            "RelativeStandbyTime": 0,  
            "AbsoluteReadyTime": 0,  
            "RelativeReadyTime": 0,  
            "AbsoluteWorkingTime": 0,  
            "RelativeWorkingTime": 0,  
            "AbsoluteErrorTime": 0,  
            "RelativeErrorTime": 0,  
            "AbsoluteMachineOnTime": 0,  
            "RelativeMachineOnTime": 0,  
            "AbsoluteProductionTime": 0,  
            "RelativeProductionTime": 0,  
            "AbsoluteProductionWithoutWorkpieceTime": 0,  
            "RelativeProductionWithoutWorkpieceTime": 0,  
            "AbsoluteProductionWaitWorkpieceTime": 0,  
            "RelativeProductionWaitWorkpieceTime": 0,  
            "AbsoluteRunsGood": 0,  
            "RelativeRunsGood": 0,  
            "AbsoluteRunsAborted": 0,  
            "RelativeRunsAborted": 0,  
            "AbsoluteLength": 0,  
            "RelativeLength": 0,  
            "AbsolutePiecesIn": 0,  
            "RelativePiecesIn": 0,  
            "AbsolutePiecesOut": 0,  
            "RelativePiecesOut": 0  
          }  
        }  
      },  
      "Events": [  
        {  
          "EventCategory": "OTHER",  
          "MessageId": "A4711",  
          "MessageName": "",  
          "PathParts": [  
            "Machine",  
            "FixedSide",  
            "Sizing",  
            "Milling1"  
          ],  
          "Group": "",  
          "LocalizedMessages": [],  
          "Arguments": []  
        }  
      ],  
      "ManufacturerSpecific": {}  
    }  
  ]  
}  
```  
</details>  
#### Machine à bois NGSI-v2 normalisée Exemple  
Voici un exemple d'une WoodworkingMachine au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:WoodWorkingMachine:WoodWorkingMachine:WwMachine",  
  "type": "WoodWorkingMachine",  
  "Machines": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "Identification": {  
          "type": "StructuredValue",  
          "value": {  
            "LocationPlant": "Frankfurt",  
            "LocationGPS": "52.3235858255059, 9.804918108600956",  
            "CustomerCompanyName": "Customer Company",  
            "ProductInstanceUri": "some-company.com/5ff40f78-9210-494f-8206-c2c082f0609c",  
            "Manufacturer": "Some Company",  
            "ManufacturerUri": "",  
            "Model": "SawingMachine 9 Series",  
            "ProductCode": "",  
            "HardwareRevision": "",  
            "SoftwareRevision": "",  
            "DeviceClass": "SawingMachine",  
            "SerialNumber": "SM-9210",  
            "YearOfConstruction": 2022,  
            "MonthOfConstruction": 1,  
            "InitialOperationDate": "2022-01-01 10:00:00",  
            "AssetId": "",  
            "ComponentName": ""  
          }  
        },  
        "State": {  
          "type": "StructuredValue",  
          "value": {  
            "Machine": {  
              "type": "StructuredValue",  
              "value": {  
                "Overview": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "CurrentState": "STANDBY",  
                    "CurrentMode": "AUTOMATIC"  
                  }  
                },  
                "Flags": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "MachineOn": false,  
                    "MachineInitialized": false,  
                    "PowerPresent": false,  
                    "AirPresent": false,  
                    "DustChipSuction": false,  
                    "Emergency": false,  
                    "Safety": false,  
                    "Calibrated": false,  
                    "Remote": false,  
                    "WorkpiecePresent": false,  
                    "Moving": false,  
                    "Error": false,  
                    "Alarm": false,  
                    "Warning": false,  
                    "Hold": false,  
                    "RecipeInRun": false,  
                    "RecipeInSetup": false,  
                    "RecipeInHold": false,  
                    "ManualActivityRequired": false,  
                    "LoadingEnabled": false,  
                    "WaitUnload": false,  
                    "WaitLoad": false,  
                    "EnergySaving": false,  
                    "ExternalEmergency": false,  
                    "MaintenanceRequired": false,  
                    "FeedRuns": false  
                  }  
                },  
                "Values": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "AxisOverride": 0,  
                    "SpindleOverride": 0,  
                    "FeedSpeed": 0.0,  
                    "ActualCycle": 0.0,  
                    "AbsoluteMachineOffTime": 0,  
                    "AbsoluteStandbyTime": 0,  
                    "RelativeStandbyTime": 0,  
                    "AbsoluteReadyTime": 0,  
                    "RelativeReadyTime": 0,  
                    "AbsoluteWorkingTime": 0,  
                    "RelativeWorkingTime": 0,  
                    "AbsoluteErrorTime": 0,  
                    "RelativeErrorTime": 0,  
                    "AbsoluteMachineOnTime": 0,  
                    "RelativeMachineOnTime": 0,  
                    "AbsoluteProductionTime": 0,  
                    "RelativeProductionTime": 0,  
                    "AbsoluteProductionWithoutWorkpieceTime": 0,  
                    "RelativeProductionWithoutWorkpieceTime": 0,  
                    "AbsoluteProductionWaitWorkpieceTime": 0,  
                    "RelativeProductionWaitWorkpieceTime": 0,  
                    "AbsoluteRunsGood": 0,  
                    "RelativeRunsGood": 0,  
                    "AbsoluteRunsAborted": 0,  
                    "RelativeRunsAborted": 0,  
                    "AbsoluteLength": 0,  
                    "RelativeLength": 0,  
                    "AbsolutePiecesIn": 0,  
                    "RelativePiecesIn": 0,  
                    "AbsolutePiecesOut": 0,  
                    "RelativePiecesOut": 0  
                  }  
                }  
              }  
            }  
          }  
        },  
        "Events": {  
          "type": "array",  
          "value": [  
            {  
              "EventCategory": "OTHER",  
              "MessageId": "A4711",  
              "MessageName": "",  
              "PathParts": [  
                "Machine",  
                "FixedSide",  
                "Sizing",  
                "Milling1"  
              ],  
              "Group": "",  
              "LocalizedMessages": [],  
              "Arguments": []  
            }  
          ]  
        }  
      }  
    ]  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.OPCUA/context.jsonld"  
  ]  
}  
```  
</details>  
#### Machine à bois Exemple de valeurs-clés NGSI-LD  
Voici un exemple de WoodworkingMachine au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:WoodWorkingMachine:WoodWorkingMachine:WwMachine",  
    "type": "WoodWorkingMachine",  
    "Machines": [  
        {  
            "Identification": {  
                "LocationPlant": "Frankfurt",  
                "LocationGPS": "52.3235858255059, 9.804918108600956",  
                "CustomerCompanyName": "Customer Company",  
                "ProductInstanceUri": "some-company.com/5ff40f78-9210-494f-8206-c2c082f0609c",  
                "Manufacturer": "Some Company",  
                "ManufacturerUri": "",  
                "Model": "SawingMachine 9 Series",  
                "ProductCode": "",  
                "HardwareRevision": "",  
                "SoftwareRevision": "",  
                "DeviceClass": "SawingMachine",  
                "SerialNumber": "SM-9210",  
                "YearOfConstruction": 2022,  
                "MonthOfConstruction": 1,  
                "InitialOperationDate": "2022-01-01 10:00:00",  
                "AssetId": "",  
                "ComponentName": ""  
            },  
            "State": {  
                "Machine": {  
                    "Overview": {  
                        "CurrentState": "STANDBY",  
                        "CurrentMode": "AUTOMATIC"  
                    },  
                    "Flags": {  
                        "MachineOn": false,  
                        "MachineInitialized": false,  
                        "PowerPresent": false,  
                        "AirPresent": false,  
                        "DustChipSuction": false,  
                        "Emergency": false,  
                        "Safety": false,  
                        "Calibrated": false,  
                        "Remote": false,  
                        "WorkpiecePresent": false,  
                        "Moving": false,  
                        "Error": false,  
                        "Alarm": false,  
                        "Warning": false,  
                        "Hold": false,  
                        "RecipeInRun": false,  
                        "RecipeInSetup": false,  
                        "RecipeInHold": false,  
                        "ManualActivityRequired": false,  
                        "LoadingEnabled": false,  
                        "WaitUnload": false,  
                        "WaitLoad": false,  
                        "EnergySaving": false,  
                        "ExternalEmergency": false,  
                        "MaintenanceRequired": false,  
                        "FeedRuns": false  
                    },  
                    "Values": {  
                        "AxisOverride": 0,  
                        "SpindleOverride": 0,  
                        "FeedSpeed": 0.0,  
                        "ActualCycle": 0.0,  
                        "AbsoluteMachineOffTime": 0,  
                        "AbsoluteStandbyTime": 0,  
                        "RelativeStandbyTime": 0,  
                        "AbsoluteReadyTime": 0,  
                        "RelativeReadyTime": 0,  
                        "AbsoluteWorkingTime": 0,  
                        "RelativeWorkingTime": 0,  
                        "AbsoluteErrorTime": 0,  
                        "RelativeErrorTime": 0,  
                        "AbsoluteMachineOnTime": 0,  
                        "RelativeMachineOnTime": 0,  
                        "AbsoluteProductionTime": 0,  
                        "RelativeProductionTime": 0,  
                        "AbsoluteProductionWithoutWorkpieceTime": 0,  
                        "RelativeProductionWithoutWorkpieceTime": 0,  
                        "AbsoluteProductionWaitWorkpieceTime": 0,  
                        "RelativeProductionWaitWorkpieceTime": 0,  
                        "AbsoluteRunsGood": 0,  
                        "RelativeRunsGood": 0,  
                        "AbsoluteRunsAborted": 0,  
                        "RelativeRunsAborted": 0,  
                        "AbsoluteLength": 0,  
                        "RelativeLength": 0,  
                        "AbsolutePiecesIn": 0,  
                        "RelativePiecesIn": 0,  
                        "AbsolutePiecesOut": 0,  
                        "RelativePiecesOut": 0  
                    }  
                }  
            },  
            "Events": [  
                {  
                    "EventCategory": "OTHER",  
                    "MessageId": "A4711",  
                    "MessageName": "",  
                    "PathParts": [  
                        "Machine",  
                        "FixedSide",  
                        "Sizing",  
                        "Milling1"  
                    ],  
                    "Group": "",  
                    "LocalizedMessages": [],  
                    "Arguments": []  
                }  
            ],  
            "ManufacturerSpecific": {}  
        }  
    ],  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.OPCUA/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OPCUA/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Machine à bois NGSI-LD normalisée Exemple  
Voici un exemple d'une WoodworkingMachine au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:WoodWorkingMachine:WoodWorkingMachine:WwMachine",  
    "type": "WoodWorkingMachine",  
    "Machines": {  
        "type": "Property",  
        "value": [  
            {  
                "Identification": {  
                    "type": "Property",  
                    "value": {  
                        "LocationPlant": "Frankfurt",  
                        "LocationGPS": "52.3235858255059, 9.804918108600956",  
                        "CustomerCompanyName": "Customer Company",  
                        "ProductInstanceUri": "some-company.com/5ff40f78-9210-494f-8206-c2c082f0609c",  
                        "Manufacturer": "Some Company",  
                        "ManufacturerUri": "",  
                        "Model": "SawingMachine 9 Series",  
                        "ProductCode": "",  
                        "HardwareRevision": "",  
                        "SoftwareRevision": "",  
                        "DeviceClass": "SawingMachine",  
                        "SerialNumber": "SM-9210",  
                        "YearOfConstruction": 2022,  
                        "MonthOfConstruction": 1,  
                        "InitialOperationDate": "2022-01-01 10:00:00",  
                        "AssetId": "",  
                        "ComponentName": ""  
                    }  
                },  
                "State": {  
                    "type": "Property",  
                    "value": {  
                        "Machine": {  
                            "type": "Property",  
                            "value": {  
                                "Overview": {  
                                    "type": "Property",  
                                    "value": {  
                                        "CurrentState": "STANDBY",  
                                        "CurrentMode": "AUTOMATIC"  
                                    }  
                                },  
                                "Flags": {  
                                    "type": "Property",  
                                    "value": {  
                                        "MachineOn": false,  
                                        "MachineInitialized": false,  
                                        "PowerPresent": false,  
                                        "AirPresent": false,  
                                        "DustChipSuction": false,  
                                        "Emergency": false,  
                                        "Safety": false,  
                                        "Calibrated": false,  
                                        "Remote": false,  
                                        "WorkpiecePresent": false,  
                                        "Moving": false,  
                                        "Error": false,  
                                        "Alarm": false,  
                                        "Warning": false,  
                                        "Hold": false,  
                                        "RecipeInRun": false,  
                                        "RecipeInSetup": false,  
                                        "RecipeInHold": false,  
                                        "ManualActivityRequired": false,  
                                        "LoadingEnabled": false,  
                                        "WaitUnload": false,  
                                        "WaitLoad": false,  
                                        "EnergySaving": false,  
                                        "ExternalEmergency": false,  
                                        "MaintenanceRequired": false,  
                                        "FeedRuns": false  
                                    }  
                                },  
                                "Values": {  
                                    "type": "Property",  
                                    "value": {  
                                        "AxisOverride": 0,  
                                        "SpindleOverride": 0,  
                                        "FeedSpeed": 0.0,  
                                        "ActualCycle": 0.0,  
                                        "AbsoluteMachineOffTime": 0,  
                                        "AbsoluteStandbyTime": 0,  
                                        "RelativeStandbyTime": 0,  
                                        "AbsoluteReadyTime": 0,  
                                        "RelativeReadyTime": 0,  
                                        "AbsoluteWorkingTime": 0,  
                                        "RelativeWorkingTime": 0,  
                                        "AbsoluteErrorTime": 0,  
                                        "RelativeErrorTime": 0,  
                                        "AbsoluteMachineOnTime": 0,  
                                        "RelativeMachineOnTime": 0,  
                                        "AbsoluteProductionTime": 0,  
                                        "RelativeProductionTime": 0,  
                                        "AbsoluteProductionWithoutWorkpieceTime": 0,  
                                        "RelativeProductionWithoutWorkpieceTime": 0,  
                                        "AbsoluteProductionWaitWorkpieceTime": 0,  
                                        "RelativeProductionWaitWorkpieceTime": 0,  
                                        "AbsoluteRunsGood": 0,  
                                        "RelativeRunsGood": 0,  
                                        "AbsoluteRunsAborted": 0,  
                                        "RelativeRunsAborted": 0,  
                                        "AbsoluteLength": 0,  
                                        "RelativeLength": 0,  
                                        "AbsolutePiecesIn": 0,  
                                        "RelativePiecesIn": 0,  
                                        "AbsolutePiecesOut": 0,  
                                        "RelativePiecesOut": 0  
                                    }  
                                }  
                            }  
                        }  
                    }  
                },  
                "Events": {  
                    "type": "Property",  
                    "value": [  
                        {  
                            "EventCategory": "OTHER",  
                            "MessageId": "A4711",  
                            "MessageName": "",  
                            "PathParts": [  
                                "Machine",  
                                "FixedSide",  
                                "Sizing",  
                                "Milling1"  
                            ],  
                            "Group": "",  
                            "LocalizedMessages": [],  
                            "Arguments": []  
                        }  
                    ]  
                },  
                "ManufacturerSpecific": {  
                    "type": "Property",  
                    "value": {}  
                }  
            }  
        ]  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.DigitalInnovationHub/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OPCUA/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
