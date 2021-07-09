
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

## Setting the model multiple choices

## preferred areas choices
ILEBIZARD = 'L’Île-Bizard—Sainte-Geneviève'
PIERREFONDS = 'Pierrefonds-Roxboro'
SAINTLAURENT = 'Saint-Laurent'
AHUNTSIC = 'Ahuntsic-Cartierville'
MONTREAL = 'Montréal-Nord'
RIVPRAIRES = 'Rivière-des-Prairies—Pointe-aux-Trembles'
ANJOU = 'Anjou'
SAINTLEONARD = 'Saint-Léonard'
VILLERAY = 'Villeray—Saint-Michel—Parc-Extension'
ROSEMONT = 'Rosemont—La Petite-Patrie'
MERCIER = 'Mercier—Hochelaga-Maisonneuve'
PLATEAU = 'Le Plateau-Mont-Royal'
OUTREMONT = 'Outremont'
VILLEMARIE = 'Ville-Marie'
CDN = 'Côte-des-Neiges—Notre-Dame-de-Grâce'
SUDOUEST = 'Le Sud-Ouest'
VERDUN = 'Verdun'
LASALLE = 'LaSalle'

location_choices = (
    (ILEBIZARD, 'L’Île-Bizard—Sainte-Geneviève'),
    (PIERREFONDS, 'Pierrefonds-Roxboro'),
    (SAINTLAURENT, 'Saint-Laurent'),
    (AHUNTSIC, 'Ahuntsic-Cartierville'),
    (MONTREAL, 'Montréal-Nord'),
    (RIVPRAIRES, 'Rivière-des-Prairies—Pointe-aux-Trembles'),
    (ANJOU, 'Anjou'),
    (SAINTLEONARD, 'Saint-Léonard'),
    (VILLERAY, 'Villeray—Saint-Michel—Parc-Extension'),
    (ROSEMONT, 'Rosemont—La Petite-Patrie'),
    (MERCIER, 'Mercier—Hochelaga-Maisonneuve'),
    (PLATEAU, 'Le Plateau-Mont-Royal'),
    (OUTREMONT, 'Outremont'),
    (VILLEMARIE, 'Ville-Marie'),
    (CDN, 'Côte-des-Neiges—Notre-Dame-de-Grâce'),
    (SUDOUEST, 'Le Sud-Ouest'),
    (VERDUN, 'Verdun'),
    (LASALLE, 'LaSalle'),
    )

   
## Preferred service size
SMALL = 'small'
MEDIUM = 'medium'
LARGE = 'large'

service_size_choices = (
	(SMALL, 'Small'),
	(MEDIUM, 'Medium'),
	(LARGE, 'Large'),
	)

## Prefered organization size
SMALL = 'small'
MEDIUM = 'medium'
LARGE = 'large'

organization_size_choices = (
	(SMALL, 'Small'),
	(MEDIUM, 'Medium'),
	(LARGE, 'Large'),
	)

## Preferred roles
CLEAN = 'clean'
COOK = 'cook'
SERVE = 'serve'
PREP = 'prep'
GARDEN = 'garden'
DELIVERY = 'delivery'
EDUCATION = 'education'
WAREHOUSE = 'warehouse'
DAYCARE = 'daycare'
SORT = 'sort'

role_choices = (
	(CLEAN, 'Clean'),
	(COOK, 'Cook'),
	(SERVE, 'Serve'),
	(PREP, 'Prep'),
	(GARDEN, 'Garden'),
	(DELIVERY, 'Delivery'),
	(EDUCATION, 'Education'),
	(WAREHOUSE, 'Warehouse'),
	(DAYCARE, 'Day care'),
	(SORT, 'Sort'),
	)


class User_input(models.Model):
	## model fields
	locations = MultiSelectField(choices = location_choices,
		max_choices = 2,
		max_length = 60)
	services = MultiSelectField(choices = service_size_choices,
		max_choices = 2,
		max_length = 60)
	organizations = MultiSelectField(choices = organization_size_choices,
		max_choices = 2,
		max_length = 60)
	roles = MultiSelectField(choices = role_choices,
		max_choices = 2,
		max_length = 60)
	

