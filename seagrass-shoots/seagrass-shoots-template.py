import MarinegeoTemplateBuilder

metadataValues = {"TemplateVersion": "v0.0.1",
                  "ProtocolVersion": "v0.0.1",
                  "Title": "Seagrass Shoots - [your site name] - [date in YYYY-MM-DD format]"}


MarinegeoTemplateBuilder.main('MarineGEO_Seagrass-Shoots_DataEntryTemplate_v0.0.1.xlsx',
           'fields_v0.0.1.csv',
           'vocab_v0.0.1.csv',
           "MarineGEO Shoots Quadrat Template",
           'DEFAULT', protect=True, metadataValues=metadataValues)
