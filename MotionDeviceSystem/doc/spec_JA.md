<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティMotionDeviceSystem  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.OPCUA/blob/master/MotionDeviceSystem/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**MotionDeviceSystemは、OPC UAデバイスセットへのエントリーポイントとして、モーションデバイスシステムの表現を提供する。このインスタンスは、記述されたObjectTypesのインスタンスを使用して、完全なロボットシステムの情報モデルを編成する。モーション・デバイス・システムは、複数のモーション・デバイス、コントローラ、安全システムで構成される。  
バージョン: 0.1.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `controllers[array]`: Controllers は、ControllerType のインスタンスを 1 つ以上格納するコンテナである。コントローラは、1つ以上のモーションデバイスの制御ユニットを表す。コントローラは、特定の制御盤やPLCなどである。  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `motionDevices[array]`: MotionDevices は、MotionDeviceType のインスタンスを 1 つ以上格納するコンテナである。モーションデバイスは、少なくとも1つの軸を持ち、さまざまなタスクを実行するためにプログラムされた可変モーションによって材料、部品、ツール、または特殊なデバイスを移動するように設計された多機能マニピュレータである。例えば、産業用ロボット、ポジショナー、移動プラットフォームなどです。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: モーションデバイス・システム  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
<!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MotionDeviceSystem:    
  description: 'MotionDeviceSystem provides a representation of a motion device system as an entry point to the OPC UA device set. This instance organises the information model of a complete robotics system using instances of the described ObjectTypes. A motion device system may consist of multiple motion devices, controllers and safety systems.'    
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
    controllers:    
      description: ' Controllers is a container for one or more instances of the ControllerType. Controller represents a controlling unit of one or more motion devices. A controller can be e.g. a specific control cabinet or a PLC'    
      items:    
        description: A Controller    
        properties:    
          browseName:    
            description: Controller BrowseName    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          components:    
            description: 'Components is a container for one or more instances of subtypes of ComponentType defined in OPC UA DI. The listed components are installed in the motion device system, e.g. a processing-unit, a power-supply, an IO-board or a drive, and have an electrical interface to the controller'    
            items:    
              description: A component    
              properties:    
                browseName:    
                  description: Component BrowseName    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
          manufacturer:    
            description: The name of the company that manufactured the device    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          model:    
            description: The name of the product    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          parameterSet:    
            description: Provides a set of parameters    
            properties:    
              cabinetFanSpeed:    
                description: The speed of the cabinet fan    
                type: number    
                x-ngsi:    
                  model: https://schema.org/Number    
                  type: Property    
              cpuFanSpeed:    
                description: The speed of the CPU fan    
                type: number    
                x-ngsi:    
                  model: https://schema.org/Number    
                  type: Property    
              inputVoltage:    
                description: The input voltage of the controller which can be a configured value. To distinguish between an AC or DC supply the optional property Definition of the base type DataItemType shall be used    
                type: number    
                x-ngsi:    
                  model: https://schema.org/Number    
                  type: Property    
              startUpTime:    
                description: The date and time of the last start-up of the controller    
                format: date-time    
                x-ngsi:    
                  model: https://schema.org/DateTime    
                  type: Property    
              temperature:    
                description: The controller temperature given by a temperature sensor inside of the controller    
                type: number    
                x-ngsi:    
                  model: https://schema.org/Number    
                  type: Property    
              totalEnergyConsumption:    
                description: The total accumulated energy consumed by the motion devices related with this controller instance    
                type: number    
                x-ngsi:    
                  model: https://schema.org/Number    
                  type: Property    
              totalPowerOnTime:    
                description: The total accumulated time the controller was powered on    
                type: string    
                x-ngsi:    
                  model: https://schema.org/Text    
                  type: Property    
              upsState:    
                description: The vendor specific status of an integrated uninterruptible power supply or accumulator system    
                type: string    
                x-ngsi:    
                  model: https://schema.org/Text    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          productCode:    
            description: A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          serialNumber:    
            description: A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          software:    
            description: Software is a container for one or more instances of SoftwareType defined in OPC UA DI. Each controller has at least one software installed that is a runtime software or firmware of the controller. NOTE This type of program is usually generated before installation and can only be modified thereafter by the manufacturer    
            items:    
              description: A software    
              properties:    
                browseName:    
                  description: Software BrowseName    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
          taskControls:    
            description: TaskControls is a container for one or more instances of TaskControlType. The task control describes an execution engine that loads and runs task programs. One task runs one task program at the time. The system should instantiate the maximum allowed number of task controls    
            items:    
              description: A TaskControl    
              properties:    
                browseName:    
                  description: TaskControl BrowseName    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
                componentName:    
                  description: The name of the component    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
                parameterSet:    
                  description: Provides a set of parameters    
                  properties:    
                    executionMode:    
                      description: How the task control executes the task program    
                      type: number    
                      x-ngsi:    
                        model: https://schema.org/Number    
                        type: Property    
                    taskProgramLoaded:    
                      description: 'TRUE if a task program is loaded in the task control, FALSE otherwise'    
                      type: boolean    
                      x-ngsi:    
                        model: https://schema.org/Boolean    
                        type: Property    
                    taskProgramName:    
                      description: A customer given identifier for the task program    
                      type: string    
                      x-ngsi:    
                        model: https://schema.org/Text    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
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
    motionDevices:    
      description: 'MotionDevices is a container for one or more instances of the MotionDeviceType. A motion device has as least one axis and is a multifunctional manipulator designed to move material, parts, tools or specialized devices through variable programmed motions for the performance of a variety of tasks. Examples are an industrial robot, positioner or mobile platform'    
      items:    
        description: A MotionDevice    
        properties:    
          additionalComponents:    
            description: 'AdditionalComponents is a container for one or more instances of subtypes of ComponentType defined in OPC UA DI. The listed components are installed at the motion device, e.g. an IO-board'    
            items:    
              description: An additional component    
              properties:    
                browseName:    
                  description: AdditionalComponent BrowseName    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
          axes:    
            description: Axes is a container for one or more instances of the AxisType    
            items:    
              description: An axis    
              properties:    
                browseName:    
                  description: Axis BrowseName    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
                motionProfile:    
                  description: The kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373    
                  enum:    
                    - OTHER    
                    - ROTARY    
                    - ROTARY_ENDLESS    
                    - LINEAR    
                    - LINEAR_ENDLESS    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Number    
                    type: Property    
                parameterSet:    
                  description: Provides a set of parameters    
                  properties:    
                    actualAcceleration:    
                      description: The axis acceleration    
                      type: number    
                      x-ngsi:    
                        model: https://schema.org/Number    
                        type: Property    
                    actualPosition:    
                      description: The current position of the axis    
                      type: number    
                      x-ngsi:    
                        model: https://schema.org/Number    
                        type: Property    
                    actualSpeed:    
                      description: The axis speed    
                      type: number    
                      x-ngsi:    
                        model: https://schema.org/Number    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
          browseName:    
            description: MotionDevice BrowseName    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          manufacturer:    
            description: The name of the company that manufactured the device    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          model:    
            description: The name of the product    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          motionDeviceCategory:    
            description: The kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373    
            enum:    
              - OTHER    
              - ARTICULATED_ROBOT    
              - SCARA_ROBOT    
              - CARTESIAN_ROBOT    
              - SPHERICAL_ROBOT    
              - PARALLEL_ROBOT    
              - CYLINDRICAL_ROBOT    
            type: string    
            x-ngsi:    
              model: https://schema.org/Number    
              type: Property    
          parameterSet:    
            description: Provides a set of parameters    
            properties:    
              inControl:    
                description: 'The information if the actuators (in most cases a motor) of the motion device are powered up and in control: ''true'''    
                type: boolean    
                x-ngsi:    
                  model: https://schema.org/Boolean    
                  type: Property    
              onPath:    
                description: 'True if the motion device is on or near enough the planned program path such that program execution can continue. If the MotionDevice deviates too much from this path in case of errors or an emergency stop, this value becomes false. If OnPath is false, the motion device needs repositioning to continue program execution'    
                type: boolean    
                x-ngsi:    
                  model: https://schema.org/Boolean    
                  type: Property    
              speedOverride:    
                description: The current speed setting in percent of programmed speed (0 - 100%)    
                type: number    
                x-ngsi:    
                  model: https://schema.org/Number    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          powerTrains:    
            description: PowerTrains is a container for one or more instances of the PowerTrainType    
            items:    
              description: A powerTrain    
              properties:    
                browseName:    
                  description: PowerTrain BrowseName    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
                gears:    
                  description: Gears is a container for one or more instances of the GearType    
                  items:    
                    description: A gear    
                    properties:    
                      browseName:    
                        description: Gear BrowseName    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                      gearRatio:    
                        description: The transmission ratio of the gear expressed as a fraction as input velocity (motor side) by output velocity (load side)    
                        type: number    
                        x-ngsi:    
                          model: https://schema.org/Number    
                          type: Property    
                      manufacturer:    
                        description: The name of the company that manufactured the device    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                      model:    
                        description: The name of the product    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                      pitch:    
                        description: The distance covered in millimeters (mm) for linear motion per one revolution of the output side of the driving unit. Pitch is used in combination with GearRatio to describe the overall transmission from input to output of the gear    
                        type: number    
                        x-ngsi:    
                          model: https://schema.org/Number    
                          type: Property    
                      productCode:    
                        description: A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                      serialNumber:    
                        description: A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                    type: object    
                  type: array    
                  x-ngsi:    
                    type: Property    
                motors:    
                  description: Motors is a container for one or more instances of the MotorType    
                  items:    
                    description: A motor    
                    properties:    
                      browseName:    
                        description: Motor BrowseName    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                      manufacturer:    
                        description: The name of the company that manufactured the device    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                      model:    
                        description: The name of the product    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                      parameterSet:    
                        description: Provides a set of parameters    
                        properties:    
                          brakeReleased:    
                            description: TRUE the motor is free to run. FALSE means that the motor shaft is locked by the brake    
                            type: boolean    
                            x-ngsi:    
                              model: https://schema.org/Boolean    
                              type: Property    
                          effectiveLoadRate:    
                            description: A percentage of maximum continuous load    
                            type: number    
                            x-ngsi:    
                              model: https://schema.org/Number    
                              type: Property    
                          motorTemperature:    
                            description: The temperature of the motor    
                            type: number    
                            x-ngsi:    
                              model: https://schema.org/Number    
                              type: Property    
                        type: object    
                        x-ngsi:    
                          type: Property    
                      productCode:    
                        description: A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                      serialNumber:    
                        description: A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes    
                        type: string    
                        x-ngsi:    
                          model: https://schema.org/Text    
                          type: Property    
                    type: object    
                  type: array    
                  x-ngsi:    
                    type: Property    
              type: object    
            productCode:    
              description: 'Property. Model:''https://schema.org/Text''. A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems.'    
              type: string    
            serialNumber:    
              description: 'Property. Model:''https://schema.org/Text''. A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes.'    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        type: object    
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
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    safetyStates:    
      description: SafetyStates is a container for one or more instances of the SafetyStatesType    
      items:    
        description: A powerTrain    
        properties:    
          browseName:    
            description: SafetyState BrowseName    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          componentName:    
            description: The name of the component    
            type: string    
            x-ngsi:    
              model: https://schema.org/Text    
              type: Property    
          emergencyStopFunctions:    
            description: EmergencyStopFunctions is a container for one or more instances of the EmergencyStopFunctionType. The number and names of emergency stop functions is vendor specific    
            items:    
              description: A emergencyStopFunction    
              properties:    
                active:    
                  description: 'TRUE if this particular emergency stop function is active, e.g. that the emergency stop button is pressed, FALSE otherwise'    
                  type: boolean    
                  x-ngsi:    
                    model: https://schema.org/Boolean    
                    type: Property    
                browseName:    
                  description: EmergencyStopFunction BrowseName    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
                name:    
                  description: Manufacturer-specific protective stop function identifier within the safety system    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
          parameterSet:    
            description: Provides a set of parameters    
            properties:    
              EmergencyStop:    
                description: 'TRUE if one or more of the emergency stop functions in the robot system are active, FALSE otherwise. If the EmergencyStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed emergency stop functions are active'    
                type: boolean    
                x-ngsi:    
                  model: https://schema.org/Boolean    
                  type: Property    
              operationalMode:    
                description: 'The current operational mode. Allowed values are described in OperationalModeEnumeration, see ISO 10218-1:2011'    
                enum:    
                  - OTHER    
                  - MANUAL_REDUCED_SPEED    
                  - MANUAL_HIGH_SPEED    
                  - AUTOMATIC    
                  - AUTOMATIC_EXTERNAL    
                type: number    
                x-ngsi:    
                  model: https://schema.org/Number    
                  type: Property    
              protectiveStop:    
                description: 'TRUE if one or more of the enabled protective stop functions in the system are active, FALSE otherwise. If the ProtectiveStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed protective stop functions are enabled and active'    
                type: boolean    
                x-ngsi:    
                  model: https://schema.org/Boolean    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          protectiveStopFunctions:    
            description: ProtectiveStopFunctions is a container for one or more instances of the ProtectiveStopFunctionType. The number and names of protective stop functions is vendor specific    
            items:    
              description: A protectiveStopFunction    
              properties:    
                active:    
                  description: 'TRUE if this particular protective stop function is active, e.g. that a stop is initiated, FALSE otherwise. If Enabled is FALSE then Active shall be FALSE'    
                  type: boolean    
                  x-ngsi:    
                    model: https://schema.org/Boolean    
                    type: Property    
                browseName:    
                  description: ProtectiveStopFunction BrowseName    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
                enabled:    
                  description: 'TRUE if this protective stop function is currently supervising the system, FALSE otherwise. A protective stop function may or may not be enabled at all times, e.g. the protective stop function of the safety doors are typically enabled in automatic operational mode and disabled in manual mode. On the other hand for example, the protective stop function of the teach pendant enabling device is enabled in manual modes and disabled in automatic modes'    
                  type: boolean    
                  x-ngsi:    
                    model: https://schema.org/Boolean    
                    type: Property    
                name:    
                  description: Manufacturer-specific protective stop function identifier within the safety system    
                  type: string    
                  x-ngsi:    
                    model: https://schema.org/Text    
                    type: Property    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
        type: object    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OPCUA/blob/master/MotionDeviceSystem/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.MotionDeviceSystem/MotionDeviceSystem/schema.json    
  x-model-tags: ""    
  x-version: 0.2.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### MotionDeviceSystem NGSI-v2 キー値の例  
JSON-LD形式のMotionDeviceSystemのkey-valuesの例です。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### MotionDeviceSystem NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のMotionDeviceSystemの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "MotionDeviceSystem",  
  "type": "MotionDeviceSystem",  
  "controllers": {  
    "type": "StructuredValue",  
    "value": [  
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
    ]  
  },  
  "motionDevices": {  
    "type": "StructuredValue",  
    "value": [  
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
              "actualPosition": 1.5,  
              "actualSpeed": 2.0,  
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
    ]  
  },  
  "safetyStates": {  
    "type": "StructuredValue",  
    "value": [  
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
}  
```  
</details>  
#### MotionDeviceSystem NGSI-LD キー値の例  
JSON-LD形式のMotionDeviceSystemのkey-valuesの例です。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### MotionDeviceSystem NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の MotionDeviceSystem の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
