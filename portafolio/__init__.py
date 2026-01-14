import pymysql

# Le decimos a Django que use PyMySQL
pymysql.install_as_MySQLdb()

# Engañamos a Django para que crea que tenemos la versión más reciente
pymysql.version_info = (2, 2, 1, "final", 0)