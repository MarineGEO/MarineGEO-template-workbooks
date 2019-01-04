import MarinegeoTemplateBuilder
from MarinegeoTemplateBuilder import Field, Vocab

metadataValues = {"TemplateVersion": "v0.1.0",
                  "Title": "Seagrass Biomass - [your site name] - [date in YYYY-MM-DD format]"}


fields = [
    Field(sheet='Location', fieldName='site', fieldDefinition='MarineGEO site abbreviation', fieldType='list', warnLevel='warning'),
    Field(sheet='Location', fieldName='locationID', fieldDefinition='Unique code for each sampling location', fieldType='string', warnLevel='warning'),
    Field(sheet='Location', fieldName='locality', fieldDefinition='Local or common name of the sampling location', fieldType='string', warnLevel='warning'),
    Field(sheet='Location', fieldName='decimalLatitude', fieldDefinition='Decimal latitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-90', maxValue='90', warnLevel='warning'),
    Field(sheet='Location', fieldName='decimalLongitude', fieldDefinition='Decimal longitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-180', maxValue='180', warnLevel='warning'),
    Field(sheet='Location', fieldName='locationRemarks', fieldDefinition='Comments or notes about the location', fieldType='string', warnLevel='warning'),
    Field(sheet='Taxon', fieldName='taxonID', fieldDefinition='Unique Identifer for taxon', fieldType='string', warnLevel='warning'),
    Field(sheet='Taxon', fieldName='vernacularName', fieldDefinition='A common or vernacular name', fieldType='string', warnLevel='warning'),
    Field(sheet='Taxon', fieldName='taxonRank', fieldDefinition='The taxonomic rank of the most specific name in the scientificName.', fieldType='list', warnLevel='warning'),
    Field(sheet='Taxon', fieldName='scientificName', fieldDefinition='Lowest known taxon name', fieldType='string', warnLevel='warning'),
    Field(sheet='MacrophyteMass', fieldName='locationID', fieldDefinition='Foreign key to the locationID defined on the Location sheet', fieldType='fkey', lookup='Location$locationID', warnLevel='warning'),
    Field(sheet='MacrophyteMass', fieldName='sampleID', fieldDefinition='Biomass Core Sample Identifier', fieldType='string', warnLevel='warning'),
    Field(sheet='MacrophyteMass', fieldName='macrophyteTaxaID', fieldDefinition='Foreign key to taxonID on the Taxon sheet', fieldType='fkey', lookup='Taxon$taxonID', warnLevel='warning'),
    Field(sheet='MacrophyteMass', fieldName='tinMass', fieldDefinition='Empty tin mass in grams', fieldType='decimal', unit='grams', minValue='0', warnLevel='warning'),
    Field(sheet='MacrophyteMass', fieldName='macrophyteWetMass', fieldDefinition='Macrophyte wet mass in grams', fieldType='decimal', unit='grams', minValue='0', warnLevel='warning'),
    Field(sheet='MacrophyteMass', fieldName='macrophyteDryMass', fieldDefinition='Macrophyte dry mass in grams', fieldType='decimal', unit='grams', minValue='0', warnLevel='warning'),
    Field(sheet='MacrophyteMass', fieldName='macrophyteMass', fieldDefinition='Macrophyte total mass in grams (wet minus dry minus tin)', fieldType='equation', lookup='=macrophyteWetMass-macrophyteDryMass-tinMass', unit='grams', minValue='0', warnLevel='warning'),
    Field(sheet='InfaunaCount', fieldName='locationID', fieldDefinition='Foreign key to the locationID defined on the Location sheet', fieldType='fkey', lookup='Location$locationID', warnLevel='warning'),
    Field(sheet='InfaunaCount', fieldName='sampleID', fieldDefinition='Biomass Core Sample Identifier', fieldType='string', warnLevel='warning'),
    Field(sheet='InfaunaCount', fieldName='infaunaTaxaID', fieldDefinition='Foreign key to taxonID on the Taxon sheet', fieldType='fkey', lookup='Taxon$taxonID', warnLevel='warning'),
    Field(sheet='InfaunaCount', fieldName='count', fieldDefinition='Number of individuals', fieldType='integer', unit='dimensionless', minValue='0', warnLevel='warning'),
]

vocab = [
    Vocab(fieldName='site', code='AUS-TAS', definition='Tasmania'),
    Vocab(fieldName='site', code='BEL-CBC', definition='Carrie Bow Cay, Belize'),
    Vocab(fieldName='site', code='CAN-BCC', definition='Hakai Institute, British Columbia, Canada'),
    Vocab(fieldName='site', code='HKG-HKG', definition='Hong Kong'),
    Vocab(fieldName='site', code='PAN-BDT', definition='Bocas del Toro, Panama'),
    Vocab(fieldName='site', code='POR-MAD', definition='Madeira'),
    Vocab(fieldName='site', code='USA-IRL', definition='Smithsonian Marine station at Fort Pierce, Florida'),
    Vocab(fieldName='site', code='USA-HIK', definition='Kaneohe Bay, Hawaii'),
    Vocab(fieldName='site', code='USA-MDA', definition='Smithsonian Environmental Research Center at Edgewater, Maryland'),
    Vocab(fieldName='site', code='USA-SFB', definition='San Francisco Bay, California'),
    Vocab(fieldName='site', code='USA-TXS', definition='Gulf Coast, Texas'),
    Vocab(fieldName='site', code='USA-WAS', definition='Friday Harbor, Washington'),
    Vocab(fieldName='taxonRank', code='Class'),
    Vocab(fieldName='taxonRank', code='Order'),
    Vocab(fieldName='taxonRank', code='Family'),
    Vocab(fieldName='taxonRank', code='Genus'),
    Vocab(fieldName='taxonRank', code='Species'),
    Vocab(fieldName='taxonRank', code='Subgenus'),
    Vocab(fieldName='taxonRank', code='Subspecies'),
]


MarinegeoTemplateBuilder.main('MarineGEO_Seagrass-Biomass_Data-Entry-Template.xlsx',
           fields,
           vocab,
           'DEFAULT', metadataValues=metadataValues)
