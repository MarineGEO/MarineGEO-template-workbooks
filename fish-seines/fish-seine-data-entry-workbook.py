import MarinegeoTemplateBuilder
from MarinegeoTemplateBuilder.classes import Field, Vocab

metadataValues = {"TemplateVersion": "v0.1.0",
                  "Title": "Fish Seines [your site name] [date in YYYY-MM-DD format]"}

fields = [
    Field(sheet='Location', fieldName='site', fieldDefinition='MarineGEO site abbreviation', fieldType='list', warnLevel='warning'),
    Field(sheet='Location', fieldName='locationID', fieldDefinition='Unique code for each sampling location', fieldType='string', warnLevel='warning'),
    Field(sheet='Location', fieldName='locality', fieldDefinition='Local or common name of the sampling location', fieldType='string', warnLevel='warning'),
    Field(sheet='Location', fieldName='decimalLatitude', fieldDefinition='Decimal latitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-90', maxValue='90', warnLevel='warning'),
    Field(sheet='Location', fieldName='decimalLongitude', fieldDefinition='Decimal longitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-180', maxValue='180', warnLevel='warning'),
    Field(sheet='Location', fieldName='locationRemarks', fieldDefinition='Comments or notes about the location', fieldType='string', warnLevel='warning'),
    Field(sheet='Transect', fieldName='locationID', fieldDefinition='Foreign key to the locationID defined on the Location sheet', fieldType='fkey', lookup='Location$locationID', warnLevel='warning'),
    Field(sheet='Transect', fieldName='transectID', fieldDefinition='Unique identifier for the transect', fieldType='string', warnLevel='warning'),
    Field(sheet='Transect', fieldName='date', fieldDefinition='Sampling date', fieldType='date', formatString='YYYY-MM-DD', warnLevel='warning'),
    Field(sheet='Transect', fieldName='netHeight', fieldDefinition='Net height in meters', fieldType='decimal', unit='meters', minValue='0', warnLevel='warning'),
    Field(sheet='Transect', fieldName='netWidth', fieldDefinition='Net width in meters', fieldType='decimal', unit='meters', minValue='0', warnLevel='warning'),
    Field(sheet='Transect', fieldName='meshSize', fieldDefinition='Net mesh size in mm', fieldType='decimal', unit='milimeters', minValue='0', warnLevel='warning'),
    Field(sheet='Taxon', fieldName='taxonID', fieldDefinition='Unique Identifer for taxon', fieldType='string', warnLevel='warning'),
    Field(sheet='Taxon', fieldName='vernacularName', fieldDefinition='A common or vernacular name', fieldType='string', warnLevel='warning'),
    Field(sheet='Taxon', fieldName='taxonRank', fieldDefinition='The taxonomic rank of the most specific name in the scientificName.', fieldType='list', warnLevel='warning'),
    Field(sheet='Taxon', fieldName='scientificName', fieldDefinition='Lowest known taxon name', fieldType='string', warnLevel='warning'),
    Field(sheet='Taxon', fieldName='lifeStage', fieldDefinition='Taxa life stage', fieldType='string', warnLevel='warning'),
    Field(sheet='Abundance', fieldName='transectID', fieldDefinition='Foreign key to the transectID defined on the transect sheet', fieldType='fkey', lookup='Transect$transectID', warnLevel='warning'),
    Field(sheet='Abundance', fieldName='taxonID', fieldDefinition='Foreign key to the taxaID defined on the Taxon sheet', fieldType='fkey', lookup='Taxon$taxonID', warnLevel='warning'),
    Field(sheet='Abundance', fieldName='count', fieldDefinition='Number of individuals', fieldType='integer', unit='dimensionless', minValue='0', warnLevel='warning'),
    Field(sheet='Length', fieldName='transectID', fieldDefinition='Foreign key to the transectID defined on the transect sheet', fieldType='fkey', lookup='Transect$transectID', warnLevel='warning'),
    Field(sheet='Length', fieldName='taxonID', fieldDefinition='Foreign key to the taxaID defined on the Taxon sheet', fieldType='fkey', lookup='Taxon$taxonID', warnLevel='warning'),
    Field(sheet='Length', fieldName='length', fieldDefinition='Length of individual in mm', fieldType='decimal', unit='milimeters', minValue='0', warnLevel='warning'),
]

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

    # controlled vocabulary for taxonomic ranks
    Vocab(fieldName="taxonRank", code="Class"),
    Vocab(fieldName="taxonRank", code="Order"),
    Vocab(fieldName="taxonRank", code="Family"),
    Vocab(fieldName="taxonRank", code="Genus"),
    Vocab(fieldName="taxonRank", code="Species"),
    Vocab(fieldName="taxonRank", code="Subgenus"),
    Vocab(fieldName="taxonRank", code="Subspecies"),

]

MarinegeoTemplateBuilder.main('MarineGEO_Fish-Seines_Data-Entry-Template.xlsx',
                              fields, vocab, 'DEFAULT', metadataValues=metadataValues)
