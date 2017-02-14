bob = {"name": "Bob Smith", "age": 42, "pay": 30000, "job": "dev"}
sue = {"name": "Sue Jones", "age": 45, "pay": 40000, "job": "hdw"}
tom = {"name": "Tom Lucky", "age": 47, "pay": 80000, "job": "fullstack"}

db = {}
db["bob"] = bob
db["sue"] = sue
db["tom"] = tom


if __name__ == "__main__":
	for key in db:
		print(key, "=>", db[key])





