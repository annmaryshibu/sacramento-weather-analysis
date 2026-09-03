'''                       Final Coding Project – Weather Data Analysis using OpenMeteo API

In this project, 7 days of the weather temperature of Sacramento has been retrieved using the OpenMeteo Historical API. 
Then the data is parsed and visualized as a scatter plot, and a two-page PDF report is generated using ReportLab.

Note: ReportLab was used instead of Aspose for PDF generation. Since ReportLab does not automatically adjust long text,and sentences on Page 1 are manually split across multiple lines to fit the page layout. '''

# Importing Libraries
import requests
import datetime as dtFunctions
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas

# 1) Get historical weather data

# Sacramento Coordinates
latitude = 38.5816
longitude = -121.4944                                  

# Assigning Start and end date(7 day period)
strStartDate= "08/27/2026"
strEndDate =  "09/02/2026"

# Convert MM/DD/YYYY into the YYYY-MM-DD format required by Open-Meteo
startDate = dtFunctions.datetime.strptime(strStartDate, "%m/%d/%Y")
endDate = dtFunctions.datetime.strptime(strEndDate, "%m/%d/%Y")


apiStartDate = startDate.strftime("%Y-%m-%d")
apiEndDate = endDate.strftime("%Y-%m-%d")

urlHistory = "https://archive-api.open-meteo.com/v1/archive"
parameters = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": apiStartDate,
    "end_date": apiEndDate,
    "hourly": "temperature_2m",
    "temperature_unit": "fahrenheit",
    "timezone": "America/Los_Angeles"
}
# Send request to Open-meteo API 
data =requests.get(urlHistory,params=parameters,timeout=30)
print("Status Code :",data.status_code)
print("Response", data.text[:300]) # To verify if the data is accessed properly

# Stop the program if the API request fails
if data.status_code != 200:
    raise RuntimeError(
        f"Unable to fetch historical weather data. "
        f"Status code: {data.status_code}. "
        f"Response: {data.text[:300]}"
    )

# Parse the JSON data
jsondata = data.json()

# Retrieve hourly times and temperatures from Open-Meteo
lstDateTimes = jsondata["hourly"]["time"]
lstHourlyTemperatures = jsondata["hourly"]["temperature_2m"]

# Create hour numbers: 0, 1, 2, 3...
lstHours = list(range(len(lstHourlyTemperatures)))

print("\nTemperatures =", lstHourlyTemperatures)
print("\nHours =", lstHours)
print("\nNumber of readings =", len(lstHourlyTemperatures))

# Calculate temperature statistics
highestTemperature = max(lstHourlyTemperatures)
lowestTemperature = min(lstHourlyTemperatures)
averageTemperature = sum(lstHourlyTemperatures) / len(lstHourlyTemperatures)

print("\nHighest temperature =", highestTemperature)
print("Lowest temperature =", lowestTemperature)
print("Average temperature =", averageTemperature)


# 2) Plot the data

hours = lstHours
temps = lstHourlyTemperatures

# Creating scatter plot of hourly temp data
plt.scatter(hours, temps)
plt.xlabel("Hours")
plt.ylabel("Temperature (F)")
plt.title(f"Sample Scatter Plot ({strStartDate}-{strEndDate})")

# Saving it as an image to embed into the pdf because reportlab needs seperate embedding
plt.savefig(r"Final scatterplot.png")
plt.close()

# 3) Creating PDF Report
c = canvas.Canvas("final.pdf")

# First Page of the PDF
c.drawString(200, 750, "Name: Ann Mary Shibu")
c.drawString(200, 730, "Course: CISP-357 - Introduction to Data Science ")
c.drawString(200, 710, "Final Project Report")
c.drawString(10, 650, "Project Description:")
c.drawString(10, 620, "In this project,Open-Meteo API is used to collect real world hourly temperature data for the city of")
c.drawString(10, 600, "Sacramento. The data represents temperature readings over a seven-day period.The purpose of this project")
c.drawString(10, 580, "is to demonstrate how to retrieve data from an external API,Parse the data using python,visualize it using a")
c.drawString(10, 560, "scatter plot and generate a PDF report programmatically. Some of the libraries i used in this program includes")
c.drawString(10, 540, "reportlab(For generating PDF and to write the report),requests(for requesting the API acess),Datetime")
c.drawString(10, 520, "and Matplotlib(For plotting)")
c.drawString(10, 490, "Data Trend Analysis:")
c.drawString(10, 460, "The scatter plot represents hourly recorded temperature readings of seven days of weather data from ")
c.drawString(10, 440, f"{strStartDate} through {strEndDate}. The data shows a consistent daily temperature pattern, with higher")
c.drawString(10, 420, "temperatures  during the daytime hours and decrease during the night time hours repeating the cycle ")
c.drawString(10, 400, f"across all seven days.During this time period, the highest recorded temperature was {highestTemperature:.1f}°F,")
c.drawString(10, 380, f"while the lowest temperature was {lowestTemperature:.1f}°F,indicating mild spring weather conditions & The average recorded temperature was {averageTemperature:.1f}°F.Overall,")
c.drawString(10, 360, "the data reflects typical daily temperature variations for Sacramento during this season.")
c.showPage()

# Second Page
c.drawString(100, 750, "Hourly Temperature Scatter Plot (Sacramento, 7 Days)")

#Embedding the saved scatterplot image
c.drawImage("Final scatterplot.png", 50, 400, width=400, height=300)

c.save()


