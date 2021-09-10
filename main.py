
import pandas as pd 
from src.model.Manage import Manage
from src.model.License import License
from src.model.Holder import Holder
from typing import List
import os 
from os import listdir
import json


def read_manage(path):
    output: List[Manage] = []
    data = pd.read_csv(path, encoding="utf8")
    for index, row in data.iterrows():
        instance = Manage(row)
        output.append(instance)
    return output

def read_license(path) -> List[License]:
    output = []
    aggregatedRawData = []
    for i in listdir(path):
        with open(os.path.join(path, i), encoding='utf-8') as f:
            data = json.load(f)
            for j in data.keys():
                aggregatedRawData += data[j]
    for i in aggregatedRawData:
        license = License(i)
        output.append(license)
    return output

def filterNonDeviantData(dataArray):
    output = []
    for i in dataArray:
        if i.isDeviant == False:
            output.append(i)
    return output

def joinData(filteredManageArray: List[Manage], 
             filteredLicenseArray: List[License]) -> None:
    output = []
    for i in filteredLicenseArray:
        for j in filteredManageArray:
            if str(i.parsedLicenseNumber) == str(j.parsedLicenseNumber) and str(i.parsedLicenseYear) == str(j.parsedLicenseYear):
                holder = Holder(i, j)
                output.append(holder)
    return output

if __name__ == "__main__":
    manageArray: List[Manage] = read_manage("./data/manage.csv")
    licenseArray: List[License] = read_license("./data/license")

    filteredManageArray: List[Manage] = filterNonDeviantData(manageArray)
    filteredLicenseArray: List[License] = filterNonDeviantData(licenseArray)

    joinedArray: List[Holder] = joinData(filteredManageArray, filteredLicenseArray)
    for i in joinedArray:
        print(i.manage.licenseNumber, i.license.assignLicenseNumber)