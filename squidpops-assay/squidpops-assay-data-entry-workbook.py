import MarinegeoTemplateBuilder
from MarinegeoTemplateBuilder.classes import Field, Vocab

metadataValues = {"TemplateVersion": "v0.1.0", "Title": "Squidpop Assay - [your site name] - [date in YYYY-MM-DD format]"}


fields = [
    Field(sheet='Location', fieldName='site', fieldDefinition='MarineGEO site abbreviation', fieldType='list'),
    Field(sheet='Location', fieldName='locationID', fieldDefinition='Unique code for each deployment location', fieldType='string'),
    Field(sheet='Location', fieldName='locality', fieldDefinition='Local or common name of the sampling location', fieldType='string'),
    Field(sheet='Location', fieldName='decimalLatitude', fieldDefinition='Decimal Latitude hh.hhhhhhh, approximate', fieldType='decimal', unit='degree', minValue='-90', maxValue='90'),
    Field(sheet='Location', fieldName='decimalLongitude', fieldDefinition='Decimal Longitude hh.hhhhhhh, approximate', fieldType='decimal', unit='degree', minValue='-180', maxValue='180'),
    Field(sheet='Location', fieldName='habitat', fieldDefinition='habitat type of deployment location', fieldType='list'),
    Field(sheet='Data', fieldName='locationID', fieldDefinition='Foreign key to locationID', fieldType='fkey', lookup='Location$locationID'),
    Field(sheet='Data', fieldName='dateDeployed', fieldDefinition='Date baits were deployed', fieldType='date', formatString='YYYY-MM-DD'),
    Field(sheet='Data', fieldName='timeDeployed', fieldDefinition='Time baits were deployed', fieldType='date', formatString='HH:MM'),
    Field(sheet='Data', fieldName='numberDeployed', fieldDefinition='Number of baits deployed at each location', fieldType='integer', unit='dimensionless', minValue='0'),
    Field(sheet='Data', fieldName='baitType', fieldDefinition='Type of bait used (squid, etc.)', fieldType='list'),
    Field(sheet='Data', fieldName='stakesRemaining1hr', fieldDefinition='Number of units located (stakes remaining) at 1 hr', fieldType='integer', unit='dimensionless', minValue='0'),
    Field(sheet='Data', fieldName='baitMissing1hr', fieldDefinition='Number of baits missing (removed) after 1 hour', fieldType='integer', unit='dimensionless', minValue='0'),
    Field(sheet='Data', fieldName='dateCollected', fieldDefinition='Date stakes were collected ', fieldType='date', formatString='YYYY-MM-DD'),
    Field(sheet='Data', fieldName='timeCollected', fieldDefinition='Time stakes were collected ', fieldType='date', formatString='HH:MM'),
    Field(sheet='Data', fieldName='stakesRemaining24hr', fieldDefinition='Number of units located (stakes recovered) at end of experiment (24 hrs)', fieldType='integer', unit='dimensionless', minValue='0'),
    Field(sheet='Data', fieldName='baitMissing24hr', fieldDefinition='Cumulative number of baits missing (removed) after 24 hours', fieldType='integer', unit='dimensionless', minValue='0'),
    Field(sheet='Data', fieldName='dataCollector', fieldDefinition='Name (First Last) of the individual who deployed and collected the experiment', fieldType='string'),
    Field(sheet='Data', fieldName='weather', fieldDefinition='General notes about the weather on deployment/retrieval', fieldType='string'),
    Field(sheet='Data', fieldName='depth', fieldDefinition='Depth of deployment in meters', fieldType='decimal', unit='meter', minValue='0'),
    Field(sheet='Data', fieldName='notes', fieldDefinition='Additional notes about the location, dive conditions, photos', fieldType='string'),
    Field(sheet='Data', fieldName='media', fieldDefinition='File names of the recordings if video was collected', fieldType='string'),
]

vocab = [
    Vocab(fieldName='baitType', code='Squid'),
    Vocab(fieldName='habitat', code='Mangrove', definition='Tidally influenced, dense, tropical or subtropical forest with a shore zone dominated by true mangroves'),
    Vocab(fieldName='habitat', code='Reef', definition='Areas dominated by reef-building fauna, including living corals, mollusks, polychaetes or glass sponges.'),
    Vocab(fieldName='habitat', code='Sand', definition='Sandy bottoms without vegetation beds or reefs'),
    Vocab(fieldName='habitat', code='Seagrass', definition='Tidal aquatic vegetation beds dominated by any number of seagrass or eelgrass species'),
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

MarinegeoTemplateBuilder.main('MarineGEO_Squidpops-Assay_Data-Entry-Template.xlsx', fields, vocab,
           'DEFAULT', metadataValues=metadataValues)
