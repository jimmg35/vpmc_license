
from .License import License
from .Manage import Manage

class Holder():
    license: License
    manage: Manage

    def __init__(self, license, manage):
        self.license = license
        self.manage = manage