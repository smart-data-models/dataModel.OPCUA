<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティマシンツール  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.OPCUA/blob/master/MachineTool/LICENSE.md)  
[文書が自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**機械工具とは、固定された（つまり移動できない）機械装置であり、（通常は電気と圧縮空気によって）動力を供給される。  
バージョン: 0.0.1  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `myMachine[array]`: 情報モデルの工作機械インターフェース全体のリストを表す。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSIタイプ。MachineToolでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `myMachine`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### MachineTool NGSI-v2 キー値の例  
以下は、JSON-LD形式のMachineToolのkey-valuesの例である。これは、`options=keyValues`を使用したときにNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### MachineTool NGSI-v2 正規化例  
以下は、正規化されたJSON-LDフォーマットのMachineToolの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### MachineTool NGSI-LD キー値の例  
JSON-LD形式のMachineToolのkey-valuesの例である。これは、`options=keyValues`を使用したときにNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### MachineTool NGSI-LD 正規化例  
以下は、正規化されたJSON-LDフォーマットのMachineToolの例である。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
