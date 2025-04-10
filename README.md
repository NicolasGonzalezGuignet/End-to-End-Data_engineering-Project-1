# End-to-end-Azure-Data-Engineering-Project


#resumen
En este proyecto se extrae los datos de las fuente de datos que son principalmente una pagina web (mediante web scraping) y de una Azure sql database (oltp database), la ingesta de los datos se hace mediante azure data factory, se procede a guardarlo en un datalake (ADLSg2), este datalake contendra 3 capas (raw/silver/gold) basada en la Medallion Architecture ([imagen](https://i.imgur.com/dMMYxvw.png)), donde en un primer momento se guarda los datos de forma nativa (csv)(raw layer), luego se realiza algunas transformaciones (filtrado, limpiado, etc) en databricks y se guarda en formato delta en la segunda capa (silver layer), luego se procede al dimension modelling para responder a los intereses del negocio (dichas transformaciones se hacen usando lenguaje sql en el entorno de databricks) y dichas dimensions and fact tables se guardan en una tercera capa (gold layer). Luego se procede a crear una bd se guardan las tablas en databricks para poder conectar/serve  a power bi y de esta forma los interesados/end users puedan visualizar estos datos y tomar decisiones. Todo esto orquesteado mediante Azure data factory.

#Tools and technologies

Cloud: Azure
OLTP Database: Azure SQL
Processing: Databricks
Storage: Azure Data Lake Storage Gen 2
Business Intelligence Dashboard: Power BI
Data Pipelines/Rrchestrator: Azure Data Factory

#arquitectura del proyecto
Aqui se puede visualizar el poryecto realizado.
 <img src="https://i.imgur.com/jDJ8lNT.png" alt="architecture">

 #objetivos

 Extrear datos de una pagina web y una base de datos oltp, trasformarlos y cargarlos en power bi.


## recursos aprovisionados en azure:
-Azure Data Factory (ADF)
-Azure Databricks
-Storage Account (ADLSg2)
-Azure SQL Database
-Azure SQL server
-Function App (Azure function)

## Descripcion del proceso

1° pipeline (ingest_http_rebrickable)
-Se crea una actividad [Azure Function](scripts/azure-function/web_scraping.py) para poder hacer webscraping en la pagina "https://rebrickable.com/downloads/" para obtener    
 los links de descarga y poder de esta forma obtener la bd del catalogo de LEGO

  esta base de datos contiene informacion como:
  Official LEGO items - Sets, Parts and Minifigs (no B-Models, Sub-Sets, MOCs)
  Sets and Minifigs contain one or more Inventories (inventories.csv)
  Inventories can contain Sets (inventory_sets.csv) and/or Parts (inventory_parts.csv) and/or Minifigs (inventory_minifigs.csv)
  Part Relationship rel_types are: (P)rint, Pai(R), Su(B)-Part, (M)old, Pa(T)tern, (A)lternate
  [imagen](https://i.imgur.com/LYDhQID.png)
-Otra actividad que es para convertir esa cadena de links de la actividad anterior en un array y de esta forma poder procesarlo en la actividad siguiente
-Una actividad ForEach y dentro de una actividad copydata que va a descargar los links y guardarlos en la raw layer en un ADLSg2
[imagen](https://i.imgur.com/efTcCUZ.png)

 2° pipeline (ingest_oltp_db_rebrickable)
 -Se crea una actividad LookUp para obtener los nombres de las tablas en la [oltp-database](scripts/oltp-database/) (scripts para generar las tablas, datos e importar los datos), esto devuelve un array con el nombre de las tablas 
 -Dicho array lo utilizaremos en un actividad ForEach para luego utilizar una actividad copydata dentro de este, que mueve las tablas a la raw layer en el ADLSg2.
 [imagen](https://i.imgur.com/aONY9Sr.png)

 3° pipeline (databricks_pipeline)
- Se crean 2 notebooks en Databricks, el primero(agregar hipervinculo) es para transformar los datos (limpiar,filtrar,aumentarlos,etc) y guardar los datos tranformados en delta en una segunda "silver" layer y luego el segundo (agregar hipervinculo) es para obtener un modelado de datos basado en el dimension modelling (fact y dimension tables)(agregar pic de como quedo el modelo, de power bi sacarlo..) que tratara de responder los intereses del negocio, dichas tablas se guardan en una tercera "gold" layer, estos dos notebooks se agregaran como actividades separadas dentro de ADF.
  [imagen](https://i.imgur.com/CL67s0o.png)


4° pipeline
- Este pipeline es para agrupar todos los pipeline en un solo pipeline, usando la actividad Execute Pipeline.
  [imagen](https://i.imgur.com/uUBEYPB.png)


5° Se hace un conexion entre la bd "gold" en databricks y power Bi, para poder ver los datos en tiempo real.
[imagen](https://i.imgur.com/OpWGgAq.png)

En este file(hipervinculo al arm template) se puede ver el ARM template para aprovisionar un workspace igual en ADF.

 

 

 


 

