#install dependinices

import os
import imp


def try_and_install(module):
    try:
        imp.find_module(module)

    except:
        os.system("pip3 install "+str(module))


try_and_install("imageio")
