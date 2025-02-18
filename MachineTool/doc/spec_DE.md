<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: MachineTool  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.OPCUA/blob/master/MachineTool/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Werkzeugmaschine ist ein feststehendes (d. h. nicht bewegliches) mechanisches Gerät, das mit Strom und Druckluft betrieben wird und typischerweise zur Bearbeitung von Werkstücken durch selektives Entfernen/Zufügen von Material oder mechanische Verformung verwendet wird**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `myMachine[array]`: Sie stellt die Liste der gesamten Werkzeugmaschinenschnittstelle des Informationsmodells dar  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Typ. Es muss MachineTool sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `myMachine`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MachineTool:    
  description: 'MachineTool is a mechanical device which is fixed (i.e. not mobile) and powered (typically by electricity and compressed air), typically used to process workpieces by selective removal/addition of material or mechanical deformation'    
  properties:    
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
        type: Relationship    
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
    myMachine:    
      description: It represents the list of entire machine tool interface of the information model    
      items:    
        description: It represents the entire machine tool interface of the information model    
        properties:    
          components:    
            description: ""    
            items:    
              description: (I have included this here because we need an structure of this array)    
              type: string    
              x-ngsi:    
                type: Property    
            type: array    
            x-ngsi:    
              type: Property    
          equipment:    
            description: It describes elements that are an inseparable part of the machine    
            properties:    
              tools:    
                description: 'It provides here shall contain the tools that are present in the machine and the magazines the machine has automated access to. '    
                items:    
                  description: It contains the description of the item    
                  properties:    
                    nodeVersion:    
                      description: It identifies the version node    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    toolN:    
                      description: Property.It Identifies the tool-n    
                      properties:    
                        identifier:    
                          description: 'It is a unique identifier for a tool. '    
                          type: string    
                          x-ngsi:    
                            type: Property    
                        location:    
                          description: 'It indicates where the tool is located, '    
                          properties:    
                            name:    
                              description: It specifies a name for the tool’s location (e.g. the tool magazine)    
                              type: string    
                              x-ngsi:    
                                type: Property    
                            placeNumber:    
                              description: It identifies the place number at this location    
                              type: number    
                              x-ngsi:    
                                type: Property    
                          type: object    
                          x-ngsi:    
                            type: Property    
                        name:    
                          description: 'It is used to name a tool to ease recognition. '    
                          type: string    
                          x-ngsi:    
                            type: Property    
                      type: object    
                  type: object    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          identification:    
            description: It describes the Machine Tools information model holds static data which shall uniquely identify a machine tool among a pool of the machine tool operating entity    
            properties:    
              softwareIdentification:    
                description: 'It contains the machine tool’s software identification information. It allows to add multiple software items, e.g. one for each of PLC, NC and HMI'    
                properties:    
                  hmi:    
                    description: 'Property.It provides a description of the hmi '    
                    properties:    
                      identifier:    
                        description: 'It provides an identifier to distinguish the software component. '    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      manufacturer:    
                        description: 'It refers to the manufacturer/producer of the software. '    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      softwareRevision:    
                        description: 'It provides a string representation of the version or revision level of the software component, the software/firmware of a hardware component. Examples are: “PLL01 1.10.0.3”, “V05.01.01.15”, “3.1 R1293”, “70.0.1” '    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                  machineSoftware:    
                    description: It identifies a machine software    
                    properties:    
                      identifier:    
                        description: It provides an identifier to distinguish the software component    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      manufacturer:    
                        description: It refers to the manufacturer/producer of the software    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      softwareRevision:    
                        description: 'It provides a string representation of the version or revision level of the software component, the software/firmware of a hardware component. Examples are: “PLL01 1.10.0.3”, “V05.01.01.15”, “3.1 R1293”, “70.0.1”'    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          monitoring:    
            description: It contains the monitoring information of the machine tool and its subsystems    
            properties:    
              machineTool:    
                description: It provides overall monitoring information of the machine tool    
                properties:    
                  feedOverride:    
                    description: It is the combined actual feed override value that is effective for the manufacturing program of the machine tool    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  isWarmUp:    
                    description: 'It being True indicates if the machine tool is performing a warmup task. A warmup is not used for production, it is the mode used to reach a stable operating point for the machine tool. An example is reaching the optimal operating temperature. This might be indicated by a hardware switch on the machine tool, a special control command, a special production program (referenced by program name) or otherwise'    
                    type: boolean    
                    x-ngsi:    
                      type: Property    
                  operationMode:    
                    description: 'It contains a Machine Operation Mode value as defined. It is an enum derived from the MO modes of machinery functional safety standards. For a machine adhering to such a standard, this property shall show the respective mode. For a machine not adhering to such a standard, this property shall be filled with the appropriate mode available from the Machine Operation Mode Enum'    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  powerOnDuration:    
                    description: 'It is the duration the machine has been powered, meaning all systems have line voltage. It is counted in full hours. This value only increases during the lifetime of the machine and is not reset when the machine is power cycled'    
                    type: number    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              monitoredElementN:    
                description: It describers the element-n monitored    
                properties:    
                  name:    
                    description: It refers to a name of the element    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              stacklight:    
                description: It contains the information about a stacklight’s composition and status    
                items:    
                  description: 'It describes one item '    
                  properties:    
                    signalColor:    
                      description: It specifies the color of the signal    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    signalMode:    
                      description: It specifies the mode of the signal    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    signalOn:    
                      description: It specifies if the signal  is On    
                      type: boolean    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          notification:    
            description: It is used to structure information given in the MachineTool. It groups the messages and alerts of the machine and contains the prognoses for the machining operation    
            properties:    
              messages:    
                description: 'It is used to define the object sending events. These events are used for errors, warnings and messages'    
                items:    
                  description: 'It is used to define the object event. This event is used for errors, warnings and messages'    
                  properties:    
                    alertType:    
                      description: It defines an alert type    
                      properties:    
                        errorCode:    
                          description: Identifies an error code    
                          type: string    
                          x-ngsi:    
                            type: Property    
                      type: object    
                      x-ngsi:    
                        type: Property    
                    notificationEventType:    
                      description: Defines an Event Notification Type    
                      properties:    
                        identifier:    
                          description: Identifies an Event Notification Type    
                          type: string    
                          x-ngsi:    
                            type: Property    
                      type: object    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
              prognoses:    
                description: It contains a list of the current prognoses for machine operation. Reliability for any prognosis in the list will rely on the specific case and cannot be guaranteed to be precise    
                items:    
                  description: It contains a prognosis for machine operation    
                  properties:    
                    nodeVersion:    
                      description: Identifies a node version    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    prognosisN:    
                      description: It contains a prognosis N for machine operation    
                      properties:    
                        predictedTime:    
                          description: 'It is used to indicate the point in time the predicted user interaction will become necessary. '    
                          type: string    
                          x-ngsi:    
                            type: Property    
                      type: object    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          production:    
            description: It is used to structure information given in the MachineTool. It groups the information about the production plan and the production statistics    
            properties:    
              activeProgram:    
                description: It is used to represent programs that are currently running within the machine    
                properties:    
                  jobIdentifier:    
                    description: It holds the same content as the Identifier Property of the Production Object instance this program is used in    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  jobNodeId:    
                    description: It contains the NodeId of the Production Object instance this program is used in    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  state:    
                    description: It is inherited from the Production Program Type and override to be mandatory    
                    type: number    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              productionPlan:    
                description: 'It  is a type used for structuring objects of Production Job Type in an ordered list structure. '    
                items:    
                  description: It provides aggregated production data for running a sequence to produce several parts after one preparation mounting    
                  properties:    
                    customerOrderIdentifier:    
                      description: 'It is used to reference the customer order this job belongs to. This information often originates from an external system handling production organisation '    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    identifier:    
                      description: 'It is the identifier of the job '    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    orderIdentifier:    
                      description: It is used to reference a company internal order the job belongs to. This information often originates from an external system handling production organisation    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    partSets:    
                      description: 'It contains a list of Production Part Set Type nodes related to the job. It is a list of the part sets, which contain the parts produced in the current run of the job. '    
                      items:    
                        description: It is used to group parts within a production job. It also contains information about the parts in the group    
                        properties:    
                          partSetN:    
                            description: It describes parts-N within a production job    
                            properties:    
                              containsMixedParts:    
                                description: It indicates if the parts in a Production Part Set may be different from each other (True) or if they are parts of the same type (False)    
                                type: boolean    
                                x-ngsi:    
                                  type: Property    
                              name:    
                                description: It is used to specify the type of parts in a group    
                                type: string    
                                x-ngsi:    
                                  type: Property    
                              partsCompletedPerRun:    
                                description: It indicates how many parts of this group have been completed in the current run of the job. This counter does not give any indication about the part quality    
                                type: integer    
                                x-ngsi:    
                                  type: Property    
                              partsPerRun:    
                                description: It contains a list of the parts in the current run of the job    
                                items:    
                                type: array    
                                x-ngsi:    
                                  type: Property    
                              partsPlannedPerRun:    
                                description: It indicates how many of the parts in this group are intended to be produced in one run of a job    
                                type: integer    
                                x-ngsi:    
                                  type: Property    
                            type: object    
                            x-ngsi:    
                              type: Property    
                        type: object    
                        x-ngsi:    
                          type: Property    
                      type: array    
                      x-ngsi:    
                        type: Property    
                    partsCompleted:    
                      description: 'It indicates how many parts have been completed in the current job including all runs. This counter does not give any indication about the part quality. '    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    partsGood:    
                      description: It indicates how many good parts have been completed in the current job including all runs    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    productionPrograms:    
                      description: 'It contains a list of Production Program nodes representing the programs used in the job. '    
                      properties:    
                        name:    
                          description: It is used to distinguish and identify programs on a machine    
                          type: string    
                          x-ngsi:    
                            type: Property    
                        numberInList:    
                          description: 'It is used to enumerate Production Program  instances used as list elements. This index shall be 0 for the first list element and increase by one for each subsequent list element. If nodes are deleted from the list or inserted into the list, the NumberInList has to be adjusted for all following nodes in the list, such that the NumberInList elements always form a sequential series of numbers'    
                          type: integer    
                          x-ngsi:    
                            type: Property    
                        state:    
                          description: 'It indicates the current state the job is in and the transition used to get into this state. '    
                          type: integer    
                          x-ngsi:    
                            type: Property    
                      type: object    
                      x-ngsi:    
                        type: Property    
                    runsCompleted:    
                      description: 'It is a counter that increases after each completed run of the job. This means, the run was not aborted and finished regularly. This counter does not give any indication about the part quality'    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    runsPlanned:    
                      description: 'It indicates how many times a job should be executed. '    
                      type: number    
                      x-ngsi:    
                        type: Property    
                    state:    
                      description: It indicates the current state the job is in and the transition used to get into this state    
                      type: number    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
              statistics:    
                description: 'It is the object that contains statistics information related to production. '    
                items:    
                  description: Item statistic    
                  properties:    
                    partsProducedInLifetime:    
                      description: 'It is the counter for the total number of produced parts during the machine’s lifetime. The exact way this number is acquired may differ between different machines. '    
                      type: number    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
                type: array    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
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
          type: Relationship    
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
      description: NGSI type. It has to be MachineTool    
      enum:    
        - MachineTool    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - myMachine    
  type: object    
  x-derived-from: https://reference.opcfoundation.org/MachineTool/v101/docs    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OPCUA/blob/master/MachineTool/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.MachineTool/MachineTool/schema.json    
  x-model-tags: MachineTool    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### MachineTool NGSI-v2 Schlüssel-Werte Beispiel  
Hier ist ein Beispiel für ein MachineTool im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "MachineTool:001",  
  "type": "MachineTool",  
  "myMachine": [  
    {  
      "notification": {  
        "messages": [  
          {  
            "alertType": {  
              "errorCode": "334"  
            },  
            "notificationEventType": {  
              "identifier": "1"  
            }  
          }  
        ],  
        "prognoses": [  
          {  
            "prognosisN": {  
              "predictedTime": "09:59:01Z"  
            },  
            "nodeVersion": "2"  
          }  
        ]  
      },  
      "production": {  
        "activeProgram": {  
          "jobNodeId": 1,  
          "jobIdentifier": "JobIdentifier",  
          "state": 1  
        },  
        "productionPlan": [  
          {  
            "customerOrderIdentifier": "CustomerOrderIdentifier",  
            "identifier": "Identifier",  
            "orderIdentifier": "OrderIdentifier",  
            "partsCompleted": 1,  
            "partSets": [  
              {  
                "partSetN": {  
                  "name": "",  
                  "partsPlannedPerRun": 0,  
                  "partsCompletedPerRun": 0,  
                  "partsPerRun": [  
                    {  
                      "customerOrderIdentifier": "CustomerOrderIdentifier",  
                      "name": "Name",  
                      "identifier": "Identifier",  
                      "partQuality": 0,  
                      "processIrregularity": 0,  
                      "state": 0  
                    }  
                  ],  
                  "containsMixedParts": true  
                }  
              }  
            ],  
            "partsGood": 1,  
            "productionPrograms": {  
              "name": "Name",  
              "numberInList": 0,  
              "state": 0  
            },  
            "runsCompleted": 2,  
            "runsPlanned": 3,  
            "state": 0  
          }  
        ],  
        "statistics": [  
          {  
            "partsProducedInLifetime": 1  
          }  
        ]  
      },  
      "identification": {  
        "softwareIdentification": {  
          "machineSoftware": {  
            "softwareRevision": "0.5-Beta",  
            "identifier": "MachineSoftware",  
            "manufacturer": "AManufacturer"  
          },  
          "hmi": {  
            "softwareRevision": "1.5",  
            "identifier": "HMI-DesktopX",  
            "manufacturer": "BManufacturer"  
          }  
        }  
      },  
      "equipment": {  
        "tools": [  
          {  
            "toolN": {  
              "name": "Name",  
              "identifier": "Identifier",  
              "location": {  
                "name": "Name",  
                "placeNumber": 0  
              }  
            },  
            "nodeVersion": "NodeVersion"  
          }  
        ]  
      },  
      "monitoring": {  
        "monitoredElementN": {  
          "name": "MonitoredElement_0"  
        },  
        "machineTool": {  
          "feedOverride": 0,  
          "powerOnDuration": 1,  
          "operationMode": 2,  
          "isWarmUp": false  
        },  
        "stacklight": [  
          {  
            "signalOn": true,  
            "signalColor": 0,  
            "signalMode": 0  
          }  
        ]  
      }  
    }  
  ]  
}  
```  
</details>  
#### MachineTool NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein MachineTool im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "MachineTool",  
  "type": "MachineTool",  
  "myMachine": {  
    "type": "array",  
    "value": [  
      {  
        "notification": {  
          "type": "StructuredValue",  
          "value": {  
            "messages": [  
              {  
                "type": "StructuredValue",  
                "value": {  
                  "alertType": {  
                    "type": "StructuredValue",  
                    "value": {  
                      "errorCode": "334"  
                    }  
                  },  
                  "notificationEventType": {  
                    "type": "StructuredValue",  
                    "value": {  
                      "identifier": "1"  
                    }  
                  }  
                }  
              }  
            ],  
            "prognoses": [  
              {  
                "type": "StructuredValue",  
                "value": {  
                  "prognosisN": {  
                    "type": "StructuredValue",  
                    "value": {  
                      "predictedTime": "09:59:01Z"  
                    }  
                  },  
                  "nodeVersion": "2"  
                }  
              }  
            ]  
          }  
        },  
        "production": {  
          "type": "StructuredValue",  
          "value": {  
            "activeProgram": {  
              "type": "StructuredValue",  
              "value": {  
                "jobNodeId": 1,  
                "jobIdentifier": "JobIdentifier",  
                "state": 1  
              }  
            },  
            "productionPlan": [  
              {  
                "type": "StructuredValue",  
                "value": {  
                  "customerOrderIdentifier": "CustomerOrderIdentifier",  
                  "identifier": "Identifier",  
                  "orderIdentifier": "OrderIdentifier",  
                  "partsCompleted": 1,  
                  "partSets": [  
                    {  
                      "type": "StructuredValue",  
                      "value": {  
                        "partSetN": {  
                          "type": "StructuredValue",  
                          "value": {  
                            "name": "",  
                            "partsPlannedPerRun": 0,  
                            "partsCompletedPerRun": 0,  
                            "partsPerRun": [  
                              {  
                                "customerOrderIdentifier": "CustomerOrderIdentifier",  
                                "name": "Name",  
                                "identifier": "Identifier",  
                                "partQuality": 0,  
                                "processIrregularity": 0,  
                                "state": 0  
                              }  
                            ],  
                            "containsMixedParts": true  
                          }  
                        }  
                      }  
                    }  
                  ],  
                  "partsGood": 1,  
                  "productionPrograms": {  
                    "type": "StructuredValue",  
                    "value": {  
                      "name": "Name",  
                      "numberInList": 0,  
                      "state": 0  
                    }  
                  },  
                  "runsCompleted": 2,  
                  "runsPlanned": 3,  
                  "state": 0  
                }  
              }  
            ],  
            "statistics": [  
              {  
                "type": "StructuredValue",  
                "value": {  
                  "partsProducedInLifetime": 1  
                }  
              }  
            ]  
          }  
        },  
        "identification": {  
          "type": "StructuredValue",  
          "value": {  
            "softwareIdentification": {  
              "type": "StructuredValue",  
              "value": {  
                "machineSoftware": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "softwareRevision": "0.5-Beta",  
                    "identifier": "MachineSoftware",  
                    "manufacturer": "AManufacturer"  
                  }  
                },  
                "hmi": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "softwareRevision": "1.5",  
                    "identifier": "HMI-DesktopX",  
                    "manufacturer": "BManufacturer"  
                  }  
                }  
              }  
            }  
          }  
        },  
        "equipment": {  
          "type": "StructuredValue",  
          "value": {  
            "tools": [  
              {  
                "type": "StructuredValue",  
                "value": {  
                  "toolN": {  
                    "name": "Name",  
                    "identifier": "Identifier",  
                    "location": {  
                      "type": "StructuredValue",  
                      "value": {  
                        "name": "Name",  
                        "placeNumber": 0  
                      }  
                    }  
                  },  
                  "nodeVersion": "NodeVersion"  
                }  
              }  
            ]  
          }  
        },  
        "monitoring": {  
          "type": "StructuredValue",  
          "value": {  
            "monitoredElementN": {  
              "type": "StructuredValue",  
              "value": {  
                "name": "MonitoredElement_0"  
              }  
            },  
            "machineTool": {  
              "type": "StructuredValue",  
              "value": {  
                "feedOverride": 0,  
                "powerOnDuration": 1,  
                "operationMode": 2,  
                "isWarmUp": false  
              }  
            },  
            "stacklight": [  
              {  
                "type": "StructuredValue",  
                "value": {  
                  "signalOn": true,  
                  "signalColor": 0,  
                  "signalMode": 0  
                }  
              }  
            ]  
          }  
        }  
      }  
    ]  
  }  
}  
```  
</details>  
#### MachineTool NGSI-LD Schlüssel-Werte Beispiel  
Hier ist ein Beispiel für ein MachineTool im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MachineTool:MachineTool",  
  "type": "MachineTool",  
  "myMachine": [  
    {  
      "notification": {  
        "messages": [  
          {  
            "alertType": {  
              "errorCode": "334"  
            },  
            "notificationEventType": {  
              "identifier": "1"  
            }  
          }  
        ],  
        "prognoses": [  
          {  
            "prognosisN": {  
              "predictedTime": "09:59:01Z"  
            },  
            "nodeVersion": "2"  
          }  
        ]  
      },  
      "production": {  
        "activeProgram": {  
          "jobNodeId": 1,  
          "jobIdentifier": "JobIdentifier",  
          "state": 1  
        },  
        "productionPlan": [  
          {  
            "customerOrderIdentifier": "CustomerOrderIdentifier",  
            "identifier": "Identifier",  
            "orderIdentifier": "OrderIdentifier",  
            "partsCompleted": 1,  
            "partSets": [  
              {  
                "partSetN": {  
                  "name": "",  
                  "partsPlannedPerRun": 0,  
                  "partsCompletedPerRun": 0,  
                  "partsPerRun": [  
                    {  
                      "customerOrderIdentifier": "CustomerOrderIdentifier",  
                      "name": "Name",  
                      "identifier": "Identifier",  
                      "partQuality": 0,  
                      "processIrregularity": 0,  
                      "state": 0  
                    }  
                  ],  
                  "containsMixedParts": true  
                }  
              }  
            ],  
            "partsGood": 1,  
            "productionPrograms": {  
              "name": "Name",  
              "numberInList": 0,  
              "state": 0  
            },  
            "runsCompleted": 2,  
            "runsPlanned": 3,  
            "state": 0  
          }  
        ],  
        "statistics": [  
          {  
            "partsProducedInLifetime": 1  
          }  
        ]  
      },  
      "identification": {  
        "softwareIdentification": {  
          "machineSoftware": {  
            "softwareRevision": "0.5-Beta",  
            "identifier": "MachineSoftware",  
            "manufacturer": "AManufacturer"  
          },  
          "hmi": {  
            "softwareRevision": "1.5",  
            "identifier": "HMI-DesktopX",  
            "manufacturer": "BManufacturer"  
          }  
        }  
      },  
      "equipment": {  
        "tools": [  
          {  
            "toolN": {  
              "name": "Name",  
              "identifier": "Identifier",  
              "location": {  
                "name": "Name",  
                "placeNumber": 0  
              }  
            },  
            "nodeVersion": "NodeVersion"  
          }  
        ]  
      },  
      "monitoring": {  
        "monitoredElementN": {  
          "name": "MonitoredElement_0"  
        },  
        "machineTool": {  
          "feedOverride": 0,  
          "powerOnDuration": 1,  
          "operationMode": 2,  
          "isWarmUp": false  
        },  
        "stacklight": [  
          {  
            "signalOn": true,  
            "signalColor": 0,  
            "signalMode": 0  
          }  
        ]  
      }  
    }  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.OPCUA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### MachineTool NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein MachineTool im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MachineTool:MachineTool",  
  "type": "MachineTool",  
  "myMachine": {  
    "type": "Property",  
    "value": {  
      "notification": {  
        "type": "Property",  
        "value": {  
          "messages": [  
            {  
              "type": "Property",  
              "alertType": {  
                "type": "Property",  
                "value": {  
                  "errorCode": "334"  
                }  
              },  
              "notificationEventType": {  
                "type": "Property",  
                "value": {  
                  "identifier": "1"  
                }  
              }  
            }  
          ],  
          "prognoses": [  
            {  
              "type": "Property",  
              "value": {  
                "prognosisN": {  
                  "type": "Property",  
                  "value": {  
                    "predictedTime": "09:59:01Z"  
                  }  
                },  
                "nodeVersion": "2"  
              }  
            }  
          ]  
        }  
      },  
      "production": {  
        "type": "Property",  
        "value": {  
          "activeProgram": {  
            "type": "Property",  
            "value": {  
              "jobNodeId": 1,  
              "jobIdentifier": "JobIdentifier",  
              "state": 1  
            }  
          },  
          "productionPlan": [  
            {  
              "type": "Property",  
              "value": {  
                "customerOrderIdentifier": "CustomerOrderIdentifier",  
                "identifier": "Identifier",  
                "orderIdentifier": "OrderIdentifier",  
                "partsCompleted": 1,  
                "partSets": [  
                  {  
                    "type": "Property",  
                    "value": {  
                      "partSetN": {  
                        "type": "Property",  
                        "value": {  
                          "name": "Name",  
                          "partsPlannedPerRun": 0,  
                          "partsCompletedPerRun": 0,  
                          "partsPerRun": [  
                            {  
                              "type": "Property",  
                              "value": {  
                                "customerOrderIdentifier": "CustomerOrderIdentifier",  
                                "name": "Name",  
                                "identifier": "Identifier",  
                                "partQuality": 0,  
                                "processIrregularity": 0,  
                                "state": 0  
                              }  
                            }  
                          ],  
                          "containsMixedParts": true  
                        }  
                      }  
                    }  
                  }  
                ],  
                "partsGood": 1,  
                "productionPrograms": {  
                  "type": "Property",  
                  "value": {  
                    "name": "Name",  
                    "numberInList": 0,  
                    "state": 0  
                  }  
                },  
                "runsCompleted": 2,  
                "runsPlanned": 3,  
                "state": 0  
              }  
            }  
          ],  
          "statistics": {  
            "type": "Property",  
            "value": [  
              {  
                "partsProducedInLifetime": 1  
              }  
            ]  
          }  
        }  
      },  
      "identification": {  
        "type": "Property",  
        "value": {  
          "softwareIdentification": {  
            "type": "Property",  
            "value": {  
              "machineSoftware": {  
                "type": "Property",  
                "value": {  
                  "softwareRevision": "0.5-Beta",  
                  "identifier": "MachineSoftware",  
                  "manufacturer": "AManufacturer"  
                }  
              },  
              "hmi": {  
                "type": "Property",  
                "value": {  
                  "softwareRevision": "1.5",  
                  "identifier": "HMI-DesktopX",  
                  "manufacturer": "BManufacturer"  
                }  
              }  
            }  
          }  
        }  
      },  
      "equipment": {  
        "type": "Property",  
        "value": {  
          "tools": [  
            {  
              "type": "Property",  
              "value": {  
                "toolN": {  
                  "type": "Property",  
                  "value": {  
                    "name": "Name",  
                    "identifier": "Identifier",  
                    "location": {  
                      "type": "Property",  
                      "value": {  
                        "name": "Name",  
                        "placeNumber": 0  
                      }  
                    }  
                  },  
                  "nodeVersion": "NodeVersion"  
                }  
              }  
            }  
          ]  
        }  
      },  
      "monitoring": {  
        "type": "Property",  
        "value": {  
          "monitoredElementN": {  
            "type": "Property",  
            "value": {  
              "name": "MonitoredElement_0"  
            }  
          },  
          "machineTool": {  
            "type": "Property",  
            "value": {  
              "feedOverride": 0,  
              "powerOnDuration": 1,  
              "operationMode": 2,  
              "isWarmUp": false  
            }  
          },  
          "stacklight": {  
            "type": "Property",  
            "value": [  
              {  
                "signalOn": true,  
                "signalColor": 0,  
                "signalMode": 0  
              }  
            ]  
          }  
        }  
      }  
    }  
  },  
  "@context": [  
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
