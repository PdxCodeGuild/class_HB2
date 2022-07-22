import requests
import pprint

routes = input('What route would you like to view? ')

# response = requests.get(f'https://developer.trimet.org/ws/v2/vehicles?appID=D065A3A5DAE4622752786CEB9&routes={routes}')
response = requests.get(f'https://developer.trimet.org/ws/v2/vehicles', params={'appID': 'D065A3A5DAE4622752786CEB9', 'routes': routes})
# print(response)
# print(response.url)
# print(response.status_code)
# print(response.encoding)
# print(response.headers)
# pprint.pprint(response.text)
# pprint.pprint(response.json())

trains_and_buses = response.json()['resultSet']['vehicle']
# pprint.pprint(trains_and_buses)

print(f"there are {len(trains_and_buses)} results:")
for vehicle in trains_and_buses:
    print(f"{vehicle['type']} {vehicle['signMessageLong']} -- ({vehicle['latitude']},{vehicle['longitude']})")
