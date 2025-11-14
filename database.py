student_info = {
    "student1" : {
        "name":"mahadi hasan",
        "class": 10,
        "profession":"student",
        "age": 18,
        "address":{
            "gram":"golapgram",
            "thana":"savar",
            "district":"Dhaka",
            "division":"dhaka",
            
        }
    },
    "student2": {
        "name":"imran hasan",
        "class": 12,
        "profession":"student",
        "age": 20,
        "address":{
            "gram":"gopalpur",
            "thana":"gopalpur",
            "district":"tangail",
            "division":"dhaka",
            
        }
            
    },
    "student3" : {
        "name":"labib hasan",
        "class": 8,
        "profession":"student",
        "age": 15,
        "address":{
            "gram":"shimla",
            "thana":"modupur",
            "district":"rajshahi",
            "division":"dhaka",
            
        
        }    
            
            
    },
    "student4" : {
        "name":"rakib hasan",
        "class": 13,
        "profession":"student",
        "age": 20,
        "address":{
            "gram":"atorbari",
            "thana":"tongi",
            "district":"gazipur",
            "division":"dhaka",
            
        }    
            
    }
}
    
a = student_info["student2"]["address"]

print(a)