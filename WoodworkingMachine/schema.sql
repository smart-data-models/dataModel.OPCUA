/* (Beta) Export of data model WoodworkingMachine of the subject dataModel.OPCUA for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WoodworkingMachine_type AS ENUM ('WoodworkingMachine');
CREATE TABLE WoodworkingMachine (Machines JSON, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, name TEXT, owner JSON, source TEXT, type WoodworkingMachine_type);