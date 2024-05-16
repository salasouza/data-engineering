#!/bin/bash
import apache_beam as beam
import pandas as pd 
import os 

with beam.Pipeline() as p_1:

    consulta = (
        p_1 
        |"Read database" >> beam.io.ReadFromText("database/raw/iris.csv", skip_header_lines = 1)
        |"Transform" >> beam.Map(lambda record: record.split(','))
        |"Filter values" >> beam.Filter(lambda record: float(record[2]) > 2)
        # |"Show database" >> beam.Map(print)
        |"Save database" >> beam.io.WriteToText('database/trusted/iris_test.csv')    
        )
    
    if consulta:
        p_1.run()
        print("Operation Success!")
    else:
        print("Operation Failed!")