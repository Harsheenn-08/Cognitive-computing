sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New York"
}
print(sample_dict)

sample_dict["loaction"]=sample_dict.pop("city")
print("Updated dictionary:",sample_dict)