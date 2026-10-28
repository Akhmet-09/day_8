# A = {1,2,3,4,5,6,7,8,9}
# B = {10,11,12,13,14,15,1,2,3,4,45,6,7,98}
# all = A.union(B)
# # print(all)
# both_has = A.intersection(B)
# # print(both_has)
# A_has_B_not = A.difference(B)
# # print(A_has_B_not)
# B_has_A_not = B.difference(A)
# print(B_has_A_not)

# def divissors(x,y):
#     divissors_of_x = set()
#     divissors_of_y = set()
#     for a in range(1,x+1):
#         if x%a==0:
#             divissors_of_x.add(a)
#     for b in range(1,y+1):
#         if y%b==0:
#             divissors_of_y.add(b)
#     common_divissors = divissors_of_x.intersection(divissors_of_y) 
#     return common_divissors
# print(divissors(10,15))               


# import json 
# student_dict = {
#     'name' : 'Adam',
#     'surname' : 'Smith',
#     'age' : '17',
#     'langauge' : 'Python'
# }
# json_p = json.dumps(student_dict,indent=5)
# # print(json)
# json_data = '{"name": "Bob", "age": 16, "active": true}'
# python_dict = json.loads(json_data)
# # print(python_dict)


# with open('test_1.py','a') as file :
#     file.write("print('Hello world')")
# with open('test_2.txt', 'a') as file_1 :
#     file_1.write('Hello world')


# with open('test_3.py','a') as add :
#     input = add.write("print('Hello Python')")
#     print(f"({input}) added successfully'")



# with open('test_1.py','r') as read :
#     matn= read.read()
#     print(matn )

# with open('test10.py','a') as test_10 :
#     test_10.write("print('Hello world')\n")
#     print(test_10)


with open('test10.py','r') as test_10_r :
    text = test_10_r.read()
    print(text)
















