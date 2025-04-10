# End-to-end-Azure-Data-Engineering-Project


#resumen
En este proyecto se extrae los datos de las fuente de datos que son principalmente una pagina web (mediante web scraping) y de una Azure sql database (oltp database), la ingesta de los datos se hace mediante azure data factory, se procede a guardarlo en un datalake (ADLSg2), este datalake contendra 3 capas (raw/silver/gold), donde en un primer momento se guarda los datos de forma nativa (csv)(raw layer), luego se realiza algunas transformaciones (filtrado, limpiado, etc) en databricks y se guarda en formato delta en la segunda capa (silver layer), luego se procede al dimension modelling para responder a los intereses del negocio (dichas transformaciones se hacen usando lenguaje sql en el entorno de databricks) y dichas dimensions and fact tables se guardan en una tercera capa (gold layer). Luego se procede a crear un serveless sql warehouse donde se guardan las tablas en databricks para poder conectar/serve  a power bi y de esta forma los interesados/end users puedan visualizar estos datos y tomar decisiones. Todo esto orquesteado mediante Azure data factory.

#Tools and technologies

Cloud: Azure
OLTP Database: Azure SQL
Processing: Databricks
Storage: Azure Data Lake Storage Gen 2
Business Intelligence Dashboard: Power BI
Data Pipelines/Rrchestrator: Azure Data Factory

#arquitectura del proyecto
Aqui se puede visualizar el poryecto realizado. (imagen.png)
 <img src="https://i.imgur.com/Kn6sx3y.png" alt="Profile Banner">

 #objetivos

 Extrear datos de una pagina web y una base de datos oltp, trasformarlos y cargarlos en power bi.

#pasos
 

