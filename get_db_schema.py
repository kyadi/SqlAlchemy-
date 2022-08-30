
#sudo pip install configparser
#sudo pip install sqlalchemy
#sudo pip install pydot
#sudo pip install sqlalchemy_schemadisplay
#sudo pip install graphviz

#sudo apt-get install GraphViz


#Python Script to generate ER diagram

#!/usr/bin/env python
import ConfigParser
from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph

config = ConfigParser.RawConfigParser()
##Open nova.conf file
config.read('/etc/nova/nova.conf')
##Read the flag "sql_connection" from nova.conf and make connection to database
connection = config.get("DEFAULT", "sql_connection")


##Or you can directly specify the connection like
##connection = "mysql://root:password@127.0.0.1/nova?charset=utf8"

##Generate graph of connected database
graph = create_schema_graph(metadata=MetaData(connection),
                 show_datatypes=False,
                 show_indexes=False,
                 rankdir='LR',
                 concentrate=False)

##Generate png image                
graph.write_png('dbschema.png')