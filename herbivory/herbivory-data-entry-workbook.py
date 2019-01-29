import MarinegeoTemplateBuilder
from MarinegeoTemplateBuilder.classes import Field, Vocab

metadataValues = {"Version": "v0.0.1"
                  }

# list of fields to construct
fields = [
    Field(sheet='SiteAndDeploymentInformation', fieldName='site', fieldDefinition='MarineGEO site abbreviation; e.g USA-MDA', fieldType='list', warnLevel='warning'),
    Field(sheet='SiteAndDeploymentInformation', fieldName='locationName', fieldDefinition='Unique code for each sampling location; e.g. CBC30', fieldType='string', warnLevel='warning'),
    Field(sheet='SiteAndDeploymentInformation', fieldName='locality', fieldDefinition='Local or common name of the sampling location; e.g. Tobacco Reef', fieldType='string', warnLevel='warning'),
    Field(sheet='SiteAndDeploymentInformation', fieldName='decimalLatitude', fieldDefinition='Decimal latitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-90', maxValue='90', warnLevel='warning'),
    Field(sheet='SiteAndDeploymentInformation', fieldName='decimalLongitude', fieldDefinition='Decimal longitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-180', maxValue='180', warnLevel='warning'),
    Field(sheet='SiteAndDeploymentInformation', fieldName='depth', fieldDefinition='Average site depth in meters', fieldType='decimal', unit='meters', minValue='0', maxValue='30', warnLevel='warning'),
    Field(sheet='SiteAndDeploymentInformation', fieldName='numberDeployed', fieldDefinition='Number of weedpops deployed', fieldType='integer', warnLevel='warning'),
    Field(sheet="PlantTaxa", fieldName="TaxaNames", fieldDefinition="Species Names of Plant Taxa (including Wakame Standard) used in assay", fieldType="string", warnLevel='warning'),
    Field(sheet="oneHourCheck", fieldName="Taxa", fieldDefinition="PlantTaxa ", fieldType="fkey", lookup="PlantTaxa$TaxaNames", warnLevel='warning'),
    Field(sheet='oneHourCheck', fieldName='DeployDate', fieldDefinition='Deployment Date', fieldType='date', formatString='YYYY-MM-DD', warnLevel='warning'),
    Field(sheet='oneHourCheck', fieldName='CheckData', fieldDefinition='Check Date', fieldType='date', formatString='YYYY-MM-DD', warnLevel='warning'),
    Field(sheet='oneHourCheck', fieldName='DeployTime', fieldDefinition='Deployment Time', fieldType='time', formatString='HH:MM', warnLevel='warning'),
    Field(sheet='oneHourCheck', fieldName='CheckTime', fieldDefinition='Check Time', fieldType='time', formatString='HH:MM', warnLevel='warning'),
    Field(sheet='oneHourCheck', fieldName='numberBaitPresent', fieldDefinition='The number of bait present or partially consumed', fieldType='integer', minValue='0', maxValue='25', warnLevel='warning'),
    Field(sheet='oneHourCheck', fieldName='numberBaitAbsent', fieldDefinition='The number of bait absent', fieldType='integer', minValue='0', maxValue='25', warnLevel='warning'),
    Field(sheet='oneHourCheck', fieldName='numberStakesMissing', fieldDefinition='The number of stakes missing', fieldType='integer', minValue='0', maxValue='25', warnLevel='warning'),
    Field(sheet="twentyFourHourCheck", fieldName="Taxa", fieldDefinition="PlantTaxa ", fieldType="fkey", lookup="PlantTaxa$TaxaNames", warnLevel='warning'),
    Field(sheet='twentyFourHourCheck', fieldName='DeployDate', fieldDefinition='Deployment Date', fieldType='date', formatString='YYYY-MM-DD', warnLevel='warning'),
    Field(sheet='twentyFourHourCheck', fieldName='CheckData', fieldDefinition='Check Date', fieldType='date', formatString='YYYY-MM-DD', warnLevel='warning'),
    Field(sheet='twentyFourHourCheck', fieldName='DeployTime', fieldDefinition='Deployment Time', fieldType='time', formatString='HH:MM', warnLevel='warning'),
    Field(sheet='twentyFourHourCheck', fieldName='CheckTime', fieldDefinition='Check Time', fieldType='time', formatString='HH:MM', warnLevel='warning'),
    Field(sheet='twentyFourHourCheck', fieldName='numberBaitPresent', fieldDefinition='The number of bait present or partially consumed', fieldType='integer', minValue='0', maxValue='25', warnLevel='warning'),
    Field(sheet='twentyFourHourCheck', fieldName='numberBaitAbsent', fieldDefinition='The number of bait absent', fieldType='integer', minValue='0', maxValue='25', warnLevel='warning'),
    Field(sheet='twentyFourHourCheck', fieldName='numberStakesMissing', fieldDefinition='The number of stakes missing', fieldType='integer', minValue='0', maxValue='25', warnLevel='warning'),
    ]

# list of vocab terms
vocab = [
    # controlled vocabulary for site codes
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

# construct the workbook
MarinegeoTemplateBuilder.main(
    'Herbivory-Data-Entry-Template.xlsx',  # name of the output excel workbook
    fields,  # list of field objects to construct
    vocab,  # list of vocab object to use (optional - only needed for building list fieldTypes)
    'DEFAULT',  # use the MarineGEO logo for the default branding
    metadataValues=metadataValues  # seed the first sheet with the metatdata values defined above
)