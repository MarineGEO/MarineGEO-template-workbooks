import MarinegeoTemplateBuilder

metadataValues = {"TemplateVersion": "v0.0.3", "ProtocolVersion": "V20180802", "Title": "Squidpop data - [your site name] - [date in YYYY-MM-DD format]"}


MarinegeoTemplateBuilder.main('MarineGEO_Squidpops_DataEntry_Template_v0.0.3.xlsx', 'attributes.csv', 'vocab.csv', "MarineGEO Squidpop template",
           'DEFAULT', protect=True, metadataValues=metadataValues)
