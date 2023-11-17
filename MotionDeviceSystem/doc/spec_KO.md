<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 모션 디바이스 시스템    
================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.OPCUA/blob/master/MotionDeviceSystem/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **모션 디바이스 시스템은 OPC UA 디바이스 세트에 대한 진입점으로 모션 디바이스 시스템의 표현을 제공합니다. 이 인스턴스는 설명된 ObjectTypes의 인스턴스를 사용하여 전체 로봇 시스템의 정보 모델을 구성합니다. 모션 장치 시스템은 여러 모션 장치, 컨트롤러 및 안전 시스템으로 구성될 수 있습니다.**    
버전: 0.1.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `controllers[array]`:  컨트롤러는 컨트롤러 타입의 하나 이상의 인스턴스를 위한 컨테이너입니다. 컨트롤러는 하나 이상의 모션 디바이스의 제어 유닛을 나타냅니다. 컨트롤러는 예를 들어 특정 제어 캐비닛 또는 PLC일 수 있습니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `motionDevices[array]`: 모션 디바이스는 모션 디바이스 타입의 하나 이상의 인스턴스를 위한 컨테이너입니다. 모션 디바이스는 하나 이상의 축을 가지며 다양한 작업을 수행하기 위해 프로그래밍된 다양한 동작을 통해 재료, 부품, 도구 또는 특수 장치를 이동하도록 설계된 다기능 조작기입니다. 산업용 로봇, 포지셔너 또는 모바일 플랫폼이 그 예입니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: 모션 디바이스 시스템  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
<!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
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
## 페이로드 예시    
#### MotionDeviceSystem NGSI-v2 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 MotionDeviceSystem의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### MotionDeviceSystem NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 MotionDeviceSystem의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### MotionDeviceSystem NGSI-LD 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 모션 디바이스 시스템의 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### MotionDeviceSystem NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 모션 디바이스 시스템의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
