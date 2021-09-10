import re


regex = re.compile(r'使字第*\D(\d+)')

class License():
    licenseType: str
    assignLicenseNumber: str
    originalLicenseNumber: str
    reDesignCount: str
    baseArea: str
    buildingArea: str
    totalFloorArea: str
    buildingHeight: str
    basementRefugeArea: str
    lawVacantArea: str
    buildingType: str
    structureType: str
    groundLevelCount: str
    underGroundLevelCount: str
    buildingCount: str
    householdCount: str
    buildingRepresentative: str
    designer: str
    supervisor: str
    responsor: str
    grocItem: str
    parkSpace: str
    assignDate: str
    startDate: str
    finishDate: str
    levelDesc: str
    landNumberDesc: str
    addressDesc: str
    county: str


    parsedLicenseNumber: str
    parsedLicenseYear: str


    isDeviant: bool


    def __init__(self, row):
        self.licenseType = row["執照類別"]
        self.assignLicenseNumber = row["核發執照字號"]
        self.originalLicenseNumber = row["原領執照字號"]
        self.reDesignCount = row["變更設計次數"]
        self.baseArea = row["基地面積"]
        self.buildingArea = row["建築面積"]
        self.totalFloorArea = row["總樓地板面積"]
        self.buildingHeight = row["建築物高度"]
        self.basementRefugeArea = row["地下避難面積"]
        self.lawVacantArea = row["法定空地面積"]
        self.buildingType = row["建造類別"]
        self.structureType = row["構造別"]
        self.groundLevelCount = row["地上層數"]
        self.underGroundLevelCount = row["地下層數"]
        self.buildingCount = row["棟數"]
        self.householdCount = row["戶數"]
        self.buildingRepresentative = row["起造人代表人"]
        self.designer = row["設計人"]
        self.supervisor = row["監造人"]
        self.responsor = row["承造人"]
        self.grocItem = row["雜項工作物"]
        self.parkSpace = row["停車空間"]
        self.assignDate = row["發照日期"]
        self.startDate = row["實際開工日期"]
        self.finishDate = row["竣工日期"]
        self.levelDesc= str(row["樓層概要"])
        self.landNumberDesc = str(row["地號"])
        self.addressDesc = str(row["門牌"])
        self.county= row["縣市別"]

        self.isDeviant = False
        self.parsedLicenseNumber = None
        self.parsedLicenseYear = None

        self.startUp()
        
    def startUp(self):
        self.parseLicenseNumber()
        self.parseLicenseYear()

    def parseLicenseNumber(self):
        try:
            self.parsedLicenseNumber = str(regex.search(self.assignLicenseNumber).group(1))
            try:
                int(self.parsedLicenseNumber)
            except:
                self.isDeviant = True
        except:
            self.isDeviant = True
    
    def parseLicenseYear(self):

        if str(self.assignLicenseNumber) != "nan":
            if "(" in self.assignLicenseNumber:
                self.parsedLicenseYear = str(self.assignLicenseNumber[self.assignLicenseNumber.find("(")+1:self.assignLicenseNumber.find(")")])
                try:
                    int(self.parsedLicenseYear)
                except:
                    self.isDeviant = True
            else:
                self.isDeviant = True
        else:
            self.isDeviant = True