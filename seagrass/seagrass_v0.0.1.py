import MarinegeoTemplateBuilder

metadataValues = {"TemplateVersion": "v0.0.1",
                  "ProtocolVersion": "V20180820",
                  "Title": "Seagrass Community data - [your site name] - [date in YYYY-MM-DD format]"}


MarinegeoTemplateBuilder.main('MarineGEO_Seagrass_DataEntryTemplate_v0.0.1.xlsx',
           'fields_v0.0.1.csv',
           'vocab_v0.0.1.csv',
           "MarineGEO Seagrass Community Sampling Template",
           'DEFAULT', protect=True, metadataValues=metadataValues)


