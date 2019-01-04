import MarinegeoTemplateBuilder

metadataValues = {"TemplateVersion": "v0.1.0",
                  "Title": "Seagrass Epifauna - [your site name] - [date in YYYY-MM-DD format]"}


MarinegeoTemplateBuilder.main('MarineGEO_Seagrass-Epifauna-Sieve-Tower_DataEntryTemplate_v0.1.0.xlsx',
           'fields_v0.0.1.csv',
           'vocab_v0.0.1.csv',
           'DEFAULT', metadataValues=metadataValues)