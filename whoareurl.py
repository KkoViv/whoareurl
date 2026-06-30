#!/usr/bin/python3

# File Description: main program orchestrator.

# General pipeline:
#   - create the argparse parser
#   - define the mutually exclusive target options
#   - define the port option
#   - parse user arguments
#   - create the shared data container
#   - create the HTTP redirect handler class
#   - call the redirection function
#   - call the analysis function
#   - display results
#   - end the program

###################################
# IMPORTED MODULES
###################################

import argparse
import ipaddress


###################################
# IMPORTED FUNCTIONS
###################################

from utils.checkport import checkport #    validates that the port received from argparse is in the range 0-65535
from utils.bye_bye import bye_bye # closes the program cleanly
from core.redir import redir # creates the HTTP request and collects response data from the redirect chain
from core.analyze import analyze #  reads collected response data and prepares the analysis result
from core.display import display # displays the analysis result
from data.http_redirect_handler import CustomHttpRedirectHandler #  custom HTTPRedirectHandler class used by urllib.request
from data.shared_data import SharedData #  data container shared between the program functions

###################################
# FUNCTIONS
###################################

def main():

    # Create the main argparse parser.
    parser = argparse.ArgumentParser(prog="whoareurl", description="Basic webpage fingerprinting", usage="whoareurl -i/-n 10.10.10.10/example.com -p 3000")
    # Create a mutually exclusive group for target selection.
    target = parser.add_mutually_exclusive_group(required=True)
    # Add the IP address target option and validate it with the ipaddress module.
    target.add_argument("-i", "--ipaddress", type=ipaddress.ip_address, help="a valid IP address is required if -i/--ipaddress is chosen" )
    # Add the hostname target option.
    target.add_argument("-n", "--name", type=str, help="a valid hostname is required if -n/--name is chosen")
    # Add the port option and validate it with checkport.
    parser.add_argument("-p", "--port", type=checkport, help="an integer between 0 and 65535") # TODO int is a placeholder for checkport
    # Parse user arguments.
    parsed_args = parser.parse_args()
    shared_data = SharedData(parsed_args.ipaddress, parsed_args.name, parsed_args.port) # Create the data container used to share values between functions.
    print (shared_data.ipaddress, shared_data.name, shared_data.port) # PLACEHOLDER
    
    CustomHttpRedirectHandler()# Create the custom HTTP redirect handler class.
    redir()# Run the redirection function.
    # It creates an urllib handler for redirects and fills a response list,
    # so every step in the redirect chain can be inspected during fingerprinting.
        # HTTPRedirectHandler.redirect_request(req, fp, code, msg, hdrs, newurl)
        # Make the request via OpenerDirector.open(url, data=None[, timeout]).
        # The redirection process reaches the final response through all redirect steps.
        # No manual while loop or for loop is needed for the basic redirect flow.
    analyze()# Run the analysis function on the response list provided by redirection.
    display()# Display the analysis result.
    bye_bye()# Close the program cleanly.



###################################
# FILE ENTRY POINT
###################################

if __name__ == "__main__":
    main()
