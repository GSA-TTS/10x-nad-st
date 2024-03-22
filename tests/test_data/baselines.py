EXPECTED_DEFAULT_CONFIG = {
    "data_required_fields": [
        "Add_Number",
        "AddNo_Full",
        "St_Name",
        "StNam_Full",
        "County",
        "Inc_Muni",
        "Post_City",
        "State",
        "UUID",
        "AddAuth",
        "Longitude",
        "Latitude",
        "NatGrid",
        "Placement",
        "AddrPoint",
        "DateUpdate",
        "NAD_Source",
        "DataSet_ID",
    ]
}

TESTPRODUCER1_CONFIG = {
    "COL_0": ["ID"],
    "COL_1": ["STCOFIPS"],
    "COL_10": ["HISPPOP"],
    "COL_11": ["AMERIND"],
    "COL_12": ["ASIAN"],
    "COL_13": ["PACIFIC"],
    "COL_14": ["RACE2UP"],
    "COL_15": ["OTHRACE"],
    "COL_16": ["LASTUPDATE"],
    "COL_17": ["LASTEDITOR"],
    "COL_18": ["AGEMAJOR"],
    "COL_19": ["AREASQMETER"],
    "COL_2": ["TRACT", "Pacific"],
    "COL_20": ["Shape_Length"],
    "COL_21": ["Shape_Area"],
    "COL_22": ["geometry"],
    "COL_3": ["STFID"],
    "COL_4": ["BLOCK"],
    "COL_5": ["TOTPOP"],
    "COL_6": ["POPDENS", "totPop"],
    "COL_7": ["RACEBASE"],
    "COL_8": ["WHITE"],
    "COL_9": ["BLACK"],
}

TESTPRODUCER2_CONFIG = {
    "COL_0": ["NAME"],
    "COL_1": ["ST"],
    "COL_2": ["ZIP"],
    "COL_3": ["RuleID"],
    "COL_4": ["geometry"],
}

NAPERVILLE_GDB_REPORT = {
    "overview": {
        "feature_count": 23,
        "features_flagged": 0,
        "records_count": 6012,
        "records_flagged": 0,
        "etl_update_required": False,
        "data_update_required": False,
    },
    "features": [
        {
            "provided_feature_name": "ID",
            "nad_feature_name": "COL_0",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "STCOFIPS",
            "nad_feature_name": "COL_1",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "HISPPOP",
            "nad_feature_name": "COL_10",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "AMERIND",
            "nad_feature_name": "COL_11",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "ASIAN",
            "nad_feature_name": "COL_12",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "PACIFIC",
            "nad_feature_name": "COL_13",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "RACE2UP",
            "nad_feature_name": "COL_14",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "OTHRACE",
            "nad_feature_name": "COL_15",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "LASTUPDATE",
            "nad_feature_name": "COL_16",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "LASTEDITOR",
            "nad_feature_name": "COL_17",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "AGEMAJOR",
            "nad_feature_name": "COL_18",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "AREASQMETER",
            "nad_feature_name": "COL_19",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "TRACT",
            "nad_feature_name": "COL_2",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "Shape_Length",
            "nad_feature_name": "COL_20",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "Shape_Area",
            "nad_feature_name": "COL_21",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "geometry",
            "nad_feature_name": "COL_22",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "STFID",
            "nad_feature_name": "COL_3",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "BLOCK",
            "nad_feature_name": "COL_4",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "TOTPOP",
            "nad_feature_name": "COL_5",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "POPDENS",
            "nad_feature_name": "COL_6",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "RACEBASE",
            "nad_feature_name": "COL_7",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "WHITE",
            "nad_feature_name": "COL_8",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
        {
            "provided_feature_name": "BLACK",
            "nad_feature_name": "COL_9",
            "populated_count": 6012,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 6012,
            "invalid_domains": [],
        },
    ],
}
MAJOR_CITIES_SHP_REPORT = {
    "overview": {
        "feature_count": 5,
        "features_flagged": 2,
        "records_count": 120,
        "records_flagged": 6,
        "etl_update_required": False,
        "data_update_required": False,
        "missing_required_fields": [
            "Add_Number",
            "AddNo_Full",
            "St_Name",
            "StNam_Full",
            "County",
            "Inc_Muni",
            "Post_City",
            "State",
            "UUID",
            "AddAuth",
            "Longitude",
            "Latitude",
            "NatGrid",
            "Placement",
            "AddrPoint",
            "DateUpdate",
            "NAD_Source",
            "DataSet_ID",
        ],
    },
    "features": [
        {
            "provided_feature_name": "NAME",
            "nad_feature_name": "COL_0",
            "populated_count": 120,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "ST",
            "nad_feature_name": "COL_1",
            "populated_count": 120,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "ZIP",
            "nad_feature_name": "COL_2",
            "populated_count": 117,
            "null_count": 3,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "RuleID",
            "nad_feature_name": "COL_3",
            "populated_count": 117,
            "null_count": 3,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "geometry",
            "nad_feature_name": "COL_4",
            "populated_count": 120,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
    ],
}

NM911_ADDRESS_202310_REPORT = {
    "overview": {
        "feature_count": 15,
        "features_flagged": 9,
        "records_count": 1000,
        "records_flagged": 1000,
        "etl_update_required": False,
        "data_update_required": False,
        "missing_required_fields": [
            "AddNo_Full",
            "County",
            "Inc_Muni",
            "State",
            "UUID",
            "Longitude",
            "Latitude",
            "NatGrid",
            "Placement",
            "AddrPoint",
            "NAD_Source",
            "DataSet_ID",
        ],
    },
    "features": [
        {
            "provided_feature_name": "ADD_NUMBER",
            "nad_feature_name": "Add_Number",
            "populated_count": 1000,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "ADD_SUFFIX",
            "nad_feature_name": "AddNum_Suf",
            "populated_count": 114,
            "null_count": 886,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "STR_DIR",
            "nad_feature_name": "St_PreDir",
            "populated_count": 160,
            "null_count": 840,
            "invalid_domain_count": 6,
            "valid_domain_count": 154,
            "invalid_domains": ["northerns", "southerns"],
            "domain_frequency": {
                "N": 50,
                "W": 36,
                "S": 35,
                "E": 33,
                "northerns": 3,
                "southerns": 3,
            },
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "STR_PRETYP",
            "nad_feature_name": "St_PreTyp",
            "populated_count": 10,
            "null_count": 990,
            "invalid_domain_count": 0,
            "valid_domain_count": 10,
            "invalid_domains": [],
            "domain_frequency": {
                "STHY": 5,
                "CALLE": 2,
                "CAMINO": 2,
                "NEW MEXICO HWY": 1,
            },
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "STR_NAME",
            "nad_feature_name": "St_Name",
            "populated_count": 1000,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "STR_SUFFIX",
            "nad_feature_name": "St_PosTyp",
            "populated_count": 839,
            "null_count": 161,
            "invalid_domain_count": 8,
            "valid_domain_count": 831,
            "invalid_domains": ["Drive Parkway", "Crossings Drive", "Unknown Drive"],
            "domain_frequency": {
                "RD": 178,
                "ST": 167,
                "DR": 164,
                "AVE": 126,
                "LN": 46,
                "CT": 36,
                "PL": 25,
                "BLVD": 22,
                "TRL": 18,
                "WAY": 18,
                "CIR": 14,
                "LOOP": 12,
                "Crossings Drive": 3,
                "Drive Parkway": 3,
                "PKWY": 3,
                "Unknown Drive": 2,
                "HWY": 1,
                "RD.": 1,
            },
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "POST_DIR",
            "nad_feature_name": "St_PosDir",
            "populated_count": 328,
            "null_count": 672,
            "invalid_domain_count": 0,
            "valid_domain_count": 328,
            "invalid_domains": [],
            "domain_frequency": {
                "NE": 159,
                "NW": 64,
                "SE": 51,
                "SW": 48,
                "N": 2,
                "S": 2,
                "E": 1,
                "W": 1,
            },
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "ROAD_LABEL",
            "nad_feature_name": "StNam_Full",
            "populated_count": 1000,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "COMNAME",
            "nad_feature_name": "Post_City",
            "populated_count": 717,
            "null_count": 283,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "MSAG_COM",
            "nad_feature_name": "Uninc_Comm",
            "populated_count": 794,
            "null_count": 206,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "ZIPCODE",
            "nad_feature_name": "Zip_Code",
            "populated_count": 859,
            "null_count": 141,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "DPID",
            "nad_feature_name": "AddAuth",
            "populated_count": 1000,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "DATE_UPD",
            "nad_feature_name": "Effective",
            "populated_count": 1000,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "last_edi_1",
            "nad_feature_name": "DateUpdate",
            "populated_count": 1000,
            "null_count": 0,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
        {
            "provided_feature_name": "EXCEPTION",
            "nad_feature_name": "AnomStatus",
            "populated_count": 791,
            "null_count": 209,
            "invalid_domain_count": 0,
            "valid_domain_count": 0,
            "invalid_domains": [],
            "domain_frequency": {},
            "high_domain_cardinality": False,
        },
    ],
}
