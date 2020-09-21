import argparse
import ipaddress

from plenum.common.util import is_hostname_valid

class PoolLedger:

    @staticmethod
    def _bootstrap_args_type_ips_hosts(ips_hosts_str_arg):
        ips = []
        for arg in ips_hosts_str_arg.split(','):
            arg = arg.strip()
            try:
                ipaddress.ip_address(arg)
            except ValueError:
                if not is_hostname_valid(arg):
                    raise argparse.ArgumentTypeError(
                    "'{}' is not a valid IP or hostname".format(arg)
                )
                else:
                    ips.append(arg)
            else:
                ips.append(arg)

        return ips

    @staticmethod
    def _bootstrap_args_type_verkeys(verkeys_str_arg):
        verkeys = []
        i =1 
        for arg in verkeys_str_arg.split(','):
            arg = str(arg)
            arg = arg.strip()
            if len(arg) != 64:
                raise argparse.ArgumentTypeError("The lenght verification key {} should be 64 digit long".format(i))           
            verkeys.append(arg)
            i += 1

        return verkeys

    
    @staticmethod
    def _bootstrap_args_type_bls(bls_str_arg):
        bls = []
        i =1 
        for arg in bls_str_arg.split(','):
            arg = str(arg)
            arg = arg.strip()
            if len(arg) != 174:
                raise argparse.ArgumentTypeError("The lenght of this key {} should be 174 digit long".format(i))           
            bls.append(arg)
            i += 1

        return bls

    @staticmethod
    def _bootstrap_args_type_list(list_str_arg):
        arg_list = []
        i =1 
        for arg in list_str_arg.split(','):
            arg = str(arg)
            arg = arg.strip()
            arg_list.append(arg)
            i += 1

        return arg_list

    @staticmethod
    def _bootstrap_args_type_port(port_str_arg):
        arg_list = []
        i =1 
        for arg in port_str_arg.split(','):
            arg = str(arg)
            arg = arg.strip()
            try:
                arg_list.append(int(arg))
            except Exception as ex:
                print("Port must be an integer")
                print(ex)
                exit()
            i += 1

        return arg_list


    @staticmethod
    def _bootstrap_args_type_dids(dids_str_arg):
        did = []
        i =1 
        for arg in dids_str_arg.split(','):
            arg = str(arg)
            arg = arg.strip()
            if len(arg) != 22:
                raise argparse.ArgumentTypeError("The lenght of did {} should be 22 digit long".format(i))           
            did.append(arg)
            i += 1

        return did

