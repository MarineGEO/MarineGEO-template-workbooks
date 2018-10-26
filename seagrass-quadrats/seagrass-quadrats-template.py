import MarinegeoTemplateBuilder

metadataValues = {"TemplateVersion": "v0.0.1",
                  "ProtocolVersion": "v0.0.1",
                  "Title": "Seagrass Quadrats - [your site name] - [date in YYYY-MM-DD format]"}


MarinegeoTemplateBuilder.main('MarineGEO_Seagrass-Quadrat_DataEntryTemplate_v0.0.1.xlsx',
           'attributes_v0.0.1.csv',
           'vocab_v0.0.1.csv',
           "MarineGEO Seagrass Quadrat Template",
           'DEFAULT', protect=True, metadataValues=metadataValues)
