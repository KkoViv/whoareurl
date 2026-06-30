#!/usr/bin/python3

# File Description : class storage for data needed by all fuctions

# General pipeline:
# - N/A

###################################
# IMPORTED MODULES
###################################

# N/A

###################################
# IMPORTED FUNCTIONS
###################################

# N/A

###################################
# FUNCTIONS
###################################

class SharedData:
    def __init__ (self, ipaddress, name, port):
        
        self.ipaddress = ipaddress
        self.name = name
        self.port = port
        self.result_list = []
        
        print(f"SharedData") # TODO remove
        return
