import re


regex = re.compile(r'使字第*\D(\d+)')

class Manage():
    name: str                  # 管委會名稱
    address: str               # 地址門牌
    licenseNumber: str         # 使照號碼
    approveDate: str           # 核准日期
    approveNumber: str         # 核准文號 
    certificationNumber: str   # 證書編號

    parsedLicenseNumber: str
    parsedLicenseYear: str


    isDeviant: bool

    def __init__(self, row):
        self.name = row["管理組織名稱"]
        self.address = row["地址門牌"]
        self.licenseNumber = row["使照號碼"]
        self.approveDate = row["核准日期"]
        self.approveNumber = row["核准文號"]
        self.certificationNumber = row["證書編號"]

        self.isDeviant = False
        self.parsedLicenseNumber = None
        self.parsedLicenseYear = None
        
        self.startUp()

    def startUp(self):
        self.parseLicenseNumber()
        self.parseLicenseYear()

    def parseLicenseNumber(self):
        try:
            self.parsedLicenseNumber = str(regex.search(self.licenseNumber).group(1))
            try:
                int(self.parsedLicenseNumber)
            except:
                self.isDeviant = True
        except:
            self.isDeviant = True
    
    def parseLicenseYear(self):

        if str(self.licenseNumber) != "nan":
            if "(" in self.licenseNumber:
                self.parsedLicenseYear = str(self.licenseNumber[self.licenseNumber.find("(")+1:self.licenseNumber.find(")")])
                try:
                    int(self.parsedLicenseYear)
                except:
                    self.isDeviant = True
            else:
                self.isDeviant = True
        else:
            self.isDeviant = True
        
