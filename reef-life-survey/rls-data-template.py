import MarinegeoTemplateBuilder

metadataValues = {"TemplateVersion": "v0.0.1",
                  "Title": "Reef Life Survey data - [your site name] - [date in YYYY-MM-DD format]"}


MarinegeoTemplateBuilder.main('MarineGEO_RLS_DataEntry_Template_v0.0.1.xlsx', 'fields.csv', 'vocab.csv',
                              "Reef Life Survey", 'DEFAULT', protect=True, metadataValues=metadataValues)
