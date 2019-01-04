import MarinegeoTemplateBuilder
from MarinegeoTemplateBuilder import Field, Vocab

metadataValues = {"TemplateVersion": "v0.1.0",
                  "Title": "Seagrass Shoots - [your site name] - [date in YYYY-MM-DD format]"}

fields = [
    Field(sheet='Location', fieldName='site', fieldDefinition='MarineGEO site abbreviation', fieldType='list', warnLevel='warning'),
    Field(sheet='Location', fieldName='locationID', fieldDefinition='Unique code for each sampling location', fieldType='string', warnLevel='warning'),
    Field(sheet='Location', fieldName='locality', fieldDefinition='Local or common name of the sampling location', fieldType='string', warnLevel='warning'),
    Field(sheet='Location', fieldName='decimalLatitude', fieldDefinition='Decimal latitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-90', maxValue='90', warnLevel='warning'),
    Field(sheet='Location', fieldName='decimalLongitude', fieldDefinition='Decimal longitude hh.hhhhhhh', fieldType='decimal', unit='degree', minValue='-180', maxValue='180', warnLevel='warning'),
    Field(sheet='Location', fieldName='locationRemarks', fieldDefinition='Comments or notes about the location', fieldType='string', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='locationID', fieldDefinition='Foreign key to the locationID defined on the Location sheet', fieldType='fkey', lookup='Location$locationID', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='sampleID', fieldDefinition='Seagrass Sample Identifier', fieldType='string', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='collectionDate', fieldDefinition='Date seagrass was collected', fieldType='date', formatString='YYYY-MM-DD', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='processingDate', fieldDefinition='Date seagrass sample was processed in the lab', fieldType='date', formatString='YYYY-MM-DD', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='epibiontTinWeight', fieldDefinition='Epibiont tin weight in mg', fieldType='decimal', unit='milligrams', minValue='0', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='epiDryMassWithTin', fieldDefinition='Epibiont drymass with tin in mg', fieldType='decimal', unit='milligrams', minValue='0', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='bladeTinWeight', fieldDefinition='blade tin weight in mg', fieldType='decimal', unit='milligrams', minValue='0', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='bladeDrymass', fieldDefinition='blade drymass with tin in mg', fieldType='decimal', unit='milligrams', minValue='0', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='longestLeafLength', fieldDefinition='longest leaf length in mm', fieldType='decimal', unit='milimeters', minValue='0', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='longestLeafWidth', fieldDefinition='longest leaf width in mm', fieldType='decimal', unit='milimeters', minValue='0', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='sheathLength', fieldDefinition='Sheath length in mm', fieldType='decimal', unit='milimeters', minValue='0', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='disease', fieldDefinition='Is there disease visible on the shoot?', fieldType='list', warnLevel='warning'),
    Field(sheet='Shoots', fieldName='longestLesionLength', fieldDefinition='Length of the longest lesion in mm', fieldType='decimal', unit='milimeters', minValue='0', warnLevel='warning'),
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
    Vocab(fieldName='disease', code='Yes', definition='Disease visible on seagrass sample'),
    Vocab(fieldName='disease', code='No', definition='No disease visible on seagrass sample'),
]

MarinegeoTemplateBuilder.main('MarineGEO_Seagrass-Shoots_Data-Entry-Template.xlsx', fields, vocab,
                              'DEFAULT', metadataValues=metadataValues)
