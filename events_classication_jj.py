# app.py
import streamlit as st

#Substituir valores
classication_incidentes  = {
  'Contact with Pedestrians or Bystanders': 'Collision with Cyclist / Motorcycle / Pedestrian',
 'J&J Driver failed to give right of way (failed to yield)': ['Client Changed Lanes', 
                                                              'Client Entering Major Road', 
                                                              'Client Overtaking',
                                                              'Client turned across path of TP',
                                                              'Client Undertaking', 
                                                              'Head on collision / Narrow Road Collision', 
                                                              'Roundabout Collision'],
  
 'J&J Driver Failed to Observe Clearance': ['Client collided with Parked Vehicle', 
                                            'Client Hit Stationary Object', 
                                            'Client Hit Third Party Whilst Reversing'],
  'J&J Driver hit rear of other vehicle.': ['Client Hit Rear Of Third Party'],

  'J&J Driver parking/unparking': ['Client collided with Parked Vehicle', 
                                   'Client Hit Stationary Object', 
                                   'Client Hit Third Party Whilst Reversing', 
                                   'Client pulled out from parked position' ],
  
  'J&J Driver parking/unparking* (while Other Driver was in motion or stopped, but not parked)': ['Client collided with Parked Vehicle',
                                                                                                  'Client Hit Stationary Object',
                                                                                                  'Client Hit Third Party Whilst Reversing', 
                                                                                                  'Client pulled out from parked position'],
  
  'Lane Encroachment (other driver)': ['Third Party Changing Lanes',
                                       'TP Overtaking',
                                       'TP Undertaking'],
  
  'Other driver failed to give right of way (failed to yield)': ['Head on collision / Narrow Road Collision',
                                                                 'Roundabout Collision',
                                                                 'Third Party Entering Major Road',
                                                                 'TP Hit client whilst Reversing',
                                                                 'TP pulled out from parked position',
                                                                 'TP turned across Path of client'
                                                                 ],
  
  'Others': ['Client Opened Door',
             'Multi-Vehicle collision',
             'TP Opened door'],
             
  
 'Incident (Not measured against CPMM, no follow up needed)': ['Attempted Theft',
                                                               'Audio',
                                                               'Blow Out / Puncture',
                                                               'Hit / Damaged By Animal',
                                                               'Items stole from vehicle',
                                                               'Load fell from client vehicle',
                                                               'Load fell from third party vehicle',
                                                               'Lost Keys',
                                                               'Rental Damage',
                                                               'Severe Weather', 
                                                               'Stolen', 
                                                               'Damaged in car wash',
                                                               'Glass', 
                                                               'Fuel Contamination',
                                                               'Vandalism',
                                                               'Valet Parking',
                                                               'Flood Damage',
                                                               'Fire Damage', 
                                                               'Decals/Livery', 
                                                               'Drover Over Pot Hole in Road',
                                                               'Driver Unaware Of Incident', 
                                                               'De Fleet / Wear & Tear Damage',
                                                               'Client Vehicle Hit Whislt Parked',
                                                               'Client Hit Debris'],
  
  'Needs Follow Up': ['Alleged Incident - Rental Damage Claim Under Investigation',
                      'Alleged Incident - TP Clain Under Investigation']


 }

st.image(r'images\CEPA-MOBILITY_logo-principal_blanco (1).png', width=150)

def find_key(input_value, classification_dict):
    for key, value in classification_dict.items():
        if isinstance(value, list) and input_value in value:
            return key
        elif input_value == value:
            return key
    return None



def main():
    st.title("Events Classification")
    st.write("Drag and drop the csv or xlsx file in to the processor")

if __name__ == "__main__":
    main()


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

