import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("C:\\Users\\DELL\\Downloads\\Data set Part 2 - propulsion_module.csv")
print(df)
print(df.count())

print(df.head())

data = {
    "Parameter": [
       "Lunar Polar Orbit",
       "Mission life",
       "Structure",
       "Dry Mass",
       "Propellant Mass",
       "Total PM Mass",
       "Power Generation",
       "Communication",
       "Attitude Sensors",
       "Propulsion System"
  ],
  "Specifications": [                               
      "From 170 x 36500 km to lunar polar orbit",
      "Carrying Lander Module & Rover upto ~100 x 100 km launch injection.",
      "Modified version of I-3 K",
      "448.62 kg (including pressurant)",
      "1696.39 kg",
      "2145.01 kg",
      "738 W, Summer solistices and with bias",
      "S-Band Transponder (TTC) – with IDSN",
      "CASS, IRAP, Micro star sensor",
      "Bi-Propellant Propulsion System (MMH + MON3)"
   ]
 }

df = pd.DataFrame(data)
print(df)
                   
data ={
    "Parameter" : [                         
          " Mission life ",                       
          " Mass",                         
          " Power",
          " Payloads",                          
          " Dimensions (mm3)",                  
          " Communication",                     
          " Landing site"
    ],
    "Specifications": [
          "1 Lunar day (14 Earth days)",
          "1749.86 kg including Rover",
          "738 W (Winter solstice)",
          " 3",
          " 2000 x 2000 x 1166",
          "ISDN, Ch-2 Orbiter, Rover",
          "69.367621 S, 32.348126 E"
    ]
}

lander_df = pd.DataFrame(data)
print(lander_df)

data = {
    "Parameter": [
        "Mission Life",
        "Mass",
        "Power",
        "Payloads",
        "Diamentions (mm3)",
        "Communication"
    ],
    "Specifications": [
        "1 Lunar day",
        "26 kg",
        "50 w",
        "2",
        "917 x 750 x 397",
        "Lander"
    ]
}

rover_df = pd.DataFrame(data)
print(rover_df)

import re

def extract_numerical_value(spec):
      numeric_pattern = r"(\d+(\,\d)?)"
      custome_numeric_pattern = r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?"

      combined_pattern = f"({numeric_pattern}{custome_numeric_pattern})"

      matches = re.findall(combined_pattern, spec)

      if matches:
          return float(matches[0][0])
      else:
          return None

df["Numeric_value"] = df["Specifications"].apply(extract_numerical_value)
print(df)

rover_df["Numeric_value"] = rover_df["Specifications"].apply(extract_numerical_value)
print(rover_df)

lander_df["Numeric_value"] = lander_df["Specifications"].apply(extract_numerical_value)
print(lander_df)

import math

rover_mass = 26
lander_dry_mass = 1749.86
total_mass = rover_mass + lander_dry_mass
delta_v_required = 1500
isp_lander_ingine = 300

propellant_mass_required = total_mass * math.exp(delta_v_required / isp_lander_ingine) - total_mass
propellant_mass_required = round(propellant_mass_required, 2)

rover_power_requirement = 50
lander_battery_capacity = 2000

rover_operating_time_hour = lander_battery_capacity / rover_power_requirement

print("Mass Budget:")
print(f"Lander Mass:{lander_dry_mass}kg")
print(f"Rover Mass:{rover_mass} kg")
print(f"Propellant Mass Required:{propellant_mass_required}kg (matches value in Lander DataFrame)")

print("\nPower Budget:")
print(f"Rover power requirement:{rover_power_requirement} w ")
print(f"Lander battery capacity:{lander_battery_capacity} wh")
print(f"Rover can operate for{rover_operating_time_hour:.2f}hours on stored power")

print("\nMobility Assessment:")
print("Low mass of the rover allows for mobility on uneven lunar surface")
print("Number of payloads for science measurments is 2")

print("Mass Budget:")
print("Lander Mass: 1749.86 kg")
print("Rover Mass: 26 kg")
print("propellant mass required: 261785.13 kg (matches value in Lander DataFrame)")

print("Power Budget:")
print("Rover power requirement: 50 w")
print("Lander battery capacity: 2000 wh")
print("Rover can operate for 40.00 hours on stored power")

print("Mobility Assessment:")
print("Low mass of the rover allows for mobility on uneven lunar surface")
print("Number of payloads for science measurments is 2")


import matplotlib.pyplot as plt

labels = ['Lander Dry Mass', 'Rover Mass', 'Propellant Mass']
mass_value = [lander_dry_mass, rover_mass, propellant_mass_required]

plt.figure(figsize=(8, 6))
plt.bar(labels, mass_value, color=['blue', 'pink', 'red'])
plt.xlabel('Components')
plt.ylabel('Mass(kg)')
plt.title('Mass Budget')
plt.ylim(0, max(mass_value) * 1.2)

for i, v in enumerate(mass_value):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.show()

#
labels = ['Rover Power Requirment', 'Lander Battery Capacity']
power_values = [rover_power_requirement, lander_battery_capacity]

plt.figure(figsize=(8, 6))
plt.bar(labels, power_values, color=['blue', 'green'])
plt.xlabel('Components')
plt.ylabel('Power(watt.hours)')
plt.title('Power Budget')
plt.ylim=(0, max(power_values) * 1.2)

for i, v in enumerate(power_values):
      plt.text(i, v, str(v), ha='center', va='bottom')

plt.show()

# same graph plotly me print kiya

import plotly.express as px

mass_labels = ['Lander Dry Mass', 'Rover Mass', 'Propellant Mass']
mass_values = [lander_dry_mass, rover_mass, propellant_mass_required]

mass_fig = px.bar(x = mass_labels, y = mass_values, color = mass_labels,
                  labels={'x': 'Components', 'y': 'Mass (kg)'},
                  title='Mass Budget')

mass_fig.update_traces(texttemplate='%{y:.2f}kg', textposition='outside')

mass_fig.show()

# Mass Budget pie chart me banane ke liye

mass_fig = px.pie(names = mass_labels, values = mass_values, title = 'Mass Budget')
mass_fig.show()


# Power Budget pie chart me

power_fig = px.pie(names = power_values, values = power_values, title = 'Power Budget')
power_fig.show()


# Mass Budget ko Matplotlib me
plt.figure(figsize=(8, 8))
plt.pie(mass_values, labels = mass_labels, autopct = '1%.1f%%', startangle = 140)
plt.title('Mass Budget')
plt.axis('equal')
plt.show()


plt.figure(figsize=(8, 8))
plt.pie(power_values, labels = power_values, autopct = '%1.1f%%', startangle = 140)
plt.title('Power Budget')
plt.axis('equal')
plt.show()














        




















      
















        




















      
