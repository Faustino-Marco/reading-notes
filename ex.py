def itinerary(plane_tickets):
    travel_itinerary = []
    origins = []
    destinations = []
    start = None
    for ticket in plane_tickets:
        origins.append(ticket["origin"])
        destinations.append(ticket["destination"])
        if ticket["origin"] not in destinations:
            start = ticket["origin"]
    
    while origins:
        
        for index, origin in enumerate(origins):
            if origin == start:
                old_start = origins.pop(index)
                travel_itinerary.append(old_start)
                start = destinations[index]
                destinations.pop(index)
                if destinations == []:
                    travel_itinerary.append(start)
                
    
    return travel_itinerary


if __name__ == "__main__":

    plane_tickets = [
        {'origin': 'Seattle', 'destination': 'Raleigh'},
        {'origin': 'Raleigh', 'destination': 'New York'},
        {'origin': 'Miami', 'destination': 'Seattle'},
    ]

    test = itinerary(plane_tickets)
    print(test)