"""Constants for the Garmin Connect integration."""
from datetime import timedelta
from typing import NamedTuple

from homeassistant.const import (
    UnitOfMass,
    UnitOfTime,
    UnitOfLength,
    PERCENTAGE,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)

DOMAIN = "garmin_connect"
DATA_COORDINATOR = "coordinator"
DEFAULT_UPDATE_INTERVAL = timedelta(minutes=5)

GARMIN_ENTITY_LIST = {
    "totalSteps": ["Total Steps", "steps", "mdi:walk", None, SensorStateClass.TOTAL, True],
    "dailyStepGoal": ["Daily Step Goal", "steps", "mdi:walk", None, SensorStateClass.TOTAL, True],
    "totalKilocalories": ["Total KiloCalories", "kcal", "mdi:food", None, SensorStateClass.TOTAL, True],
    "activeKilocalories": ["Active KiloCalories", "kcal", "mdi:food", None, SensorStateClass.TOTAL, True],
    "bmrKilocalories": ["BMR KiloCalories", "kcal", "mdi:food", None, SensorStateClass.TOTAL, True],
    "consumedKilocalories": ["Consumed KiloCalories", "kcal", "mdi:food", None, SensorStateClass.TOTAL, False],
    "burnedKilocalories": ["Burned KiloCalories", "kcal", "mdi:food", None, SensorStateClass.TOTAL, True],
    "remainingKilocalories": [
        "Remaining KiloCalories",
        "kcal",
        "mdi:food",
        None,
        SensorStateClass.TOTAL,
        False,
    ],
    "netRemainingKilocalories": [
        "Net Remaining KiloCalories",
        "kcal",
        "mdi:food",
        None,
        SensorStateClass.TOTAL,
        False,
    ],
    "netCalorieGoal": ["Net Calorie Goal", "kcal", "mdi:food", None, SensorStateClass.TOTAL, False],
    "totalDistanceMeters": [
        "Total Distance Mtr",
        UnitOfLength.METERS,
        "mdi:walk",
        SensorDeviceClass.DISTANCE,
        SensorStateClass.TOTAL,
        True,
    ],
    "wellnessStartTimeLocal": [
        "Wellness Start Time",
        None,
        "mdi:clock",
        SensorDeviceClass.TIMESTAMP,
        None,
        False,
    ],
    "wellnessEndTimeLocal": [
        "Wellness End Time",
        None,
        "mdi:clock",
        SensorDeviceClass.TIMESTAMP,
        None,
        False,
    ],
    "wellnessDescription": ["Wellness Description", "", "mdi:clock", None, SensorStateClass.TOTAL, False],
    "wellnessDistanceMeters": [
        "Wellness Distance Mtr",
        UnitOfLength.METERS,
        "mdi:walk",
        SensorDeviceClass.DISTANCE,
        SensorStateClass.TOTAL,
        False,
    ],
    "wellnessActiveKilocalories": [
        "Wellness Active KiloCalories",
        "kcal",
        "mdi:food",
        None,
        SensorStateClass.TOTAL,
        False,
    ],
    "wellnessKilocalories": ["Wellness KiloCalories", "kcal", "mdi:food", None, SensorStateClass.TOTAL, False],
    "highlyActiveSeconds": [
        "Highly Active Time",
        UnitOfTime.MINUTES,
        "mdi:fire",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        False,
    ],
    "activeSeconds": ["Active Time", UnitOfTime.MINUTES, "mdi:fire", None, SensorStateClass.TOTAL, True],
    "sedentarySeconds": ["Sedentary Time", UnitOfTime.MINUTES, "mdi:seat", None, SensorStateClass.TOTAL, True],
    "sleepingSeconds": ["Sleeping Time", UnitOfTime.MINUTES, "mdi:sleep", None, SensorStateClass.TOTAL, True],
    "measurableAwakeDuration": [
        "Awake Duration",
        UnitOfTime.MINUTES,
        "mdi:sleep",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        True,
    ],
    "measurableAsleepDuration": [
        "Sleep Duration",
        UnitOfTime.MINUTES,
        "mdi:sleep",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        True,
    ],
    "floorsAscendedInMeters": [
        "Floors Ascended Mtr",
        UnitOfLength.METERS,
        "mdi:stairs",
        SensorDeviceClass.DISTANCE,
        SensorStateClass.TOTAL,
        False,
    ],
    "floorsDescendedInMeters": [
        "Floors Descended Mtr",
        UnitOfLength.METERS,
        "mdi:stairs",
        SensorDeviceClass.DISTANCE,
        SensorStateClass.TOTAL,
        False,
    ],
    "floorsAscended": ["Floors Ascended", "floors", "mdi:stairs", None, SensorStateClass.TOTAL, True],
    "floorsDescended": ["Floors Descended", "floors", "mdi:stairs", None, SensorStateClass.TOTAL, True],
    "userFloorsAscendedGoal": [
        "Floors Ascended Goal",
        "floors",
        "mdi:stairs",
        None,
        SensorStateClass.TOTAL,
        True,
    ],
    "minHeartRate": ["Min Heart Rate", "bpm", "mdi:heart-pulse", None, SensorStateClass.MEASUREMENT, True],
    "maxHeartRate": ["Max Heart Rate", "bpm", "mdi:heart-pulse", None, SensorStateClass.MEASUREMENT, True],
    "restingHeartRate": ["Resting Heart Rate", "bpm", "mdi:heart-pulse", None, SensorStateClass.MEASUREMENT, True],
    "minAvgHeartRate": ["Min Avg Heart Rate", "bpm", "mdi:heart-pulse", None, SensorStateClass.MEASUREMENT, False],
    "maxAvgHeartRate": ["Max Avg Heart Rate", "bpm", "mdi:heart-pulse", None, SensorStateClass.MEASUREMENT, False],
    "abnormalHeartRateAlertsCount": [
        "Abnormal HR Counts",
        None,
        "mdi:heart-pulse",
        None,
        SensorStateClass.TOTAL,
        False,
    ],
    "lastSevenDaysAvgRestingHeartRate": [
        "Last 7 Days Avg Heart Rate",
        "bpm",
        "mdi:heart-pulse",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "averageStressLevel": ["Avg Stress Level", "lvl", "mdi:flash-alert", None, SensorStateClass.MEASUREMENT, True],
    "maxStressLevel": ["Max Stress Level", "lvl", "mdi:flash-alert", None, SensorStateClass.MEASUREMENT, True],
    "stressQualifier": ["Stress Qualifier", None, "mdi:flash-alert", None, None, False],
    "stressDuration": ["Stress Duration", UnitOfTime.MINUTES, "mdi:flash-alert", None, SensorStateClass.TOTAL, False],
    "restStressDuration": [
        "Rest Stress Duration",
        UnitOfTime.MINUTES,
        "mdi:flash-alert",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        True,
    ],
    "activityStressDuration": [
        "Activity Stress Duration",
        UnitOfTime.MINUTES,
        "mdi:flash-alert",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        True,
    ],
    "uncategorizedStressDuration": [
        "Uncat. Stress Duration",
        UnitOfTime.MINUTES,
        "mdi:flash-alert",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        True,
    ],
    "totalStressDuration": [
        "Total Stress Duration",
        UnitOfTime.MINUTES,
        "mdi:flash-alert",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        True,
    ],
    "lowStressDuration": [
        "Low Stress Duration",
        UnitOfTime.MINUTES,
        "mdi:flash-alert",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        True,
    ],
    "mediumStressDuration": [
        "Medium Stress Duration",
        UnitOfTime.MINUTES,
        "mdi:flash-alert",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        True,
    ],
    "highStressDuration": [
        "High Stress Duration",
        UnitOfTime.MINUTES,
        "mdi:flash-alert",
        None,
        SensorStateClass.TOTAL,
        True,
    ],
    "stressPercentage": [
        "Stress Percentage",
        PERCENTAGE,
        "mdi:flash-alert",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "restStressPercentage": [
        "Rest Stress Percentage",
        PERCENTAGE,
        "mdi:flash-alert",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "activityStressPercentage": [
        "Activity Stress Percentage",
        PERCENTAGE,
        "mdi:flash-alert",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "uncategorizedStressPercentage": [
        "Uncat. Stress Percentage",
        PERCENTAGE,
        "mdi:flash-alert",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "lowStressPercentage": [
        "Low Stress Percentage",
        PERCENTAGE,
        "mdi:flash-alert",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "mediumStressPercentage": [
        "Medium Stress Percentage",
        PERCENTAGE,
        "mdi:flash-alert",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "highStressPercentage": [
        "High Stress Percentage",
        PERCENTAGE,
        "mdi:flash-alert",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "moderateIntensityMinutes": [
        "Moderate Intensity",
        UnitOfTime.MINUTES,
        "mdi:flash-alert",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        False,
    ],
    "vigorousIntensityMinutes": [
        "Vigorous Intensity",
        UnitOfTime.MINUTES,
        "mdi:run-fast",
        SensorDeviceClass.DURATION,
        SensorStateClass.TOTAL,
        False,
    ],
    "intensityMinutesGoal": [
        "Intensity Goal",
        UnitOfTime.MINUTES,
        "mdi:run-fast",
        None,
        SensorStateClass.TOTAL,
        False,
    ],
    "bodyBatteryChargedValue": [
        "Body Battery Charged",
        PERCENTAGE,
        "mdi:battery-charging-100",
        None,
        SensorStateClass.TOTAL,
        True,
    ],
    "bodyBatteryDrainedValue": [
        "Body Battery Drained",
        PERCENTAGE,
        "mdi:battery-alert-variant-outline",
        None,
        SensorStateClass.TOTAL,
        True,
    ],
    "bodyBatteryHighestValue": [
        "Body Battery Highest",
        PERCENTAGE,
        "mdi:battery-heart",
        None,
        SensorStateClass.TOTAL,
        True,
    ],
    "bodyBatteryLowestValue": [
        "Body Battery Lowest",
        PERCENTAGE,
        "mdi:battery-heart-outline",
        None,
        SensorStateClass.TOTAL,
        True,
    ],
    "bodyBatteryMostRecentValue": [
        "Body Battery Most Recent",
        PERCENTAGE,
        "mdi:battery-positive",
        None,
        SensorStateClass.TOTAL,
        True,
    ],
    "averageSpo2": ["Average SPO2", PERCENTAGE, "mdi:diabetes", None, SensorStateClass.MEASUREMENT, True],
    "lowestSpo2": ["Lowest SPO2", PERCENTAGE, "mdi:diabetes", None, SensorStateClass.MEASUREMENT, True],
    "latestSpo2": ["Latest SPO2", PERCENTAGE, "mdi:diabetes", None, SensorStateClass.MEASUREMENT, True],
    "latestSpo2ReadingTimeLocal": [
        "Latest SPO2 Time",
        None,
        "mdi:diabetes",
        SensorDeviceClass.TIMESTAMP,
        None,
        False,
    ],
    "averageMonitoringEnvironmentAltitude": [
        "Average Altitude",
        PERCENTAGE,
        "mdi:image-filter-hdr",
        None,
        SensorStateClass.TOTAL,
        False,
    ],
    "highestRespirationValue": [
        "Highest Respiration",
        "brpm",
        "mdi:progress-clock",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "lowestRespirationValue": [
        "Lowest Respiration",
        "brpm",
        "mdi:progress-clock",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "latestRespirationValue": [
        "Latest Respiration",
        "brpm",
        "mdi:progress-clock",
        None,
        SensorStateClass.MEASUREMENT,
        False,
    ],
    "latestRespirationTimeGMT": [
        "Latest Respiration Update",
        None,
        "mdi:progress-clock",
        SensorDeviceClass.TIMESTAMP,
        None,
        False,
    ],
    "weight": ["Weight", UnitOfMass.KILOGRAMS, "mdi:weight-kilogram", SensorDeviceClass.WEIGHT, SensorStateClass.MEASUREMENT, False],
    "bmi": ["BMI", "bmi", "mdi:food", None, SensorStateClass.MEASUREMENT, False],
    "bodyFat": ["Body Fat", PERCENTAGE, "mdi:food", None, SensorStateClass.MEASUREMENT, False],
    "bodyWater": ["Body Water", PERCENTAGE, "mdi:water-percent", None, SensorStateClass.MEASUREMENT, False],
    "boneMass": ["Bone Mass", UnitOfMass.KILOGRAMS, "mdi:bone", SensorDeviceClass.WEIGHT, SensorStateClass.MEASUREMENT, False],
    "muscleMass": ["Muscle Mass", UnitOfMass.KILOGRAMS, "mdi:dumbbell", SensorDeviceClass.WEIGHT, SensorStateClass.MEASUREMENT, False],
    "physiqueRating": ["Physique Rating", None, "mdi:numeric", None, SensorStateClass.MEASUREMENT, False],
    "visceralFat": ["Visceral Fat", PERCENTAGE, "mdi:food", None, SensorStateClass.MEASUREMENT, False],
    "metabolicAge": ["Metabolic Age", UnitOfTime.YEARS, "mdi:calendar-heart", None, SensorStateClass.MEASUREMENT, False],
    "nextAlarm": ["Next Alarm Time", None, "mdi:alarm", SensorDeviceClass.TIMESTAMP, None, True],
    "lastActivities": ["Last Activities", None, "mdi:numeric", SensorStateClass.TOTAL, None, False],
    "badges": ["Badges", None, "mdi:numeric", SensorStateClass.TOTAL, None, False],
    "sleepScore": [
        "Sleep Score",
        None,
        "mdi:sleep",
        SensorStateClass.TOTAL,
        SensorStateClass.MEASUREMENT,
        True,
    ],
    "hrvStatus": [
        "HRV Status",
        None,
        "mdi:heart-pulse",
        None,
        None,
        True,
    ],
}

GEAR_ICONS = {
    "Shoes": "mdi:shoe-sneaker",
    "Bike": "mdi:bike",
    "Other": "mdi:basketball",
    "Golf Clubs": "mdi:golf",
}


class SERVICE_SETTING(NamedTuple):
    """Options for the service settings, see services.yaml"""

    ONLY_THIS_AS_DEFAULT = "set this as default, unset others"
    DEFAULT = "set as default"
    UNSET_DEFAULT = "unset default"


class GEAR(NamedTuple):
    UUID = "uuid"
    TYPE_KEY = "typeKey"
    TYPE_ID = "typeId"
    USERPROFILE_ID = "userProfileId"
    ACTIVITY_TYPE_PK = "activityTypePk"
