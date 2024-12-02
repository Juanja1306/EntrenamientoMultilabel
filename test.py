import torch

file1 = "modelo_pesos1.pth"
file2 = "modelo_pesos2.pth"

# Cargar los archivos
state_dict1 = torch.load(file1)
state_dict2 = torch.load(file2)


# Cargar los archivos
state_dict1 = torch.load(file1)
state_dict2 = torch.load(file2)

# Comparar clave por clave
differences = []

for key in state_dict1.keys():
    if key not in state_dict2:
        differences.append(f"La clave '{key}' está en el primer archivo pero no en el segundo.")
    elif not torch.equal(state_dict1[key], state_dict2[key]):
        differences.append(f"Diferencia en la clave '{key}'.")

for key in state_dict2.keys():
    if key not in state_dict1:
        differences.append(f"La clave '{key}' está en el segundo archivo pero no en el primero.")

if not differences:
    print("Los archivos son idénticos.")
else:
    print("Los archivos son diferentes:")
    for diff in differences:
        print(diff)