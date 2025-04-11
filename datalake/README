datalake/
├── raw/                                  # RAW Layer: Original/unprocessed data (full load)
│   └── rebrickable/                      # Data Source: Rebrickable
│       ├── LEGO_Catalog_Database/        # Dataset 1: LEGO Catalog
│       │   └── year=YYYY/                # Ingestion date (e.g., year=2024)
│       │       └── month=MM/             
│       │           └── day=DD/           
│       │               └── file.csv      # Native files (CSV/JSON)
│       └── oltp_db/                      # Dataset 2: OLTP Database
│           └── year=YYYY/                # Same ingestion structure
│               └── month=MM/             
│                   └── day=DD/           
│                       └── file.csv      
│
├── silver/                               # SILVER Layer: Cleaned/enriched data
│   └── rebrickable/                     
│       ├── LEGO_Catalog_Database/        # Delta tables by category
│       │   ├── sets/                     # Example: "sets" table
│       │   │   ├── _delta_log/           # Delta transaction log
│       │   │   └── part-XXXX.parquet     # Data in Parquet format
│       │   ├── themes/                   # Another category
│       │   │   ├── _delta_log/           
│       │   │   └── part-XXXX.parquet     
│       │   └── ...                       
│       └── oltp_db/                      # Processed OLTP data
│           ├── orders/                   
│           │   ├── _delta_log/           
│           │   └── part-XXXX.parquet     
│           └── users/                    
│               ├── _delta_log/           
│               └── part-XXXX.parquet     
│
└── gold/                                 # GOLD Layer: Dimensional modeling (BI-ready)
    └── rebrickable/                      
        └── delta_tables_data_modelling/  # Star schema
            ├── dim_date/                 # Date dimension
            │   ├── _delta_log/           
            │   └── part-XXXX.parquet     
            ├── dim_set/                  # Set dimension
            │   ├── _delta_log/           
            │   └── part-XXXX.parquet     
            ├── dim_user/                 # User dimension
            │   ├── _delta_log/           
            │   └── part-XXXX.parquet     
            └── fact_orders/              # Orders fact table
                ├── _delta_log/           
                └── part-XXXX.parquet     
