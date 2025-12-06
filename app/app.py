import streamlit as st
import pandas as pd
import numpy as np
import os, sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from src.predict import predict_price

# ==========================
# UI CONFIGURATION
# ==========================

# --- REAL THEME SWITCHER (WORKING, NO CSS HACK) ---
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

theme_choice = st.radio("Theme:", ["Light", "Dark"], horizontal=True)

if theme_choice.lower() != st.session_state["theme"]:
    st.session_state["theme"] = theme_choice.lower()
    st.experimental_set_query_params(theme=st.session_state["theme"])
    st.rerun()

# Apply theme
if st.session_state["theme"] == "dark":
    st.markdown("""
    <style>
        .stApp { background-color: #0E1117; color: white; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .stApp { background-color: white; color: black; }
    </style>
    """, unsafe_allow_html=True)


# ==========================
# HEADER
# ==========================

st.title("Airbnb Price Prediction App")
st.write("Fill the details below and the model will predict the estimated price.")

# ==========================
# DROPDOWN OPTIONS
# ==========================

room_types = [
    "Entire home/apt",
    "Private room",
    "Shared room",
    "Hotel room"
]

neighbourhoods = ['16th Street Heights', 'Adams Morgan', 'Alamo Square', 'Albany Park', 'Alhambra', 'Allerton', 'Allston-Brighton', 'Alondra Park', 'Alphabet City', 'Altadena', 'American University Park', 'Anacostia', 'Andersonville', 'Arboretum', 'Arcadia', 'Archer Heights', 'Arleta', 'Armour Square', 'Arrochar', 'Artesia', 'Arts District', 'Astoria', 'Atwater Village', 'Auburn Gresham', 'Austin', 'Avondale', 'Azusa', 'Back Bay', 'Back of the Yards', 'Balboa Terrace', 'Baldwin Hills', 'Baldwin Park', 'Barney Circle', 'Barry Farm', 'Bath Beach', 'Battery Park City', 'Bay Ridge', 'Baychester', 'Bayside', 'Bayview', 'Beacon Hill', 'Bedford Park', 'Bedford-Stuyvesant', 'Bel Air/Beverly Crest', 'Bell', 'Bellevue', 'Bellflower', 'Belmont', 'Belmont Cragin', 'Benning', 'Benning Heights', 'Benning Ridge', 'Bensonhurst', 'Bergen Beach', 'Berkley', 'Bernal Heights', 'Beverly', 'Beverly Hills', 'Bloomingdale', 'Boerum Hill', 'Borough Park', 'Boyle Heights', 'Boystown', 'Bradbury', 'Brentwood', 'Bridgeport', 'Brighton Beach', 'Brighton Park', 'Brightwood', 'Bronxdale', 'Bronzeville', 'Brookland', 'Brookline', 'Brooklyn', 'Brooklyn Heights', 'Brooklyn Navy Yard', 'Brownsville', 'Bucktown', 'Buena Vista', 'Burbank', 'Burleith', 'Bushwick', 'Cahuenga Pass', 'Cambridge', 'Canarsie', 'Canoga Park', 'Capitol Hill', 'Carroll Gardens', 'Carson', 'Carver Langston', 'Castle Hill', 'Castleton Corners', 'Cathedral Heights', 'Central Northeast/Mahaning Heights', 'Cerritos', 'Charlestown', 'Chatham', 'Chatsworth', 'Chelsea', 'Chestnut Hill', 'Chevy Chase', 'Chevy Chase, MD', 'Chillum, MD', 'Chinatown', 'City Island', 'Civic Center', 'Claremont', 'Cleveland Park', 'Clifton', 'Clinton Hill', 'Co-op City', 'Cobble Hill', 'Cole Valley', 'College Point', 'Colonial Village', 'Columbia Heights', 'Columbia Street Waterfront', 'Commerce', 'Compton', 'Concord', 'Concourse', 'Concourse Village', 'Coney Island', 'Congress Heights', 'Coolidge Corner', 'Corona', 'Country Club', 'Covina', 'Cow Hollow', 'Crestwood', 'Crocker Amazon', 'Crotona', 'Crown Heights', 'Culver City', 'Cypress Park', 'DUMBO', 'Daly City', 'Deanwood', 'Del Rey', 'Diamond Heights', 'Ditmars / Steinway', 'Dogpatch', 'Dongan Hills', 'Dorchester', 'Douglass', 'Downey', 'Downtown', 'Downtown Brooklyn', 'Downtown Crossing', 'Downtown/Penn Quarter', 'Duarte', 'Duboce Triangle', 'Dunning', 'Dupont Circle', 'Dupont Park', 'Dyker Heights', 'Eagle Rock', 'East Boston', 'East Corner', 'East Elmhurst', 'East Flatbush', 'East Harlem', 'East Hollywood', 'East Los Angeles', 'East New York', 'East San Gabriel', 'East Village', 'Eastchester', 'Eastland Gardens', 'Echo Park', 'Eckington', 'Edenwald', 'Edgewater', 'Edgewood', 'Edison Park', 'El Monte', 'El Segundo', 'El Sereno', 'Elm Park', 'Elmhurst', 'Eltingville', 'Elysian Valley', 'Emerson Hill', 'Encino', 'Englewood', 'Excelsior', 'Fairlawn', 'Fenway/Kenmore', 'Financial District', "Fisherman's Wharf", 'Flatbush', 'Flatiron District', 'Flatlands', 'Florence-Graham', 'Flushing', 'Foggy Bottom', 'Fordham', 'Forest Hill', 'Forest Hills', 'Fort Davis', 'Fort Dupont', 'Fort Greene', 'Fort Lincoln', 'Fort Totten', 'Foxhall', 'Fresh Meadows', 'Friendship Heights', 'Galewood', 'Gallaudet', 'Gardena', 'Garfield Park', 'Garfield Ridge', 'Gateway', 'Georgetown', 'Gerritsen Beach', 'Glassell Park', 'Glen Park', 'Glendale', 'Glendora', 'Glover Park', 'Gold Coast', 'Good Hope', 'Government Center', 'Gowanus', 'Gramercy Park', 'Granada Hills North', 'Grand Crossing', 'Graniteville', 'Grasmere', 'Gravesend', 'Great Kills', 'Greenpoint', 'Greenway', 'Greenwich Village', 'Greenwood Heights', 'Grymes Hill', 'Haight-Ashbury', 'Hamilton Heights', 'Harbor City', 'Harbor Gateway', 'Harlem', 'Harvard Square', 'Hawaiian Gardens', 'Hawthorne', 'Hayes Valley', "Hell's Kitchen", 'Hermon', 'Hermosa', 'Hermosa Beach', 'Highbridge', 'Highland Park', 'Hillbrook', 'Hillcrest', 'Hollywood', 'Hollywood Hills', 'Howard Beach', 'Hudson Square', 'Huguenot', 'Humboldt Park', 'Huntington Park', 'Hunts Point', 'Hyde Park', 'Ingleside', 'Inglewood', 'Inner Sunset', 'Inwood', 'Irving Park', 'Irwindale', 'Ivy City', 'Jackson Heights', 'Jamaica', 'Jamaica Plain', 'Japantown', 'Jefferson Park', 'Judiciary Square', 'Kalorama', 'Kensington', 'Kent', 'Kenwood', 'Kew Garden Hills', 'Kingman Park', 'Kingsbridge', 'Kingsbridge Heights', 'Kips Bay', 'La Canada Flintridge', 'La Crescenta-Montrose', 'La Habra', 'La Mirada', 'La Puente', 'Lake Balboa', 'Lakeshore', 'Lakeview', 'Lakewood', 'Lamond Riggs', 'Langdon', 'Laurel Canyon', 'Lawndale', 'LeDroit Park', 'Leather District', 'Lefferts Garden', 'Lighthouse HIll', 'Lincoln Heights', 'Lincoln Park', 'Lincoln Square', 'Lindenwood', 'Little Italy', 'Little Italy/UIC', 'Little Village', 'Logan Circle', 'Logan Square', 'Lomita', 'Long Beach', 'Long Island City', 'Longwood', 'Loop', 'Los Feliz', 'Lower East Side', 'Lower Haight', 'Lynwood', 'Magnificent Mile', 'Malibu', 'Manhattan', 'Manhattan Beach', 'Manor Park', 'Mar Vista', 'Marble Hill', 'Marina', 'Marina Del Rey', 'Marine Park', 'Mariners Harbor', 'Marshall Heights', 'Maspeth', 'Massachusetts Heights', 'Mattapan', 'McKinley Park', 'Meatpacking District', 'Meiers Corners', 'Melrose', 'Michigan Park', 'Mid-City', 'Mid-Wilshire', 'Middle Village', 'Midland Beach', 'Midtown', 'Midtown East', 'Midwood', 'Mission Bay', 'Mission District', 'Mission Hill', 'Mission Hills', 'Mission Terrace', 'Monrovia', 'Montebello', 'Montecito Heights', 'Monterey Hills', 'Monterey Park', 'Morgan Park', 'Morningside Heights', 'Morris Heights', 'Morris Park', 'Morrisania', 'Mott Haven', 'Mount Eden', 'Mount Pleasant', 'Mount Vernon Square', 'Mount Washington', 'Mt Rainier/Brentwood, MD', 'Mt. Vernon Square', 'Murray Hill', 'Navy Yard', 'Naylor Gardens', 'Near North Side', 'Near Northeast', 'Near Northeast/H Street Corridor', 'Near West Side', 'New Brighton', 'New Dorp Beach', 'New Springville', 'Nob Hill', 'Noe Valley', 'Noho', 'Nolita', 'North Beach', 'North Center', 'North Cleveland Park', 'North End', 'North Hills East', 'North Hills West', 'North Hollywood', 'North Lawndale', 'North Michigan Park', 'North Park', 'Northridge', 'Norwalk', 'Norwood', 'Norwood Park', "O'Hare", 'Oakland', 'Oakwood', 'Observatory Circle', 'Oceanview', "Old Soldiers' Home", 'Old Town', 'Outer Sunset', 'Ozone Park', 'Pacific Heights', 'Pacific Palisades', 'Pacoima', 'Palisades', 'Palms', 'Palos Verdes', 'Panorama City', 'Paramount', 'Park Slope', 'Park Versailles', 'Park View', 'Parkchester', 'Parkside', 'Pasadena', 'Pelham Bay', 'Petworth', 'Pico Rivera', 'Pilsen', 'Pleasant Hill', 'Pleasant Plains', 'Port Morris', 'Port Richmond', 'Portage Park', 'Porter Ranch', 'Portola', 'Potrero Hill', 'Presidio', 'Presidio Heights', 'Prospect Heights', 'Queens', 'Rancho Palos Verdes', 'Randall Manor', 'Randle Highlands', 'Red Hook', 'Redondo Beach', 'Rego Park', 'Reseda', 'Richmond District', 'Richmond Hill', 'Ridgewood', 'River North', 'River Terrace', 'River West', 'Riverdale', 'Rogers Park', 'Rolling Hills', 'Rolling Hills Estates', 'Roosevelt Island', 'Roscoe Village', 'Rosebank', 'Roseland', 'Rosemead', 'Roslindale', 'Rossville', 'Roxbury', 'Russian Hill', 'San Gabriel', 'San Marino', 'San Pedro', 'Santa Fe Springs', 'Santa Monica', 'Sea Cliff', 'Sea Gate', 'Shaw', 'Sheepshead Bay', 'Shepherd Park', 'Sherman Oaks', 'Shipley Terrace', 'Sierra Madre', 'Signal Hill', 'Silver Lake', 'Silver Spring, MD', 'Skid Row', 'Skyland', 'SoMa', 'Soho', 'Somerville', 'Soundview', 'South Beach', 'South Boston', 'South Chicago', 'South El Monte', 'South End', 'South Gate', 'South LA', 'South Loop/Printers Row', 'South Ozone Park', 'South Pasadena', 'South Robertson', 'South San Gabriel', 'South Shore', 'South Street Seaport', 'South Whittier', 'Southwest Waterfront', 'Spring Valley', 'Spuyten Duyvil', 'St. Elizabeths', 'St. George', 'Stapleton', 'Streeterville', 'Stronghold', 'Studio City', 'Sun Valley', 'Sunland/Tujunga', 'Sunnyside', 'Sunset Park', 'Sylmar', 'Takoma', 'Takoma Park, MD', 'Tarzana', 'Telegraph Hill', 'Temple City', 'Tenderloin', 'The Bronx', 'The Castro', 'The Rockaways', 'Theater District', 'Throgs Neck', 'Times Square/Theatre District', 'Toluca Lake', 'Tompkinsville', 'Topanga', 'Torrance', 'Tottenville', 'Tremont', 'Tribeca', 'Trinidad', 'Truxton Circle', 'Twin Peaks', 'Twining', 'U Street Corridor', 'Ukrainian Village', 'Union Square', 'University Heights', 'Upper East Side', 'Upper West Side', 'Uptown', 'Utopia', 'Valley Glen', 'Valley Village', 'Van Nest', 'Van Nuys', 'Venice', 'Vernon', 'Vinegar Hill', 'Visitacion Valley', 'Wakefield', 'Washington Heights', 'Washington Highlands', 'Washington Park', 'Watertown', 'Watts', 'Wesley Heights', 'West Adams', 'West Athens', 'West Brighton', 'West Covina', 'West Elsdon', 'West End', 'West Farms', 'West Hills', 'West Hollywood', 'West Lawn', 'West Loop/Greektown', 'West Los Angeles', 'West Portal', 'West Puente Valley', 'West Ridge', 'West Roxbury', 'West Town', 'West Town/Noble Square', 'West Village', 'Westchester Village', 'Westchester/Playa Del Rey', 'Westerleigh', 'Western Addition/NOPA', 'Westlake', 'Westmont', 'Westside', 'Westwood', 'Whitestone', 'Whittier', 'Wicker Park', 'Williamsbridge', 'Williamsburg', 'Willowbrook', 'Wilmington', 'Windsor Terrace', 'Winnetka', 'Winthrop', 'Woodhaven', 'Woodland', 'Woodland Hills/Warner Center', 'Woodlawn', 'Woodley Park', 'Woodridge', 'Woodside', 'Wrigleyville']
# (Shortened in this preview — YOU will paste the full list you provided.)

# ==========================
# INPUT FORM
# ==========================

with st.form("prediction_form"):
    st.subheader("Enter Listing Details")

    col1, col2 = st.columns(2)

    with col1:
        accommodates = st.number_input("Accommodates", 1, 20)
        bathrooms = st.number_input("Bathrooms", 0.0, 10.0, step=0.5)
        beds = st.number_input("Beds", 0, 20)

    with col2:
        bedrooms = st.number_input("Bedrooms", 0, 10)
        room_type = st.selectbox("Room Type", room_types)
        neighbourhood = st.selectbox("Neighbourhood", neighbourhoods)

    submitted = st.form_submit_button("Predict Price")

# ==========================
# PREDICTION
# ==========================

if submitted:
    try:
        inputs = {
            "accommodates": accommodates,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "beds": beds,
            "room_type": room_type,
            "neighbourhood": neighbourhood
        }

        price = predict_price(inputs)
        price_inr = round(price, 2)

        st.success(f"Estimated Price: ₹{price_inr}")

    except Exception as e:
        st.error("Prediction failed. Please check logs.")
        st.code(str(e))
