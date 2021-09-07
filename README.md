# End-to-End-Machine-Learning

## Project Motivation
The aim of the project is to build an end to end machine learning project. Create a Python package, collect dataset using data scraping technique, train model and deploy it

## To use the package:
```python
!pip install propertypro-scrapper

from propertypro.propertypro import Propertypro

scraper = Propertypro()

scraper.scrape_data(100, ["enugu"])
```

## To Use the app for prediction :
-  Go to https://price-house.herokuapp.com/ and make your prediction
- To use Postman for the prediction, enter the url https://price-house.herokuapp.com/results, Using the ```POST``` request, enter a sample input array below

```
{
    "bed": 2,
      "bath": 1,
      "toilet": 2,
      "new": 0,
      "furnished": 1,
      "serviced": 0,
      "location": 2
   
   }
   ```


## License
This project is licensed under the terms of the **MIT** [license](https://opensource.org/licenses/MIT).

## Acknowledgements
Turing College