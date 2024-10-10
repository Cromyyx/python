from ezgpx import GPX

# Parse GPX file
gpx = GPX("C:\\Users\\thoma\\OneDrive - Bildungsdirektion\\4DNW\\Informatik\\Füla\\radweg.gpx")

# Convert to CSV
gpx.to_csv("radweg.csv", columns = ["lat", "lon", "ele"])