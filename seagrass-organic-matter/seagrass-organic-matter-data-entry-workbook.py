import MarinegeoTemplateBuilder
from MarinegeoTemplateBuilder.classes import Field, Vocab

templateVersion = "v0.1.0"

metadataValues = {"TemplateVersion": templateVersion,
                  "Title": "Seagrass Organic Matter - [your site name] - [date in YYYY-MM-DD format]"}


# columns to add to the workbook as a list of Field()'s
fields = [
    # sites worksheet
    Field(sheet="Location", fieldName="site", fieldDefinition="MarineGEO Network Site Code", fieldType="list"),
    Field(sheet="Location", fieldName="locationID", fieldDefinition="RLS Survey Site Code", fieldType="string"),
    Field(sheet="Location", fieldName="locality", fieldDefinition="RLS Survey Site Name", fieldType="string"),
    Field(sheet="Location", fieldName="latitude", fieldDefinition="site latitude in decimal degrees", fieldType="decimal", unit="degree", minValue=-90,maxValue=90),
    Field(sheet="Location", fieldName="longitude", fieldDefinition="site longitude in decimal degrees", fieldType="decimal", unit="degree", minValue=-180,maxValue=180),
    Field(sheet="Location", fieldName="date", fieldDefinition="sample collection date", fieldType="date", formatString="YYYY-MM-DD"),
    Field(sheet="Location", fieldName="depth", fieldDefinition="depth at site in meters", fieldType="decimal", unit="meter", minValue=0),
    Field(sheet='Location', fieldName='locationRemarks', fieldDefinition='Comments or notes about the location', fieldType='string'),

    # Data
    Field(sheet="Data", fieldName="locationID", fieldDefinition="Foreign key to the sample location", fieldType="fkey", lookup="Location$locationID"),
    Field(sheet="Data", fieldName="sampleID", fieldDefinition="Unique Sample ID", fieldType="string"),
    Field(sheet="Data", fieldName="emptyTinMass", fieldDefinition="Empty tin mass in grams", fieldType="decimal", minValue=0, unit="gram"),
    Field(sheet="Data", fieldName="wetTinMass", fieldDefinition="Tin plus wet sediment mass in grams", fieldType="decimal", minValue=0, unit="gram"),
    Field(sheet="Data", fieldName="dryTinMass", fieldDefinition="Tin plus dry sediment mass in grams", fieldType="decimal", minValue=0, unit="gram"),
    Field(sheet="Data", fieldName="combustTinMass", fieldDefinition="Tin plus combusted sediment mass in grams", fieldType="decimal", minValue=0, unit="gram"),
    Field(sheet="Data", fieldName="wetSedimentMass",
          fieldDefinition="wet sediment mass in grams (wetTinMass minus emptyTinMass", fieldType="equation",
          lookup="=wetTinMass-emptyTinMass", minValue=0, unit="gram"),
    Field(sheet="Data", fieldName="drySedimentMass",
          fieldDefinition="dry sediment mass in grams (dryTinMass minus emptyTinMass", fieldType="equation",
          lookup="=dryTinMass-emptyTinMass", minValue=0, unit="gram"),
    Field(sheet="Data", fieldName="combustSedimentMass", fieldDefinition="combusted sediment mass in grams (combustTinMass - emptyTinMass", fieldType="equation", lookup="=combustTinMass-emptyTinMass", minValue=0, unit="gram"),
]

vocab = [
    # Sites
    Vocab(fieldName='site', code='BT', definition='Bocas del Toro, Panama'),
    Vocab(fieldName='site', code='CB', definition='Carrie Bow Cay, Belize'),
    Vocab(fieldName='site', code='EW', definition='Smithsonian Environmental Research Center at Edgewater, Maryland'),
    Vocab(fieldName='site', code='FHL', definition='Friday Harbor, Washington'),
    Vocab(fieldName='site', code='FP', definition='Smithsonian Marine station at Fort Pierce, Florida'),
    Vocab(fieldName='site', code='HAK', definition='Hakai Institute, British Columbia, Canada'),
    Vocab(fieldName='site', code='HKG', definition='Hong Kong'),
    Vocab(fieldName='site', code='KB', definition='Kaneohe Bay, Hawaii'),
    Vocab(fieldName='site', code='MAD', definition='Madeira'),
    Vocab(fieldName='site', code='SFB', definition='San Francisco Bay, California'),
    Vocab(fieldName='site', code='TAS', definition='Tasmania'),
    Vocab(fieldName='site', code='TGC', definition='Gulf Coast, Texas'),
]


MarinegeoTemplateBuilder.main('MarineGEO_Seagrass-Organic-Matter_Data-Entry-Template.xlsx',
           fields, vocab, 'DEFAULT', metadataValues=metadataValues)
