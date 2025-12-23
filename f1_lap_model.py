import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Load correct file
data = pd.read_csv("lap_times.csv")

# Convert lap time
data['lap_time_sec'] = data['milliseconds'] / 1000

# Remove abnormal laps
data = data[data['lap_time_sec'] < 200]

# FEATURES (IMPORTANT CHANGE)
X = data[['lap', 'position', 'driverId', 'raceId']]
y = data['lap_time_sec']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("MAE (seconds):", round(mae, 2))
print("R2 Score:", round(r2, 2))

plt.scatter(y_test, predictions)
plt.xlabel("Actual Lap Time (s)")
plt.ylabel("Predicted Lap Time (s)")
plt.title("F1 Lap Time Prediction")
plt.show()

plt.hist(data['lap_time_sec'], bins=50)
plt.xlabel("Lap Time (seconds)")
plt.ylabel("Frequency")
plt.title("Distribution of Formula 1 Lap Times")
plt.show()

plt.scatter(data['lap'], data['lap_time_sec'], alpha=0.5)
plt.xlabel("Lap Number")
plt.ylabel("Lap Time (seconds)")
plt.title("Lap Number vs Lap Time")
plt.show()

plt.scatter(data['position'], data['lap_time_sec'], alpha=0.5)
plt.xlabel("Race Position")
plt.ylabel("Lap Time (seconds)")
plt.title("Position vs Lap Time")
plt.show()

plt.scatter(y_test, predictions, alpha=0.6)
plt.xlabel("Actual Lap Time (seconds)")
plt.ylabel("Predicted Lap Time (seconds)")
plt.title("Actual vs Predicted F1 Lap Times")
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()])
plt.show()
