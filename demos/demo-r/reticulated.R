# install dev version of reticulate
devtools::install_github("rstudio/reticulate") 
library(reticulate)

# create a new conda environment (could also use virtualenv)
conda_create("reticulatedtest", packages = "python", conda = "auto")

# install MarinegeoTemplateBuilder from pypi 
conda_install("reticulatedtest", "MarinegeoTemplateBuilder", pip=TRUE)
conda_install("reticulatedtest", "numpy", pip=TRUE) # required?

# activate virtual environment
#use_condaenv("reticulatedtest", required = TRUE) # Not activating using reticulate. Check using system("which python"). 
use_python("/Users/ambell/anaconda3/envs/reticulatedtest/bin/python", required=TRUE)

# import the marinegeo template builder package
mtb <- import("MarinegeoTemplateBuilder")

# build the excel workbook. Use paths relative to the current working directory. 
mtb$main("Reticulated-Workbook.xlsx", "fields.csv", "vocab.csv", "RETICULATE DEMO", 
         'DEFAULT', metadataValues = list("TemplateVersion"="test",  "Title"="This was made from reticulate"))

# TODO allow for user to supply a dataframe via reticulate or numpy
