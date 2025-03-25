# Input
data = ["5cse", "10ads","17ece","25it","83amml"]
extra_value = 5

# Processing
output = []
for item in data:
    num = int(''.join(filter(str.isdigit, item)))  
    text = ''.join(filter(str.isalpha, item)) 
    output.append(f"{num + extra_value}{text}") 


l=len(output)
for i in range(l-1,-1,-1):
    print(output[i],end=" ")