-- ceates the table to hold the types and their definitions for all the eve types

CREATE TABLE universe_types (
    type_id INTEGER PRIMARY KEY,
    capacity FLOAT,
    description TEXT,
    graphic_id INTEGER,
    group_id INTEGER NOT NULL,
    icon_id INTEGER,
    market_group_id INTEGER,
    mass FLOAT,
    name TEXT NOT NULL,
    packaged_volume FLOAT,
    portion_size INTEGER,
    published BOOLEAN,
    radius FLOAT,
    volume FLOAT
);

CREATE TABLE universe_types_dogma_attributes (
    type_id INTEGER NOT NULL,
    attribute_id INTEGER NOT NULL,
    value FLOAT NOT NULL,
    PRIMARY KEY (type_id, attribute_id),
    FOREIGN KEY (type_id) REFERENCES universe_types (type_id)
);

CREATE TABLE universe_types_dogma_effects (
    type_id INTEGER NOT NULL,
    effect_id INTEGER NOT NULL,
    is_default BOOLEAN NOT NULL,
    PRIMARY KEY (type_id, effect_id),
    FOREIGN KEY (type_id) REFERENCES universe_types (type_id)
);

-- Index for the name field
CREATE INDEX idx_universe_types_name ON universe_types (name);

-- Index for the group_id field
CREATE INDEX idx_universe_types_group_id ON universe_types (group_id);

