<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: MotionDeviceSystem  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.OPCUA/blob/master/MotionDeviceSystem/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **MotionDeviceSystem fornisce una rappresentazione di un sistema di dispositivi di movimento come punto di ingresso all'insieme di dispositivi OPC UA. Questa istanza organizza il modello informativo di un sistema robotico completo utilizzando istanze dei tipi di oggetti descritti. Un sistema di dispositivi di movimento può essere composto da più dispositivi di movimento, controllori e sistemi di sicurezza **.  
versione: 0.1.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `controllers[array]`:  Controllori è un contenitore per una o più istanze di ControllerType. Il controllore rappresenta un'unità di controllo di uno o più dispositivi di movimento. Un controllore può essere, ad esempio, un armadio di controllo specifico o un PLC.  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `motionDevices[array]`: MotionDevices è un contenitore per una o più istanze di MotionDeviceType. Un dispositivo di movimento ha almeno un asse ed è un manipolatore multifunzionale progettato per spostare materiali, parti, strumenti o dispositivi specializzati attraverso movimenti programmati variabili per l'esecuzione di una serie di compiti. Ne sono un esempio un robot industriale, un posizionatore o una piattaforma mobile.  - `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Sistema di dispositivi di movimento  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MotionDeviceSystem:    
  description: 'MotionDeviceSystem provides a representation of a motion device system as an entry point to the OPC UA device set. This instance organises the information model of a complete robotics system using instances of the described ObjectTypes. A motion device system may consist of multiple motion devices, controllers and safety systems.'    
  properties:    
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
    controllers:    
      description: ' Controllers is a container for one or more instances of the ControllerType. Controller represents a controlling unit of one or more motion devices. A controller can be e.g. a specific control cabinet or a PLC.'    
      items:    
        description: 'A Controller.'    
        properties:    
          browseName:    
            description: 'Property. Model:''https://schema.org/Text''. Controller BrowseName'    
            type: string    
          components:    
            description: 'Property. Components is a container for one or more instances of subtypes of ComponentType defined in OPC UA DI. The listed components are installed in the motion device system, e.g. a processing-unit, a power-supply, an IO-board or a drive, and have an electrical interface to the controller.'    
            items:    
              description: 'A component.'    
              properties:    
                browseName:    
                  description: 'Property. Model:''https://schema.org/Text''. Component BrowseName'    
                  type: string    
              type: object    
            type: array    
          manufacturer:    
            description: 'Property. Model:''https://schema.org/Text''. The name of the company that manufactured the device.'    
            type: string    
          model:    
            description: 'Property. Model:''https://schema.org/Text''. The name of the product.'    
            type: string    
          parameterSet:    
            description: 'Property. Provides a set of parameters.'    
            properties:    
              cabinetFanSpeed:    
                description: 'Property. Model:''https://schema.org/Number''. The speed of the cabinet fan.'    
                type: number    
              cpuFanSpeed:    
                description: 'Property. Model:''https://schema.org/Number''. The speed of the CPU fan.'    
                type: number    
              inputVoltage:    
                description: 'Property. Model:''https://schema.org/Number''. The input voltage of the controller which can be a configured value. To distinguish between an AC or DC supply the optional property Definition of the base type DataItemType shall be used.'    
                type: number    
              startUpTime:    
                description: 'Property. Model:''https://schema.org/DateTime''. The date and time of the last start-up of the controller.'    
                format: date-time    
              temperature:    
                description: 'Property. Model:''https://schema.org/Number''. The controller temperature given by a temperature sensor inside of the controller.'    
                type: number    
              totalEnergyConsumption:    
                description: 'Property. Model:''https://schema.org/Number''. The total accumulated energy consumed by the motion devices related with this controller instance.'    
                type: number    
              totalPowerOnTime:    
                description: 'Property. Model:''https://schema.org/Text''. The total accumulated time the controller was powered on.'    
                type: string    
              upsState:    
                description: 'Property. Model:''https://schema.org/Text''. The vendor specific status of an integrated uninterruptible power supply or accumulator system.'    
                type: string    
            type: object    
          productCode:    
            description: 'Property. Model:''https://schema.org/Text''. A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems.'    
            type: string    
          serialNumber:    
            description: 'Property. Model:''https://schema.org/Text''. A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes.'    
            type: string    
          software:    
            description: 'Property. Software is a container for one or more instances of SoftwareType defined in OPC UA DI. Each controller has at least one software installed that is a runtime software or firmware of the controller. NOTE This type of program is usually generated before installation and can only be modified thereafter by the manufacturer.'    
            items:    
              description: 'A software.'    
              properties:    
                browseName:    
                  description: 'Property. Model:''https://schema.org/Text''. Software BrowseName'    
                  type: string    
              type: object    
            type: array    
          taskControls:    
            description: 'Property. TaskControls is a container for one or more instances of TaskControlType. The task control describes an execution engine that loads and runs task programs. One task runs one task program at the time. The system should instantiate the maximum allowed number of task controls'    
            items:    
              description: 'A TaskControl.'    
              properties:    
                browseName:    
                  description: 'Property. Model:''https://schema.org/Text''. TaskControl BrowseName'    
                  type: string    
                componentName:    
                  description: 'Property. Model:''https://schema.org/Text''. The name of the component.'    
                  type: string    
                parameterSet:    
                  description: 'Property. Provides a set of parameters.'    
                  properties:    
                    executionMode:    
                      description: 'Property. Model:''https://schema.org/Number''. How the task control executes the task program.'    
                      type: number    
                    taskProgramLoaded:    
                      description: 'Property. Model:''https://schema.org/Boolean''. TRUE if a task program is loaded in the task control, FALSE otherwise.'    
                      type: boolean    
                    taskProgramName:    
                      description: 'Property. Model:''https://schema.org/Text''. A customer given identifier for the task program.'    
                      type: string    
                  type: object    
              type: object    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
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
      anyOf: &motiondevicesystem_-_properties_-_owner_-_items_-_anyof    
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
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
      x-ngsi:    
        type: GeoProperty    
    motionDevices:    
      description: 'MotionDevices is a container for one or more instances of the MotionDeviceType. A motion device has as least one axis and is a multifunctional manipulator designed to move material, parts, tools or specialized devices through variable programmed motions for the performance of a variety of tasks. Examples are an industrial robot, positioner or mobile platform.'    
      items:    
        description: 'A MotionDevice.'    
        properties:    
          additionalComponents:    
            description: 'Property. AdditionalComponents is a container for one or more instances of subtypes of ComponentType defined in OPC UA DI. The listed components are installed at the motion device, e.g. an IO-board.'    
            items:    
              description: 'An additional component.'    
              properties:    
                browseName:    
                  description: 'Property. Model:''https://schema.org/Text''. AdditionalComponent BrowseName'    
                  type: string    
              type: object    
            type: array    
          axes:    
            description: 'Property. Axes is a container for one or more instances of the AxisType.'    
            items:    
              description: 'An axis.'    
              properties:    
                browseName:    
                  description: 'Property. Model:''https://schema.org/Text''. Axis BrowseName'    
                  type: string    
                motionProfile:    
                  description: 'Property. Model:''https://schema.org/Number''. The kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373.'    
                  enum:    
                    - OTHER    
                    - ROTARY    
                    - ROTARY_ENDLESS    
                    - LINEAR    
                    - LINEAR_ENDLESS    
                  type: string    
                parameterSet:    
                  description: 'Property. Provides a set of parameters.'    
                  properties:    
                    actualAcceleration:    
                      description: 'Property. Model:''https://schema.org/Number''. The axis acceleration.'    
                      type: number    
                    actualPosition:    
                      description: 'Property. Model:''https://schema.org/Number''. The current position of the axis.'    
                      type: number    
                    actualSpeed:    
                      description: 'Property. Model:''https://schema.org/Number''. The axis speed.'    
                      type: number    
                  type: object    
              type: object    
            type: array    
          browseName:    
            description: 'Property. Model:''https://schema.org/Text''. MotionDevice BrowseName'    
            type: string    
          manufacturer:    
            description: 'Property. Model:''https://schema.org/Text''. The name of the company that manufactured the device.'    
            type: string    
          model:    
            description: 'Property. Model:''https://schema.org/Text''. The name of the product.'    
            type: string    
          motionDeviceCategory:    
            description: 'Property. Model:''https://schema.org/Number''. The kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373.'    
            enum:    
              - OTHER    
              - ARTICULATED_ROBOT    
              - SCARA_ROBOT    
              - CARTESIAN_ROBOT    
              - SPHERICAL_ROBOT    
              - PARALLEL_ROBOT    
              - CYLINDRICAL_ROBOT    
            type: string    
          parameterSet:    
            description: 'Property. Provides a set of parameters.'    
            properties:    
              inControl:    
                description: 'Property. Model:''https://schema.org/Boolean''. The information if the actuators (in most cases a motor) of the motion device are powered up and in control: ''true''.'    
                type: boolean    
              onPath:    
                description: 'Property. Model:''https://schema.org/Boolean''. True if the motion device is on or near enough the planned program path such that program execution can continue. If the MotionDevice deviates too much from this path in case of errors or an emergency stop, this value becomes false. If OnPath is false, the motion device needs repositioning to continue program execution.'    
                type: boolean    
              speedOverride:    
                description: 'Property. Model:''https://schema.org/Number''. The current speed setting in percent of programmed speed (0 - 100%).'    
                type: number    
            type: object    
          powerTrains:    
            description: 'Property. PowerTrains is a container for one or more instances of the PowerTrainType.'    
            items:    
              description: 'A powerTrain.'    
              properties:    
                browseName:    
                  description: 'Property. Model:''https://schema.org/Text''. PowerTrain BrowseName'    
                  type: string    
                gears:    
                  description: 'Property. Gears is a container for one or more instances of the GearType.'    
                  items:    
                    description: 'A gear.'    
                    properties:    
                      browseName:    
                        description: 'Property. Model:''https://schema.org/Text''. Gear BrowseName'    
                        type: string    
                      gearRatio:    
                        description: 'Property. Model:''https://schema.org/Number''. The transmission ratio of the gear expressed as a fraction as input velocity (motor side) by output velocity (load side).'    
                        type: number    
                      manufacturer:    
                        description: 'Property. Model:''https://schema.org/Text''. The name of the company that manufactured the device.'    
                        type: string    
                      model:    
                        description: 'Property. Model:''https://schema.org/Text''. The name of the product.'    
                        type: string    
                      pitch:    
                        description: 'Property. Model:''https://schema.org/Number''. The distance covered in millimeters (mm) for linear motion per one revolution of the output side of the driving unit. Pitch is used in combination with GearRatio to describe the overall transmission from input to output of the gear.'    
                        type: number    
                      productCode:    
                        description: 'Property. Model:''https://schema.org/Text''. A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems.'    
                        type: string    
                      serialNumber:    
                        description: 'Property. Model:''https://schema.org/Text''. A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes.'    
                        type: string    
                    type: object    
                  type: array    
                motors:    
                  description: 'Property. Motors is a container for one or more instances of the MotorType.'    
                  items:    
                    description: 'A motor.'    
                    properties:    
                      browseName:    
                        description: 'Property. Model:''https://schema.org/Text''. Motor BrowseName'    
                        type: string    
                      manufacturer:    
                        description: 'Property. Model:''https://schema.org/Text''. The name of the company that manufactured the device.'    
                        type: string    
                      model:    
                        description: 'Property. Model:''https://schema.org/Text''. The name of the product.'    
                        type: string    
                      parameterSet:    
                        description: 'Property. Provides a set of parameters.'    
                        properties:    
                          brakeReleased:    
                            description: 'Property. Model:''https://schema.org/Boolean''. TRUE the motor is free to run. FALSE means that the motor shaft is locked by the brake.'    
                            type: boolean    
                          effectiveLoadRate:    
                            description: 'Property. Model:''https://schema.org/Number''. A percentage of maximum continuous load.'    
                            type: number    
                          motorTemperature:    
                            description: 'Property. Model:''https://schema.org/Number''. The temperature of the motor.'    
                            type: number    
                        type: object    
                      productCode:    
                        description: 'Property. Model:''https://schema.org/Text''. A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems.'    
                        type: string    
                      serialNumber:    
                        description: 'Property. Model:''https://schema.org/Text''. A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes.'    
                        type: string    
                    type: object    
                  type: array    
              type: object    
            productCode:    
              description: 'Property. Model:''https://schema.org/Text''. A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems.'    
              type: string    
            serialNumber:    
              description: 'Property. Model:''https://schema.org/Text''. A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes.'    
              type: string    
            type: array    
        safetyStates:    
          description: 'Property. SafetyStates is a container for one or more instances of the SafetyStatesType.'    
          items:    
            description: 'A powerTrain.'    
            properties:    
              browseName:    
                description: 'Property. Model:''https://schema.org/Text''. SafetyState BrowseName'    
                type: string    
              componentName:    
                description: 'Property. Model:''https://schema.org/Text''. The name of the component.'    
                type: string    
              emergencyStopFunctions:    
                description: 'Property. EmergencyStopFunctions is a container for one or more instances of the EmergencyStopFunctionType. The number and names of emergency stop functions is vendor specific.'    
                items:    
                  description: 'A emergencyStopFunction.'    
                  properties:    
                    active:    
                      description: 'Property. Model:''https://schema.org/Boolean''. TRUE if this particular emergency stop function is active, e.g. that the emergency stop button is pressed, FALSE otherwise.'    
                      type: boolean    
                    browseName:    
                      description: 'Property. Model:''https://schema.org/Text''. EmergencyStopFunction BrowseName'    
                      type: string    
                    name:    
                      description: 'Property. Model:''https://schema.org/Text''. Manufacturer-specific protective stop function identifier within the safety system.'    
                      type: string    
                  type: object    
                type: array    
              parameterSet:    
                description: 'Property. Provides a set of parameters.'    
                properties:    
                  EmergencyStop:    
                    description: 'Property. Model:''https://schema.org/Boolean''. TRUE if one or more of the emergency stop functions in the robot system are active, FALSE otherwise. If the EmergencyStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed emergency stop functions are active.'    
                    type: boolean    
                  operationalMode:    
                    description: 'Property. Model:''https://schema.org/Number''. The current operational mode. Allowed values are described in OperationalModeEnumeration, see ISO 10218-1:2011.'    
                    enum:    
                      - OTHER    
                      - MANUAL_REDUCED_SPEED    
                      - MANUAL_HIGH_SPEED    
                      - AUTOMATIC    
                      - AUTOMATIC_EXTERNAL    
                    type: number    
                  protectiveStop:    
                    description: 'Property. Model:''https://schema.org/Boolean''. TRUE if one or more of the enabled protective stop functions in the system are active, FALSE otherwise. If the ProtectiveStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed protective stop functions are enabled and active.'    
                    type: boolean    
                type: object    
              protectiveStopFunctions:    
                description: 'Property. ProtectiveStopFunctions is a container for one or more instances of the ProtectiveStopFunctionType. The number and names of protective stop functions is vendor specific.'    
                items:    
                  description: 'A protectiveStopFunction.'    
                  properties:    
                    active:    
                      description: 'Property. Model:''https://schema.org/Boolean''. TRUE if this particular protective stop function is active, e.g. that a stop is initiated, FALSE otherwise. If Enabled is FALSE then Active shall be FALSE.'    
                      type: boolean    
                    browseName:    
                      description: 'Property. Model:''https://schema.org/Text''. ProtectiveStopFunction BrowseName'    
                      type: string    
                    enabled:    
                      description: 'Property. Model:''https://schema.org/Boolean''. TRUE if this protective stop function is currently supervising the system, FALSE otherwise. A protective stop function may or may not be enabled at all times, e.g. the protective stop function of the safety doors are typically enabled in automatic operational mode and disabled in manual mode. On the other hand for example, the protective stop function of the teach pendant enabling device is enabled in manual modes and disabled in automatic modes.'    
                      type: boolean    
                    name:    
                      description: 'Property. Model:''https://schema.org/Text''. Manufacturer-specific protective stop function identifier within the safety system.'    
                      type: string    
                  type: object    
                type: array    
            type: object    
          type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *motiondevicesystem_-_properties_-_owner_-_items_-_anyof    
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
      description: MotionDeviceSystem    
      enum:    
        - MotionDeviceSystem    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OPCUA/blob/master/MotionDeviceSystem/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.MotionDeviceSystem/MotionDeviceSysten/schema.json    
  x-model-tags: ""    
  x-version: 0.1.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### MotionDeviceSystem Valori chiave NGSI-v2 Esempio  
Ecco un esempio di MotionDeviceSystem in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "MotionDeviceSystem",  
  "type": "MotionDeviceSystem",  
  "controllers": [  
    {  
      "browseName": "Controller",  
      "components": [  
        {  
          "browseName": "Component"  
        }  
      ],  
      "manufacturer": "Engineering Ingegneria Informatica",  
      "model": "Model",  
      "parameterSet": {  
        "cpuFanSpeed": 1600.0,  
        "cabinetFanSpeed": 2000.5,  
        "inputVoltage": 2500.0,  
        "startUpTime": "2020-10-19T07:36:06.713Z",  
        "temperature": 50.0,  
        "totalEnergyConsumption": 170.1,  
        "totalPowerOnTime": "",  
        "upsState": "alive"  
      },  
      "productCode": "MP695ENG004",  
      "serialNumber": "ENG-004",  
      "software": [  
        {  
          "browseName": "Software"  
        }  
      ],  
      "taskControls": [  
        {  
          "browseName": "TaskControl",  
          "componentName": "TaskControl",  
          "parameterSet": {  
            "taskProgramName": "TaskProg",  
            "taskProgramLoaded": true,  
            "executionMode": 0  
          }  
        }  
      ]  
    }  
  ],  
  "motionDevices": [  
    {  
      "browseName": "MotionDevice",  
      "additionalComponents": [  
        {  
          "browseName": "AdditionalComponent"  
        }  
      ],  
      "axes": [  
        {  
          "browseName": "AxisX",  
          "motionProfile": "OTHER",  
          "parameterSet": {  
            "actualPosition": 1.0,  
            "actualSpeed": 2.5,  
            "actualAcceleration": 3.0  
          }  
        },  
        {  
          "browseName": "AxisY",  
          "motionProfile": "LINEAR",  
          "parameterSet": {  
            "actualPosition": 1.0,  
            "actualSpeed": 2.5,  
            "actualAcceleration": 3.0  
          }  
        }  
      ],  
      "manufacturer": "Engineering Ingegneria Informatica",  
      "model": "Model",  
      "motionDeviceCategory": "OTHER",  
      "powerTrains": [  
        {  
          "browseName": "PowerTrain",  
          "gears": [  
            {  
              "browseName": "Gear",  
              "gearRatio": 0.5,  
              "manufacturer": "Engineering Ingegneria Informatica",  
              "model": "Model",  
              "pitch": 1.0,  
              "productCode": "MP695ENG003",  
              "serialNumber": "ENG-003"  
            }  
          ],  
          "motors": [  
            {  
              "browseName": "Motor",  
              "manufacturer": "Engineering Ingegneria Informatica",  
              "model": "Model",  
              "parameterSet": {  
                "brakeReleased": true,  
                "effectiveLoadRate": 0,  
                "motorTemperature": 75  
              },  
              "productCode": "MP695ENG002",  
              "serialNumber": "ENG-002"  
            }  
          ]  
        }  
      ]  
    }  
  ],  
  "safetyStates": [  
    {  
      "browseName": "SafetyState",  
      "emergencyStopFunctions": [  
        {  
          "browseName": "EmergencyStopFunction",  
          "active": true,  
          "name": "emergencyStop"  
        }  
      ],  
      "parameterSet": {  
        "emergencyStop": true,  
        "operationalMode": "AUTOMATIC",  
        "protectiveStop": true  
      },  
      "protectiveStopFunctions": [  
        {  
          "browseName": "ProtectiveStopFunction",  
          "active": true,  
          "enabled": true,  
          "name": "protectiveStop"  
        }  
      ]  
    }  
  ]  
}  
```  
</details>  
#### MotionDeviceSystem NGSI-v2 normalizzato Esempio  
Ecco un esempio di MotionDeviceSystem in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "MotionDeviceSystem",  
  "type": "MotionDeviceSystem",  
  "controllers": [  
    {  
      "browseName": {  
        "value": "Controller"  
      },  
      "components": [  
        {  
          "browseName": {  
            "value": "Component"  
          }  
        }  
      ],  
      "manufacturer": {  
        "value": "Engineering Ingegneria Informatica"  
      },  
      "model": {  
        "value": "Model"  
      },  
      "parameterSet": {  
        "value": {  
          "cpuFanSpeed": 1600.0,  
          "cabinetFanSpeed": 2000.5,  
          "inputVoltage": 2500.0,  
          "startUpTime": "2020-10-19T07:36:06.713Z",  
          "temperature": 50.0,  
          "totalEnergyConsumption": 170.1,  
          "totalPowerOnTime": "",  
          "upsState": "alive"  
        }  
      },  
      "productCode": {  
        "value": "MP695ENG004"  
      },  
      "serialNumber": {  
        "value": "ENG-004"  
      },  
      "software": [  
        {  
          "browseName": {  
            "value": "Software"  
          }  
        }  
      ],  
      "taskControls": [  
        {  
          "browseName": {  
            "value": "TaskControl"  
          },  
          "componentName": {  
            "value": "TaskControl"  
          },  
          "parameterSet": {  
            "value": {  
              "taskProgramName": "TaskProg",  
              "taskProgramLoaded": true,  
              "executionMode": 0  
            }  
          }  
        }  
      ]  
    }  
  ],  
  "motionDevices": [  
    {  
      "browseName": {  
        "value": "MotionDevice"  
      },  
      "additionalComponents": [  
        {  
          "browseName": {  
            "value": "AdditionalComponent"  
          }  
        }  
      ],  
      "axes": [  
        {  
          "browseName": {  
            "value": "AxisX"  
          },  
          "motionProfile": {  
            "value": "OTHER"  
          },  
          "parameterSet": {  
            "value": {  
              "actualPosition": 1.0,  
              "actualSpeed": 2.5,  
              "actualAcceleration": 3.0  
            }  
          }  
        },  
        {  
          "browseName": {  
            "value": "AxisY"  
          },  
          "motionProfile": {  
            "value": "LINEAR"  
          },  
          "parameterSet": {  
            "value": {  
              "actualPosition": 1.5,  
              "actualSpeed": 2.0,  
              "actualAcceleration": 3.0  
            }  
          }  
        }  
      ],  
      "manufacturer": {  
        "value": "Engineering Ingegneria Informatica"  
      },  
      "model":  {  
        "value": "Model"  
      },  
      "motionDeviceCategory": {  
        "value": "OTHER"  
      },  
      "powerTrains": [  
        {  
          "browseName": {  
            "value": "PowerTrain"  
          },  
          "gears": [  
            {  
              "browseName": {  
                "value": "Gear"  
              },  
              "gearRatio": {  
                "value": 0.5  
              },  
              "manufacturer": {  
                "value": "Engineering Ingegneria Informatica"  
              },  
              "model": {  
                "value": "Model"  
              },  
              "pitch": {  
                "value": 1.0  
              },  
              "productCode": {  
                "value": "MP695ENG003"  
              },  
              "serialNumber": {  
                "value": "ENG-003"  
              }  
            }  
          ],  
          "motors": [  
            {  
              "browseName": {  
                "value": "Motor"  
              },  
              "manufacturer": {  
                "value": "Engineering Ingegneria Informatica"  
              },  
              "model": {  
                "value": "Model"  
              },  
              "parameterSet": {  
                "value": {  
                  "brakeReleased": true,  
                  "effectiveLoadRate": 0,  
                  "motorTemperature": 75  
                }  
              },  
              "productCode": {  
                "value": "MP695ENG002"  
              },  
              "serialNumber": {  
                "value": "ENG-002"  
              }  
            }  
          ]  
        }  
      ]  
    }  
  ],  
  "safetyStates": [  
    {  
      "browseName": {  
        "value": "SafetyState"  
      },  
      "emergencyStopFunctions": [  
        {  
          "browseName": {  
            "value": "EmergencyStopFunction"  
          },  
          "active": {  
            "value": true  
          },  
          "name": {  
            "value": "emergencyStop"  
          }  
        }  
      ],  
      "parameterSet": {  
        "value": {  
          "emergencyStop": true,  
          "operationalMode": "AUTOMATIC",  
          "protectiveStop": true  
        }  
      },  
      "protectiveStopFunctions": [  
        {  
          "browseName": {  
            "value": "ProtectiveStopFunction"  
          },  
          "active": {  
            "value": true  
          },  
          "enabled": {  
            "value": true  
          },  
          "name": {  
            "value": "protectiveStop"  
          }  
        }  
      ]  
    }  
  ]  
}  
```  
</details>  
#### MotionDeviceSystem Valori chiave NGSI-LD Esempio  
Ecco un esempio di MotionDeviceSystem in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:MotionDeviceSystem:MotionDeviceSystem",  
    "type": "MotionDeviceSystem",  
    "controllers": [  
        {  
            "browseName": "uri:ngsi-ld:Controller",  
            "components": [  
                {  
                    "browseName": "uri:ngsi-ld:Component"  
                }  
            ],  
            "manufacturer": "Engineering Ingegneria Informatica",  
            "model": "Model",  
            "parameterSet": {  
                "cpuFanSpeed": 1600.0,  
                "cabinetFanSpeed": 2000.5,  
                "inputVoltage": 2500.0,  
                "startUpTime": "2020-10-19T07:36:06.713Z",  
                "temperature": 50.0,  
                "totalEnergyConsumption": 170.1,  
                "totalPowerOnTime": "",  
                "upsState": "alive"  
            },  
            "productCode": "MP695ENG004",  
            "serialNumber": "ENG-004",  
            "software": [  
                {  
                    "browseName": "uri:ngsi-ld:Software"  
                }  
            ],  
            "taskControls": [  
                {  
                    "browseName": "uri:ngsi-ld:TaskControl",  
                    "componentName": "TaskControl",  
                    "parameterSet": {  
                        "taskProgramName": "TaskProg",  
                        "taskProgramLoaded": true,  
                        "executionMode": 0  
                    }  
                }  
            ]  
        }  
    ],  
    "motionDevices": [  
        {  
            "browseName": "uri:ngsi-ld:MotionDevice",  
            "additionalComponents": [  
                {  
                    "browseName": "uri:ngsi-ld:AdditionalComponent"  
                }  
            ],  
            "axes": [  
                {  
                    "browseName": "uri:ngsi-ld:AxisX",  
                    "motionProfile": "OTHER",  
                    "parameterSet": {  
                        "actualPosition": 1.0,  
                        "actualSpeed": 2.5,  
                        "actualAcceleration": 3.0  
                    }  
                },  
                {  
                    "browseName": "uri:ngsi-ld:AxisY",  
                    "motionProfile": "LINEAR",  
                    "parameterSet": {  
                        "actualPosition": 1.0,  
                        "actualSpeed": 2.5,  
                        "actualAcceleration": 3.0  
                    }  
                }  
            ],  
            "manufacturer": "Engineering Ingegneria Informatica",  
            "model": "Model",  
            "motionDeviceCategory": "OTHER",  
            "powerTrains": [  
                {  
                    "browseName": "uri:ngsi-ld:PowerTrain",  
                    "gears": [  
                        {  
                            "browseName": "uri:ngsi-ld:Gear",  
                            "gearRatio": 0.5,  
                            "manufacturer": "Engineering Ingegneria Informatica",  
                            "model": "Model",  
                            "pitch": 1.0,  
                            "productCode": "MP695ENG003",  
                            "serialNumber": "ENG-003"  
                        }  
                    ],  
                    "motors": [  
                        {  
                            "browseName": "uri:ngsi-ld:Motor",  
                            "manufacturer": "Engineering Ingegneria Informatica",  
                            "model": "Model",  
                            "parameterSet": {  
                                "brakeReleased": true,  
                                "effectiveLoadRate": 0,  
                                "motorTemperature": 75  
                            },  
                            "productCode": "MP695ENG002",  
                            "serialNumber": "ENG-002"  
                        }  
                    ]  
                }  
            ]  
        }  
    ],  
    "safetyStates": [  
        {  
            "browseName": "uri:ngsi-ld:SafetyState",  
            "emergencyStopFunctions": [  
                {  
                    "browseName": "uri:ngsi-ld:EmergencyStopFunction",  
                    "active": true,  
                    "name": "emergencyStop"  
                }  
            ],  
            "parameterSet": {  
                "emergencyStop": true,  
                "operationalMode": "AUTOMATIC",  
                "protectiveStop": true  
            },  
            "protectiveStopFunctions": [  
                {  
                    "browseName": "uri:ngsi-ld:ProtectiveStopFunction",  
                    "active": true,  
                    "enabled": true,  
                    "name": "protectiveStop"  
                }  
            ]  
        }  
    ],  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OPCUA/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### MotionDeviceSystem NGSI-LD normalizzato Esempio  
Ecco un esempio di MotionDeviceSystem in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:MotionDeviceSystem",  
    "type": "MotionDeviceSystem",  
    "controllers": [  
        {  
            "browseName": {  
                "type": "Property",  
                "value": "uri:ngsi-ld:Controller"  
            },  
            "components": [  
                {  
                    "browseName": {  
                        "type": "Property",  
                        "value": "uri:ngsi-ld:Component"  
                    }  
                }  
            ],  
            "manufacturer": {  
                "type": "Property",  
                "value": "Engineering Ingegneria Informatica"  
            },  
            "model": {  
                "type": "Property",  
                "value": "Model"  
            },  
            "parameterSet": {  
                "type": "Property",  
                "value": {  
                    "cpuFanSpeed": 1600.0,  
                    "cabinetFanSpeed": 2000.5,  
                    "inputVoltage": 2500.0,  
                    "startUpTime": "2020-10-19T07:36:06.713Z",  
                    "temperature": 50.0,  
                    "totalEnergyConsumption": 170.1,  
                    "totalPowerOnTime": "",  
                    "upsState": "alive"  
                }  
            },  
            "productCode": {  
                "type": "Property",  
                "value": "MP695ENG004"  
            },  
            "serialNumber": {  
                "type": "Property",  
                "value": "ENG-004"  
            },  
            "software": [  
                {  
                    "browseName": {  
                        "type": "Property",  
                        "value": "uri:ngsi-ld:Software"  
                    }  
                }  
            ],  
            "taskControls": [  
                {  
                    "browseName": {  
                        "type": "Property",  
                        "value": "uri:ngsi-ld:TaskControl"  
                    },  
                    "componentName": {  
                        "type": "Property",  
                        "value": "TaskControl"  
                    },  
                    "parameterSet": {  
                        "type": "Property",  
                        "value": {  
                            "taskProgramName": "TaskProg",  
                            "taskProgramLoaded": true,  
                            "executionMode": 0  
                        }  
                    }  
                }  
            ]  
        }  
    ],  
    "motionDevices": [  
        {  
            "browseName": {  
                "type": "Property",  
                "value": "uri:ngsi-ld:MotionDevice"  
            },  
            "additionalComponents": [  
                {  
                    "browseName": {  
                        "type": "Property",  
                        "value": "uri:ngsi-ld:AdditionalComponent"  
                    }  
                }  
            ],  
            "axes": [  
                {  
                    "browseName": {  
                        "type": "Property",  
                        "value": "uri:ngsi-ld:AxisX"  
                    },  
                    "motionProfile": {  
                        "type": "Property",  
                        "value": "OTHER"  
                    },  
                    "parameterSet": {  
                        "type": "Property",  
                        "value": {  
                            "actualPosition": 1.0,  
                            "actualSpeed": 2.5,  
                            "actualAcceleration": 3.0  
                        }  
                    }  
                },  
                {  
                    "browseName": {  
                        "type": "Property",  
                        "value": "uri:ngsi-ld:AxisY"  
                    },  
                    "motionProfile": {  
                        "type": "Property",  
                        "value": "LINEAR"  
                    },  
                    "parameterSet": {  
                        "type": "Property",  
                        "value": {  
                            "actualPosition": 1.5,  
                            "actualSpeed": 2.0,  
                            "actualAcceleration": 3.0  
                        }  
                    }  
                }  
            ],  
            "manufacturer": {  
                "type": "Property",  
                "value": "Engineering Ingegneria Informatica"  
            },  
            "model": {  
                "type": "Property",  
                "value": "Model"  
            },  
            "motionDeviceCategory": {  
                "type": "Property",  
                "value": "OTHER"  
            },  
            "powerTrains": [  
                {  
                    "browseName": {  
                        "type": "Property",  
                        "value": "uri:ngsi-ld:PowerTrain"  
                    },  
                    "gears": [  
                        {  
                            "browseName": {  
                                "type": "Property",  
                                "value": "uri:ngsi-ld:Gear"  
                            },  
                            "gearRatio": {  
                                "type": "Property",  
                                "value": 0.5  
                            },  
                            "manufacturer": {  
                                "type": "Property",  
                                "value": "Engineering Ingegneria Informatica"  
                            },  
                            "model": {  
                                "type": "Property",  
                                "value": "Model"  
                            },  
                            "pitch": {  
                                "type": "Property",  
                                "value": 1.0  
                            },  
                            "productCode": {  
                                "type": "Property",  
                                "value": "MP695ENG003"  
                            },  
                            "serialNumber": {  
                                "type": "Property",  
                                "value": "ENG-003"  
                            }  
                        }  
                    ],  
                    "motors": [  
                        {  
                            "browseName": {  
                                "type": "Property",  
                                "value": "uri:ngsi-ld:Motor"  
                            },  
                            "manufacturer": {  
                                "type": "Property",  
                                "value": "Engineering Ingegneria Informatica"  
                            },  
                            "model": {  
                                "type": "Property",  
                                "value": "Model"  
                            },  
                            "parameterSet": {  
                                "type": "Property",  
                                "value": {  
                                    "brakeReleased": true,  
                                    "effectiveLoadRate": 0,  
                                    "motorTemperature": 75  
                                }  
                            },  
                            "productCode": {  
                                "type": "Property",  
                                "value": "MP695ENG002"  
                            },  
                            "serialNumber": {  
                                "type": "Property",  
                                "value": "ENG-002"  
                            }  
                        }  
                    ]  
                }  
            ]  
        }  
    ],  
    "safetyStates": [  
        {  
            "browseName": {  
                "type": "Property",  
                "value": "uri:ngsi-ld:SafetyState"  
            },  
            "emergencyStopFunctions": [  
                {  
                    "browseName": {  
                        "type": "Property",  
                        "value": "uri:ngsi-ld:EmergencyStopFunction"  
                    },  
                    "active": {  
                        "type": "Property",  
                        "value": true  
                    },  
                    "name": {  
                        "type": "Property",  
                        "value": "emergencyStop"  
                    }  
                }  
            ],  
            "parameterSet": {  
                "type": "Property",  
                "value": {  
                    "emergencyStop": true,  
                    "operationalMode": "AUTOMATIC",  
                    "protectiveStop": true  
                }  
            },  
            "protectiveStopFunctions": [  
                {  
                    "browseName": {  
                        "type": "Property",  
                        "value": "uri:ngsi-ld:ProtectiveStopFunction"  
                    },  
                    "active": {  
                        "type": "Property",  
                        "value": true  
                    },  
                    "enabled": {  
                        "type": "Property",  
                        "value": true  
                    },  
                    "name": {  
                        "type": "Property",  
                        "value": "protectiveStop"  
                    }  
                }  
            ]  
        }  
    ],  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OPCUA/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
