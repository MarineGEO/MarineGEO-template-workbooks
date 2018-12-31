import MarinegeoTemplateBuilder
from MarinegeoTemplateBuilder.classes import Field, Vocab

templateVersion = "v0.1.0"

metadataValues = {"TemplateVersion": templateVersion,
                  "Title": "Seagrass Sediment Organic Matter - [your site name] - [date in YYYY-MM-DD format]"}


# columns to add to the workbook as a list of Field()'s
fields = [
    # sites worksheet
    Field(sheet="Location", fieldName="site", fieldDefinition="MarineGEO Network Site Code", fieldType="list"),
    Field(sheet="Location", fieldName="locationID", fieldDefinition="RLS Survey Site Code", fieldType="string"),
    Field(sheet="Location", fieldName="locality", fieldDefinition="RLS Survey Site Name", fieldType="string"),
    Field(sheet="Location", fieldName="latitude", fieldDefinition="site latitude in decimal degrees", fieldType="decimal", unit="degree", minValue=-90,maxValue=90),
    Field(sheet="Location", fieldName="longitude", fieldDefinition="site longitude in decimal degrees", fieldType="decimal", unit="degree", minValue=-180,maxValue=180),


    # Data
    Field(sheet="Data", fieldName="locationID", fieldDefinition="Foreign key to the sample location", fieldType="fkey", lookup="Location$locationID"),
    Field(sheet="Data", fieldName="sampleID", fieldDefinition="Unique Sample ID", fieldType="string"),
    Field(sheet="Data", fieldName="replicate", fieldDefinition="Sample replicate number", fieldType="integer"),
]


vocab = [
    # Sites
    Vocab(fieldName="site", code="AUS-TAS", definition="Tasmania"),
    Vocab(fieldName="site", code="BEL-CBC", definition="Carrie Bow Cay, Belize"),
    Vocab(fieldName="site", code="CAN-BCC", definition="Hakai Institute, British Columbia, Canada"),
    Vocab(fieldName="site", code="HKG-HKG", definition="Hong Kong"),
    Vocab(fieldName="site", code="PAN-BDT", definition="Bocas del Toro, Panama"),
    Vocab(fieldName="site", code="POR-MAD", definition="Madeira"),
    Vocab(fieldName="site", code="USA-IRL", definition="Smithsonian Marine station at Fort Pierce, Florida"),
    Vocab(fieldName="site", code="USA-HIK", definition="Kane'ohe Bay, Hawai'i"),
    Vocab(fieldName="site", code="USA-MDA", definition="Smithsonian Environmental Research Center at Edgewater, Maryland"),
    Vocab(fieldName="site", code="USA-SFB", definition="San Francisco Bay, California"),
    Vocab(fieldName="site", code="USA-TXS", definition="Gulf Coast, Texas"),
    Vocab(fieldName="site", code="USA-WAS", definition="Friday Harbor, Washington"),
]


MarinegeoTemplateBuilder.main('MarineGEO_Seagrass-Shoots_DataEntryTemplate_' + templateVersion + '.xlsx',
           fields, vocab, 'DEFAULT', metadataValues=metadataValues, seededValues="RANDOM")
