import requests

BASE = "http://127.0.0.1:8080/"


data = [
    {"likes": 78, "name": "Joe", "views": 1000},
    {"likes": 108, "name": "How to Make REST API", "views": 100800},
    {"likes": 5, "name": "Tim", "views": 100},
]

# PUT requests to add videos
print("Adding videos:")
for i in range(len(data)):
    response = requests.put(BASE + f"video/{i}", json=data[i])
    print(f"PUT Response for video/{i}: {response.json()}")

input("Press Enter to test GET requests...")

# GET requests to retrieve videos
print("\nRetrieving videos:")
for i in range(len(data)):
    response = requests.get(BASE + f"video/{i}")
    print(f"GET Response for video/{i}: {response.json()}")

input("Press Enter to test PATCH requests...")

# PATCH requests to update specific fields
print("\nUpdating videos with PATCH:")
patch_data = [
    {"name": "Updated Joe"},
    {"views": 150000},
    {"likes": 10, "views": 200},
]
for i in range(len(patch_data)):
    response = requests.patch(BASE + f"video/{i}", json=patch_data[i])
    print(f"PATCH Response for video/{i}: {response.json()}")

input("Press Enter to test GET requests after PATCH...")

# GET requests again to verify PATCH updates
print("\nRetrieving videos after PATCH:")
for i in range(len(data)):
    response = requests.get(BASE + f"video/{i}")
    print(f"GET Response for video/{i}: {response.json()}")

input("Press Enter to test DELETE requests...")

# DELETE requests to remove videos
print("\nDeleting videos:")
for i in range(len(data)):
    response = requests.delete(BASE + f"video/{i}")
    print(f"DELETE Response for video/{i}: {response.status_code}")

input("Press Enter to test GET requests after DELETE...")

#GET requests after DELETE to ensure videos are removed
print("\nRetrieving videos after DELETE:")
for i in range(len(data)):
    response = requests.get(BASE + f"video/{i}")
    print(f"GET Response for video/{i}: {response.status_code} - {response.json() if response.status_code == 200 else 'Not Found'}")
