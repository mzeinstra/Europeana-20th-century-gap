# Europeana-20th-century-gap
Code to research the 20th century content gap

## General
The Europeana dataset contains roughly 45 million objects. Of these objects about 20 million objects have dc:date fields. Dublin Core date or dc:date are used to store ‘Use for a significant date in the life of the [object].’ The use of this field is open for interpretation, it can be used to communicate the date that the physical objects was created, acquired, digitised, published, etc. Overall dc:date remains the best metadata field to indicate the existence of the 20th century gap. We do expect false positives but generally the older the year get the less false positives we will receive. We expect that dc:date is used for digitisation efforts and that this use of dc:date increases with years larger than 1990. We also expect that publication year and creation year is used, for our research this can give false positives as well.

We request the number of search results per year in dc:date between 1700 up until 2016. This means that we ask per year how many search results europeana has with the exact phrase of that year.

## Patterns
dc:date is a open text field. This means that it can be filled with all kinds of information. From only a year, to a date, to a whole sentence. We use a series of 13 patterns that help filter out only those objects that fit a certain year (YYYY):
*	The exact phrase YYYY
*	Phrases that starts with YYYY- to matchYYYY-DD-MM and YYYY-MM-DD, 
*	Phrases that ends with -YYYY to match DD-MM-YYYY and MM-DD-YYYY, 
*	The exact phrase "YYYY"
*	Phrases that starts with “YYYY-
*	Phrases that ends with -YYYY”
*	The exact phrase (YYYY)
*	Phrases that starts with (YYYY-
*	Phrases that ends with -YYYY)
*	The exact phrase  [YYYY]
*	Phrases that starts with [YYYY-
*	Phrases that ends with -YYYY]
*	The exact phrase YYYY.
More patterns can be used to add more data to our dataset, it is assumed that these patterns provide a representative overview of dates.

## Types of work
Europeana’s dataset is categorised in images, texts, video, 3D objects, and sounds. Of these we are only interested in images and texts, as these other types of work can only be found in the 20th century and can therefore skew our dataset.

## Queries
We make 12.285 request from the Europeana dataset:
*	Per year (1700-2015)
*	*	per type of work (all types, images, texts)
*	*	*	per pattern (13x)

## Code
The code in this repository is used to get the dataset described above. The code is written in Python 2.7.10 and outputs a CSV per data type. Please add your own API key.
