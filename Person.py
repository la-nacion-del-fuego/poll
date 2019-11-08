#!/usr/bin/env python




class Person:
    
    
    
    def __init__(self,race,religion,marital_status,sexual_orientation,security_perception=10,childrens=0,age=18,sex="M",income=1825,education=12,):
        self.age = age #year
        self.sex = sex #m,f
        self.income = income # DLS per Year
        self.education = education #years
        self.race = race #
        self.religion = religion
        self.marital_status = marital_status
        self.sexual_orientation = sexual_orientation
        self.childrens = childrens
        self.security_perception = security_perception #0 insecure -> 10 secure
