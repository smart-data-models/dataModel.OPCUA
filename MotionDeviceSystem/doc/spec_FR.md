[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : MotionDeviceSystem  
===========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.OPCUA/blob/master/MotionDeviceSystem/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **MotionDeviceSystem fournit une représentation d'un système de dispositifs de mouvement comme point d'entrée à l'ensemble de dispositifs OPC UA. Cette instance organise le modèle d'information d'un système robotique complet en utilisant des instances des ObjectTypes décrits. Un système de dispositifs de mouvement peut être composé de plusieurs dispositifs de mouvement, de contrôleurs et de systèmes de sécurité.  
version : 0.1.2  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `controllers`:  Controllers est un conteneur pour une ou plusieurs instances du ControllerType. Le contrôleur représente une unité de commande d'un ou de plusieurs dispositifs de mouvement. Un contrôleur peut être, par exemple, une armoire de commande spécifique ou un automate programmable.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `motionDevices`: MotionDevices est un conteneur pour une ou plusieurs instances du type MotionDeviceType. Un dispositif de mouvement possède au moins un axe et est un manipulateur multifonctionnel conçu pour déplacer des matériaux, des pièces, des outils ou des dispositifs spécialisés au moyen de mouvements programmés variables pour l'exécution de diverses tâches. Il s'agit par exemple d'un robot industriel, d'un positionneur ou d'une plate-forme mobile.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: MotionDeviceSystem    
Propriétés requises  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      x-ngsi:    
        type: Geoproperty    
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
## Exemples de charges utiles  
#### MotionDeviceSystem Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de MotionDeviceSystem au format JSON-LD sous forme de valeurs de clé. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### MotionDeviceSystem NGSI-v2 normalisé Exemple  
Voici un exemple de MotionDeviceSystem au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### MotionDeviceSystem Valeurs-clés NGSI-LD Exemple  
Voici un exemple de MotionDeviceSystem au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### MotionDeviceSystem NGSI-LD normalisé Exemple  
Voici un exemple de MotionDeviceSystem au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
        "https://smart-data-models.github.io/data-models/context.jsonld"  
    ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
