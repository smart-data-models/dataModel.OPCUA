<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: WoodworkingMachine    
===========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.OPCUA/blob/master/WoodworkingMachine/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Holzbearbeitungsmaschine ist eine Maschine, die für die Bearbeitung von Holz bestimmt ist.**    
Version: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `Machines[array]`: Liste aller in einem Werk verwalteten Holzbearbeitungsmaschinen. Jedes <Maschine>-Objekt stellt eine Instanz einer Maschine dar. Im einfachsten Fall gibt es nur eine Maschine  - `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Entitätstyp. Es muss WoodworkingMachine sein  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `Machines`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Angepasst von der ursprünglichen OPC UA https://opcfoundation.org/developer-tools/specifications-opc-ua-information-models/opc-ua-for-woodworking für die Arbeit mit NGSI und zur Erfüllung der Mindestanforderungen von Smart Data Models    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
WoodworkingMachine:      
  description: WoodworkingMachine is a machine that is intended to process wood.      
  properties:      
    Machines:      
      description: 'List of all woodworking machines managed in a plant. Each <Machine> Object represents an instance of a machine. In the simplest case, there is only one machine'      
      items:      
        properties:      
          Events:      
            description: The Events Object provides events      
            items:      
              properties:      
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
            x-ngsi:      
              model: https://schema.org/StructuredValue      
              type: Property      
          Identification:      
            description: The Identification Object provides identification information of the woodworking machine      
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
                description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
                oneOf:      
                  - bbox:      
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
                  - bbox:      
                      items:      
                        type: number      
                      minItems: 4      
                      type: array      
                    coordinates:      
                      items:      
                        items:      
                        minItems: 2      
                        type: array      
                      minItems: 2      
                      type: array      
                    type:      
                      enum:      
                        - LineString      
                      type: string      
                  - bbox:      
                      items:      
                        type: number      
                      minItems: 4      
                      type: array      
                    coordinates:      
                      items:      
                        items:      
                        minItems: 4      
                        type: array      
                      type: array      
                    type:      
                      enum:      
                        - Polygon      
                      type: string      
                  - bbox:      
                      items:      
                        type: number      
                      minItems: 4      
                      type: array      
                    coordinates:      
                      items:      
                        items:      
                        minItems: 2      
                        type: array      
                      type: array      
                    type:      
                      enum:      
                        - MultiPoint      
                      type: string      
                  - bbox:      
                      items:      
                        type: number      
                      minItems: 4      
                      type: array      
                    coordinates:      
                      items:      
                        items:      
                        minItems: 2      
                        type: array      
                      type: array      
                    type:      
                      enum:      
                        - MultiLineString      
                      type: string      
                  - bbox:      
                      items:      
                        type: number      
                      minItems: 4      
                      type: array      
                    coordinates:      
                      items:      
                        items:      
                        type: array      
                      type: array      
                    type:      
                      enum:      
                        - MultiPolygon      
                      type: string      
                x-ngsi:      
                  type: GeoProperty      
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
            x-ngsi:      
              model: https://schema.org/StructuredValue      
              type: Property      
          ManufacturerSpecific:      
            description: The ManufacturerSpecific Object provides manufacturer specific functionality      
            properties: {}      
            type: object      
            x-ngsi:      
              model: https://schema.org/StructuredValue      
              type: Property      
          State:      
            description: The State Object provide information about the states of the machine      
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
            x-ngsi:      
              model: https://schema.org/StructuredValue      
              type: Property      
        type: object      
      type: array      
      x-ngsi:      
        type: Property      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI entity type. It has to be WoodworkingMachine      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.OPCUA/blob/master/WoodworkingMachine/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WoodworkingMachine/WoodworkingMachine/schema.json      
  x-model-tags: WoodworkingMachine      
  x-version: 0.0.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### WoodworkingMachine NGSI-v2 Schlüsselwerte Beispiel    
Hier ist ein Beispiel für eine WoodworkingMachine im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### WoodworkingMachine NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für eine WoodworkingMachine im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
#### WoodworkingMachine NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für eine WoodworkingMachine im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### WoodworkingMachine NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für eine WoodworkingMachine im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
