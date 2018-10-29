import MarinegeoTemplateBuilder
from MarinegeoTemplateBuilder.classes import Vocab, Field

# create the attributes to add to the workbook
fields = [
    Field(sheet="Location",fieldName="site",fieldDefinition="MarineGEO site abbreviation",fieldType="list"),
    Field(sheet="Location",fieldName="locationID",fieldDefinition="Unique code for each sampling location",fieldType="string"),
    Field(sheet="Location",fieldName="locality",fieldDefinition="Local or common name of the sampling location",fieldType="string"),
    Field(sheet="Cover",fieldName="locationID",fieldDefinition="Foreign key to the locationID defined on the Location sheet",fieldType="fkey",lookup="Location$locationID"),
    Field(sheet="Cover",fieldName="transectNumber",fieldDefinition="Transect Number",fieldType="integer",unit="dimensionless",minValue=1,maxValue=3),
    Field(sheet="Cover",fieldName="stopNumber",fieldDefinition="Stop number along transect",fieldType="integer",unit="dimensionless",minValue=1,maxValue=5),
    Field(sheet="Cover",fieldName="percentCover", fieldDefinition="Percent Cover", fieldType="list")

]

# define the controlled vocabulary
vocab = [
    Vocab(fieldName="percentCover", code="<5%", definition="Less than 5%"),
    Vocab(fieldName="percentCover", code="10%", definition="Between 5-10%"),
    Vocab(fieldName="percentCover", code="15%", definition="Between 10-15%"),
    Vocab(fieldName="site", code="USA-MDA", definition="SERC"),
    Vocab(fieldName="site", code="BEL-CBC", definition="Carrie Bow Cay"),
    Vocab(fieldName="site", code="USA-SFB", definition="San Fransisco")
]

# build the data entry template workbook
MarinegeoTemplateBuilder.main('Demo-Template.xlsx', fields, vocab, "MarineGEO DEMO template", 'DEFAULT')
