#!/bin/bash
import apache_beam as beam
import pandas as pd 
import os 


# df = pd.read_csv('database/iris.csv')

# print(df.head(3))

p1 = beam.Pipeline()

consulta = (
    p1 
    |"Read database" >> beam.io.ReadFromText("database/iris.txt", skip_header_lines = 1)
    # |"Transform" >> beam.Map(lambda record: record.split(','))
    # |"Show database" >> beam.Map(print)
    |"Save database" >> beam.io.WriteToText('database/iris_test.txt')    

)

p1.run()