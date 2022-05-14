import os
##DATA BASE
##modificar segun tu configuracion
user = "root"  # os.environ["MYSQL_USER"]
password = "5492"  # os.environ["MYSQL_PASSWORD"]
host = "localhost"  # os.environ["MYSQL_HOST"]
database = "sepomex"  # os.environ["MYSQL_DATABASE"]

Database = f"mysql://{user}:{password}@{host}/{database}"
print(Database)
