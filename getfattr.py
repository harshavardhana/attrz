#!/usr/bin/env python2

import os
import sys
from optparse import OptionParser
import base64

import xattr

if __name__ == '__main__':
    usage = "usage: %prog [-n name|-d] [-e en] [-m pattern] path...."
    parser = OptionParser(usage=usage)
    parser.add_option("-n", action="store", dest="name", type="string",
                      help="Dump the value of the named extended attribute"
                      " extended attribute.")
    parser.add_option("-d", action="store_true", dest="dump",
                      help="Dump the values of all extended attributes"
                      " associated with pathname.")
    parser.add_option("-e", action="store", dest="encoding", type="string",
                      help="Encode values after retrieving them. Valid values"
                      " of [en] are `text`, `hex`, and `base64`. Values encoded"
                      " as text strings are enclosed in double quotes (\"),"
                      " while strings encoded as hexidecimal and base64 are"
                      " prefixed with 0x and 0s, respectively.")
    parser.add_option("-m", action="store", dest="pattern", type="string",
                      help="Only include attributes with names matching the"
                      " regular expression pattern. The default value for"
                      " pattern is \"^user\\.\", which includes all the"
                      " attributes in the user namespace. Specify \"-\" for"
                      " including all attributes. Refer to attr(5) for a more"
                      " detailed discussion of namespaces.")
    parser.add_option("--absolute-names", action="store_true", dest="absnames",
                      help="Do not strip leading slash characters ('/')."
                      " The default behaviour is to strip leading slash characters.")
    parser.add_option("--only-values", action="store_true", dest="onlyvalues",
                      help="Dump out the raw extended attribute value(s)"
                      " without encoding them.")

    (option,args) = parser.parse_args()
    if not args:
        print ("Usage: getfattr [-hRLP] [-n name|-d] [-e en] [-m pattern] path...")
        print ("Try `getfattr --help' for more information.")
        sys.exit(1)

    if option.encoding and option.onlyvalues:
        print ("-e/encoding and --only-values are mutually exclusive...")
        sys.exit(1)

    if option.dump and option.name:
        print ("-d and -n are mutually exclusive...")
        sys.exit(1)

    args[0] = os.path.abspath(args[0])

    if option.name:
        try:
            attr = xattr.getxattr(args[0], option.name)
            print (attr.encode('hex'))
        except Exception as err:
            print (err)
            sys.exit(1)

    if option.dump:
        try:
            xattrs = xattr.listxattr(args[0])
            print (xattrs)
        except Exception as err:
            print (err)
            sys.exit(1)
