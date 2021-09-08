''' Attempt at implementing the following code from :https://iliauk.wordpress.com/2015/12/18/data-mining-google-places-cafe-nero-example/

This code is attempting to obtain the information from Google Place API within a square
of coordinates to circumvent the limit of 60 items from the Google Place API Search query.

'''

import urllib
import csv
import time
import math
import requests
import itertools
import json

#key_json = json.load(open("credentials.json"))

API_KEY = [
    "AIzaSyAJ97RuEMWKQnXxVQLPhu0OaljMVu76bfI"
]
shops_list = []
debug_list = []
SAVE_PATH = r'C:\Users\Pedro\Documents\Propulsion_Academy\Course_Structure_Template\Challenge-Migros-1-Propulsion-Academy\notebooks'
COMPANY_SEARCH = 'supermarkt'
RADIUS_KM = 0.5
LIMIT = 60


class coordinates_box(object):
    """
    Initialise a coordinates_box class which will hold the produced coordinates and
    output a html map of the search area
    """
    def __init__(self):
        self.coordset = []

    def createcoordinates(self,
                          southwest_lat,
                          southwest_lng,
                          northeast_lat,
                          northeast_lng):
        """
        Based on the input radius this tesselates a 2D space with circles in
        a hexagonal structure
        """
        earth_radius_km = 6371
        lat_start = math.radians(southwest_lat)
        lon_start = math.radians(southwest_lng)
        lat = lat_start
        lon = lon_start
        lat_level = 1
        while True:
            if (math.degrees(lat) <= northeast_lat) & (math.degrees(lon) <= northeast_lng):
                self.coordset.append([math.degrees(lat), math.degrees(lon)])
            parallel_radius = earth_radius_km * math.cos(lat)
            if math.degrees(lat) > northeast_lat:
                break
            elif math.degrees(lon) > northeast_lng:
                lat_level += 1
                lat += (RADIUS_KM / earth_radius_km) + (RADIUS_KM / earth_radius_km) * math.sin(math.radians(30))
                if lat_level % 2 != 0:
                    lon = lon_start
                else:
                    lon = lon_start + (RADIUS_KM / parallel_radius) * math.cos(math.radians(30))
            else:
                lon += 2 * (RADIUS_KM / parallel_radius) * math.cos(math.radians(30))

        print('Coordinates-set contains %d coordinates' % len(self.coordset))
        # Save coordinates:
        f = open(SAVE_PATH + 'circles_' + COMPANY_SEARCH + '_python_mined.csv', 'w', newline='')
        w = csv.writer(f)
        for coord in self.coordset:
            w.writerow(coord)
        f.close()
        # LOG MAP
        self.htmlmaplog(SAVE_PATH + 'htmlmaplog_' + COMPANY_SEARCH + '.html')

    def htmlmaplog(self,
                   map_save_path):
        """
        Outputs a HTML map
        """
        htmltext = """
        <!DOCTYPE html >
          <style type="text/css">
                    html, body {
                        height: 100%;
                        width: 100%;
                        padding: 0px;
                        margin: 0px;
                    }
        </style>
        <head>
        <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
        <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
        <title>Boundary Partitioning</title>
        <xml id="myxml">
        <markers>
        """
        # Content
        for coord in self.coordset:
            rowcord = '<marker name = "' + COMPANY_SEARCH + '" lat = "' + \
                      '%.5f' % coord[0] + '" lng = "' + '%.5f' % coord[1] + '"/>\n'
            htmltext += rowcord
        # Bottom
        htmltext += """
        </markers>
        </xml>
        <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?&sensor=false&libraries=geometry"></script>
        <script type="text/javascript">
        var XML = document.getElementById("myxml");
        if(XML.documentElement == null)
        XML.documentElement = XML.firstChild;
        var MARKERS = XML.getElementsByTagName("marker");
        """
        htmltext += "var RADIUS_KM = " + str(RADIUS_KM) + ";"
        htmltext += """
        var map;
        var geocoder = new google.maps.Geocoder();
        var counter = 0
        function load() {
            // Initialize around City, London
            var my_lat = 51.518175;
            var my_lng = -0.129064;
            var mapOptions = {
                    center: new google.maps.LatLng(my_lat, my_lng),
                    zoom: 12
            };
            map = new google.maps.Map(document.getElementById('map'),
                mapOptions);
            var bounds = new google.maps.LatLngBounds();
            for (var i = 0; i < MARKERS.length; i++) {
                var name = MARKERS[i].getAttribute("name");
                var point_i = new google.maps.LatLng(
                    parseFloat(MARKERS[i].getAttribute("lat")),
                    parseFloat(MARKERS[i].getAttribute("lng")));
                var icon = {icon: 'http://labs.google.com/ridefinder/images/mm_20_gray.png'};
                var col = '#0033CC';
                var draw_circle = new google.maps.Circle({
                    center: point_i,
                    radius: RADIUS_KM*1000,
                    strokeColor: col,
                    strokeOpacity: 0.15,
                    strokeWeight: 2,
                    fillColor: col,
                    fillOpacity: 0.15,
                    map: map
                });
                var marker = new google.maps.Marker({
                    position: point_i,
                    map: map,
                    icon: 'https://maps.gstatic.com/intl/en_us/mapfiles/markers2/measle_blue.png'
                })
                bounds.extend(point_i);
            };
            map.fitBounds(bounds);
        }
        </script>
        </head>
        <body onload="load()">
        <center>
        <div style="padding-top: 20px; padding-bottom: 20px;">
        <div id="map" style="width:90%; height:1024px;"></div>
        </center>
        </body>
        </html>
        """
        with open(map_save_path, 'w') as f:
            f.write(htmltext)
        f.close()


class counter(object):
    """
    Counter class to keep track of the requests usage
    """
    def __init__(self):
        self.keynum = 0
        self.partition_num = 0
        self.detailnum = 0

    def increment_key(self):
        self.keynum += 1

    def increment_partition(self):
        self.partition_num += 1

    def increment_detail(self):
        self.detailnum += 1


def googleplaces(lat,
                 lng,
                 radius_metres,
                 search_term,
                 key,
                 pagetoken=None,
                 nmbr_returned=0):
    """
    Function uses the 'nearbysearch', however it is possible to use the radar-search and others
    located here: https://developers.google.com/places/web-service/search
    The API call returns a page_token for the next page up to a total of 60 results
    """
    location = urllib.parse.quote("%.5f,%.5f" % (lat,lng))
    radius = float(radius_metres)
    name = urllib.parse.quote(str(search_term))

    search_url = ('https://maps.googleapis.com/maps/api/place/' + 'nearbysearch' +
                  '/json?location=%s&radius=%d&keyword=%s&key=%s') % (location, radius, name, key)
    if pagetoken is not None:
        search_url += '&pagetoken=%s' % pagetoken
        # SLEEP so that request is generated
        time.sleep(2)

    time.sleep(0.1)
    req_count.increment_key()
    print("Search number %d: %s" % (req_count.keynum, search_url))
    google_search_request = requests.get(search_url)
    search_json_data = google_search_request.json()

    print(search_json_data['status'])
    if search_json_data['status'] == 'OK':
        nmbr_returned += len(search_json_data['results'])
        for place in search_json_data['results']:
            shop = [place['name'].encode('ascii', 'ignore').decode('ascii'),
                    place['vicinity'].encode('ascii', 'ignore').decode('ascii'),
                    place['geometry']['location']['lat'],
                    place['geometry']['location']['lng'],
                    place['types'],
                    place['place_id']]
            if shop not in shops_list:
                shops_list.append(shop)
        # Possible to get up to 60 results
        # from one search by passing next_page_token
        try:
            next_token = search_json_data['next_page_token']
            googleplaces(lat=lat,
                         lng=lng,
                         radius_metres=radius_metres,
                         search_term=search_term,
                         key=key,
                         pagetoken=next_token,
                         nmbr_returned=nmbr_returned)
            return
        except KeyError:
            pass
    elif search_json_data['status'] == 'ZERO_RESULTS':
        pass
    else:
        try:
            print('Error: %s' % search_json_data['error_message'])
        except KeyError:
            print('Unknown error message - check URL')

    debug_list.append([lat, lng, nmbr_returned])
    print('Partition %s no. %d/%d - found %d stores' %
          (location, req_count.partition_num, len(coord.coordset), nmbr_returned))
    if nmbr_returned >= LIMIT:
        print('Warning possible cut-off')
    print('List contains %d stores with key number: %d' % (len(shops_list), (req_count.keynum // 900)))


def googledetails(place_id,
                  key):
    """
    Function uses the miend place_ids to get further data from the details API
    """
    detail_url = ('https://maps.googleapis.com/maps/api/place/' + 'details' +
                  '/json?placeid=%s&key=%s') % (place_id, key)
    print(detail_url)
    google_detail_request = requests.get(detail_url)
    detail_json_data = google_detail_request.json()
    time.sleep(0.1)

    if detail_json_data['status'] == 'OK':
        try:
            address_components = detail_json_data['result']['address_components']
            print(address_components)
            # At the moment care only about extracting postcode, however possible to get:
            # Street number, Town, etc.
            for x in address_components:
                if x['types'] == ["postal_code"]:
                    postcode = x['long_name'].encode('ascii', 'ignore').decode('ascii')
                    break
                postcode = 'Nan'
        except KeyError:
            postcode = 'NaN'
        try:
            formatted_address = detail_json_data['result']['formatted_address'].encode('ascii', 'ignore').decode('ascii')
        except KeyError:
            formatted_address = 'NaN'
        try:
            website = detail_json_data['result']['website'].encode('ascii', 'ignore').decode('ascii')
        except KeyError:
            website = 'NaN'
        detail = [postcode, formatted_address, website]
    else:
        detail = detail_json_data['status'].encode('ascii', 'ignore').decode('ascii')

    print(detail)
    return detail


def fillindetails(f=SAVE_PATH + COMPANY_SEARCH + '_python_mined.csv'):
    """
    Opens the produced CSV and extracts the place ID for querying
    """
    detailed_stores_out = []
    simple_stores_out = []
    with open(f, 'r') as csvin:
        reader = csv.reader(csvin)

        for store in reader:
            req_count.increment_detail()
            key_number = (req_count.keynum // 950)

            detailed_store = googledetails(store[5],  API_KEY[key_number])
            print('Row number %d/%d, store info: %s' % (req_count.detailnum, len(shops_list), detailed_store))
            detailed_stores_out.append(detailed_store)
            simple_stores_out.append(store)

    # OUTPUT to CSV
    f = open(SAVE_PATH + 'detailed_' + COMPANY_SEARCH + '_python_mined.csv', 'w', newline='')
    w = csv.writer(f)

    # Combine both lists into one
    combined_list = [list(itertools.chain(*a)) for a in zip(simple_stores_out, detailed_stores_out)]

    for one_store in combined_list:
        try:
            w.writerow(one_store)
        except Exception as err:
            print("Something went wrong: %s" % err)
            w.writerow("Error")
    f.close()


def runsearch():
    """
    Initialises the searches for each partition produced
    """
    print("%d Keys Remaining" % (len(API_KEY)-1))
    for partition in coord.coordset:
        # Keys have a life-span of 1000 requests
        key_number = (req_count.keynum // 1000)
        req_count.increment_partition()

        googleplaces(lat=partition[0],
                     lng=partition[1],
                     radius_metres=RADIUS_KM*1000,
                     search_term=COMPANY_SEARCH,
                     key=API_KEY[key_number])

    # OUTPUT to CSV
    f = open(SAVE_PATH + COMPANY_SEARCH + '_python_mined.csv', 'w', newline='')
    w = csv.writer(f)
    for one_store in shops_list:
        w.writerow(one_store)
    f.close()

    # OUTPUT LOG to CSV
    f = open(SAVE_PATH + 'log_' + COMPANY_SEARCH + '_python_mined.csv', 'w', newline='')
    w = csv.writer(f)
    for debug_result in debug_list:
        w.writerow(debug_result)
    f.close()

    # DETAIL SEARCH
    fillindetails()


if __name__ == "__main__":
    # 1. CREATE PARTITIONS
    # Setup coordinates
    # Our coordinate system based on max/min of lng and lat
    # max_lat	47.4323
    # min_lat	47.3577
    # max_lng	8.61147
    # min_lng	8.42736

    coord = coordinates_box()
    # coord.createcoordinates(51.471834, -0.204326, 51.542672, -0.049488)
    # diff of lon = 0.070838 / diff of lat = 0.154838
    coord.createcoordinates(47.3577, 8.42736, 47.4323, 8.61147)
    # diff of lon = 0.0746 / diff of lat = 0.18411

    # 2. SEARCH PARTITIONS
    # Setup counter
    req_count = counter()
    runsearch()
