from data_manager import DataManager
from pprint import pprint

data = DataManager()

pprint(data.get_users())
pprint(data.get_users()[0]["email"])