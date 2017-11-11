import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for d in data_files:
    name = d.split(".")[0]
    path = "schools/"+d
    df = pd.read_csv(path)
    data[name] = df

all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding="windows-1252")
survey = pd.concat([all_survey,d75_survey], axis=0)
print(survey.head(5))

survey["DBN"] = survey["dbn"]
columns_to_use = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey = survey[columns_to_use]
data["survey"] = survey
print(data["survey"].shape)

def add_padding(number):
    return str(number).zfill(2)

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(add_padding)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"]+data["class_size"]["SCHOOL CODE"]
print(data["class_size"].head(3))