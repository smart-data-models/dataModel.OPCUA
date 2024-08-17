from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Component(BaseModel):
    browseName: Optional[str] = Field(None, description='Component BrowseName')


class ParameterSet(BaseModel):
    cabinetFanSpeed: Optional[float] = Field(
        None, description='The speed of the cabinet fan'
    )
    cpuFanSpeed: Optional[float] = Field(None, description='The speed of the CPU fan')
    inputVoltage: Optional[float] = Field(
        None,
        description='The input voltage of the controller which can be a configured value. To distinguish between an AC or DC supply the optional property Definition of the base type DataItemType shall be used',
    )
    startUpTime: Optional[Any] = Field(
        None, description='The date and time of the last start-up of the controller'
    )
    temperature: Optional[float] = Field(
        None,
        description='The controller temperature given by a temperature sensor inside of the controller',
    )
    totalEnergyConsumption: Optional[float] = Field(
        None,
        description='The total accumulated energy consumed by the motion devices related with this controller instance',
    )
    totalPowerOnTime: Optional[str] = Field(
        None, description='The total accumulated time the controller was powered on'
    )
    upsState: Optional[str] = Field(
        None,
        description='The vendor specific status of an integrated uninterruptible power supply or accumulator system',
    )


class SoftwareItem(BaseModel):
    browseName: Optional[str] = Field(None, description='Software BrowseName')


class ParameterSet1(BaseModel):
    executionMode: Optional[float] = Field(
        None, description='How the task control executes the task program'
    )
    taskProgramLoaded: Optional[bool] = Field(
        None,
        description='TRUE if a task program is loaded in the task control, FALSE otherwise',
    )
    taskProgramName: Optional[str] = Field(
        None, description='A customer given identifier for the task program'
    )


class TaskControl(BaseModel):
    browseName: Optional[str] = Field(None, description='TaskControl BrowseName')
    componentName: Optional[str] = Field(None, description='The name of the component')
    parameterSet: Optional[ParameterSet1] = Field(
        None, description='Provides a set of parameters'
    )


class Controller(BaseModel):
    browseName: Optional[str] = Field(None, description='Controller BrowseName')
    components: Optional[List[Component]] = Field(
        None,
        description='Components is a container for one or more instances of subtypes of ComponentType defined in OPC UA DI. The listed components are installed in the motion device system, e.g. a processing-unit, a power-supply, an IO-board or a drive, and have an electrical interface to the controller',
    )
    manufacturer: Optional[str] = Field(
        None, description='The name of the company that manufactured the device'
    )
    model: Optional[str] = Field(None, description='The name of the product')
    parameterSet: Optional[ParameterSet] = Field(
        None, description='Provides a set of parameters'
    )
    productCode: Optional[str] = Field(
        None,
        description='A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems',
    )
    serialNumber: Optional[str] = Field(
        None,
        description='A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes',
    )
    software: Optional[List[SoftwareItem]] = Field(
        None,
        description='Software is a container for one or more instances of SoftwareType defined in OPC UA DI. Each controller has at least one software installed that is a runtime software or firmware of the controller. NOTE This type of program is usually generated before installation and can only be modified thereafter by the manufacturer',
    )
    taskControls: Optional[List[TaskControl]] = Field(
        None,
        description='TaskControls is a container for one or more instances of TaskControlType. The task control describes an execution engine that loads and runs task programs. One task runs one task program at the time. The system should instantiate the maximum allowed number of task controls',
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class AdditionalComponent(BaseModel):
    browseName: Optional[str] = Field(
        None, description='AdditionalComponent BrowseName'
    )


class MotionProfile(Enum):
    OTHER = 'OTHER'
    ROTARY = 'ROTARY'
    ROTARY_ENDLESS = 'ROTARY_ENDLESS'
    LINEAR = 'LINEAR'
    LINEAR_ENDLESS = 'LINEAR_ENDLESS'


class ParameterSet2(BaseModel):
    actualAcceleration: Optional[float] = Field(
        None, description='The axis acceleration'
    )
    actualPosition: Optional[float] = Field(
        None, description='The current position of the axis'
    )
    actualSpeed: Optional[float] = Field(None, description='The axis speed')


class Axe(BaseModel):
    browseName: Optional[str] = Field(None, description='Axis BrowseName')
    motionProfile: Optional[MotionProfile] = Field(
        None,
        description='The kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373',
    )
    parameterSet: Optional[ParameterSet2] = Field(
        None, description='Provides a set of parameters'
    )


class MotionDeviceCategory(Enum):
    OTHER = 'OTHER'
    ARTICULATED_ROBOT = 'ARTICULATED_ROBOT'
    SCARA_ROBOT = 'SCARA_ROBOT'
    CARTESIAN_ROBOT = 'CARTESIAN_ROBOT'
    SPHERICAL_ROBOT = 'SPHERICAL_ROBOT'
    PARALLEL_ROBOT = 'PARALLEL_ROBOT'
    CYLINDRICAL_ROBOT = 'CYLINDRICAL_ROBOT'


class ParameterSet3(BaseModel):
    inControl: Optional[bool] = Field(
        None,
        description="The information if the actuators (in most cases a motor) of the motion device are powered up and in control: 'true'",
    )
    onPath: Optional[bool] = Field(
        None,
        description='True if the motion device is on or near enough the planned program path such that program execution can continue. If the MotionDevice deviates too much from this path in case of errors or an emergency stop, this value becomes false. If OnPath is false, the motion device needs repositioning to continue program execution',
    )
    speedOverride: Optional[float] = Field(
        None,
        description='The current speed setting in percent of programmed speed (0 - 100%)',
    )


class Gear(BaseModel):
    browseName: Optional[str] = Field(None, description='Gear BrowseName')
    gearRatio: Optional[float] = Field(
        None,
        description='The transmission ratio of the gear expressed as a fraction as input velocity (motor side) by output velocity (load side)',
    )
    manufacturer: Optional[str] = Field(
        None, description='The name of the company that manufactured the device'
    )
    model: Optional[str] = Field(None, description='The name of the product')
    pitch: Optional[float] = Field(
        None,
        description='The distance covered in millimeters (mm) for linear motion per one revolution of the output side of the driving unit. Pitch is used in combination with GearRatio to describe the overall transmission from input to output of the gear',
    )
    productCode: Optional[str] = Field(
        None,
        description='A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems',
    )
    serialNumber: Optional[str] = Field(
        None,
        description='A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes',
    )


class ParameterSet4(BaseModel):
    brakeReleased: Optional[bool] = Field(
        None,
        description='TRUE the motor is free to run. FALSE means that the motor shaft is locked by the brake',
    )
    effectiveLoadRate: Optional[float] = Field(
        None, description='A percentage of maximum continuous load'
    )
    motorTemperature: Optional[float] = Field(
        None, description='The temperature of the motor'
    )


class Motor(BaseModel):
    browseName: Optional[str] = Field(None, description='Motor BrowseName')
    manufacturer: Optional[str] = Field(
        None, description='The name of the company that manufactured the device'
    )
    model: Optional[str] = Field(None, description='The name of the product')
    parameterSet: Optional[ParameterSet4] = Field(
        None, description='Provides a set of parameters'
    )
    productCode: Optional[str] = Field(
        None,
        description='A unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems',
    )
    serialNumber: Optional[str] = Field(
        None,
        description='A unique production number assigned by the manufacturer of the device. This is often stamped on the outside of the device and may be used for traceability and warranty purposes',
    )


class PowerTrain(BaseModel):
    browseName: Optional[str] = Field(None, description='PowerTrain BrowseName')
    gears: Optional[List[Gear]] = Field(
        None,
        description='Gears is a container for one or more instances of the GearType',
    )
    motors: Optional[List[Motor]] = Field(
        None,
        description='Motors is a container for one or more instances of the MotorType',
    )


class MotionDevice(BaseModel):
    additionalComponents: Optional[List[AdditionalComponent]] = Field(
        None,
        description='AdditionalComponents is a container for one or more instances of subtypes of ComponentType defined in OPC UA DI. The listed components are installed at the motion device, e.g. an IO-board',
    )
    axes: Optional[List[Axe]] = Field(
        None,
        description='Axes is a container for one or more instances of the AxisType',
    )
    browseName: Optional[str] = Field(None, description='MotionDevice BrowseName')
    manufacturer: Optional[str] = Field(
        None, description='The name of the company that manufactured the device'
    )
    model: Optional[str] = Field(None, description='The name of the product')
    motionDeviceCategory: Optional[MotionDeviceCategory] = Field(
        None,
        description='The kind of motion device defined by MotionDeviceCategoryEnumeration based on ISO 8373',
    )
    parameterSet: Optional[ParameterSet3] = Field(
        None, description='Provides a set of parameters'
    )
    powerTrains: Optional[List[PowerTrain]] = Field(
        None,
        description='PowerTrains is a container for one or more instances of the PowerTrainType',
    )


class EmergencyStopFunction(BaseModel):
    active: Optional[bool] = Field(
        None,
        description='TRUE if this particular emergency stop function is active, e.g. that the emergency stop button is pressed, FALSE otherwise',
    )
    browseName: Optional[str] = Field(
        None, description='EmergencyStopFunction BrowseName'
    )
    name: Optional[str] = Field(
        None,
        description='Manufacturer-specific protective stop function identifier within the safety system',
    )


class OperationalMode(Enum):
    OTHER = 'OTHER'
    MANUAL_REDUCED_SPEED = 'MANUAL_REDUCED_SPEED'
    MANUAL_HIGH_SPEED = 'MANUAL_HIGH_SPEED'
    AUTOMATIC = 'AUTOMATIC'
    AUTOMATIC_EXTERNAL = 'AUTOMATIC_EXTERNAL'


class ParameterSet5(BaseModel):
    EmergencyStop: Optional[bool] = Field(
        None,
        description='TRUE if one or more of the emergency stop functions in the robot system are active, FALSE otherwise. If the EmergencyStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed emergency stop functions are active',
    )
    operationalMode: Optional[OperationalMode] = Field(
        None,
        description='The current operational mode. Allowed values are described in OperationalModeEnumeration, see ISO 10218-1:2011',
    )
    protectiveStop: Optional[bool] = Field(
        None,
        description='TRUE if one or more of the enabled protective stop functions in the system are active, FALSE otherwise. If the ProtectiveStopFunctions object is provided, then the value of this variable is TRUE if one or more of the listed protective stop functions are enabled and active',
    )


class ProtectiveStopFunction(BaseModel):
    active: Optional[bool] = Field(
        None,
        description='TRUE if this particular protective stop function is active, e.g. that a stop is initiated, FALSE otherwise. If Enabled is FALSE then Active shall be FALSE',
    )
    browseName: Optional[str] = Field(
        None, description='ProtectiveStopFunction BrowseName'
    )
    enabled: Optional[bool] = Field(
        None,
        description='TRUE if this protective stop function is currently supervising the system, FALSE otherwise. A protective stop function may or may not be enabled at all times, e.g. the protective stop function of the safety doors are typically enabled in automatic operational mode and disabled in manual mode. On the other hand for example, the protective stop function of the teach pendant enabling device is enabled in manual modes and disabled in automatic modes',
    )
    name: Optional[str] = Field(
        None,
        description='Manufacturer-specific protective stop function identifier within the safety system',
    )


class SafetyState(BaseModel):
    browseName: Optional[str] = Field(None, description='SafetyState BrowseName')
    componentName: Optional[str] = Field(None, description='The name of the component')
    emergencyStopFunctions: Optional[List[EmergencyStopFunction]] = Field(
        None,
        description='EmergencyStopFunctions is a container for one or more instances of the EmergencyStopFunctionType. The number and names of emergency stop functions is vendor specific',
    )
    parameterSet: Optional[ParameterSet5] = Field(
        None, description='Provides a set of parameters'
    )
    protectiveStopFunctions: Optional[List[ProtectiveStopFunction]] = Field(
        None,
        description='ProtectiveStopFunctions is a container for one or more instances of the ProtectiveStopFunctionType. The number and names of protective stop functions is vendor specific',
    )


class Type6(Enum):
    MotionDeviceSystem = 'MotionDeviceSystem'


class MotionDeviceSystem(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    controllers: Optional[List[Controller]] = Field(
        None,
        description=' Controllers is a container for one or more instances of the ControllerType. Controller represents a controlling unit of one or more motion devices. A controller can be e.g. a specific control cabinet or a PLC',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    motionDevices: Optional[List[MotionDevice]] = Field(
        None,
        description='MotionDevices is a container for one or more instances of the MotionDeviceType. A motion device has as least one axis and is a multifunctional manipulator designed to move material, parts, tools or specialized devices through variable programmed motions for the performance of a variety of tasks. Examples are an industrial robot, positioner or mobile platform',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    safetyStates: Optional[List[SafetyState]] = Field(
        None,
        description='SafetyStates is a container for one or more instances of the SafetyStatesType',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(None, description='MotionDeviceSystem')
