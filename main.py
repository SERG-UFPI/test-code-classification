#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fileAnalysis import *

from utilities import *

def simple_example(file):
    
    keyword_lookup = lookup_generator("keywords.txt") #keywords
    
    tech_lookup = tech_lookup_generator("testingTechnologiesFixed3.csv") #testtechs
    
    opened_file = open(file, "r", encoding="latin-1")
    
    file_extension = file.rpartition(".")[-1]
    
    file_contents = ""
    for line in opened_file:
        file_contents += line
        file_contents += "\n"
    opened_file.close()
    
    test_import = findTestTechs(tech_lookup, file_extension, file_contents)
    
    test_call = findKeywordTechs(keyword_lookup, file_extension, file_contents)
    
    if test_import and test_call :      
        has_test = True
    
    else :
        has_test = False
    
    print({'test_import': test_import, 'test_call': test_call, 'has_test': has_test})
    

simple_example("example1/CalculatorTest.java")