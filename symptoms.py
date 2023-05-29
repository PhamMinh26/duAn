import json

def load_diseases_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        diseases_data = json.load(file)
    return diseases_data if isinstance(diseases_data, list) else []

def sort_diseases(matched_diseases, diseases):
    sorted_diseases = sorted(matched_diseases, key=lambda x: (-len([d for d in diseases if d['name'] == x and 'symptoms' in d][0]['symptoms']) if any(d['name'] == x and 'symptoms' in d for d in diseases) else 0, -diseases.index(x)))
    return sorted_diseases

def diagnose_disease(diseases_file):
    diseases = load_diseases_from_file(diseases_file)

    user_symptoms = input("Nhập các triệu chứng bạn đang gặp phải (cách nhau bằng dấu phẩy): ").split(",")
    user_symptoms = [symptom.strip() for symptom in user_symptoms]

    matched_diseases = []
    for disease in diseases:
        matched_symptoms = [symptom for symptom in user_symptoms if symptom in disease["symptoms"]]
        if matched_symptoms:
            matched_diseases.append(disease["name"])

    if len(matched_diseases) > 0:
        sorted_diseases = sort_diseases(matched_diseases, diseases)
        print("Kết quả chẩn đoán:")
        for i, disease in enumerate(sorted_diseases, 1):
            print(f"{i}. {disease}")
    else:
        print("Không chẩn đoán được")

diseases_file = "C:/Users/name/Desktop/duAn/diseases.json"
diagnose_disease(diseases_file)
