import MarinegeoTemplateBuilder

# metadata values to write to the workbook

metadataValues = {"Title": "DEMO - fields and vocab from csv files and seeded with random values"}

# build the data entry template workbook
MarinegeoTemplateBuilder.main('Demo-Template-CSV.xlsx', "fields.csv", "vocab.csv", 'DEFAULT',
                              metadataValues=metadataValues, seededValues="RANDOM")
