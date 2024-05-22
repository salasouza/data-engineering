#!/bin/bash
import apache_beam as beam
import pandas as pd 
import os 

with beam.Pipeline() as p_1:

    consulta = (
        p_1 
        |"Read database" >> beam.io.ReadFromText("database/raw/consulta.txt", skip_header_lines = 1) # Read Transform gerando Pcoll 
        |"Transform" >> beam.Map(lambda record: record.split(','))
        # |"Filter values" >> beam.Filter(lambda record: float(record[2]) > 2)
        |"Filter 1">> beam.Filter(lambda record: float(record[2]) < 10)
        |"Filter 2">> beam.Filter(lambda record: str(record[1])=='Finalizado')
        |"Show database" >> beam.Map(print)
        |"Save database" >> beam.io.WriteToText('database/trusted/consulta_test.txt')    # Write transform gerando Pcoll
        )
    
    if consulta:
        p_1.run()
        print("\nOperation Success!\n")
    else:
        print("\nOperation Failed!\n")