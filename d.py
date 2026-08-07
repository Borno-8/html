st_data = {
    "id1": {"name": "Saraa", "class": "5", "subject_interagation": "en, mth, sci"},
    "id2": {"name": "David", "class": "5", "subject_interagation": "en, mth, sci"},
    "id3": {"name": "urmom", "class": "5", "subject_interagation": "en, mth, sci"},
    "id4": {"name": "Surya", "class": "5", "subject_interagation": "en, mth, sci"}
}

result = {}
sn_k = []

for st_id, details in st_data.items():
    unique_k = (details["name"], details["class"], details["subject_interagation"])

    if unique_k not in sn_k:
        sn_k.append(unique_k)
        result[st_id] = details

    for k, v in result.items():
        print(k, ".", v)