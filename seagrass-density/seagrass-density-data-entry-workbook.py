import MarinegeoTemplateBuilder
from MarinegeoTemplateBuilder.classes import Field, Vocab

metadataValues = {"TemplateVersion": "v0.1.0",
                  "Title": "Seagrass Density - [your site name] - [date in YYYY-MM-DD format]"}

fields = [
    Field(sheet='Location', fieldName='site', fieldDefinition='MarineGEO site abbreviation', fieldType='list', warnLevel='warning'),
    Field(sheet='Location', fieldName='locationID', fieldDefinition='Unique code for each sampling location', fieldType='string', warnLevel='warning'),
    Field(sheet='Location', fieldName='locality', fieldDefinition='Local or common name of the sampling location', fieldType='string', warnLevel='warning'),
    Field(sheet='Location', fieldName='date', fieldDefinition='Sampling date', fieldType='date', formatString='YYYY-MM-DD', warnLevel='warning'),
    Field(sheet='Location', fieldName='decimalLatitude', fieldDefinition='Decimal latitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-90', maxValue='90', warnLevel='warning'),
    Field(sheet='Location', fieldName='decimalLongitude', fieldDefinition='Decimal longitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-180', maxValue='180', warnLevel='warning'),
    Field(sheet='Location', fieldName='locationRemarks', fieldDefinition='Comments or notes about the location', fieldType='string', warnLevel='warning'),
    Field(sheet='Cover', fieldName='locationID', fieldDefinition='Foreign key to the locationID defined on the Location sheet', fieldType='fkey', lookup='Location$locationID', warnLevel='warning'),
    Field(sheet='Cover', fieldName='transectNumber', fieldDefinition='Transect Number', fieldType='integer', unit='dimensionless', minValue='1', maxValue='3', warnLevel='warning'),
    Field(sheet='Cover', fieldName='quadrat', fieldDefinition='Stop number along transect', fieldType='integer', unit='dimensionless', minValue='1', maxValue='12', warnLevel='warning'),
    Field(sheet='Cover', fieldName='coverType', fieldDefinition='Type of cover', fieldType='list', warnLevel='warning'),
    Field(sheet='Cover', fieldName='ScientificName', fieldDefinition='Lowest known taxon name', fieldType='string', warnLevel='warning'),
    Field(sheet='Cover', fieldName='percentCover', fieldDefinition=' Percent cover of category', fieldType='list', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='locationID', fieldDefinition='Foreign key to the locationID defined on the Location sheet', fieldType='fkey', lookup='Location$locationID', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='transectNumber', fieldDefinition='Transect Number', fieldType='integer', unit='dimensionless', minValue='1', maxValue='3', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='quadrat', fieldDefinition='Stop number along transect', fieldType='integer', unit='dimensionless', minValue='1', maxValue='12', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='totalShoots', fieldDefinition='Total number of shoots in the 0.25x0.25m subquadrat', fieldType='integer', unit='dimensionless', minValue='0', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='grazingScars', fieldDefinition='Presence of any grazing scars within or immediately adjacent to the quadrat', fieldType='list', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='media', fieldDefinition='File names of quadrat photos.', fieldType='string', warnLevel='warning'),
    Field(sheet='Invertebrates', fieldName='locationID', fieldDefinition='Foreign key to the locationID defined on the Location sheet', fieldType='fkey', lookup='Location$locationID', warnLevel='warning'),
    Field(sheet='Invertebrates', fieldName='transectNumber', fieldDefinition='Transect Number', fieldType='integer', unit='dimensionless', minValue='1', maxValue='3', warnLevel='warning'),
    Field(sheet='Invertebrates', fieldName='quadrat', fieldDefinition='Stop number along transect', fieldType='integer', unit='dimensionless', minValue='1', maxValue='12', warnLevel='warning'),
    Field(sheet='Invertebrates', fieldName='vernacularName', fieldDefinition='A common or vernacular name', fieldType='string', warnLevel='warning'),
    Field(sheet='Invertebrates', fieldName='taxonRank', fieldDefinition='The taxonomic rank of the most specific name in the scientificName.', fieldType='list', warnLevel='warning'),
    Field(sheet='Invertebrates', fieldName='scientificName', fieldDefinition='Lowest known taxon name', fieldType='string', warnLevel='warning'),
    Field(sheet='Invertebrates', fieldName='speciesIdentifiedBy', fieldDefinition='Full name (first last) of person who identified the taxon.', fieldType='string', warnLevel='warning'),
    Field(sheet='Invertebrates', fieldName='bodyLength', fieldDefinition='Approximate size of the mobile benthic invertebrate in centimeters', fieldType='decimal', unit='centimeter', minValue='0', warnLevel='warning'),
]

vocab = [
    Vocab(fieldName='taxonRank', code='Class'),
    Vocab(fieldName='taxonRank', code='Order'),
    Vocab(fieldName='taxonRank', code='Family'),
    Vocab(fieldName='taxonRank', code='Genus'),
    Vocab(fieldName='taxonRank', code='Species'),
    Vocab(fieldName='taxonRank', code='Subgenus'),
    Vocab(fieldName='taxonRank', code='Subspecies'),
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
    Vocab(fieldName='percentCover', code='5', definition='Less than 5%'),
    Vocab(fieldName='percentCover', code='10', definition='Between 5-10%'),
    Vocab(fieldName='percentCover', code='15', definition='Between 10-15%'),
    Vocab(fieldName='percentCover', code='20', definition='Between 15-20%'),
    Vocab(fieldName='percentCover', code='25', definition='Between 20-25%'),
    Vocab(fieldName='percentCover', code='30', definition='Between 25-30%'),
    Vocab(fieldName='percentCover', code='35', definition='Between 30-35%'),
    Vocab(fieldName='percentCover', code='40', definition='Between 35-40%'),
    Vocab(fieldName='percentCover', code='45', definition='Between 40-45%'),
    Vocab(fieldName='percentCover', code='50', definition='Between 45-50%'),
    Vocab(fieldName='percentCover', code='55', definition='Between 50-55%'),
    Vocab(fieldName='percentCover', code='60', definition='Between 55-60%'),
    Vocab(fieldName='percentCover', code='65', definition='Between 60-65%'),
    Vocab(fieldName='percentCover', code='70', definition='Between 65-70%'),
    Vocab(fieldName='percentCover', code='75', definition='Between 70-75%'),
    Vocab(fieldName='percentCover', code='80', definition='Between 75-80%'),
    Vocab(fieldName='percentCover', code='85', definition='Between 80-85%'),
    Vocab(fieldName='percentCover', code='90', definition='Between 85-90%'),
    Vocab(fieldName='percentCover', code='95', definition='Between 90-95%'),
    Vocab(fieldName='percentCover', code='100', definition='100% cover'),
    Vocab(fieldName='coverType', code='Seagrass', definition='Seagrass - note species in ScientificName field'),
    Vocab(fieldName='coverType', code='Sand', definition='Sandy bottoms'),
    Vocab(fieldName='coverType', code='Mud', definition='Muddy bottoms'),
    Vocab(fieldName='coverType', code='Mixed', definition='Mixed bottoms'),
    Vocab(fieldName='grazingScars', code='Present', definition='Grazing scars present within or immediately adjacent to the quadrat'),
    Vocab(fieldName='grazingScars', code='Absent', definition='No grazing scars present within or immediately adjacent to the quadrat'),
]

MarinegeoTemplateBuilder.main('MarineGEO_Seagrass-Density_Data-Entry-Template.xlsx', fields, vocab,
           'DEFAULT', metadataValues=metadataValues)
