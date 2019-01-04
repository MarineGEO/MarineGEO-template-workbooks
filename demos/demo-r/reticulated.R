# install dev version of reticulate
devtools::install_github("rstudio/reticulate") 
library(reticulate)
library(tidyverse)

# create a new conda environment (could also use virtualenv)
conda_create("reticulatedtest", packages = "python", conda = "auto")

# install MarinegeoTemplateBuilder from pypi 
conda_install("reticulatedtest", "MarinegeoTemplateBuilder", pip=TRUE)

# activate virtual environment
#use_condaenv("reticulatedtest", required = TRUE) # Not activating using reticulate. Check using system("which python"). 
use_python("/Users/ambell/anaconda3/envs/reticulatedtest/bin/python", required=TRUE)

# import the marinegeo template builder package
mtb <- import("MarinegeoTemplateBuilder")

# build the excel workbook. Use paths relative to the current working directory. 
mtb$main("Demo-Reticulated-Workbook.xlsx", 'fields.csv', 'vocab.csv',
         'DEFAULT', metadataValues = list("TemplateVersion"="test",  "Title"="This was made from reticulate"))

# TODO - loading the csv files as DF in R corrupts the workbook